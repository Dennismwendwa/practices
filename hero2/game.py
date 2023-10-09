from random import randint, shuffle

HEROLIFE = 0
HEROPOWER = 0

VILLAINLIFE = 0
VILLAINPOWER = 0

class Charactor:
    def __init__(self, name: str, power: int, life: int):
        self.name = name
        self.power = power
        self.life = life


    def __str__(self):
        return f"{self.name} {self.power} {self.life}"


# superheros
class SuperHero(Charactor):
    def __init__(self, name, power, life):
        super().__init__(name, power, life)


class Villain(Charactor):
    def __init__(self, name, power, life):
        super().__init__(name, power, life)

# superheros
SolarFlare = SuperHero("SolarFlare", 800, 9)
ShadowStrike = SuperHero("ShadowStrike", 700, 8)
NovaKnight = SuperHero("NovaKnight", 500, 7)
AquaSorceress = SuperHero("AquaSorceress", 550, 6)
MechaMonarch = SuperHero("MechaMonarch", 600, 6)

# villians
ToxicTerror = Villain("ToxicTerror", 1400, 10)
PhantomThief = Villain("PhantomThief", 1500, 9)
Enigma = Villain("Enigma", 1000, 15)
NexusNemesis = Villain("NexusNemesis", 1300, 11)


superHeroList = [SolarFlare, ShadowStrike, NovaKnight, AquaSorceress, MechaMonarch]
villainList = [ToxicTerror, PhantomThief, Enigma, NexusNemesis]

attackingSuperHeroTeam = []
attackingVillianTeam = []

def play(superHeroList, villainList):

    shuffle(superHeroList)

    shuffle(villainList)

    for h in range(3):
        attackingSuperHeroTeam.append(superHeroList[h])

    for v in range(2):
        attackingVillianTeam.append(villainList[v])
        
    attack()


def powerBalance(heroLife, villainLife, heropower, villainpower):
    
    heroDieRate = 10
    villainDieRate = 8

    newheropower, newvillainpower = basic_attack(heropower, villainpower)
    
    newHeroLife = heroLife - (heroLife * 10 / 100)
    newVillainLife = villainLife - (villainLife * 10 / 100)

    return newHeroLife, newVillainLife, newheropower, newvillainpower

def basic_attack(heropower, villainpower):
    print("Hero power", heropower)
    print("Villain power", villainpower)
    if heropower >= 30:
        damage = ((40 / 100) * villainpower)
        heropower -= 30
        villainpower -= damage
    elif heropower >= 10:
        damage = ((20 / 100) * villainpower)
        heropower -= 10
        villainpower -= damege

    if villainpower >= 30:
        damage = ((40 / 100) * heropower)
        villainpower -= 30
        heropower -= damage
    elif villainpower >= 10:
        damage = ((20 / 100) * heropower)
        villainpower -= 10
        heropower -= damege
    print()
    print("Hero power", heropower)
    print("Villain power", villainpower)
    print()

    return heropower, villainpower


def attack():

    global VILLAINLIFE
    global VILLAINPOWER

    global HEROLIFE
    global HEROPOWER

    VILLAINLIFE = attackingVillianTeam[0].life + attackingVillianTeam[1].life
    VILLAINPOWER = attackingVillianTeam[0].power + attackingVillianTeam[1].power
    print(VILLAINPOWER)
    for hero in attackingSuperHeroTeam:
        HEROLIFE += hero.life
        HEROPOWER += hero.power
    print(HEROPOWER)
    for h in range(3):
        herofinallife, villianFinallife, heropower, villainpower = powerBalance(
                HEROLIFE, VILLAINLIFE, HEROPOWER, VILLAINPOWER)
        
        HEROLIFE = herofinallife
        HEROPOWER = heropower
        VILLAINLIFE = villianFinallife
        VILLAINPOWER = villainpower

    if herofinallife > villianFinallife:
        print("Hero Team have won")
    elif herofinallife == villianFinallife:
        print("Its a tier game")
    else:
        print("Villian team have won")



def game():
    count = 1
    gameplay = True
    while gameplay:
        play(superHeroList, villainList)
        count += 1
        print()
        if count > 1:
            gameplay = False


if __name__ == "__main__":
    game()
