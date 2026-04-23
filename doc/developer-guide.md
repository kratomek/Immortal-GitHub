# Immortal - Developer Guide

![JavaScript](https://img.shields.io/badge/javascript-ES6-f7df1e?style=flat-square&logo=javascript&logoColor=black)

This document is a **guide for new developers** or designers working on Immortal: running locally, editing maps and data, and using debug shortcuts.

## 1. Requirements

- **2+ GB RAM** recommended
- **Browser:** modern ES6+ (Chrome, Edge, Firefox)
- **JavaScript** enabled
- **Storage:** LocalStorage, IndexedDB, SessionStorage
- **Tiled** (optional): edit `.tmx` / `.tmj` collision maps
- **Python 3** (optional): local static file server (`server.py`)

## 2. Running locally

The game can be opened as `index.html`, but a **local server** avoids browser restrictions and matches production paths (service worker, `fetch`, etc.).

```bash
cd Immortal
py server.py
```

Then open `http://127.0.0.1:5500/` (or `http://localhost:5500/`).

From the repo root you can also run `npm start` if you use the npm script wrapper.

## 3. Project structure

| Path | Role |
|------|------|
| `src/core/` | Engine loop (`engine.js`), init, security, utils, UI helpers |
| `src/game/` | Gameplay: movement, collision, combat, AI, items, spawner, status |
| `src/input/` | Keyboard, gamepad, unified `inputHandler` |
| `src/map/` | Tiled exports, `collisionMap.js`, map helpers |
| `src/data/` | Persistence, auth, statistics, `dataManager` |
| `src/config/` | `config.js`, controls, positions (`ourPlayer`, etc.) |
| `src/locales/` | `en` / `cs` / `zh` strings and `i18n.js` |
| `src/multiplayer/` | Experimental multiplayer / second player |
| `src/server/` | Client-side server helpers, URLs |
| `src/dev/` | Debug tools, error logs, **tests** (`src/dev/test/test.js`) |
| `doc/` | Controls, credits, changelog, this guide |

## 4. Editing the map (`collisionMap.js`)

1. Open the map (`.tmx`, `.tmj`, or exported `.js`) in **Tiled**.
2. Edit tile layers and collision as needed.
3. Export or save the collision data in the format your pipeline expects.
4. Merge the result into `src/map/collisionMap.js` (see existing structure).

## 5. Saving and loading data

- **LocalStorage** holds UI state, login profile, positions, HP, gold, items, and similar keys.
- **IndexedDB** (`DataDB` / `dbConfig` in `src/config/config.js`) is used for larger or structured data (see `src/data/indexedDB.js`).

Example:

```javascript
localStorage.setItem("PlayerPos", JSON.stringify(ourPlayer));
```

```javascript
const raw = localStorage.getItem("PlayerPos");
if (!raw) return;
const savedPlayer = JSON.parse(raw);
ourPlayer.x = savedPlayer.x;
ourPlayer.y = savedPlayer.y;
```

Player defaults are created in `src/config/config.positions.js` (`window.ourPlayer`).

## 6. Debug shortcuts

| Key | Action |
|-----|--------|
| **F3** | Toggle debug mode: shows collision map (red walls), player hitbox, fog of war visibility polygon (green), sets HP to 100, speed to max, gold to 9999 |
| **F2** | Factory reset: clears IndexedDB, localStorage, sessionStorage, console; reloads page |

### Debug Features (F3)
- **Collision Map Visualization**: Red overlay showing walls and collision tiles
- **Player Hitbox**: Red outline showing player collision area
- **Fog of War Polygon**: Green polygon showing current line of sight visibility
- **Infinite HP**: HP set to 100 continuously
- **Max Speed**: Player speed set to dev.maxSpeed
- **Infinite Gold**: Gold set to 9999
- **Performance**: Visibility polygon throttled to 1000ms for minimal FPS impact
