#!/usr/bin/env python3
"""
Batch convert all .canvas files in the content directory to Mermaid diagrams
"""

import os
from pathlib import Path
from convert_canvas_to_mermaid import CanvasToMermaidConverter

def main():
    content_dir = Path("content")
    converter = CanvasToMermaidConverter()
    
    # Find all .canvas files
    canvas_files = list(content_dir.rglob("*.canvas"))
    
    if not canvas_files:
        print("No .canvas files found in content directory")
        return
    
    print(f"Found {len(canvas_files)} canvas file(s):")
    for canvas_file in canvas_files:
        print(f"  - {canvas_file}")
    
    print("\nConverting...")
    
    for canvas_file in canvas_files:
        try:
            # Create output filename: "filename.canvas" -> "filename - Mermaid.md"
            output_file = canvas_file.with_name(f"{canvas_file.stem} - Mermaid.md")
            
            mermaid_content = converter.process_file(canvas_file, output_file)
            print(f"✓ Converted {canvas_file.name} -> {output_file.name}")
            
        except Exception as e:
            print(f"✗ Failed to convert {canvas_file}: {e}")
    
    print("\nConversion complete!")
    print("\nTo use in your markdown files, replace:")
    print("  ![[filename.canvas]]")
    print("with:")
    print("  ![[filename - Mermaid.md]]")

if __name__ == "__main__":
    main()
