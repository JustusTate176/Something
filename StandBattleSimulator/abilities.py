class Ability:
    def use(self, user, target=None):
        raise NotImplementedError


class RewindAbility(Ability):
    def use(self, user, target=None):
        user.hp = user.previous_hp
        return True


class TimeStopAbility(Ability):
    def use(self, user, target=None):
        if target is None:
            return False

        target.is_time_stopped = True
        return True


class ReflectAbility(Ability):
    def reflect_damage(self, user, attacker, damage):
        reflected_damage = round(damage * 0.5)
        attacker.take_damage(reflected_damage)