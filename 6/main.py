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

class Character:
    def __init__(self, name, description, hp) -> None:
        self.name = name
        self.description = description
        self.hp = hp
        self.item = None
    def set_gun(self, gun):
        self.item = gun
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

class Item:
    def __init__(self, name, dm) -> None:
        self.name = name
        self.dm = dm

class Support(Item):
    def __init__(self, name, dm) -> None:
        super().__init__(name, dm)
    def store_items(self):
        pass

class Gun(Item):
    def __init__(self, name ,dm) -> None:
        super().__init__(name, dm)
    def update_gun(self, dm):
        self.dm += dm


struyska = Street("vul. Struyska")
kozelnutska = Street("vul. Kozelnutska")

me = Character('Markiyan', 'very nice guy', 70)
gun1 = Gun("ar15", 30)
me.set_gun(gun1)

moskal = Character('Korabyl', 'idi nahuy', 80)
gun2 = Gun("kolash", 30)
moskal.set_gun(gun2)
kozelnutska.set_character(moskal)

aptechka = Support('podorozhnyk', 20)
struyska.set_item(aptechka)

struyska.link_street(kozelnutska)

current_street = struyska

dead = False
body_count = 0
backpack = []

while dead == False:

    if body_count == 1:
        print('congrads')
        break

    print('\n')
    current_street.get_details()
    if len(backpack) != 0:
        print("your elems {}".format([x.name for x in backpack]))
    
    inhabitant = current_street.character
    if inhabitant is not None:
        print("Your opponent: {}  -  {}   -  hp: {}".format(inhabitant.name, inhabitant.description, inhabitant.hp))
    
    item = current_street.item
    if item is not None:
        print("Items here: {}  -  hp: {}".format(item.name, item.dm))
    
    command = input("> ")

    if command == "ahead":
        current_street = current_street.link
    
    elif command == 'fight':
        if inhabitant is not None:
            a =  me.fight(inhabitant)
            if a == "me dead":
                dead = True
            if a == 'dead':
                body_count += 1

    elif command == "take":
        if item is not None:
            print("You put the " + item.name + " in your backpack")
            backpack.append(item)
            current_street.set_item(None)
        else:
            print("There's nothing here to take!")
    
    for x in backpack:
        if command == x.name:
            me.heal(x)
            print("your hp now {}".format(me.hp))
            backpack.remove(x)
