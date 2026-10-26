import random


# I believe that every user that reads this code or any other code I've written should make it's comments enjoyable and fun to read
# every now and then. I will put a laugh here and there. Hope you like reading it and I hope most of the comments aren't too annoying
# to read. There is a lot and it makes it cluttered, hope it isn't that bad though. :)


# Health Stats (Testing)
max_player_health = 50
current_player_health = 25

# Hunger Stats (Testing)
max_player_hunger = 50
current_player_hunger = 10

# Water Stats (Testing)
max_player_water = 50
current_player_water = 45

# Types of Cells (Testing)
cell_types = ["Forest", "Grassy", "Water"] # Three cell types
cell_numbers = [0, 1, 2] # Corresponding numbers to each cell type. Used for matrix.  
cell_abundancy = [0.5, 0.4, 0.1] # How common each cell type is out of the total number of cells. Ex: Three cell types above, put [1.4, 1.2, 0.4] for the abundancy.


# Command Stuff (Testing)
command_list = ["Inventory", "Move", "Forage", "Hunt", "Build", "Rest", "Use", "List", "Quit"] # List of commands that you will be able to use in the game and interact with the world.


# Item Stuff (Testing)
starting_item_choices = ["Binoculars - Lets you scout areas far away for animals and dangers.", "Bow & Arrows - A fine weapon that can be used to hunt various animals with 10 arrows provided.", "Hatchet - Can be used as a weapon and a way to gather materials.", "Fire Starter - A quick and easy way to get a fire going for warmth and cooking.", "Fishing Rod - An easier way to catch fish in nearby ponds."] # List of items to choose from at the start of the game, and descriptions of what they do.
starting_item_choices_short = {"binoculars": "Binoculars", # A dictionary that "translates" what you type into the responses for choosing your starting items.
                               "bow": "Bow and Arrows", 
                               "hatchet": "Hatchet", 
                               "fire": "Fire Starter", 
                               "rod": "Fishing Rod"}
starting_item_name_choices = ["binoculars", "bow", "hatchet", "fire", "rod"] # A list of your choices to actually type out when selecting the starting items. Makes it easier to type out when selecting.
inventory_mandatory_items = ["Family Photo", "Rope", "Knife", "String", "Fish Net"] # A list of items that are in your inventory by default and added after you select all of your items.
chosen_inventory = [] # A list for your inventory that has all of the full names of the items you've selected.
chosen_items = [] # A list for keeping track of all of the items you have selected. Used for preventing trying to add multiple of the same item to your inventory.
new_line_reference = "\n" # A quick reference so I could add another line break in an f-string in which "\n" cannot work on it's own. It helps to separate all of the choices with the descriptions so it's easier to read.


# Location Stuff (Testing)
add_movement_x = 0 # Defines what tile you are on based on what this number is added to your current position on the x axis.
add_movement_y = 0 # Same as above but for the y axis.


class Command_System:
    # Initializes the parts of the command system class. Unfinished.
    def __init__(self, command_list): 
        self.command_list = command_list # Initializes a variable for the class to reference to.
    # A function that the class can use to display all of the usable commands to interact with the world.
    def display_commands(self):
        print("Available Commands: -") # Self Explanitory
        for command in self.command_list: # Loops through the commands in the provided list from before in the class.
            print(f" {command} -") # Prints out each command. Ex:        Available Commands: - Move - Forage - Build - Rest - Use -
    # A function that will let the user enter the commands that are listed or available.
    def enter_command(self):
        command = input().strip().upper() # Stores the user's command option in this variable.
        if command in self.command_list: # Checks if the command entered is one from the command list.
            if command == "move":
                while True:
                    direction = input("Which Direction? Enter: North, South, East or West").strip().upper() # Takes the user's input and saves it in a variable for use below to see if the player wants to move north, south, east or west.
                    if direction == "north": # Checks if the user chose north
                        add_movement_y += 1
                        break # Stops loop
                    elif direction == "south": # Checks if the user chose south
                        add_movement_y -= 1
                        break # Also stops loop
                    elif direction == "east": # Checks if the user chose east
                        add_movement_x -= 1
                        break # I hope it stops the loop
                    elif direction == "west": # Checks if the user chose west
                        add_movement_x += 1
                        break # It better stop the loop
                    else: # Checks if the user screwed up.
                        print("Something didn't work or command not valid, try again.")
                    # Come back, need to work on finding a way to display where you moved afterwards.
        else:
            print("Action not recognized, please refer to command list.") # If the entered command from the user's input before is incorrect in some way, it prompts the user to make sure it is a usuable command.


