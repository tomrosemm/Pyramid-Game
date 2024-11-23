import random
import time

player = {
    "name": "Player",
    "health": 100,
    "baseDamageRange": (10,20),
    "hasAxe": False,
    "hasSword": False,
    "axeBonus": (5, 10),
    "swordBonus": (10,15)
}

tombGoblin = {
    "name": "Goblin Fred",
    "health": 75,
    "damageRange": (5,15)
}

def calculateDamageRange(player):
    
    if player["hasAxe"] and not player["hasSword"]:
        return (
            player["baseDamageRange"][0] + player["axeBonus"][0],
            player["baseDamageRange"][1] + player["axeBonus"][1]
        )
    
    elif player["hasSword"]:
        return (
            player["baseDamageRange"][0] + player["swordBonus"][0],
            player["baseDamageRange"][1] + player["swordBonus"][1]
        )
    
    return player["baseDamageRange"]

def combat(player,enemy):
    print(f"TIME TO FIGHT A {enemy['name']}!")
    
    while player["health"] > 0 and enemy["health"] > 0:
        
        #Player attack
        playerDamageRange = calculateDamageRange(player)
        playerDamage = random.randint(*playerDamageRange)
        enemy["health"] -= playerDamage
        time.sleep(1.5)
        print(f"{player['name']} attacks for {playerDamage} damage!")
        
        if enemy["health"] <= 0:
            print(f"{enemy['name']} has been defeated!")
            break
        
        #Enemy attack
        enemyDamage = random.randint(*enemy["damageRange"])
        player["health"] -= enemyDamage
        time.sleep(1.5)
        print(f"{enemy['name']} attacks for {enemyDamage} damage!")
        
        if player["health"] <= 0:
            print(f"{player['name']} has been defeated!")
            break
    
    print(f"Combat ended. {player['name']} health: {player['health']}, {enemy['name']} health: {enemy['health']}")

combat(player,tombGoblin)
