from childclass import Player, Enemy
import time

def simulate_battle(char1, char2):
    round = 1
    while char1.is_alive() and char2.is_alive():
        print(f"\nRound {round}")
        char1.attack(char2)
        if char2.is_alive():
            char2.attack(char1)
        round += 1
        time.sleep(1)  # Add delay between rounds
    
    winner = char1 if char1.is_alive() else char2
    print(f"\n{winner.name} wins the battle!")

# Test the battle
if __name__ == "__main__":
    hero = Player("Hero", 50, 15, 5)
    monster = Enemy("Goblin", 40, 12, 3,'Gold Coin')
    simulate_battle(hero, monster)