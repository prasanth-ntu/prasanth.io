---
tags:
  - softwareengineering
  - Mac
  - OpenSource
---
Operating System (OS)

# Windows

# Linux vs Unix

- **Unix** is the original operating system from the 1970s (AT&T Bell Labs). It's a proprietary, certified OS family (e.g. Solaris, HP-UX, AIX).
- **Linux** is a free, open-source kernel created by Linus Torvalds in 1991 that is _Unix-like_ — it was inspired by Unix and follows similar design principles (POSIX standards), but it does **not** share Unix source code. It's a reimplementation from scratch.

Think of it like: Unix is the original blueprint, Linux is a free recreation built from the ground up following that same blueprint.

## macOS

macOS is built on **Unix**, not Linux. Specifically:

- macOS sits on top of **Darwin**, an open-source Unix-based kernel
- Darwin is derived from **BSD** (Berkeley Software Distribution), which is a direct descendant of the original AT&T Unix
- macOS is **POSIX-certified** — meaning it's officially a "real" Unix, not just Unix-like

```
AT&T Unix (1970s)
├── BSD (direct descendant)
│   └── Darwin
│       └── macOS (certified Unix)
└── Inspired (but no shared code)
    └── Linux (Unix-like)
        ├── Ubuntu, Debian, Fedora...
        └── Alpine (what Docker uses)
```

That's also why the macOS terminal feels so natural for Linux users — they share the same Unix philosophy and many of the same commands (`ls`, `cd`, `grep`, `chmod`, etc.).

### Why Apple chose Unix (BSD) over Linux

**Historical context:** When Steve Jobs returned to Apple in 1997, he brought **NeXTSTEP** — the OS from his company NeXT, which was already built on top of BSD Unix (Mach kernel + BSD). macOS is literally the evolution of NeXTSTEP. Apple didn't sit down and choose between Linux and Unix — they inherited BSD through the NeXT acquisition. At that point, Linux was only ~6 years old and far less mature.

**But even if they had the choice, BSD had clear advantages:**

1. **Licensing (the biggest reason)**
   - BSD license: "Do whatever you want, just give credit" — allows proprietary/closed-source modifications
   - Linux (GPL): Any modifications to the kernel **must** be open-sourced and shared back
   - Apple wanted to build proprietary features on top of the kernel without being forced to release their source code. BSD's permissive license made this possible
2. **Maturity and stability** — BSD had ~20+ years of production use in academia and enterprise. Its networking stack was considered superior (the original TCP/IP implementation came from BSD)
3. **Code quality and coherence** — BSD is a complete, cohesive OS (kernel + userland designed together). Linux is just a kernel — you need to assemble userland tools from various GNU projects
4. **POSIX certification** — Building on BSD made it easier for Apple to get official Unix certification, which mattered for enterprise credibility

> Sony also chose BSD for the PlayStation OS, and Netflix runs on FreeBSD — for the same licensing reasons.

### But who maintains Darwin, and why not just use Linux?

**Darwin** is maintained primarily by **Apple engineers**. While it's technically open source, in practice almost nobody outside Apple contributes to it — the community is tiny compared to Linux.

Apple's competitive advantage isn't in the kernel — it's in **everything on top of it**:

- The kernel is a commodity — it manages memory, processes, I/O, etc. Whether it's Darwin or Linux, it does largely the same job
- What makes macOS _macOS_ is the **proprietary stack above the kernel**: Aqua UI, Metal graphics, Core Animation, Swift/Cocoa frameworks, Continuity with iPhone, etc.
- With BSD, Apple can keep all of that closed. With Linux (GPL), there's a risk that the copyleft requirement could "infect upward" — if proprietary code links too closely to the kernel, it may legally need to be open-sourced. This is a grey area that companies like Google (with Android) have to carefully navigate (e.g. Oracle v. Google)

**The trade-off:** Less community help maintaining the kernel, but total legal freedom above it. For a company with Apple's resources, that trade-off is worth it — they don't need the Linux community's contributions to the kernel, but they _do_ need the legal freedom to build proprietary software on top without licensing obligations bleeding into their closed-source products.

