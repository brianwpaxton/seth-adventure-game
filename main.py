from character import *
from attack import *
from place import *
from action import *
import random
import constants


def ask_question(question, options):
    print(question)
    option_number = 1
    for option in options:
        print(option_number, ".", option)
        option_number += 1

    choice = int(input())
    answer = options[choice - 1]
    print("You chose", answer)

    return answer


def fight(level, player, the_monsters, additional_attacks):
    player.reset_hp()
    monster = ask_question("Who would you like to fight?", the_monsters)

    while monster.hp > 0 and player.hp > 0:
        player_attack = ask_question("Choose your attack...", player.attacks)
        monster.hp -= player_attack.damage

        print(f"The {monster}'s HP is now {monster.hp}")

        if monster.hp > 0:
            monster_attack = random.choice(monster.attacks)
            player.hp -= monster_attack.damage

            print(f"The monster attacked you with a {monster_attack.name}, your HP is now {player.hp}")

    if monster.hp <= 0:
        print("hooray, you have defeated the opposing monster")
        new_attack = random.choice(additional_attacks)
        player.attacks.append(new_attack)
        additional_attacks.remove(new_attack)
        the_monsters.remove(monster)
        print("You've earned a new attack", new_attack)
        print("\n ==========================\n")
        print("Congratulations you've completed level", level+1)
        level += 1
        return level

    else:
        print("oh no the monster has defeated you.")


def fight_carnival(player, monster, _additional_attacks):
    player.reset_hp()
    monster.reset_hp()
    accuracy_range = [0, 0.3, 0.5, 1]

    print(f"you bumped into {monster.name} its health is {monster.hp}")
    while monster.hp > 0 and player.hp > 0:
        player_attack = ask_question("Choose your attack...", player.attacks)
        monster.hp -= player_attack.damage

        print(f"The {monster}'s HP is now {monster.hp}")

        if monster.hp > 0:
            monster_attack = random.choice(monster.attacks)
            accuracy = random.choice(accuracy_range)
            if accuracy < 1:
                print("Your opponents accuracy fell")

            player.hp -= accuracy * monster_attack.damage

            print(f"The monster attacked you with a {monster_attack.name}, your HP is now {player.hp}")

    if monster.hp <= 0:
        print("hooray, you have defeated the opposing monster")

        if len(_additional_attacks) > 0:
            new_attack = random.choice(_additional_attacks)
            player.attacks.append(new_attack)
            _additional_attacks.remove(new_attack)
            print("You've earned a new attack", new_attack)
        print("\n ==========================\n")

    else:
        print("oh no the monster has defeated you.")


def create_kitchen():
    the_kitchen = Place("kitchen")
    action_make_goblin_goulash = Action("make goblin goulash")
    action_make_cyclops_sandwich = Action("make cyclops sandwich")
    action_make_siren_sausage = Action("make siren sausage")
    action_make_killer_cake = Action("make killer cake")
    the_kitchen.actions = [action_make_siren_sausage, action_make_killer_cake, action_make_goblin_goulash,
                           action_make_cyclops_sandwich]
    return the_kitchen


def create_bedroom():
    bedroom = Place("your bedroom")
    action_put_on_suit = Action("to put on suit")
    action_put_on_monster_hunting_gear = Action("to put on monster hunting gear")
    action_put_on_monster_fight_club_outfit = Action("to put on monster fight club outfit")
    action_put_on_casual_clothes = Action("to put on casual clothes")
    bedroom.actions = [action_put_on_suit, action_put_on_monster_hunting_gear, action_put_on_casual_clothes,
                       action_put_on_monster_fight_club_outfit]
    return bedroom


def create_level_1_attacks():
    fireball = Attack("fireball", 20)
    energy_pulse = Attack("energy pulse", 30)
    sound_wave = Attack("sound wave", 50)
    blazing_inferno = Attack("blazing inferno", 40)

    super_jolt = Attack("super jolt", 40)
    return [fireball, energy_pulse, sound_wave, blazing_inferno , super_jolt]




def create_additional_player_attacks():
    lazer_beam = Attack("lazer beam", 60)
    combo_strike = Attack("combo strike", 30)
    trio_bash = Attack("trio bash", 50)
    deep_sea_smash = Attack("deep sea smash", 70)
    hiden_power = Attack("hiden power", 70)
    return [lazer_beam, combo_strike]


def create_level_2_attacks():
    canon_blast = Attack("canon blast", 50)
    extreme_force = Attack("extreme force", 30)
    tectonic_boom = Attack("tectonic boom", 40)
    splash_wheel = Attack("splash wheel", 40)
    internal_terror = Attack("internal terror", 40)
    wave_knockout = Attack("wave knockout", 50)
    frozen_temper = Attack("frozen temper", 50)
    return [canon_blast, extreme_force, tectonic_boom, splash_wheel, internal_terror, wave_knockout, frozen_temper]


