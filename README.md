# Bottle Pattern Grammar

**YJ&DS SCRIPTING (48-724)** — Yewon Jang & Diego Serna
48-724 Scripting and Parametric Design, CMU, Fall 2026

A Grasshopper plugin that turns an image into line-only patterns (shape grammar)
for a robotic arm to draw with a marker on a bottle.

```
Image → Patterns (lines) → Projection onto the bottle → Robot path → RobotStudio
```

| Part | 
|---|---|
| Pattern generation | 
| Fabrication (projection, robot path) |

## Folders

```
src/patterns/      Python code – pattern generation 
src/fabrication/   Python code – projection + robot path 
gh/                Grasshopper files
docs/              research, notes, plugin guide
```

## Workflow (GitHub Desktop)

1. **Pull** before you start.
2. Work.
3. **Commit** + **Push** when you finish.

Each person edits only their own files.
