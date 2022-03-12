class Street:
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
        print(self.name)
        print("--------------------")
    def link_street(self, street):
        self.link = street
    def get_character(self):
        return self.character
    def get_item(self):
        return self.item
    def get_link(self):
        return self.link

class Character:
    def __init__(self, name, description, hp) -> None:
        self.name = name
        self.description = description
        self.hp = hp
        self.item = None
    def get_hp(self):
        return self.hp
    def set_gun(self, gun):
        self.item = gun
    def get_gun(self):
        return self.item

class Main_Character(Character):
    def __init__(self, name, description, hp) -> None:
        super().__init__(name, description, hp)
        self.item = None
        self.backpack = []
        self.body_count = 0
    def backpack_(self):
        return self.backpack
    def append_backpack(self, elem):
        self.backpack.append(elem)
    def backpack_repr(self):
        return [x.name for x in self.backpack]
    def get_description(self):
        print('Your soldier: {}\n{}\nHP: {}'.format(self.name, self.description, self.hp))
    def get_body_count(self):
        return self.body_count
    def plus_body_count(self):
        self.body_count += 1
    def heal(self, obj):
        self.hp += obj.dm
    def fight(self, chr):
        self.hp -= chr.item.dm
        chr.hp -= self.item.dm
        if self.hp <=0:
            if self.hp > chr.hp:
                print("He lost")
                self.hp += chr.item.dm
                return 'dead'
            else:
                print("You lost")
                return "me dead"
        if chr.hp<=0:
            print("He lost")
            return 'dead'
        else:
            print("{} - your, {} - his".format(self.hp, chr.hp))
    def change_gun(self, gun):
        self.item = gun

class Enemy(Character):
    def __init__(self, name, description, hp) -> None:
        super().__init__(name, description, hp)
        self.item = None
    def get_description(self):   # добав ше дамаг ворога
        print("Your opponent: {}  -  {}   -  hp:{}".format(self.name, self.description, self.hp))

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
        print('{} Gun: {} - dm: {}'.format(obj, self.name, self.dm))
    def update_gun(self, dm):
        pass

class Support(Item):
    def __init__(self, name, dm) -> None:
        super().__init__(name, dm)
    def get_description(self):
        print("Items here: {}  -  hp: {}".format(self.name, self.dm))


struyska = Street("vul. Struyska")
kozelnutska = Street("vul. Kozelnutska")
franka = Street("vul. Franka")
shevchenka = Street("vul. Shevchenka")

me = Main_Character('Markiyan', 'very nice guy', 70)
gun1 = Gun("ar15", 30)
me.set_gun(gun1)

aptechka = Support('aptechka', 20)
struyska.set_item(aptechka)
struyska.link_street([None,kozelnutska])

moskal = Enemy('moskal', 'v pizdu', 80)
gun2 = Gun("kolash", 30)
moskal.set_gun(gun2)
kozelnutska.set_character(moskal)
kozelnutska.link_street([struyska,franka])

podorozhnyk = Support('podorozhnyk', 5)
franka.set_item(podorozhnyk)
franka.link_street([kozelnutska ,shevchenka])

korabl = Enemy("ruskiy korabl", "idi nahuy", 40)
gun3 = Gun('artileriya', 40)
korabl.set_gun(gun3)
shevchenka.set_character(korabl)
shevchenka.link_street([shevchenka, None])

current_street = struyska

dead = False

#start
print('welcome to the game GAME\n\n')
me.get_description()
print('\n')
(me.get_gun()).get_description('Your')


while dead == False:
    
    print('\n')
    print('Your HP:{}'. format(me.get_hp()))
    current_street.get_details()

    if len(me.backpack_()) != 0:
        print("your backpack: {}".format(me.backpack_repr()))  #print("your elems {}".format([x.name for x in backpack]))
    
    inhabitant = current_street.get_character()
    if inhabitant is not None:
        inhabitant.get_description()    #print("Your opponent: {}  -  {}   -  hp: {}".format(inhabitant.name, inhabitant.description, inhabitant.hp))
        (inhabitant.get_gun()).get_description('His')

    item = current_street.get_item()
    if item is not None:
        item.get_description()    #print("Items here: {}  -  hp: {}".format(item.name, item.dm))
    
    command = input("> ")

    if command == "ahead":
        if inhabitant:
                print("win enemy first")
        else:
            current_street_posible = current_street.get_link()[1]
            if current_street_posible != None:
                current_street = current_street_posible
            else:
                print("You are on the final street")

    elif command == "back":
        current_street_posible = current_street.get_link()[0]
        if current_street_posible != None:
            current_street = current_street_posible
        else:
            print("you are on the start line")

    elif command == 'fight':
        if inhabitant is not None:
            a =  me.fight(inhabitant)
            if a == "me dead":
                dead = True
            if a == 'dead':
                me.plus_body_count()

                if me.get_body_count() == 2:
                    print('congradddddds - won')
                    dead = True
                else:
                    print("gun dropped: {} - hp: {}".format((inhabitant.get_gun()).get_name(), (inhabitant.get_gun()).get_dm()))
                    chs = input("would you like to take > ")
                    if chs == "yes":
                        me.set_gun(inhabitant.get_gun())
                        print('\n')
                        (me.get_gun()).get_description('Your')

                current_street.character = None

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            me.append_backpack(item)
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")

    elif command == 'help':
        print("\n<<<helper>>>")

    for x in me.backpack_():
        if command == x.get_name():
            me.heal(x)
            print("your hp now {}".format(me.get_hp()))
            me.backpack_().remove(x)