# Command System Creation
command_system_start = Command_System(command_list)


# Class that acts as the template for different bar displays.
# Bar Example:   Full Bar: ▓▓▓▓▓ 50 / 50   Half Bar: ▓▓▒░░ 25 / 50   Low Bar: ▒░░░░ 5 / 50


class Bar_Display:

    # Initialization of different variables needed for the displays.
    def __init__(self, name: str, max_value: int, current_value: int, bar_length: int):
        self.name = name
        self.max_value = max_value
        self.current_value = current_value
        # May use bar_length later for different scaled bars, but unused for now.
        self.bar_length = bar_length

    # Main Function of Scale_Display for making the actual displayed bar.
    def display_bar(self):
        # Special Characters Used for Building the Bar
        filled_char = chr(0x2593) # ▓
        half_char = chr(0x2592) # ▒ 
        empty_char = chr(0x2591) # ░
        # A number that will be used for converting the current_value into a number with a decimal at the end.
        decimal_conv = 10 
        # Variables that hold the lengths of each part of the bar (Empty, Half and Filled Parts).
        empty_length = int((self.max_value - self.current_value) / decimal_conv) # Should change later to be any unfilled space out of the declared bar_length.
        filled_length = int(self.current_value / decimal_conv) 
        half_length = None # Blank variable that is changed in the if statement below.
        # The statement that decides whether the half_length is 1 or 0, meaning whether in the bar, that there will be a half character included.
        if ((self.current_value / decimal_conv) - filled_length) > 0:
            half_length = 1
        else:
            half_length = 0
        # Adds up what the bar will output at the end of the calculations. Ex: ▓▓▒░░
        final_bar = (filled_char * filled_length) + (half_char * half_length) + (empty_char * empty_length)
        print(f"{self.name}: {final_bar} {self.current_value} / {self.max_value}")

    # Test of Initialized Variables for the Bar class above
    def testing(self):
        print(f"{self.name} has a maximum {self.name} of {self.max_value} and a current {self.name} of {self.current_value}.")


# Example of Bars
    # Hunger_Bar = Bar_Display("Hunger", max_player_hunger, current_player_hunger, 5)
    # Health_Bar = Bar_Display("Health", max_player_health, current_player_health, 5)
    # Water_Bar = Bar_Display("Water", max_player_water, current_player_water, 5)
# Output of the Example Bars
    # Hunger_Bar.display_bar() # Outputs "Hunger: ▓░░░░ 10 / 50"
    # Health_Bar.display_bar() # Outputs "Health: ▓▓▒░░ 25 / 50"
    # Water_Bar.display_bar()   # Outputs "Water: ▓▓▓▓▒ 45 / 50"


class Map:
    # Initialization of the Map class.
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
    # A function that creates the map that the player will be in. They will not see it, but it will be used for actions and interacting with the world, just through text in their eyes.
    def map_creation(self):
        map_tile_total = self.width * self.height # Gets the area of the map.
        tile_abundancies = [round(map_tile_total * cell_abundancy[0]), round(map_tile_total * cell_abundancy[1]), round(map_tile_total * cell_abundancy[2])] # Gets the abundancy of what each cell type should have for later calculations.
        matrix_dictionary = {} # Empty dictionary for later use.
        matrix_dictionary.update({cell_numbers[0]: tile_abundancies[0], cell_numbers[1]: tile_abundancies[1], cell_numbers[2]: tile_abundancies[2]}) # Puts the cells with their corresponding abundancies to later use for creating the matrix initial list.
        map_matrix = [] # Empty list for putting all of the cell types into with their correct amounts with their abundancies.
        for num, times in matrix_dictionary.items(): # Loops through the dictionary and appends each occurrence with their correct abundancy to the map_matrix list from before.
            for i in range(times):
                map_matrix.append(num)
        random.shuffle(map_matrix) # Shuffles the list so the map is randomized and not looping through from 0 to 1 to 2 throughout.
        def split_to_matrix(matrix, width): # A function that splits the long randomized list into chunks of lists with the width size so that it forms the final matrix.
            all_lists = []
            for i in range(0, len(matrix), width):
                all_lists.append(matrix[i:i + width])
            return all_lists
        map_matrix = split_to_matrix(map_matrix, self.width) # Assigns the final split up matrix to the map_matrix variable list as an actual matrix.
        return map_matrix # Returns the final matrix for the function.


# Map and Location Testing
new_map = Map(250, 250) # Some testing stuff for the map creation. Creates a new instance of the Map class.
new_map.map_creation() # Returns the map matrix from the created class above. Outputs a list or matrix of 10 lists with 10 items or cells in each with randomized numbers. I don't want to write out the example.
player_start_location_x = int(new_map.width / 2)
player_start_location_y = int(new_map.height / 2)
map = new_map.map_creation()


