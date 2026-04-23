# Immortal - Project Architecture

## Overview
Immortal is a web-based 2D game inspired by League of Legends, built with vanilla JavaScript, HTML, and CSS. The game features a top-down view with combat mechanics, enemy AI, and various game systems.

## Project Structure

```
Immortal/
├── src/
│   ├── config/           # Configuration files (data only, no logic)
│   │   ├── config.js              # General configuration
│   │   ├── config.controls.js     # Key bindings
│   │   ├── config.positions.js    # Entity positions
│   │   ├── difficulty.config.js   # Difficulty settings
│   │   ├── gameplay.balance.js    # Game balance settings
│   │   ├── lasthit.config.js      # Last hit system settings
│   │   └── turret.config.js       # Turret settings
│   ├── core/             # Core engine and utility functions
│   │   ├── difficulty.js          # Difficulty helper functions
│   │   ├── engine.js              # Main game loop
│   │   ├── gameplay.feedback.js   # Feedback systems
│   │   ├── init.js                # Initialization
│   │   ├── playability.js         # HUD and playability
│   │   ├── security.js            # Security functions
│   │   ├── ui.controls.js         # UI control logic
│   │   └── utils.js               # Utility functions
│   ├── game/             # Game-specific logic
│   │   ├── ai.js                  # Enemy AI
│   │   ├── balance.js             # Balance helper functions
│   │   ├── collision.js           # Collision detection
│   │   ├── combat.state.js        # Combat state management
│   │   ├── combat.structures.js   # Structure combat logic
│   │   ├── combat.units.js        # Unit combat logic
│   │   ├── items.js               # Item system
│   │   ├── movement.js            # Movement logic
│   │   ├── spawner.js             # Entity spawning
│   │   ├── status.js              # Game status checks
│   │   └── turret.plating.js      # Turret plating system
│   ├── data/             # Data persistence
│   │   ├── auth.js                # Authentication
│   │   ├── dataInit.js            # Data initialization
│   │   ├── dataManager.js         # Data management
│   │   ├── indexedDB.js           # IndexedDB wrapper
│   │   └── statistics.js          # Player statistics
│   ├── input/            # Input handling
│   │   ├── inputHandler.js        # Input event handling
│   │   └── keyboard.js            # Keyboard input
│   ├── map/              # Map system
│   │   ├── collisionMap.js        # Collision map data
│   │   └── map.js                 # Map rendering
│   ├── multiplayer/      # Multiplayer features
│   │   ├── multiplayerClient.js   # Multiplayer client
│   │   ├── secondPlayer.js        # Second player logic
│   │   └── shared-worker.js       # Shared worker
│   ├── styles/           # CSS styles
│   ├── locales/          # Internationalization
│   │   ├── en.js                  # English
│   │   ├── cs.js                  # Czech
│   │   ├── zh.js                  # Chinese
│   │   └── i18n.js                # i18n system
│   └── dev/              # Development tools
│       ├── debug.js               # Debug utilities
│       ├── errorLogs.js           # Error logging
│       └── test/                  # Test files
├── doc/                # Documentation
├── audio/              # Audio files
├── fonts/              # Font files
├── img/                # Images
└── index.html          # Main HTML file
```

## Key Components

### Configuration System
- **Purpose**: Centralized configuration without logic
- **Location**: `src/config/`
- **Pattern**: Only data/variables, no functions
- **Usage**: Loaded before game logic, referenced by helper functions

### Core Engine
- **engine.js**: Main game loop using `requestAnimationFrame` with throttled updates for performance
- **init.js**: Game initialization and setup
- **utils.js**: Shared utility functions including fog of war implementation
- **chat.js**: Chat system with auto-close functionality
- **playability.js**: HUD and entity visibility management

### Game Loop
The game loop runs in `engine.js` with the following flow:
1. Update UI elements (HP, gold, damage, speed) - throttled to 100ms
2. Update health bar
3. Update playability HUD
4. Handle fog of war (if enabled)
5. Process keyboard input
6. Move player
7. Check player movement
8. Update player hitbox
9. Update turret AI
10. Update enemy AI
11. Update minion AI
12. Update entity visibility by vision - throttled to 100ms
13. Handle camera scroll (if gameCamera disabled) - throttled to 50ms
14. One-second loop: heal, save data, check turrets, update rank

### Combat System
- **combat.state.js**: Manages combat state for all entities
- **combat.units.js**: Unit-specific combat (minions, animals, enemy)
- **combat.structures.js**: Structure-specific combat (turrets, nexus)
- **lasthit system**: Bonus gold for last hitting minions

### AI System
- **ai.js**: Enemy AI behavior
- **turret AI**: Turret targeting and attack logic
- **minion AI**: Minion pathfinding and combat

### State Management
- Game state stored in global variables (hp, gold, damage, etc.)
- Combat state managed in `unitCombatState` and `turretCombatState` objects
- Data persistence via IndexedDB

### Input System
- **inputHandler.js**: Global input event handling
- **keyboard.js**: Keyboard-specific input processing
- Key bindings defined in `config.controls.js`

### Rendering
- DOM-based rendering (no canvas for game elements)
- Entity positions updated via CSS `top`/`left`
- HP bars rendered in `playability.js`
- Floating combat text in `gameplay.feedback.js`
- Debug overlay uses canvas for collision map and visibility polygon visualization

## Data Flow

1. **Initialization**: `init.js` loads configs and initializes state
2. **Game Loop**: `engine.js` runs continuous updates
3. **Input**: `inputHandler.js` captures events → `keyboard.js` processes
4. **Logic**: Game systems process input and update state
5. **Rendering**: UI updates reflect state changes
6. **Persistence**: `dataManager.js` saves to IndexedDB

## Difficulty System
- Three modes: easy, normal, hardcore
- Configured in `difficulty.config.js`
- Helper functions in `core/difficulty.js`
- Affects: HP, damage, gold rewards, spawn rates

## Fog of War
- Implemented in `utils.js` using CSS mask-image radial gradient
- Line of sight checks via ray casting in `hasLineOfSight()`
- Entity visibility caching with 100ms expiry
- Distance threshold: 520px
- Radius: 300px
- Update interval: 66ms (throttled)
- HP bars hidden for entities behind walls (line of sight check)
- Debug visualization available via F3 in development mode

## Performance Considerations
- DOM caching in `utils.js` via `window.domCache`
- RequestAnimationFrame for smooth rendering
- Throttled updates:
  - UI updates: 100ms
  - Visibility updates: 100ms
  - Camera scroll: 50ms
  - Fog of war: 66ms
- Entity visibility caching (100ms expiry)
- Efficient collision detection using collision map
- Debug visibility polygon throttled to 1000ms

## Extension Points
- **New entities**: Add to config.positions.js, create combat handlers
- **New items**: Add to items.js, update config.js
- **New difficulty**: Add to difficulty.config.js
- **New language**: Add to locales/ folder
