from battle import Battle
from stand import Stand
from abilities import RewindAbility, TimeStopAbility, ReflectAbility


def test_faster_stand_attacks_first():
    star_platinum = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    crazy_diamond = Stand(
        name="Crazy Diamond",
        power="A",
        speed="C",
        range="D",
        durability="B",
        precision="B",
        potential="C"
    )

    battle = Battle(star_platinum, crazy_diamond)

    assert battle.get_first_attacker() is star_platinum

def test_first_attacker_takes_a_turn():
    star_platinum = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    crazy_diamond = Stand(
        name="Crazy Diamond",
        power="A",
        speed="C",
        range="D",
        durability="B",
        precision="B",
        potential="C"
    )

    battle = Battle(star_platinum, crazy_diamond)

    battle.take_turn()

    assert crazy_diamond.hp == 76

def test_stands_alternate_turns():
    star_platinum = Stand(
        "Star Platinum",
        "A",
        "A",
        "C",
        "A",
        "A",
        "A"
    )

    crazy_diamond = Stand(
        "Crazy Diamond",
        "A",
        "C",
        "C",
        "B",
        "A",
        "A"
    )

    battle = Battle(star_platinum, crazy_diamond)

    battle.take_turn()

    assert crazy_diamond.hp == 76

    battle.take_turn()

    assert star_platinum.hp == 79

def test_battle_ends_when_stand_is_defeated():
    star_platinum = Stand(
        "Star Platinum",
        "A",
        "A",
        "C",
        "A",
        "A",
        "A"
    )

    crazy_diamond = Stand(
        "Crazy Diamond",
        "C",
        "C",
        "C",
        "B",
        "A",
        "A"
    )

    battle = Battle(star_platinum, crazy_diamond)

    winner = battle.run()

    assert winner is star_platinum
    assert crazy_diamond.hp == 0
    assert star_platinum.hp > 0

def test_battle_reduces_ability_cooldowns():
    def heal_ability(stand):
        stand.heal(20)

    star_platinum = Stand(
        "Star Platinum",
        "A",
        "A",
        "C",
        "A",
        "A",
        "A",
        ability=heal_ability,
        ability_cooldown=2
    )

    crazy_diamond = Stand(
        "Crazy Diamond",
        "C",
        "C",
        "C",
        "B",
        "A",
        "A"
    )

    battle = Battle(star_platinum, crazy_diamond)

    star_platinum.use_ability()

    assert star_platinum.ability_cooldown_remaining == 2

    battle.take_turn()

    assert star_platinum.ability_cooldown_remaining == 1

    battle.take_turn()

    assert star_platinum.ability_cooldown_remaining == 0

def test_time_stopped_stand_skips_turn():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A"
    )

    the_world = Stand(
        "The World",
        "A", "A", "C", "A", "A", "A"
    )

    battle = Battle(star_platinum, the_world)

    the_world.is_time_stopped = True

    # Star Platinum attacks normally.
    battle.take_turn()

    assert the_world.hp == 79

    # The World should skip its turn.
    battle.take_turn()

    assert star_platinum.hp == 100

def test_time_stop_ends_after_one_skipped_turn():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A"
    )

    the_world = Stand(
        "The World",
        "A", "A", "C", "A", "A", "A"
    )

    battle = Battle(star_platinum, the_world)

    the_world.is_time_stopped = True

    # Star Platinum attacks.
    battle.take_turn()

    assert the_world.hp == 79

    # The World skips its turn.
    battle.take_turn()

    assert star_platinum.hp == 100

    # Time Stop should now be over.
    assert the_world.is_time_stopped is False

def test_time_stop_ability():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A",
        ability="time_stop",
        ability_cooldown=3
    )

    the_world = Stand(
        "The World",
        "A", "A", "C", "A", "A", "A"
    )

    assert star_platinum.use_time_stop(the_world) is True
    assert the_world.is_time_stopped is True

def test_stand_can_rewind_during_battle():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A",
        ability="rewind",
        ability_cooldown=3
    )

    the_world = Stand(
        "The World",
        "A", "A", "C", "A", "A", "A",
        ability="rewind",
        ability_cooldown=3
    )

    battle = Battle(star_platinum, the_world)

    the_world.take_damage(40)

    assert the_world.hp == 60

    the_world.use_rewind()

    assert the_world.hp == 100

def test_rewind_can_be_used_during_a_turn():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A"
    )

    the_world = Stand(
        "The World",
        "A", "A", "C", "A", "A", "A",
        ability=RewindAbility(),
        ability_cooldown=3
    )

    battle = Battle(star_platinum, the_world)

    the_world.take_damage(40)

    assert the_world.hp == 60

    battle.attacker = the_world
    battle.target = star_platinum

    battle.take_turn()

    assert the_world.hp == 100