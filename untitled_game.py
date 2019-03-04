###Game
import random


##Initial Functions
def start():
    game_title = "Dungeon Game I Spent Too Long On"
    print("Welcome to " + game_title + "!")

def end():
    print("Game Over")

def start_item():
    while True:
        item = input("Would you like a sword, a bow, or a staff? ")
        if item == "sword":
            return  barbarian()
        if item == "bow":
            return  archer()
        if item == "staff":
            return  wizard()

def items():
    with open ('item_list.txt', 'r')as f:
            contents = f.readlines()
            return contents
        
def edit_inventory():            
    with open ('inventory_list.txt', 'w')as g:
        g.write(item_txt[:-2])

    
            
##Repeated Functions
def confirm(question):
    while True:
        answer = input(question + " (y/n) ")

        if answer in ["y" , "yes"]:
            return True
        elif answer in ["n", "no"]:
            return False

def roll(n):
    return random.randint(1, n)

def multi_rool(x, n):
    total = 0
    for i in range(x):
        total += rand.randint(1,n)

    return total

def room_describe(door, item):
    if door == 0:
        door_text = "no doors"
    if door == 1:
        door_text = "one door"     
    if door > 1:
        door_text = str(door) + " doors"

    if item == 0:
        item_text = "no items on the ground"
    else:
        item_text = "something on the ground"

    print ("The room has " + door_text + ", " + item_text + ", and a spooky skeleton")
        
    
def action():
    action_option = ['sneak']
    if door > 0:
        action_option.append('door')
    if mob.alive:
        action_option.append('fight')
    if item != 0:
        action_option.append('item')
        
    action = input("What will you do? " + str(action_option) + " ")
    action = action.lower()
    
    if action in ["fight"]:
        player.basic(mob)
        
    elif action in ["door"]:
        if mob.alive:
            print("Man them doors be locked my man!")
        else:
            print("You go through the door")
            in_room = False
            
    elif action in ["item"]:
        item_txt = item_list[item]
        print("There is a " + str(item_txt[:-2]) + " on the ground")
        if confirm("Would you like to pick it up?") == "y":
            edit_inventory()  
            item = 0
        
    elif action in ["sneak"]:
        player.stealth()
        
    else:
        print("Man what the bananas, we gotta do something")

def hostile_action():
    ##code determines whether an enemy is alive or in line of sight
    ##as well as what actions should be taken for sucess
    if mob.alive:
        print("The spooky skeleton is attacking, watch out!")
        mob.basic(player)
    else:
        pass

def all_update():
    player.update()
    mob.update()
    
##One time functions    
def first_room():
    global  item, door, mob, in_room
    item =  random.randint(1,100)
    door = random.randint(1,7)
    mob = skeleton()
    
    print("You stand infront of a half open door ")
    print("You walk inside to a dusty room ")
    print("A single lamp burns in the corner ")
    in_room = True

    


        
##Classes
    
class barbarian():
    def __init__(self):
        self.alive = True
        self.health = random.randint(4,12)+6
        self.damage = 3
        self.armour = 16
        self.status = None

    def basic(self, other):
        atk_roll = roll(20)
        print("You rolled a " + str(atk_roll))
        if atk_roll >= other.armour:
            other.health -= self.damage
            print("Boom get slashed on!")
            print("You deal " + str(self.damage) + " damage")
        else:
            print("Oof you missed..")
            
    def stealth(self):
        sneak_roll = roll(20)
        print("You rolled a " + str(sneak_roll))
        if sneak_roll >= 14:
            print("Your superrrrrr stealthy")
        else:
            print("You ain't very stealthy")

        
    def update(self):
        if self.health <= 0:
            self.alive = False
            
class archer():
    def __init__(self):
        self.alive = True
        self.health = random.randint(4,12)+6
        self.damage = 3
        self.armour = 14
        self.status = None

    def basic(self, other):
        atk_roll = roll(20)
        print("You rolled a " + str(atk_roll))
        if atk_roll >= other.armour:
            other.health -= self.damage
            print("Done get arrowed ye did!")
            print("You deal " + str(self.damage) + " damage")
        else:
            print("Oof you missed..")
    def stealth(self):
        sneak_roll = roll(20)
        print("You rolled a " + str(sneak_roll))
        if sneak_roll >= 14:
            print("Your superrrrrr stealthy")
        else:
            print("You ain't very stealthy")
            
    def update(self):
        if self.health <= 0:
            self.alive = False
            
class wizard():
    def __init__(self):
        self.alive = True
        self.health = random.randint(4,12)+6
        self.damage = 3
        self.armour = 14
        self.status = None

    def basic(self, other):
        atk_roll = roll(20)
        print("You rolled a " + str(atk_roll))
        if atk_roll >= other.armour:
            other.health -= self.damage
            print("Ni! Ni! Ni!")
            print("You deal " + str(self.damage) + " damage")
        else:
            print("Oof you missed..")

    def stealth(self):
        sneak_roll = roll(20)
        print("You rolled a " + str(sneak_roll))
        if sneak_roll >= 14:
            print("Your superrrrrr stealthy")
        else:
            print("You ain't very stealthy")
            
    def update(self):
        if self.health <= 0:
            self.alive = False

            
class skeleton():
    def __init__(self):
        self.alive = True
        self.health = random.randint(1,3)+4
        self.damage = 3
        self.armour = 11
        self.status = None
        
    def basic(self, other):
        atk_roll = roll(20)
        print("He rolled a " + str(atk_roll))
        
        if atk_roll >= other.armour:
            other.health -= self.damage
            print("Clangle Jangle!")
            print("You loose " + str(self.damage) + " health")
        else:
            print("He missed...like by alot")

    def kill(self):
        self.alive = False
        in_room = False
        
    def update(self):
        if self.health <= 0:
            print("Blehhhh he died")
            self.kill()

##Play
def play():
    global player, item_list
    item_list = items()
    player = start_item()
    first_room()
    room_describe(door,item)
    while in_room:
        action()
        hostile_action()
        all_update()
##        break

#Game starts here

start()
playing = True

while playing:
    play()
    playing = confirm("Would you like to play again?")

end()
