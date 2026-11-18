import pytest

from stand import Stand

from abilities import RewindAbility


def test_star_platinum():
    stand = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )


    assert stand.name == "Star Platinum"
    assert stand.power == "A"
    assert stand.speed == "A"
    assert stand.range == "C"
    assert stand.durability == "A"
    assert stand.precision == "A"
    assert stand.potential == "A"

def test_invalid_grade():
        try:
            Stand(
                name="Invalid Stand",
                power="Z",  # Invalid grade
                speed="A",
                range="C",
                durability="A",
                precision="A",
                potential="A"
            )


            assert False
        except ValueError:
            assert True

def test_stand_starts_with_100_hp():
    stand = Stand(
        name="Test Stand",
        power="B",
        speed="C",
        range="D",
        durability="E",
        precision="A",
        potential="B"
    )

    assert stand.hp == 100

def test_stand_takes_damage():
    stand = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    stand.take_damage(25)

    assert stand.hp == 75

def test_stand_hp_cannot_go_below_zero():
    stand = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    stand.take_damage(200)

    assert stand.hp == 0

def test_negative_damage_is_rejected():
    stand = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    with pytest.raises(ValueError):
        stand.take_damage(-50)

def test_stand_can_heal():
    stand = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    stand.take_damage(25)
    stand.heal(10)

    assert stand.hp == 85

def test_healing_cannot_exceed_max_hp():
    stand = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    stand.take_damage(25)
    stand.heal(100)

    assert stand.hp == 100

def test_stand_can_attack():
    star_platinum = Stand(
        name="Star Platinum",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    the_world = Stand(
        name="The World",
        power="A",
        speed="A",
        range="C",
        durability="A",
        precision="A",
        potential="A"
    )

    star_platinum.attack(the_world)

    assert the_world.hp == 79

def test_stand_speed_priority():
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

    assert star_platinum.get_speed_priority() == 5
    assert crazy_diamond.get_speed_priority() == 3
    assert star_platinum.get_speed_priority() > crazy_diamond.get_speed_priority()

def test_stand_is_alive():
    star_platinum = Stand(
        "Star Platinum",
        "A",
        "A",
        "C",
        "A",
        "A",
        "A"
    )

    assert star_platinum.is_alive()

    star_platinum.take_damage(100)

    assert not star_platinum.is_alive()

def test_stand_can_use_ability():
    def heal_ability(stand):
        stand.heal(20)
        return True

    star_platinum = Stand(
        "Star Platinum",
        "A",
        "A",
        "C",
        "A",
        "A",
        "A",
        hp=50,
        ability=heal_ability
    )

    result = star_platinum.use_ability()

    assert result is True
    assert star_platinum.hp == 70

def test_ability_has_cooldown():
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
        hp=50,
        ability=heal_ability,
        ability_cooldown=2
    )

    assert star_platinum.use_ability() is True
    assert star_platinum.hp == 70

    assert star_platinum.use_ability() is False
    assert star_platinum.hp == 70

def test_ability_cooldown_decreases():
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
        hp=50,
        ability=heal_ability,
        ability_cooldown=2
    )

    star_platinum.use_ability()

    assert star_platinum.ability_cooldown_remaining == 2

    star_platinum.reduce_cooldown()

    assert star_platinum.ability_cooldown_remaining == 1

    star_platinum.reduce_cooldown()

    assert star_platinum.ability_cooldown_remaining == 0

def test_stand_can_reflect_damage():
    attacker = Stand(
        "Star Platinum",
        "A",
        "A",
        "C",
        "A",
        "A",
        "A"
    )

    defender = Stand(
        "The World",
        "A",
        "A",
        "C",
        "A",
        "A",
        "A",
        ability="reflect"
    )

    attacker.attack(defender)

    assert defender.hp == 79
    assert attacker.hp == 90

def test_stand_can_use_time_stop():
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

    star_platinum.use_time_stop(the_world)

    assert the_world.is_time_stopped is True

def test_time_stop_has_cooldown():
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
    assert star_platinum.use_time_stop(the_world) is False

def test_time_stop_can_be_used_after_cooldown():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A",
        ability="time_stop",
        ability_cooldown=2
    )

    the_world = Stand(
        "The World",
        "A", "A", "C", "A", "A", "A"
    )

    assert star_platinum.use_time_stop(the_world) is True

    star_platinum.reduce_cooldown()
    assert star_platinum.use_time_stop(the_world) is False

    star_platinum.reduce_cooldown()
    assert star_platinum.use_time_stop(the_world) is True

def test_stand_can_rewind_damage():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A",
        ability="rewind",
        ability_cooldown=3
    )

    star_platinum.take_damage(40)

    assert star_platinum.hp == 60

    assert star_platinum.use_rewind() is True
    assert star_platinum.hp == 100

def test_rewind_has_cooldown():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A",
        ability="rewind",
        ability_cooldown=2
    )

    star_platinum.take_damage(40)

    assert star_platinum.use_rewind() is True
    assert star_platinum.hp == 100

    star_platinum.take_damage(30)

    assert star_platinum.use_rewind() is False
    assert star_platinum.hp == 70

def test_rewind_can_be_used_after_cooldown():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A",
        ability="rewind",
        ability_cooldown=2
    )

    star_platinum.take_damage(40)

    assert star_platinum.use_rewind() is True
    assert star_platinum.hp == 100

    star_platinum.take_damage(30)

    star_platinum.reduce_cooldown()
    assert star_platinum.use_rewind() is False

    star_platinum.reduce_cooldown()
    assert star_platinum.use_rewind() is True
    assert star_platinum.hp == 100

def test_rewind_ability_object():
    rewind = RewindAbility()

    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A"
    )

    star_platinum.take_damage(40)

    assert star_platinum.hp == 60

    rewind.use(star_platinum)

    assert star_platinum.hp == 100  

def test_stand_can_use_rewind_ability_object():
    star_platinum = Stand(
        "Star Platinum",
        "A", "A", "C", "A", "A", "A",
        ability=RewindAbility(),
        ability_cooldown=3
    )

    star_platinum.take_damage(40)

    assert star_platinum.hp == 60

    assert star_platinum.use_rewind() is True
    assert star_platinum.hp == 100