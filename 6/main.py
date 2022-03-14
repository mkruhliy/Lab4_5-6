import game_custom

lviv = game_custom.City("Lviv")
kyiv = game_custom.City("Kyiv")
symu = game_custom.City("Symu")
zaporizhzhia = game_custom.City("Zaporizhzhia")
mykolaiv = game_custom.City("Mykolaiv")
mariupol = game_custom.City("Mariupol")

me = game_custom.MainCharacter('Captain Price', 100, 'very nice guy')
gun1 = game_custom.Gun("AR15", 25)
me.set_gun(gun1)

aptechka = game_custom.Support('aptechka', 30)
lviv.set_item(aptechka)
lviv.link_city([None,kyiv])

moskal = game_custom.Enemy('moskal', 60, 'simple')
gun2 = game_custom.Gun("kalash", 30)
moskal.set_gun(gun2)
kyiv.set_character(moskal)
kyiv.link_city([lviv,symu])

podorozhnyk = game_custom.Support('podorozhnyk', 15)
symu.set_item(podorozhnyk)
symu.link_city([kyiv, zaporizhzhia])

katsap = game_custom.Enemy('kstsap', 28, 'simple')
gun3 = game_custom.Gun('Mosin rifle', 10)
katsap.set_gun(gun3)
zaporizhzhia.set_character(katsap)
zaporizhzhia.link_city([symu, mykolaiv])

salo = game_custom.Support('salo', 20)
mykolaiv.set_item(salo)
mykolaiv.link_city([zaporizhzhia, mariupol])

korabl = game_custom.SuperEnemy("ruskiy korabl", 100, 'super')
gun4 = game_custom.Gun('artileriya', 10)
korabl.set_gun(gun4)
mariupol.set_character(korabl)
mariupol.link_city([mykolaiv, None])


current_city = lviv

dead = False

#start
print("\nSLAVA UKRAINI and Welcome to the game GAME\n\
  _____  _    _  _____ _  _________     __  _  ______  _____            ____  _      \n\
 |  __ \| |  | |/ ____| |/ /_   _\ \   / / | |/ / __ \|  __ \     /\   |  _ \| |     \n\
 | |__) | |  | | (___ | ' /  | |  \ \_/ /  | ' / |  | | |__) |   /  \  | |_) | |     \n\
 |  _  /| |  | |\___ \|  <   | |   \   /   |  <| |  | |  _  /   / /\ \ |  _ <| |     \n\
 | | \ \| |__| |____) | . \ _| |_   | |    | . \ |__| | | \ \  / ____ \| |_) | |____ \n\
 |_|  \_\\\____/|_____/|_|\_\_____|  |_|    |_|\_\____/|_|  \_\/_/    \_\____/|______|\n\
\nSmash those russian occupants and God bless you!\n")
print("-"*38+"\ntype 'help' any time to see game rules\n"+"-"*38)
print("\n\n\n\
       .---.\n\
      /_____\\\n\
      ( \'.\' )\n\
       \_-_/_\n\
    .-\"`\'V\'//-.\n\
   / ,   |// , \\\n\
  / /|Ll //Ll|\ \\\n\
 / / |__//   | \_\\\n\
 \ \/---|[]==| / /\n\
  \/\__/ |   \/\/\n\
   |/_   | Ll_\|\n\
     |  \"\"\"  |\n\
     |   |   |\n\
     |   |   |\n\
     |   |   |\n\
     |   |   |\n\
     L___l___J\n\
      |_ | _|\n\
     (___|___)\n\
      ^^^ ^^^")
me.get_description()
(me.get_gun()).get_description('Your')
start = input("\n\nWould you like to start?(y/n) \n> ")
if start != 'y':
    dead = True

print('-'*50)

while dead == False:

    print('\n')
    print('Your HP: {}\nGun damage: {}'. format(me.get_hp(), (me.get_gun()).get_dm()))

    if len(me.backpack_capacity()) != 0:
        print("Your backpack: {}".format(me.backpack_repr()))
    else:
        print("Your backpack: Empty")

    current_city.get_details()

    inhabitant = current_city.get_character()
    if inhabitant is not None:
        inhabitant.get_description()

    item = current_city.get_item()
    if item is not None:
        item.get_description()

    if inhabitant is None and item is None:
        current_city.empty_city()

    command = input("> ")

    if command == "go":
        if inhabitant:
                print("WIN ENEMY TO GO AHEAD")
        else:
            current_city_posible = current_city.get_link()[1]
            if current_city_posible is not None:
                current_city = current_city_posible
            else:
                print("YOU ARE ON THE FINAL STREET")

    elif command == "back":
        current_city_posible = current_city.get_link()[0]
        if current_city_posible is not None:
            current_city = current_city_posible
        else:
            print("YOU ARE ON THE START LINE")

    elif command == 'fight':
        if inhabitant is not None:
            a =  me.fight(inhabitant)
            if a == "me dead":
                dead = True
            if a == 'dead':
                if inhabitant.get_type() == 'simple':
                    print("Enemy gun dropped: \nGun: {} - damage: {}".format((inhabitant.get_gun()).get_name(), (inhabitant.get_gun()).get_dm()))
                    chs = input("\nWOULD YOU LIKE TO TAKE ENEMYS GUN?(y/n)> ")
                    if chs == "y":
                        me.set_gun(inhabitant.get_gun())
                        print('\n')
                        (me.get_gun()).get_description('Your NEW')
                if inhabitant.get_type() == 'super':
                    if inhabitant.final() == True:
                        print("You won! Congrads!\n\nUKRAINA PONAD USE")
                    else:
                        print('idi v sraku, moskalyu')
                    dead = True
                current_city.character = None
        else:
            print("THERE IS NOBODY TO FIGHT WITH")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            me.append_backpack(item)
            current_city.set_item(None)
        else:
            print("THERE IS NOTHING HERE TO TAKE")

    elif command == 'help':
        print("\n<<<helper>>>\n\
  Your aim: Kill all enemies and to stay alive\n\
  Collect meds on your way and use them whenever you need\n\
  COMMANDS:\n\
  > go  - to move ahead\n\
  > back  - to move back\n\
  > fight  - to shoot your enemy(check your, enemy HP and gun damage level befor shooting)\n\
  > take  - to put the meds you found to the backpack\n\
  to USE the meds from the backpack simply type its name\n")

    else:
        if len(me.backpack_capacity()) == 0:
            print("enter valid command")

        for meds in me.backpack_capacity():
            if command == meds.get_name():
                me.heal(meds)
                print("YOUR HP NOW: {}".format(me.get_hp()))
                me.backpack_capacity().remove(meds)
            else:
                print("enter valid command")
