# Bottle Pattern Grammar

**YJ&DS SCRIPTING (48-724)** — Yewon Jang & Diego Serna
48-724 Scripting and Parametric Design, CMU, Fall 2026

A Grasshopper plugin that turns an image into line-only patterns (shape grammar)
for a robotic arm to draw with a marker on a bottle.

```
Image → Patterns (lines) → Projection onto the bottle → Robot path → RobotStudio
```

## Folders

```
src/patterns/      Python code – pattern generation
src/fabrication/   Python code – projection + robot path
gh/                Grasshopper files
docs/              research, notes, plugin guide
```

## Working together (GitHub Desktop)

1. **Pull** before you start.
2. Work.
3. **Commit** + **Push** when you finish, with a message that says what changed.

If you are both going to edit the same `.gh` file, tell each other first:
Grasshopper files can't be merged, so the last push would overwrite the other.