def create_level_1_monsters(l1_attacks):
    the_attacks = random.choices(l1_attacks, k=4)
    minotaur = Character("Minotaur", 70, the_attacks)
    goblin = Character("The goblin", 80, the_attacks)
    cyclops = Character("cyclops", 100, the_attacks)
    return [minotaur, goblin, cyclops]


def create_level_2_monsters(l2_attacks):
    the_attacks = random.choices(l2_attacks, k=4)
    ancient_king = Character("Ancient King", 120, the_attacks)
    sorcerer = Character("Sorcerer", 90, the_attacks)
    fire_knight = Character("Fire Knight", 100, the_attacks)
    return [ancient_king, sorcerer, fire_knight]


def create_level_3_monsters(l3_attacks):
    the_attacks = random.choices(l3_attacks, k=4)
    THE_CREATURE_OF_THE_DEPTHS = Character("THE CREATURE OF THE DEPTHS", 136, the_attacks)


def create_level_3_attacks():
    spectrum_spell = Attack("spectrum spell", 100)
    sweet_tears = Attack("sweet tears", 0)
    blank = Attack("blank", 0)
    lollypop_tooth = Attack("lollypop tooth", 0)

def create_carnival_1_attacks():
    noble_flame = Attack("noble flame", 50)
    tornado_burst = Attack("tornado burst", 50)
    tsunami_blitz = Attack("tsunami blitz", 50)
    wild_fangs = Attack("wild fangs", 50)
    suprime_shot = Attack("suprime shot", 50)
    return [noble_flame, suprime_shot, wild_fangs, tornado_burst, tsunami_blitz]


def create_carnival_1_monsters(c_attacks, carnical_boss_attacks):
    the_attacks = random.choices(c_attacks, k=4)
    dragon_of_fire = Character("dragon of fire", 130, the_attacks)
    dragon_of_waves = Character("dragon of waves", 130, the_attacks)
    dragon_of_nature = Character("dragon of nature", 130, the_attacks)
    dragon_of_wind = Character("dragon of wind", 130, the_attacks)
    ultimate_dragon = Character("ultimate dragon", 150, carnical_boss_attacks)
    return [dragon_of_fire, dragon_of_waves, dragon_of_nature, dragon_of_wind, ultimate_dragon]


def fight_carnival_monsters(carnival_monsters, _additional_attacks):
    for monster in carnival_monsters:
        fight_carnival(player1, monster, _additional_attacks)
        if player1.hp <= 0:
            return


level = constants.LEVEL_1

attacks = [create_level_1_attacks(), create_level_2_attacks(), create_level_3_attacks()]
monsters = [create_level_1_monsters(attacks[constants.LEVEL_1]), create_level_2_monsters(attacks[constants.LEVEL_2]), create_level_3_monsters(attacks[constants.LEVEL_3])]

carnival_attacks = []
carnival_attacks.extend(create_level_1_attacks())
carnival_attacks.extend(create_level_2_attacks())

carnival_monsters = create_carnival_1_monsters(carnival_attacks, create_carnival_1_attacks())


player1 = Character("player 1", 200, attacks[level])
additional_attacks = create_additional_player_attacks()
forest_of_mysteries = Place("Forest of Mysteries")
sapphire_beach = Place("Sapphire Beach")
battle_arena = Place("Battle Arena")
monster_fight_club = Place("Monster Fight Club")
my_house = Place("My House")
creepy_carnival = Place("Creepy Carnival")

amazica = Place("Amazica")
amazica.destinations = [forest_of_mysteries, sapphire_beach]

forest_of_mysteries.destinations = [monster_fight_club, battle_arena]
sapphire_beach.destinations = [my_house, creepy_carnival]

your_bedroom = create_bedroom()
kitchen = create_kitchen()
my_house.destinations = [kitchen, your_bedroom]

current_place = amazica

print("Welcome to Amazica")
while True:
    current_place = ask_question("Would you like to go to?", current_place.destinations)

    if current_place == monster_fight_club or current_place == battle_arena:
        level = fight(level, player1, monsters[level], additional_attacks)
        current_place = amazica
    elif current_place == your_bedroom:
        ask_question("would you like...", your_bedroom.actions)
        current_place = amazica
    elif current_place == kitchen:
        ask_question("would you like to ", kitchen.actions)
        current_place = amazica
    elif current_place == creepy_carnival:
        fight_carnival_monsters(carnival_monsters, additional_attacks)
        current_place = amazica
