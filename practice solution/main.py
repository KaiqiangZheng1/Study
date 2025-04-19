from game import Player, Enemy, Boss
import random
import time

def battle(player, enemy):
    print("\n⚔️ Battle Start! ⚔️\n")
    
    while player.is_alive() and enemy.is_alive():
        print(f"\n{player.get_status()}  |  {enemy.get_status()}")
        
        action = input("\nChoose action (attack/heal/defend): ").lower()
        
        if action == "attack":
            player.attack(enemy)
        elif action == "heal":
            player.heal()
        elif action == "defend":
            print(f"{player.name} braces for impact! (Reduced damage this turn)")
            enemy_attack = random.randint(enemy.attack_power - 3, enemy.attack_power + 3)
            enemy_attack = max(1, enemy_attack - player.defense * 2)  # Reduce damage
            player.take_damage(enemy_attack)
            print(f"{enemy.name} attacks for {enemy_attack} damage (Reduced)")
        else:
            print("Invalid action, you lose a turn!")

        if (enemy.is_alive() and action != "defend"):
            time.sleep(1)
            enemy.attack(player)

    print("\n⚔️ Battle Over! ⚔️\n")
    if player.is_alive():
        print(f"🎉 {player.name} wins!")
    else:
        print(f"💀 {player.name} was defeated...")

# Game Start
player_name = input("Enter your hero's name: ")
player = Player(player_name)

enemy1 = Enemy("Goblin")
enemy2 = Enemy("Orc")
boss = Boss("Dark Lord")

for opponent in [enemy1, enemy2, boss]:
    battle(player, opponent)
    if player.is_alive():
        player.gain_exp(opponent.exp_reward)
        print(f"{player.name} gained {opponent.exp_reward} EXP!")
        time.sleep(1)
    else:
        break
    # if not player.is_alive():
    #     break

print("\nGame Over!")
