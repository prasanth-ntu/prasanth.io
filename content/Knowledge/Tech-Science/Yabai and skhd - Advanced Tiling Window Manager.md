---
tags:
  - scripts
  - Mac
  - Hacks
---
> [!WARNING] This page is still a WIP!
# Quick intro

**Overview:**
Yabai is a tiling window manager for macOS that, when combined with skhd (a hotkey daemon), offers a powerful, keyboard-driven window management experience.

**Key Features:**
- Automatic window tiling using a binary space partitioning algorithm.
- Extensive customization through configuration files.
- Control over windows, spaces, and displays via command-line interface.
- Custom keyboard shortcuts for window manipulation with skhd.

**Considerations:**
- Requires installation via Homebrew and configuration through dotfiles.
- May require additional permissions and setup steps on macOS.

**Ideal For:**
Power users seeking a tiling window manager experience similar to i3 on Linux, with extensive keyboard control and customization.

# Comparison of different tools

| **Feature / Tool**        | **Slate**                     | **Yabai + skhd**          | **Rectangle**        |
| ------------------------- | ----------------------------- | ------------------------- | -------------------- |
| **Ease of Use**           | Moderate (requires scripting) | Advanced (requires setup) | High (user-friendly) |
| **Customization**         | High                          | Very High                 | Moderate             |
| **Tiling Support**        | Manual                        | Automatic                 | None                 |
| **Multi-Monitor Support** | Yes                           | Yes                       | Limited              |
| **Active Maintenance**    | No                            | Yes                       | Yes                  |
| **Ideal For**             | Scripting enthusiasts         | Power users               | General users        |
# Installation steps 
1. **Install Yabai and skhd**
```bash
brew install koekeishiya/formulae/yabai
brew install koekeishiya/formulae/skhd
```
2. **Configure MAC OS settings**
	- **Mission Control**
		- Disable “Automatically rearrange Spaces based on most recent use”.
		- Enable “Displays have separate Spaces”.
	- **Accessibility**
		- Grant Accessibility permissions to both `yabai` and `skhd`.
			- If having difficulties granting access permissions, try
				- `brew services start yabai`, or `yabai --start-service` or  `brew services restart yabai`
3. **Create Configuration Files**
	1. 
