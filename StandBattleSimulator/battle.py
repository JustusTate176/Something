class Battle:
    def __init__(self, stand_one, stand_two):
        self.stand_one = stand_one
        self.stand_two = stand_two

        self.attacker = self.get_first_attacker()

        if self.attacker is self.stand_one:
            self.target = self.stand_two
        else:
            self.target = self.stand_one

    def get_first_attacker(self):
        if self.stand_one.get_speed_priority() >= self.stand_two.get_speed_priority():
            return self.stand_one

        return self.stand_two

    def take_turn(self):
        current_attacker = self.attacker
        current_target = self.target

        if current_attacker.is_time_stopped:
            current_attacker.is_time_stopped = False
        else:
            if (
                (
                    current_attacker.ability == "rewind"
                    or current_attacker.ability.__class__.__name__ == "RewindAbility"
                )
                and current_attacker.hp < current_attacker.previous_hp
        ):
                current_attacker.use_rewind()

            current_attacker.attack(current_target)

        self.stand_one.reduce_cooldown()
        self.stand_two.reduce_cooldown()

        self.attacker = current_target
        self.target = current_attacker

    def run(self):
        while self.stand_one.is_alive() and self.stand_two.is_alive():
            self.take_turn()

        if self.stand_one.is_alive():
            return self.stand_one

        return self.stand_two