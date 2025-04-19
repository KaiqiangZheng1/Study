import random
import time

class Character:
    def __init__(self, name, health, attack_power, defense):
        self.name = name
        self.health = health
        self.max_health = health  # Store max health for resetting
        self.attack_power = attack_power
        self.defense = defense

    def attack(self, opponent):
        damage = random.randint(self.attack_power - 3, self.attack_power + 3)
        damage = max(1, damage - opponent.defense)  # Ensure at least 1 damage
        opponent.take_damage(damage)
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0

    def get_status(self):
        return f"{self.name}: {self.health} HP"

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 15, 3)
        self.exp = 0
        self.level = 1

    def heal(self):
        heal_amount = random.randint(8, 15)
        self.health += heal_amount
        self.health = min(self.health, self.max_health)  # Cap at max health
        print(f"{self.name} heals for {heal_amount} HP!")

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} gained {amount} EXP! Total EXP: {self.exp}")
        while self.exp >= 100:  # Level up if EXP reaches 100
            self.exp -= 100
            self.level_up()

    def level_up(self):
        self.level += 1
        self.attack_power += 2  # Increase attack power
        self.defense += 1  # Increase defense
        self.max_health += 10 # Increase max health
        self.health = self.max_health  # Restore health
        print(f"🎉 {self.name} leveled up! Now Level {self.level} | Attack Power: {self.attack_power}")

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name, random.randint(50, 70), 12, 2)
        self.exp_reward = random.randint(200, 250)

class Boss(Character):
    def __init__(self, name):
        super().__init__(name, 120, 20, 5)
        self.exp_reward = 100
