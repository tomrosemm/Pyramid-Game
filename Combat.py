#Tweak hp values on death of player or enemy to go from a negative to 0

#Import libraries
import random #Choosing from range for damage in combat
import time #Sleeping in combat for better flow

def calculateDamageRange(player):
    #Takes player dictionary, checks for sword or axe, returns augmented damage range for strongest match or base range if none found
    
    if player["hasAxe"] and not player["hasSword"]:
        #Sword stronger, so check first if we only have axe
        return (
            player["baseDamageRange"][0] + player["axeBonus"][0],
            player["baseDamageRange"][1] + player["axeBonus"][1]
        )
    
    elif player["hasSword"]:
        #Sword stronger, so if we have sword at all, match here
        return (
            player["baseDamageRange"][0] + player["swordBonus"][0],
            player["baseDamageRange"][1] + player["swordBonus"][1]
        )
    
    return player["baseDamageRange"]

def combat(player,enemy):
    #If return True, battle was won, if False, lost and player died

    print("__________________________________________________")
    print()

    print(f"Entering combat with {enemy['name']}!")
    print()
    
    while player["health"] > 0 and enemy["health"] > 0:
        
        #Player attack
        playerDamageRange = calculateDamageRange(player)
        playerDamage = random.randint(*playerDamageRange)
        enemy["health"] -= playerDamage
        time.sleep(1.5)
        print(f"{player['name']} attacks for {playerDamage} damage!")
        
        if enemy["health"] <= 0:
            print(f"{enemy['name']} has been defeated!")
            print()
            print(f"Combat ended. {player['name']} health: {player['health']}, {enemy['name']} health: 0")
            print()
            print("__________________________________________________")
            return True
        
        #Enemy attack
        enemyDamage = random.randint(*enemy["damageRange"])
        player["health"] -= enemyDamage
        time.sleep(1.5)
        print(f"{enemy['name']} attacks for {enemyDamage} damage!")
        
        if player["health"] <= 0:
            print(f"{player['name']} has been defeated!")
            print()
            print(f"Combat ended. {player['name']} health: 0, {enemy['name']} health: {enemy['health']}")
            print()
            print("__________________________________________________")
            print()
            return False

if __name__ == '__main__':
    
    player = {
        "name": "TestPlayer",
        "maxHealth": 100,
        "health": 100,
        "baseDamageRange": (10,20),
        "hasAxe": False,
        "hasSword": False,
        "axeBonus": (5, 10),
        "swordBonus": (10,15),
        "hasTorch": False
    }

    tombGoblin = {
        "name": "Goblin Fred",
        "health": 50,
        "damageRange": (3,10)
}
    
    mummy = {
        "name": "The Mummy",
        "health": 75,
        "damageRange": (4, 10)
}
    
    combat(player, tombGoblin)
