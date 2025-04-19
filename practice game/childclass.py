from character import Character

class Player(Character):
    def __init__(self, name, health, attack_power, defense, level=1):
        super().__init__(name, health, attack_power, defense)
        self.level = level

    def level_up(self):
        self.level += 1
        self.attack_power += 5
        self.defense += 2
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"New stats - Attack Power: {self.attack_power}, Defense: {self.defense}")



class Enemy(Character):
    def __init__(self, name, health, attack_power, defense, loot):
        super().__init__(name, health, attack_power, defense)
        self.loot = loot

    def drop_loot(self):
        print(f"{self.name} dropped {self.loot}!")



class Boss:
    pass