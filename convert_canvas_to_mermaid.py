#!/usr/bin/env python3
"""
Obsidian Canvas to Mermaid Converter
Converts .canvas files to Mermaid diagrams for use in Quartz/static site generators
Usage:
# Convert to file
$ python convert_canvas_to_mermaid.py <input_file> -o <output_file>
# Convert to stdout
$ python convert_canvas_to_mermaid.py <input_file> --stdout
$ python3 convert_canvas_to_mermaid.py "content/Books/The Hobbit - Tree.canvas" --stdout
# Convert to file and stdout
$ python convert_canvas_to_mermaid.py <input_file> -o <output_file> --stdout
"""

import json
import re
import argparse
from pathlib import Path
from typing import Dict, List, Any, Optional


class CanvasToMermaidConverter:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.groups = {}
        
    def clean_text(self, text: str) -> str:
        """Clean text for Mermaid compatibility"""
        if not text:
            return "Unknown"
        
        # Remove newlines and extra spaces
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Escape special characters for Mermaid
        text = text.replace('"', '&quot;')
        text = text.replace("'", '&apos;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        
        # Limit length for readability
        if len(text) > 30:
            text = text[:27] + "..."
            
        return text
    
    def generate_node_id(self, original_id: str) -> str:
        """Generate a clean node ID for Mermaid"""
        # Use first 8 characters of original ID for uniqueness
        clean_id = re.sub(r'[^a-zA-Z0-9]', '', original_id[:8])
        return f"node_{clean_id}" if clean_id else f"node_{hash(original_id) % 10000}"
    
    def get_node_style(self, node: Dict[str, Any]) -> str:
        """Determine Mermaid node style based on canvas node properties"""
        node_type = node.get('type', 'text')
        color = node.get('color', '')
        
        # Handle group nodes
        if node_type == 'group':
            return f'["{self.clean_text(node.get("label", "Group"))}"]'
        
        # Handle different colors/categories
        if color == '#964b00':  # Brown - Hobbits in your example
            return f'("{self.clean_text(node.get("text", ""))}")'
        elif color == '#ffffff':  # White - Gandalf
            return f'["{self.clean_text(node.get("text", ""))}"]'
        elif color == '3':  # Goblins/Orcs
            return f'{{"{self.clean_text(node.get("text", ""))}"}}' 
        else:
            return f'["{self.clean_text(node.get("text", ""))}"]'
    
    def is_node_in_group(self, node: Dict[str, Any], group: Dict[str, Any]) -> bool:
        """Check if a node is inside a group based on coordinates"""
        node_x = node.get('x', 0)
        node_y = node.get('y', 0)
        
        group_x = group.get('x', 0)
        group_y = group.get('y', 0)
        group_width = group.get('width', 0)
        group_height = group.get('height', 0)
        
        return (group_x <= node_x <= group_x + group_width and 
                group_y <= node_y <= group_y + group_height)
    
    def is_group_in_group(self, inner_group: Dict[str, Any], outer_group: Dict[str, Any]) -> bool:
        """Check if one group is nested inside another group"""
        inner_x = inner_group.get('x', 0)
        inner_y = inner_group.get('y', 0)
        inner_width = inner_group.get('width', 0)
        inner_height = inner_group.get('height', 0)
        
        outer_x = outer_group.get('x', 0)
        outer_y = outer_group.get('y', 0)
        outer_width = outer_group.get('width', 0)
        outer_height = outer_group.get('height', 0)
        
        # Check if inner group is completely within outer group
        return (outer_x <= inner_x and 
                outer_y <= inner_y and
                inner_x + inner_width <= outer_x + outer_width and
                inner_y + inner_height <= outer_y + outer_height)
    
    def build_group_hierarchy(self, group_nodes: List[tuple]) -> Dict[str, Any]:
        """Build a hierarchical structure of groups"""
        hierarchy = {}
        processed = set()
        
        # Sort groups by area (largest first) to process parent groups before children
        sorted_groups = sorted(group_nodes, key=lambda x: x[1].get('width', 0) * x[1].get('height', 0), reverse=True)
        
        for group_id, group in sorted_groups:
            group_label = self.clean_text(group.get('label', 'Group'))
            
            # Find parent group
            parent_found = False
            for parent_id, parent_group in sorted_groups:
                parent_label = self.clean_text(parent_group.get('label', 'Group'))
                
                # Skip self and already processed groups
                if parent_id == group_id or parent_label == group_label:
                    continue
                    
                # Check if this group is inside the parent
                if self.is_group_in_group(group, parent_group):
                    # Initialize parent in hierarchy if not exists
                    if parent_label not in hierarchy:
                        hierarchy[parent_label] = {'subgroups': {}, 'nodes': []}
                    
                    # Add this group as a subgroup
                    hierarchy[parent_label]['subgroups'][group_label] = {'subgroups': {}, 'nodes': []}
                    parent_found = True
                    break
            
            # If no parent found, it's a top-level group
            if not parent_found and group_label not in hierarchy:
                hierarchy[group_label] = {'subgroups': {}, 'nodes': []}
        
        return hierarchy
    
    def convert_to_mermaid(self, canvas_file: Path) -> str:
        """Convert canvas file to Mermaid diagram"""
        try:
            with open(canvas_file, 'r', encoding='utf-8') as f:
                canvas_data = json.load(f)
        except Exception as e:
            raise ValueError(f"Failed to read canvas file: {e}")
        
        nodes = canvas_data.get('nodes', [])
        edges = canvas_data.get('edges', [])
        
        # Process nodes
        node_mapping = {}  # Only for text nodes
        text_nodes = []
        group_nodes = []
        
        for node in nodes:
            node_id = self.generate_node_id(node['id'])
            
            if node.get('type') == 'group':
                group_nodes.append((node_id, node))
                # Don't add groups to node_mapping - they need special handling
            else:
                node_mapping[node['id']] = node_id  # Only add text nodes
                text_nodes.append((node_id, node))
        
        # Build group hierarchy
        group_hierarchy = self.build_group_hierarchy(group_nodes)
        
        # Assign nodes to their most specific (smallest) containing group
        ungrouped_nodes = []
        
        def assign_node_to_group(node_id, node, hierarchy, path=""):
            """Recursively assign node to the most specific group"""
            assigned = False
            
            for group_name, group_data in hierarchy.items():
                # Find the actual group node to check coordinates
                group_node = None
                for _, g in group_nodes:
                    if self.clean_text(g.get('label', 'Group')) == group_name:
                        group_node = g
                        break
                
                if group_node and self.is_node_in_group(node, group_node):
                    # Check if node belongs to any subgroup
                    subgroup_assigned = assign_node_to_group(node_id, node, group_data['subgroups'], f"{path}/{group_name}" if path else group_name)
                    
                    if not subgroup_assigned:
                        # Node belongs to this group directly
                        group_data['nodes'].append((node_id, node))
                    
                    assigned = True
                    break
            
            return assigned
        
        for node_id, node in text_nodes:
            if not assign_node_to_group(node_id, node, group_hierarchy):
                ungrouped_nodes.append((node_id, node))
        
        # Start building Mermaid diagram
        mermaid_lines = ["graph TD"]
        
        def render_group_hierarchy(hierarchy, indent_level=1):
            """Recursively render groups and subgroups"""
            indent = "    " * indent_level
            
            for group_name, group_data in hierarchy.items():
                # Create a safe subgraph ID
                subgraph_id = re.sub(r'[^a-zA-Z0-9]', '', group_name.replace(' ', ''))
                mermaid_lines.append(f"{indent}subgraph {subgraph_id} [\"{group_name}\"]")
                
                # Add nodes in this group
                for node_id, node in group_data['nodes']:
                    style = self.get_node_style(node)
                    mermaid_lines.append(f"{indent}    {node_id}{style}")
                
                # Add subgroups
                if group_data['subgroups']:
                    render_group_hierarchy(group_data['subgroups'], indent_level + 1)
                
                mermaid_lines.append(f"{indent}end")
                mermaid_lines.append("")
        
        # Render the hierarchy
        render_group_hierarchy(group_hierarchy)
        
        # Add ungrouped nodes
        if ungrouped_nodes:
            for node_id, node in ungrouped_nodes:
                style = self.get_node_style(node)
                mermaid_lines.append(f"    {node_id}{style}")
            mermaid_lines.append("")
        
        # Handle edges, including group-to-node connections
        group_id_mapping = {node['id']: self.generate_node_id(node['id']) for _, node in group_nodes}
        
        def handle_group_connection(group_original_id, target_node_id, relationship_label, hierarchy):
            """Handle connections from groups to nodes more intelligently"""
            group_node = next((g for _, g in group_nodes if g['id'] == group_original_id), None)
            if not group_node:
                return None
                
            group_label = self.clean_text(group_node.get('label', 'Group'))
            
            # For "members" relationships, create a collective representative node
            if 'member' in relationship_label.lower():
                # Create a virtual node representing the group
                group_virtual_id = f"group_{self.generate_node_id(group_original_id)[5:]}"  # Remove 'node_' prefix
                
                # Add the virtual group node to represent the collective
                group_display_name = f"All {group_label}" if not group_label.lower().startswith(('all', 'the')) else group_label
                mermaid_lines.append(f"    {group_virtual_id}[\"{group_display_name}\"]")
                
                return group_virtual_id
            
            # For other relationships, find an appropriate representative
            def find_representative():
                # Search hierarchy for the group
                def search_hierarchy(hier):
                    for name, data in hier.items():
                        if name == group_label:
                            # Look for a leader-like node first
                            for node_id, node in data['nodes']:
                                node_text = node.get('text', '').lower()
                                if any(title in node_text for title in ['thorin', 'leader', 'chief', 'king']):
                                    return node_id
                            # If no obvious leader, return the first node
                            if data['nodes']:
                                return data['nodes'][0][0]
                        
                        # Search in subgroups
                        if data['subgroups']:
                            result = search_hierarchy(data['subgroups'])
                            if result:
                                return result
                    return None
                
                # Try hierarchy first
                result = search_hierarchy(group_hierarchy)
                if result:
                    return result
                
                # Fallback to coordinate-based search
                for node_id, node in text_nodes:
                    if self.is_node_in_group(node, group_node):
                        node_text = node.get('text', '').lower()
                        if any(title in node_text for title in ['thorin', 'leader', 'chief', 'king']):
                            return node_id
                
                # Last resort: first node in group
                for node_id, node in text_nodes:
                    if self.is_node_in_group(node, group_node):
                        return node_id
                        
                return None
            
            return find_representative()
        
        # Add edges with labels
        for edge in edges:
            from_original = edge['fromNode']
            to_original = edge['toNode']
            label = self.clean_text(edge.get('label', ''))
            
            from_id = node_mapping.get(from_original)
            to_id = node_mapping.get(to_original)
            
            # Handle group-to-node connections
            if not from_id and from_original in group_id_mapping:
                # From node is a group, handle it intelligently
                from_id = handle_group_connection(from_original, to_id, label, group_hierarchy)
                
            if not to_id and to_original in group_id_mapping:
                # To node is a group, handle it intelligently  
                to_id = handle_group_connection(to_original, from_id, label, group_hierarchy)
            
            if from_id and to_id:
                if label:
                    mermaid_lines.append(f"    {from_id} -->|{label}| {to_id}")
                else:
                    mermaid_lines.append(f"    {from_id} --> {to_id}")
            else:
                # Skip edges we can't resolve
                if not from_id:
                    print(f"Warning: Could not resolve 'from' node: {from_original}")
                if not to_id:
                    print(f"Warning: Could not resolve 'to' node: {to_original}")
        
        # Add styling for different node types
        mermaid_lines.extend([
            "",
            "    %% Styling",
            "    classDef hobbit fill:#8B4513,stroke:#333,stroke-width:2px,color:#fff",
            "    classDef wizard fill:#fff,stroke:#333,stroke-width:2px",
            "    classDef orc fill:#654321,stroke:#333,stroke-width:2px,color:#fff",
            "    classDef dwarf fill:#4682B4,stroke:#333,stroke-width:2px,color:#fff",
            "    classDef elf fill:#98FB98,stroke:#333,stroke-width:2px",
            "    classDef men fill:#DEB887,stroke:#333,stroke-width:2px",
            "    classDef creature fill:#DDA0DD,stroke:#333,stroke-width:2px",
            "    classDef group fill:#FFE4B5,stroke:#8B4513,stroke-width:3px,stroke-dasharray: 5 5",
            "    classDef default fill:#e1f5fe,stroke:#333,stroke-width:2px"
        ])
        
        # Apply classes based on colors and group membership
        def collect_all_nodes(hierarchy):
            """Recursively collect all nodes from the hierarchy"""
            nodes = []
            for group_name, group_data in hierarchy.items():
                nodes.extend(group_data['nodes'])
                nodes.extend(collect_all_nodes(group_data['subgroups']))
            return nodes
        
        all_nodes = ungrouped_nodes + collect_all_nodes(group_hierarchy)
        
        def find_node_group_path(node_id, node, hierarchy, path=""):
            """Find the full path to a node's group"""
            for group_name, group_data in hierarchy.items():
                current_path = f"{path}/{group_name}" if path else group_name
                
                # Check if node is directly in this group
                if (node_id, node) in group_data['nodes']:
                    return current_path
                
                # Check subgroups
                subpath = find_node_group_path(node_id, node, group_data['subgroups'], current_path)
                if subpath:
                    return subpath
            
            return None
        
        for node_id, node in all_nodes:
            color = node.get('color', '')
            if color == '#964b00':
                mermaid_lines.append(f"    class {node_id} hobbit")
            elif color == '#ffffff':
                mermaid_lines.append(f"    class {node_id} wizard")
            elif color == '3':
                mermaid_lines.append(f"    class {node_id} orc")
            else:
                # Classify based on group membership
                group_path = find_node_group_path(node_id, node, group_hierarchy)
                if group_path:
                    if 'Dwarf' in group_path or 'Dwarves' in group_path:
                        mermaid_lines.append(f"    class {node_id} dwarf")
                    elif 'Elf' in group_path or 'Elves' in group_path:
                        mermaid_lines.append(f"    class {node_id} elf")
                    elif 'Men' in group_path or 'Lake-town' in group_path:
                        mermaid_lines.append(f"    class {node_id} men")
                    elif any(creature in group_path for creature in ['Eagle', 'Wolf', 'Spider']):
                        mermaid_lines.append(f"    class {node_id} creature")
        
        # Apply styling to virtual group nodes
        for line in mermaid_lines:
            if line.strip().startswith('group_') and '[' in line and '"All ' in line:
                # Extract the group node ID
                group_id = line.strip().split('[')[0].strip()
                mermaid_lines.append(f"    class {group_id} group")
        
        return '\n'.join(mermaid_lines)
    
    def process_file(self, input_file: Path, output_file: Optional[Path] = None) -> str:
        """Process a single canvas file"""
        if not input_file.exists():
            raise FileNotFoundError(f"Canvas file not found: {input_file}")
        
        mermaid_content = self.convert_to_mermaid(input_file)
        
        if output_file:
            output_file.parent.mkdir(parents=True, exist_ok=True)
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"```mermaid\n{mermaid_content}\n```")
            print(f"Converted {input_file} -> {output_file}")
        
        return mermaid_content


def main():
    parser = argparse.ArgumentParser(description="Convert Obsidian Canvas to Mermaid diagrams")
    parser.add_argument("input", help="Input .canvas file")
    parser.add_argument("-o", "--output", help="Output file (optional)")
    parser.add_argument("--stdout", action="store_true", help="Print to stdout instead of file")
    
    args = parser.parse_args()
    
    converter = CanvasToMermaidConverter()
    input_file = Path(args.input)
    
    try:
        if args.stdout:
            mermaid_content = converter.process_file(input_file)
            print("```mermaid")
            print(mermaid_content)
            print("```")
        else:
            output_file = Path(args.output) if args.output else input_file.with_suffix('.md')
            converter.process_file(input_file, output_file)
            
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
