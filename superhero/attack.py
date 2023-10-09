from random import randint, shuffle
from game import Characters, Superhero, Villain

def hero_attack_team():

    shuffle(Superhero.superhero_list)
    attack_t = Superhero.superhero_list[:3]
    hero1_attack = attack_t[1]
    hero2_attack = attack_t[2]
    hero3_attack = attack_t[0]

    return hero1_attack, hero2_attack, hero3_attack

def villian_attack_team():

    key = randint(0, 3)
    shuffle(Villain.villian_list)
    villian_attacking = Villain.villian_list[key]

    return villian_attacking

def life(hero_l, villian_l):
    print("life before ", hero_l)
    print("V life befor ", villian_l)

    hero_new_l = hero_l - (hero_l * 0.9)
    villian_new_l = villian_l - (villian_l * 0.8)

    print(hero_new_l)
    print(villian_new_l)

    return hero_new_l, villian_new_l

def attack_now():
    hero1, hero2, hero3 = hero_attack_team()
    villian_attcking = villian_attack_team()

    villains_total_l = villian_attcking.life
    hero_total_l = hero1.life + hero2.life + hero3.life
    
    round_g = 1

    print("Round ", round_g)
    print(villian_attcking, "Attacking now")
    round_g += 1
    print()
    hero_lif, villian_lif = life(hero_total_l, villains_total_l)

    for _ in range(2):
        print("Round ", round_g)
        print(villian_attcking, "Attacking now")
        round_g += 1
        print()

        hero_lif, villian_lif = life(hero_lif, villian_lif)


    if hero_lif > 1 and villian_lif <= 1:
        return "hero_win"
    elif villian_lif > 1 and hero_lif <= 1:
        return "villa_win"
    elif villian_lif > 1 and hero_lif > 1:
        return "draw"


game = attack_now()

if game == "villa_win":
    print("Villans have won")
elif game == "hero_win":
    print("Superheros won")
elif game == "draw":
    print("Draw")




