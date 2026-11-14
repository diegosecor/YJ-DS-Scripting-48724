# Guide: building and installing the YJ&DS plugin

How to turn our Python scripts into a plugin that installs in Rhino 8
(the green Grasshopper `.gha` file, plus the Rhino commands).

> **Requirement:** Rhino 8 on both computers. A plugin built from Python
> does not work in Rhino 7.

---

## 1. Files the plugin produces

| File | Icon | Contains | Purpose |
|---|---|---|---|
| `YJDS.gha` | green grasshopper | Grasshopper components (grammar, systems, layers) | a **YJ&DS** tab appears in Grasshopper |
| `YJDS.rhp` | Rhino | Rhino commands (e.g. project onto the bottle) | typed in the command line |
| `YJDS-x.y.z.yak` | package | both of the above | one-step install |

---

## 2. Create the plugin (once)

1. In Rhino type `ScriptEditor`.
2. **File → New Project** → save it in the repo's `plugin/` folder
   with the name `YJDS`.
3. In the project properties:
   - **Name:** `YJDS`
   - **Version:** `0.1.0`
   - **Author:** Yewon Jang & Diego Serna
   - **Description:** Shape grammar line patterns for robotic bottle drawing
4. **Add Rhino commands** (the scripts we already have):
   right click on *Commands* → **Add existing script** → pick the `.py`
   (e.g. `src/fabrication/bottle_lines.py`).
   Suggested name: `YJDS_BottleLines`.
5. **Add Grasshopper components:**
   right click on *Grasshopper* → **Add component** (or *Add existing script*):
   - **Name:** component name (e.g. `Subdivision Grammar`)
   - **Nickname:** short name (e.g. `SubGram`)
   - **Category:** `YJ&DS`  ← keeps them all in the same tab
   - **Subcategory:** `1 Image`, `2 Structure`, `3 Systems`, `4 Fabrication`
   - **Inputs / Outputs:** name and type of each one
   - **Icon:** 24×24 px PNG (optional, keep them in `plugin/icons/`)

---

## 3. Build (every new version)

1. Open the `plugin/YJDS` project in the `ScriptEditor`.
2. Bump the **Version** (e.g. `0.1.0` → `0.2.0`).
3. Click **Build**.
4. The `.gha`, `.rhp` and `.yak` files appear in the project's output folder
   (`plugin/build/`).
5. Commit + Push with the message `Plugin v0.2.0`.

---

## 4. Install the plugin

### Option A: the green `.gha` file (Grasshopper only)

1. In Grasshopper: **File → Special Folders → Components Folder**.
2. Copy `YJDS.gha` into that folder.
3. Right click the file → **Properties** → tick **Unblock**
   (if it shows) → OK.
4. Restart Rhino.
5. Open Grasshopper: the **YJ&DS** tab appears.

*Shortcut:* drag the `.gha` straight onto the Grasshopper canvas.

### Option B: the `.yak` package (Rhino + Grasshopper together)

1. Drag `YJDS-x.y.z.yak` onto the Rhino window.
2. Restart Rhino.
3. The commands (`YJDS_...`) and the **YJ&DS** tab are installed.

### Updating to a new version

1. **Pull** in GitHub Desktop.
2. Close Rhino.
3. Replace the `.gha` (or drag the new `.yak`).
4. Open Rhino.

---

## 5. Common problems

| Problem | Fix |
|---|---|
| The YJ&DS tab doesn't appear | Unblock the `.gha` (step 4A-3) and restart Rhino |
| "Assembly could not be loaded" | Make sure it is Rhino 8 |
| Duplicated components | Two versions installed: delete the old one from the *Components Folder* |
| A component fails on `import` | Missing libraries (e.g. `opencv-python`): add `# r: opencv-python` at the top of the script |
| The command doesn't show up in Rhino | Reinstall the `.yak`, or check *Tools → Options → Plug-ins* that `YJDS` is enabled |

---

## 6. Recommended workflow

```
Daily development   →  .gh in gh/ + code in src/   (fast changes, no build)
Stable component    →  add it to the plugin/YJDS project
Milestone / handin  →  Build → new .gha / .yak version → Commit + Push
```
