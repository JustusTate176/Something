# Resident Evil: Outbreak

A small keyboard-controlled survival game built with Python and Pygame. Explore the facility, search each room for supplies, fight your way to the Nest Core, and defeat NEMESIS-X.

## Run the game

### Windows executable

Run [`dist/ResidentEvilOutbreak.exe`](dist/ResidentEvilOutbreak.exe). The standalone build includes the Python runtime and Pygame.

### Run from source

Install Python, then install the Pygame-compatible package:

```powershell
python -m pip install pygame-ce
```

From the repository root, start the game with:

```powershell
python re_tb.py
```

Use `python -B re_tb.py` to prevent Python from creating new `__pycache__` files during the run.

## How to play

Start at the menu with **Enter**. Move through the facility with **M**. Each room allows up to three searches with **S**; searches can find ammo, credits, nothing, or occasionally disturb a weak enemy. Searching is limited per room, and the remaining count is saved with the game.

In combat, choose among three attacks:

| Key | Attack | Effect |
| --- | --- | --- |
| **1** or **A** | Quick strike | Standard weapon damage; uses no ammo |
| **2** | Aimed shot | Improves critical chance; uses 1 ammo |
| **3** | Heavy shot | Deals more damage; uses 2 ammo |

Other controls:

| Key | Action |
| --- | --- |
| **F** | Use First Aid, if carried |
| **R** | Attempt to escape combat |
| **K** | Spend a skill point on Vitality |
| **H** | Buy First Aid while exploring for 100 credits |
| **F5** / **F9** | Save / load |
| **Esc** | Quit from the title menu |

Attacks have short visual effects. Defeated enemies award experience and credits and drop an item. The game saves to `save.json` in the current working directory.

## Project layout

- `re_tb.py` — compatibility launcher.
- `resident_evil_outbreak/main.py` — Pygame setup and keyboard event loop.
- `resident_evil_outbreak/state.py` — player, room, inventory, and combat state.
- `resident_evil_outbreak/data.py` — room, enemy, weapon, event, and loot definitions.
- `resident_evil_outbreak/enemy.py` — `Enemy` class.
- `resident_evil_outbreak/combat.py` — enemy spawning, attacks, and combat rewards.
- `resident_evil_outbreak/systems.py` — messages, leveling, healing, and save/load.
- `resident_evil_outbreak/rendering.py` — game, menu, and combat drawing and effects.
- `dist/ResidentEvilOutbreak.exe` — standalone Windows build.

## Rebuild the Windows executable

Install PyInstaller and build from the repository root:

```powershell
python -m pip install pyinstaller
python -m PyInstaller --onefile --windowed --name ResidentEvilOutbreak re_tb.py
```

The result is written to `dist/ResidentEvilOutbreak.exe`.
