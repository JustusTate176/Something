# Stand Battle Simulator --- Changelog

## Development Period: November 4--18, 2026

### Added

-   Created the `Stand` class with six Stand statistics.
-   Added A--E grade validation.
-   Added 100 HP starting health.
-   Added damage and healing systems.
-   Added HP floor and maximum-health rules.
-   Added Power-based attack damage.
-   Added Durability-based damage modification.
-   Added Speed-based turn priority.
-   Created the `Battle` class.
-   Added alternating turns.
-   Added automatic battle completion when a Stand is defeated.
-   Added ability cooldown tracking.
-   Added damage Reflection.
-   Added Time Stop.
-   Added Rewind.
-   Added an `Ability` base class.
-   Added `RewindAbility`.
-   Added `TimeStopAbility`.
-   Added `ReflectAbility`.
-   Added tests for the major battle mechanics.

### Changed

-   Updated `take_damage()` to receive the attacking Stand when needed.
-   Updated attacks so the attacker is passed through the damage system.
-   Added previous-HP tracking for Rewind.
-   Updated battle turns to handle Time Stop.
-   Updated battle turns to allow Rewind during combat.
-   Added cooldown reduction after turns.
-   Began transitioning from string-based abilities to ability objects.
-   Kept compatibility with older string-based abilities during the
    refactor.

### Fixed

-   Fixed damage Reflection not knowing which Stand should receive
    reflected damage.
-   Fixed a missing attacker reference in the damage system.
-   Fixed Time Stop still allowing an affected Stand to attack.
-   Fixed Rewind being assigned to the wrong Stand in a battle test.
-   Fixed a test accidentally using `ReflectAbility` where Rewind was
    intended.
-   Fixed compatibility problems between the new ability objects and
    existing string-based ability tests.

### Testing

-   Expanded the automated test suite to **33 tests**.
-   Current result: **33 passed, 0 failed**.

### In Progress

-   Finish the ability architecture refactor.
-   Remove remaining hard-coded string ability checks.
-   Add more special abilities.
-   Improve type hints and static checking.
-   Add logging and replay functionality.
-   Improve portfolio documentation.
