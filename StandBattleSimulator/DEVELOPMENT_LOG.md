# Stand Battle Simulator --- Development Log

## Project Overview

**Project:** Stand Battle Simulator\
**Language:** Python\
**Testing:** pytest\
**Development period:** November 4--18, 2026\
**Current focus:** Turn-based battle engine, Stand abilities, cooldowns,
and test-driven development

This project started as a larger portfolio project based on the idea of
building a turn-based battle simulator inspired by JoJo's Bizarre
Adventure. The goal was to move beyond a simple Stand stat card and
build an actual battle system with different statistics, attacks, turn
order, and special abilities.

The project was developed incrementally. Each major feature was tested
before moving on to the next part. A major focus throughout development
was making sure the battle rules worked correctly and fixing problems as
they appeared.

## Development Progress

### Stand Foundation

The project began with the `Stand` class. A Stand has six main
statistics: Power, Speed, Range, Durability, Precision, and Potential.
Each statistic uses grades A through E, and invalid grades are rejected.

Health was then added. Each Stand starts with 100 HP. Damage cannot
reduce HP below zero, negative damage is rejected, and healing cannot
raise HP above 100.

### Damage and Combat

The damage system uses Power and the target's Durability. Speed was
added to determine which Stand attacks first.

A separate `Battle` class was created to manage two Stands, the current
attacker, the current target, turn switching, and the battle-ending
condition.

The battle loop continues until one Stand is defeated.

### Debugging the Core System

As the battle system became more complicated, the test suite exposed
several problems.

One early problem was that `Stand.take_damage()` only accepted damage,
while the attack system needed to pass the attacking Stand as well. This
caused a `TypeError`. The method was updated to accept an optional
attacker.

Another issue occurred when the reflection system attempted to use an
attacker variable that did not exist in the method's scope. Passing the
attacker through the damage call fixed this.

These failures showed why automated tests were useful: they identified
exactly where the new mechanics did not match the existing Stand
interface.

### Cooldowns

Cooldowns were added for abilities. A Stand can have an ability, an
ability cooldown, and a remaining cooldown. An ability cannot be used
while its cooldown is active, and cooldowns are reduced after turns.

### Damage Reflection

Damage reflection was the first major special ability. A Stand with
Reflection sends part of the damage it receives back to the attacker.

This required the damage system to know who caused the damage, which led
directly to passing the attacker into `take_damage()`.

### Time Stop

Time Stop was added as a rule-changing ability. A Stand can mark its
opponent as time-stopped. When that opponent's turn comes up, it loses
its turn instead of attacking. The time-stop state is then cleared.

A bug occurred where a time-stopped Stand still attacked because the
normal attack was outside the correct `else` block. Fixing the
indentation corrected the behavior.

Tests were added for Time Stop activation, skipped turns, clearing the
state, and cooldown behavior.

### Rewind

Rewind was added as another rule-changing ability. The Stand stores its
previous HP before taking damage, allowing Rewind to restore the
previous HP value.

The battle system was also updated so a Stand with Rewind can use it
during battle after taking damage.

During debugging, a Rewind battle test had the ability assigned to the
wrong Stand. The test was corrected. Another test temporarily had
`ReflectAbility()` where Rewind was intended; that was also corrected.

### Ability Architecture Refactor

The project originally represented abilities mainly with strings such as
`"rewind"`, `"time_stop"`, and `"reflect"`.

As more abilities were added, an `abilities.py` module was created with
an `Ability` base class and separate `RewindAbility`, `TimeStopAbility`,
and `ReflectAbility` classes.

The refactor was done gradually so existing behavior would continue
working. The current code supports both the older string-based abilities
and the newer ability objects.

This is a transitional architecture. The next step is to finish moving
the remaining ability behavior into the ability classes and remove the
hard-coded string checks.

## Testing Milestone

The project currently has **33 automated tests**.

Latest successful result:

``` text
collected 33 items

33 passed in 0.31s
```

The tests cover Stand statistics, validation, health, damage, healing,
attacks, speed, abilities, cooldowns, Reflection, Time Stop, Rewind, and
the main battle loop.

## What I Learned

### Testing catches problems early

The test suite caught problems that were easy to miss by only reading
the code. Running the tests made it clear when a new feature broke an
existing part of the system.

### Features can affect existing code

Adding Reflection changed the damage system because the game needed to
know who caused the damage. A small new feature can require changes to
older methods.

### Special abilities need their own structure

Normal attacks follow predictable rules, while Time Stop and Rewind
change the rules of the battle itself. This made an ability system
necessary instead of placing every special case directly into the battle
loop.

### Refactoring should be gradual

The ability refactor did not work perfectly on the first attempt because
existing tests still depended on the old string-based system. Supporting
both systems temporarily allowed the project to stay functional while
the architecture improved.

### Debugging is part of development

Several of the most useful improvements came directly from test
failures. Fixing those failures helped reveal how the Stand, ability,
and battle systems interact.

## Current State

Completed:

-   Stand statistics
-   Grade validation
-   Health
-   Damage
-   Healing
-   Durability-based damage
-   Speed-based turn order
-   Turn switching
-   Battle loop
-   Battle ending conditions
-   Ability cooldowns
-   Damage Reflection
-   Time Stop
-   Rewind
-   Basic ability-object architecture
-   Automated testing

The project is now moving from a working prototype toward a cleaner
portfolio project.

## Next Steps

1.  Finish the ability architecture refactor.
2.  Remove remaining hard-coded ability string checks.
3.  Add more rule-changing abilities.
4.  Improve type hints and consider strict `mypy` checking.
5.  Add battle logging.
6.  Build a replay system.
7.  Improve the README with setup instructions and examples.
8.  Add an architecture diagram.
9.  Improve core test coverage toward the 80%+ goal.
10. Prepare the project for a future GUI or web interface.

## Milestone Summary

  Milestone                 Status
  ------------------------- -------------
  Stand class               Complete
  Stand grade validation    Complete
  Health system             Complete
  Damage system             Complete
  Speed system              Complete
  Turn-based battle         Complete
  Battle loop               Complete
  Cooldowns                 Complete
  Damage Reflection         Complete
  Time Stop                 Complete
  Rewind                    Complete
  Ability architecture      In progress
  Additional abilities      Planned
  Replay system             Planned
  Logging                   Planned
  Strict type checking      Planned
  GUI/Web interface         Future
  Portfolio documentation   In progress

## Final Status for This Development Period

The project has moved from a basic Stand-stat concept into a functioning
turn-based battle engine. The current major milestone is **33 passing
automated tests** while supporting multiple special abilities.

The next phase is focused on improving the architecture, expanding the
ability system, and polishing the project into something suitable for a
software-development portfolio.
