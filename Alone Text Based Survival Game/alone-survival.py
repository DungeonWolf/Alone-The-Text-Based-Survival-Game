import random

# Health Stats (Testing)
max_player_health = 50
current_player_health = 25
# Hunger Stats (Testing)
max_player_hunger = 50
current_player_hunger = 10
# Thirst Stats (Testing)
max_player_thirst = 50
current_player_thirst = 45
# Types of Cells (Testing)
cell_types = ["Forest", "Grassy", "Water"] # Three cell types
cell_numbers = [0, 1, 2] # Corresponding numbers to each cell type. Used for matrix.  
cell_abundancy = [0.5, 0.3, 0.2] # How common each cell type is out of the total number of cells. Ex: Three cell types above, put [1.4, 1.2, 0.4] for the abundancy.

# Class that acts as the template for different bar displays.
# Bar Example:   Full Bar: █████ 50 / 50   Half Bar: ██▒░░ 25 / 50   Low Bar: ▒░░░░ 5 / 50
class Scale_Display:

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
        filled_char = chr(0x2588) # █
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
        # Adds up what the bar will output at the end of the calculations. Ex: ██▒░░
        final_bar = (filled_char * filled_length) + (half_char * half_length) + (empty_char * empty_length)
        print(f"{self.name}: {final_bar} {self.current_value} / {self.max_value}")

    # Test of Initialized Variables
    def testing(self):
        print(f"{self.name} has a maximum {self.name} of {self.max_value} and a current {self.name} of {self.current_value}.")

# Example of Bars
    # Hunger_Bar = Scale_Display("Hunger", max_player_hunger, current_player_hunger, 5)
    # Health_Bar = Scale_Display("Health", max_player_health, current_player_health, 5)
    # Thirst_Bar = Scale_Display("Thirst", max_player_thirst, current_player_thirst, 5)
# Output of the Example Bars
    # Hunger_Bar.display_bar() # Outputs "Hunger: █░░░░ 10 / 50"
    # Health_Bar.display_bar() # Outputs "Health: ██▒░░ 25 / 50"
    # Thirst_Bar.display_bar() # Outputs "Thirst: ████▒ 45 / 50"

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
        

new_map = Map(10, 10) # Some testing stuff for the map creation. Creates a new instance of the Map class.
new_map.map_creation() # Returns the map matrix from the created class above. Outputs a list or matrix of 10 lists with 10 items or cells in each with randomized numbers. I don't want to write out the example.


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
