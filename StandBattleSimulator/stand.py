from abilities import Ability

VALID_GRADES = ["A", "B", "C", "D", "E"]

POWER_DAMAGE = {
    "A": 30,
    "B": 25,
    "C": 20,
    "D": 15,
    "E": 10
}

DURABILITY_MULTIPLIER = {
    "A": 0.70,
    "B": 0.80,
    "C": 0.90,
    "D": 1.00,
    "E": 1.10
}

SPEED_PRIORITY = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
    "E": 1
}



class Stand:
    def __init__(
    self,
    name,
    power,
    speed,
    range,
    durability,
    precision,
    potential,
    hp=100,
    ability=None,
    ability_cooldown=0
):
        self.name = name
        self.power = self._validate_grade(power)
        self.speed = self._validate_grade(speed)
        self.range = self._validate_grade(range)
        self.durability = self._validate_grade(durability)
        self.precision = self._validate_grade(precision)
        self.potential = self._validate_grade(potential)
        self.hp = hp
        self.previous_hp = hp
        self.ability = ability
        self.ability_cooldown = ability_cooldown
        self.ability_cooldown_remaining = 0
        self.is_time_stopped = False

    def _validate_grade(self, grade):
        if grade not in VALID_GRADES:
            raise ValueError(f"Invalid Stand grade: {grade}. Must be one of {VALID_GRADES}")

        return grade

    def take_damage(self, damage, attacker=None):
        if damage < 0:
            raise ValueError("Damage cannot be negative")

        self.previous_hp = self.hp
        self.hp = max(0, self.hp - damage)

        if attacker is not None:
            if self.ability == "reflect":
                reflected_damage = round(damage * 0.5)
                attacker.take_damage(reflected_damage)

        elif isinstance(self.ability, Ability):
            if self.ability.__class__.__name__ == "ReflectAbility":
                self.ability.reflect_damage(self, attacker, damage)

    def is_alive(self):
            return self.hp > 0

    def heal(self, amount):
        if amount < 0:
            raise ValueError("Heal amount cannot be negative")

        self.hp = min(100, self.hp + amount)

    def attack(self, target):
        base_damage = POWER_DAMAGE[self.power]
        multiplier = DURABILITY_MULTIPLIER[target.durability]
        damage = round(base_damage * multiplier)


        target.take_damage(damage, self)

    def get_speed_priority(self):
        return SPEED_PRIORITY[self.speed]

    def use_ability(self):
        if self.ability is None:
            return False

        if self.ability_cooldown_remaining > 0:
            return False

        self.ability(self)
        self.ability_cooldown_remaining = self.ability_cooldown

        return True

    def reduce_cooldown(self):
        if self.ability_cooldown_remaining > 0:
            self.ability_cooldown_remaining -= 1

    def use_time_stop(self, target):
        if self.ability_cooldown_remaining > 0:
            return False

        if self.ability == "time_stop":
            target.is_time_stopped = True

        elif isinstance(self.ability, Ability):
            if self.ability.__class__.__name__ != "TimeStopAbility":
                return False

            if not self.ability.use(self, target):
                return False

        else:
            return False

        self.ability_cooldown_remaining = self.ability_cooldown

        return True

    def use_rewind(self):
        if self.ability_cooldown_remaining > 0:
            return False

        if self.ability == "rewind":
            self.hp = self.previous_hp

        elif isinstance(self.ability, Ability):
            if self.ability.__class__.__name__ != "RewindAbility":
                return False

            self.ability.use(self)

        else:
            return False

        self.ability_cooldown_remaining = self.ability_cooldown

        return True