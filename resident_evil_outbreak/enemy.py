"""Enemy entity and its combat state."""


class Enemy:
    """Store the combat attributes and phase state for one enemy."""

    def __init__(self, name, hp, damage, xp):
        """Create an enemy with its name, health, damage range, and experience reward."""
        self.name = name
        self.hp = hp
        self.damage = damage
        self.xp = xp
        self.phase2 = False

    def status(self):
        """Return a short display string containing the enemy's name and health."""
        return f"{self.name}: {self.hp} HP"
