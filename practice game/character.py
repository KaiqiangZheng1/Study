import random

class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, other):
        # Calculate random damage between (attack_power-3) and attack_power
        # Ensure minimum damage is 1
        base_damage = max(1, random.randint(self.attack_power - 3, self.attack_power))
        # Apply defense reduction
        damage = max(0, base_damage - other.defense)
        
        other.take_damage(damage)
        print(f"{self.name} attacks {other.name} for {damage} damage!")
        
        if not other.is_alive():
            print(f"{other.name} has been defeated!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage!")
        print(f"{self.name}'s health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
    
    def get_status(self):
        return {
            "name": self.name,
            "health": self.health,
            "attack_power": self.attack_power,
            "defense": self.defense
        }