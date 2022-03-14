class Info(object):
    """
    Helping class, indicates the number
    of defeated enemies
    """
    defeated = 0

info = Info()

class Room:
    """Room that keeps items and characters"""
    def __init__(self, room) -> None:
        self.room = room
        self.dscrpt = ''
        self.link = {}
        self.character = None
        self.item = None
    def set_description(self, statment):
        """setting description of the room"""
        self.dscrpt = statment
    def link_room(self, room, side):
        """setting connected room"""
        self.link[side] = room
    def move(self, side):
        """changing room"""
        return self.link[side]
    def get_details(self):
        """representation of the room"""
        print(self.room)
        print("--------------------")
        print(self.dscrpt)
        for key, value in self.link.items():
            print("The {} is {}".format(value.room, key))
    def set_character(self, character):
        """setting character in the room"""
        self.character = character
    def get_character(self):
        """returning character of the room"""
        return self.character
    def set_item(self, item):
        """setting item in the room"""
        self.item = item
    def get_item(self):
        """returning item of the room"""
        return self.item

class Character:
    """Enemy or Friend"""
    def __init__(self, name, descr) -> None:
        self.name = name
        self.descr = descr
        self.conversation = None
    def set_conversation(self, message):
        """setting character's conversation message"""
        self.conversation = message
    def talk(self):
        """returning character's monologue"""
        print("[{} says]: {}".format(self.name, self.conversation))

class Enemy(Character):
    """Character type"""
    def __init__(self, name, descr) -> None:
        super().__init__(name, descr)
        self.conversation = None
        self.weakness = None
    def set_weakness(self, weak):
        """setting item that could overcome the enemy """
        self.weakness = weak
    def describe(self):
        """short info about enemy existance in the room"""
        print("{} is here".format(self.name))
        print(self.descr)
    def fight(self, fight_with):
        """fighting enemy with particular item"""
        if self.weakness == fight_with:
            info.defeated += 1
            print("You fend {} off with the {}".format(self.name, fight_with))
            return True
        else:
            print("{} crushes you, puny adventurer!".format(self.name))
            return False
    def get_defeated(self):
        """returning the number of enemies defeted"""
        return info.defeated

class Friend(Character):
    """Character type"""
    def __init__(self, name, descr) -> None:
        super().__init__(name, descr)
        self.conversation = None
    def describe(self):
        """Short info about the friend"""
        print("{} (your friend) is here".format(self.name))
        print(self.descr)


class Item:
    """Object used for a fight"""
    def __init__(self, item) -> None:
        self.item = item
        self.description = None
    def set_description(self, statment):
        """setting description of the item"""
        self.description = statment
    def describe(self):
        """short maessage about item existance in the room"""
        print("The [{}] is here - {}".format(self.item, self.description))
    def get_name(self):
        """returning name of the item"""
        return self.item
