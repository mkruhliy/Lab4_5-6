class City:
    """place for main action"""
    def __init__(self, name=None) -> None:
        self.name = name
        self.character = None
        self.item = None
        self.link = None
    def set_character(self, character):
        """setting character in the city"""
        self.character = character
    def set_item(self, item):
        """setting item in the city"""
        self.item = item
    def get_details(self):
        """getting city name"""
        print("\n                 "+self.name)
    def link_city(self, city):
        """setting connecting cities"""
        self.link = city
    def get_character(self):
        """getting city character"""
        return self.character
    def get_item(self):
        """getting city item"""
        return self.item
    def get_link(self):
        """getting cities connected with the current"""
        return self.link
    def empty_city(self):
        """presentation of the empty city"""
        print('      O \n\
     /|\ \n\
_____/_\____________________________________')


class Character:
    """characters and their general behaviour"""
    def __init__(self, name=None, hp=None) -> None:
        self.name = name
        self.hp = hp
        self.item = None
    def get_hp(self):
        """getting character health points"""
        return self.hp
    def set_gun(self, gun):
        """setting a gun for the character"""
        self.item = gun
    def get_gun(self):
        """getting character's gun"""
        return self.item


class MainCharacter(Character):
    """main character behaviour"""
    def __init__(self, name=None, hp=None, description=None) -> None:
        super().__init__(name, hp)
        self.description = description
        self.item = None
        self.backpack = []
    def backpack_capacity(self):
        """getting backpack items"""
        return self.backpack
    def append_backpack(self, elem):
        """adding items to the backpack"""
        self.backpack.append(elem)
    def backpack_repr(self):
        """getting backpack items but in the pretty-looking form"""
        return [x.name for x in self.backpack]
    def get_description(self):
        """getting description of the main character"""
        print("Your soldier: {}\nHP: {}\n'{}'".format(self.name, self.hp, self.description))
    def heal(self, obj):
        """adding haelth points"""
        self.hp += obj.dm
    def fight(self, chr):
        """commiting a battle"""
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
    """enemy behaviour"""
    def __init__(self, name=None, hp=None, tp=None) -> None:
        super().__init__(name, hp)
        self.item = None
        self.type = tp
    def get_description(self):
        """getting description of the enemy"""
        print("      O_,~-                     -~,_O\n\
     /|                             |\n\
_____/_\___________________________/_\______\nYour opponent: {} -  hp:{}\n(type 'fight' to attack)".format(self.name, self.hp))
    def get_type(self):
        """getting if 'simple' or 'super' enemy"""
        return self.type


class SuperEnemy(Enemy):
    """'super' enemy behaviour"""
    def  __init__(self, name=None, hp=None, tp=None) -> None:
        super().__init__(name, hp, tp)
        self.item = None
    def get_description(self):
        """getting description of the 'super' enemy"""
        print("	                      __/___\n\
      O_,~-             _____/______| \n\
     /|         _______/_____\_______\_____ \n\
_____/_\_______ \              < < <       |\n\
Your SUPER OPPONENT: {}  -  hp:{}\n(type 'fight' to attack)".format(self.name, self.hp))
    def final(self):
        """final exam to be passed for a win"""
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
    """item general behaviour"""
    def __init__(self, name=None, dm=None) -> None:
        self.name = name
        self.dm = dm
    def get_name(self):
        """getting item's name"""
        return self.name
    def get_dm(self):
        """getting item's damage points"""
        return self.dm


class Gun(Item):
    """gun behaviour"""
    def __init__(self, name=None, dm=None) -> None:
        super().__init__(name, dm)
    def get_description(self, obj):
        """getting description of the gun"""
        print('-'*18+'\n{} Gun: {} \ndamage: {}\n  ︻╦╤───\n'.format(obj, self.name, self.dm)+'-'*18)


class Support(Item):
    """medicaments behaviour"""
    def __init__(self, name=None, dm=None) -> None:
        super().__init__(name, dm)
    def get_description(self):
        """meds description"""
        print("      O                 _______  \n\
     /|\               |  aid  |        \n\
_____/_\_______________|_______|____________\n\
Meds found here: {}  -  hp: {}\n(type 'take' to put in the backpack)".format(self.name, self.dm))
