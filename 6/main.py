class City:
    def __init__(self, name) -> None:
        self.name = name
        self.character = None
        self.item = None
        self.link = None
    def set_character(self, character):
        self.character = character
    def set_item(self, item):
        self.item = item
    def get_details(self):
        print("\n                 "+self.name)
    def link_city(self, city):
        self.link = city
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
    def get_link(self):
        return self.link
    def empty_city(self):
        print('      O \n\
     /|\ \n\
_____/_\____________________________________')

class Character:
    def __init__(self, name, hp) -> None:
        self.name = name
        self.hp = hp
        self.item = None
    def get_hp(self):
        return self.hp
    def set_gun(self, gun):
        self.item = gun
    def get_gun(self):
        return self.item

class Main_Character(Character):
    def __init__(self, name, hp, description) -> None:
        super().__init__(name, hp)
        self.description = description
        self.item = None
        self.backpack = []
    def backpack_capacity(self):
        return self.backpack
    def append_backpack(self, elem):
        self.backpack.append(elem)
    def backpack_repr(self):
        return [x.name for x in self.backpack]
    def get_description(self):
        print("Your soldier: {}\nHP: {}\n'{}'".format(self.name, self.hp, self.description))
    def heal(self, obj):
        self.hp += obj.dm
    def fight(self, chr):
        self.hp -= chr.item.dm
        chr.hp -= self.item.dm
        if self.hp <=0:
            if self.hp > chr.hp:
                print("He's DEAD")
                self.hp += chr.item.dm
                return 'dead'
            else:
                print("You're DEAD")
                return "me dead"
        if chr.hp<=0:
            print("He's DEAD")
            return 'dead'
        else:
            print("HP now: {} - your, {} - enemys".format(self.hp, chr.hp))

class Enemy(Character):
    def __init__(self, name, hp, typee) -> None:
        super().__init__(name, hp)
        self.item = None
        self.type = typee
    def get_description(self):
        print("      O_,~-                     -~,_O\n\
     /|                             |\n\
_____/_\___________________________/_\______\nYour opponent: {} -  hp:{}\n(type 'fight' to attack)".format(self.name, self.hp))
    def get_type(self):
        return self.type

class SuperEnemy(Enemy):
    def  __init__(self, name, hp, typee) -> None:
        super().__init__(name, hp, typee)
        self.item = None
    def get_description(self):
        print("	                      __/___\n\
      O_,~-             _____/______| \n\
     /|         _______/_____\_______\_____ \n\
_____/_\_______ \              < < <       |\n\
Your SUPER OPPONENT: {}  -  hp:{}\n(type 'fight' to attack)".format(self.name, self.hp))
    def final(self):
        first = input("\nBut to win the russian regime answer those questions.\n\
Your final exam:\n'Ruskiy korabl idi ... '?:\n1) nahuy\n2) domoy\n3) palanitsa\n > ")
        if first != '1':
            return False
        second = input("\nBatko nash ...: ?\n1) Petlura\n2) Biden\n3) Bandera\n> ")
        if second != '3':
            return False
        third = input("\nDobruy ... Mu z Ukrainu ?\n1) ranok\n2) palanitsa\n3) vechir\n> ")
        if third != '3':
            return False
        return True

class Item:
    def __init__(self, name, dm) -> None:
        self.name = name
        self.dm = dm
    def get_name(self):
        return self.name
    def get_dm(self):
        return self.dm

class Gun(Item):
    def __init__(self, name, dm) -> None:
        super().__init__(name, dm)
    def get_description(self, obj):
        print('-'*18+'\n{} Gun: {} \ndamage: {}\n  ︻╦╤───\n'.format(obj, self.name, self.dm)+'-'*18)

class Support(Item):
    def __init__(self, name, dm) -> None:
        super().__init__(name, dm)
    def get_description(self):
        print("      O                 _______  \n\
     /|\               |  aid  |        \n\
_____/_\_______________|_______|____________\n\
Meds found here: {}  -  hp: {}\n(type 'take' to put in the backpack)".format(self.name, self.dm))


lviv = City("Lviv")
kyiv = City("Kyiv")
dnipro = City("Dnipro")
mariupol = City("Mariupol")

me = Main_Character('Captain Price', 70, 'very nice guy')
gun1 = Gun("AR15", 30)
me.set_gun(gun1)

aptechka = Support('aptechka', 20)
lviv.set_item(aptechka)
lviv.link_city([None,kyiv])

moskal = Enemy('moskal', 60, 'simple')
gun2 = Gun("kalash", 30)
moskal.set_gun(gun2)
kyiv.set_character(moskal)
kyiv.link_city([lviv,dnipro])

podorozhnyk = Support('podorozhnyk', 5)
dnipro.set_item(podorozhnyk)
dnipro.link_city([kyiv, mariupol])

korabl = SuperEnemy("ruskiy korabl", 40, 'super')
gun3 = Gun('artileriya', 10)
korabl.set_gun(gun3)
mariupol.set_character(korabl)
mariupol.link_city([dnipro, None])


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
  Collect meds on your way and use them if whenever you need\n\
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