class Item:

    def __init__(self, name: str, description: str, bonus: int):
        self.name = name
        self.description = description
        self.bonus = bonus


class Animal:

    def __init__(self, name: str, description: str, health: int, attack: int):
        self.name = name
        self.description = description
        self.health = health
        self.attack = attack


# Animal Stuff (Testing)
# All animals below are an instance of the Animal class above.
rabbit = Animal("Rabbit", "A small jumping animal that is very fast and agile. A good snare will catch them.", 5, 1)
mink = Animal("Mink", "A small and sneaky creature that is found near water and scavenges for food near it's home.", 6, 3)
pine_martin = Animal("Pine Martin", "A small creature that is similar to the mink and known for it's mischief. They are commonly found in trees and will go a long way to find food. You cannot kill them.", 6, 3)
crow = Animal("Crow", "A smart bird that is usually found at the carcass of large animal.", 3, 1)
wolf = Animal("Wolf", "A medium to large sized creature that is attracted to the smell of blood and moves in packs", 20, 20)
bear = Animal("Bear", "A large creature that is very protective of their cubs, they are very agressive creatures and will probably attack you at the first sight they get.", 40, 30)
moose = Animal("Moose", "A large and usually passive creature, but if you get too close, they will attack.", 35, 30)
mountain_lion = Animal("Mountain Lion", "A medium sized creature similar to wolves but usually travel alone and stalk their prey", 25, 30)
# Each List below stores whether each animal defined above is harmless or harmful. (Animals most likely to attack / not that are dangerous / not)
harmless_animals = [rabbit, mink, pine_martin, crow] # Harmless animals are the animals that can be a food source or just a nuisance that steals your food when you're not looking.
dangerous_animals = [wolf, bear, moose, mountain_lion] # Dangerous animals that will attack you at first sight. You have the ability to hunt and kill them, but they are very, very, dangerous.


class Player:

    def __init__(self, health: int, hunger: int, water: int, sanity: int):
        self.health = health
        self.hunger = hunger
        self.water = water
        self.sanity = sanity
    # Drains the player's health attribute.
    def drain_health(self, damage):
        self.health -= damage
    # Drains the player's hunger attribute.
    def drain_hunger(self, food_drain):
        self.hunger -= food_drain
    # Drains the player's water attribute.
    def drain_water(self, thirst):
        self.water -= thirst
    # Drains the player's sanity attribute.
    def drain_sanity(self, sanity_drain):
        self.sanity -= sanity_drain

    def player_start_location(self):
        start_location = map[player_start_location_x][player_start_location_y] # Calculates the player's start location (The middle of the randomly generated map.)
        if start_location == 0: # What returns when you start in a forest tile.
            return "\nAll you can see around you is thick dense foliage and trees that seem to touch the sky. You start in a forest.\n"
        elif start_location == 1: # What returns when you start in a grassy tile.
            return "\nTall grass surrounds you and a small rabbit scurries past your feet. You start in a grassy field.\n"
        elif start_location == 2: # What returns when you start in a water tile.
            return "\nYour feet are soaked in cold water. You start on the shore of a lake.\n"
        else: # What returns if there is some error and you somehow didn't spawn in a tile?? If you did this, you broke my game somehow.
            return "\nError occured. Please exit game and restart.\n"

    def player_location_explanation(self):
        if self.player_location == 0:
            return "\nYou are now in a forest.\n"
        elif self.player_location == 1:
            return "\nYou are now in a grassy field.\n"
        elif self.player_location == 2:
            return "\nYou are now on the edge of a lake.\n"
        else:
            return "\nGame Broke. What happened??\n"

    def player_location(self):
        start_location = map[player_start_location_x][player_start_location_y]
        new_current_location = start_location[add_movement_x][add_movement_y]
        return new_current_location


add_movement_x
add_movement_y


# Player Creation (Testing)
player_initialization = Player(50, 40, 50, 50) # 50 Health, 40 Hunger, 50 Water and 50 Sanity.


class Inventory:

    def __init__(self, collected_items):
        self.collected_items = collected_items


