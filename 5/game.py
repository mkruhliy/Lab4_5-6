class Info(object):
    defeated = 0
info = Info()

class Room:
    def __init__(self, room) -> None:
        self.room = room
        self.dscrpt = ''
        self.link = {}
        self.character = None
        self.item = None
    def set_description(self, statment):
        self.dscrpt = statment
    def link_room(self, room, side):
        self.link[side] = room
    def move(self, side):
        return self.link[side]
    def get_details(self):
        print(self.room)
        print("--------------------")
        print(self.dscrpt)
        for key, value in self.link.items():
            print("The {} is {}".format(value.room, key))
    def set_character(self, character):
        self.character = character
    def get_character(self):
        return self.character
    def set_item(self, item):
        self.item = item
    def get_item(self):
        return self.item

class Enemy:
    def __init__(self, name, descr) -> None:
        self.name = name
        self.descr = descr
        self.conversation = None
        self.weakness = None
    def set_conversation(self, message):
        self.conversation = message
    def set_weakness(self, weak):
        self.weakness = weak
    def describe(self):
        print("{} is here".format(self.name))
        print(self.descr)
    def fight(self, fight_with):
        if self.weakness == fight_with:
            info.defeated += 1
            print("You fend {} off with the {}".format(self.name, fight_with))
            return True
        else:
            print("{} crushes you, puny adventurer!".format(self.name))
            return False
    def get_defeated(self):
        return info.defeated
    def talk(self):
        print("[{} says]: {}".format(self.name, self.conversation))

class Item:
    def __init__(self, item) -> None:
        self.item = item
        self.description = None
    def set_description(self, statment):
        self.description = statment
    def describe(self):
        print("The [{}] is here - {}".format(self.item, self.description))
    def get_name(self):
        return self.item

# kitchen = Room("Kitchen")
# kitchen.set_description("A dank and dirty room buzzing with flies.")

# dining_hall = Room("Dining Hall")
# dining_hall.set_description("A large room with ornate golden decorations on each wall.")

# ballroom = Room("Ballroom")
# ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

# kitchen.link_room(dining_hall, "south")
# dining_hall.link_room(kitchen, "north")
# dining_hall.link_room(ballroom, "west")
# ballroom.link_room(dining_hall, "east")

# dave = Enemy("Dave", "A smelly zombie")
# dave.set_conversation("What's up, dude! I'm hungry.")
# dave.set_weakness("cheese")
# dining_hall.set_character(dave)

# tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
# tabitha.set_conversation("Sssss....I'm so bored...")
# tabitha.set_weakness("book")
# ballroom.set_character(tabitha)

# cheese = Item("cheese")
# cheese.set_description("A large and smelly block of cheese")
# ballroom.set_item(cheese)

# book = Item("book")
# book.set_description("A really good book entitled 'Knitting for dummies'")
# dining_hall.set_item(book)