def Start_Game():
    print("\nYou have just dropped into a world of wilderness. \nYou will be alone for the foreseeable future, and you must survive out here for as long as you can. \nIn the end, you will win a prize of up to 1 million dollars. \nGood luck and try not to die.") # Opening introduction to the world.
    print(player_initialization.player_location()) # Says where you are based on current tile.
    print(f"You look in your bag. What items did you choose to bring? Enter your first item choice: \n\n{new_line_reference.join(starting_item_choices)} \n\n(Type {starting_item_name_choices[0].capitalize()}, {starting_item_name_choices[1].capitalize()}, {starting_item_name_choices[2].capitalize()}, {starting_item_name_choices[3].capitalize()} or {starting_item_name_choices[4].capitalize()}.)\n") # More of the introduction and what your options are for what supplies you have brought with you on your survival expedition.
    while True: # Loops the if statement, so if it goes to else, it will loop back until the criteria is met.
        starting_item_response = input().strip().lower() # Saves the user's response in a variable and gets rid of uppercase letters along with spaces.
        if starting_item_response in starting_item_choices_short: # Checks if the user input is in the dictionary of items the shorter names and their longer names.
            full_name = starting_item_choices_short[starting_item_response] # Creates a variable that stores the choice of the user as it's corresponding longer name form in the dictionary.
            chosen_inventory.append(full_name) # Puts the longer form name from the variable above into the list of chosen items for the inventory.
            chosen_items.append(starting_item_response) # Puts the chosen item that was typed in short form into a list that keeps track of what has already been entered so that you cannot have repeats of the same chosen item in your inventory.
            print(f"\nYou have chose the {full_name}.") # Prints out the chosen item in long form that confirms the users choice with the item they chose. Will come back later to add the option to pick a different item.
            break # Stops the loop, need I say more?
        else:
            print(f"\nYour choice is unrecognized, please try again.\n") # Resets the loop because the user's input was incorrect.
    print("\nChoose your second item.\n") # Prompts the user to choose a second item for their inventory.
    while True: # Loops the if statement, so if it goes to else, it will loop back until the criteria is met.
        starting_item_response = input().strip().lower() # Saves the user's response in a variable and gets rid of uppercase letters along with spaces.
        if (starting_item_response in starting_item_choices_short) & (starting_item_response not in chosen_items): # Checks if the user input is in the dictionary of items the shorter names and their longer names, but also checks if the user has already entered that option before, preventing repeats.
            full_name = starting_item_choices_short[starting_item_response] # Creates a variable that stores the choice of the user as it's corresponding longer name form in the dictionary.
            chosen_inventory.append(full_name) # Puts the longer form name from the variable above into the list of chosen items for the inventory.
            chosen_items.append(starting_item_response) # Puts the chosen item that was typed in short form into a list that keeps track of what has already been entered so that you cannot have repeats of the same chosen item in your inventory.
            print(f"\nYou have chose the {full_name}.") # Prints out the chosen item in long form that confirms the users choice with the item they chose. Will come back later to add the option to pick a different item.
            break # Guess what? It stops the loop.
        else:
            print(f"\nYour choice is unrecognized or repeated, please try again.\n") # Resets the loop because the user's input was incorrect or repeated.
    print("\nChoose your third item.\n") # Prompts the user to choose their third an final item that they brought along with them on this expedition.
    while True: # Loops the if statement, so if it goes to else, it will loop back until the criteria is met.
        starting_item_response = input().strip().lower() # Saves the user's response in a variable and gets rid of uppercase letters along with spaces.
        if (starting_item_response in starting_item_choices_short) & (starting_item_response not in chosen_items): # Checks if the user input is in the dictionary of items the shorter names and their longer names, but also checks if the user has already entered that option before, preventing repeats.
            full_name = starting_item_choices_short[starting_item_response] # Creates a variable that stores the choice of the user as it's corresponding longer name form in the dictionary. Did you think I was just copy pasting this stuff? I am.
            chosen_inventory.append(full_name) # Puts the longer form name from the variable above into the list of chosen items for the inventory.
            chosen_items.append(starting_item_response) # Puts the chosen item that was typed in short form into a list that keeps track of what has already been entered so that you cannot have repeats of the same chosen item in your inventory.
            print(f"\nYou have chose the {full_name}.") # Prints out the chosen item in long form that confirms the users choice with the item they chose. Will come back later to add the option to pick a different item.
            break # Woah, balance is restored to the code and the loop stops.
        else:
            print(f"\nYour choice is unrecognized or repeated, please try again.\n") # Resets the loop because the user's input was incorrect or repeated.
    for item in inventory_mandatory_items:
        chosen_inventory.append(item)
    print(f"In your bag, you brought with you: \n{new_line_reference.join(chosen_inventory)}")


# Calls the start game function, used for testing right now and anyone who wants to try out picking items from a few options.
Start_Game() 


# Do I have too many comments?