# Health Stats (Testing)
max_player_health = 50
current_player_health = 25
# Hunger Stats (Testing)
max_player_hunger = 50
current_player_hunger = 10
# Thirst Stats (Testing)
max_player_thirst = 50
current_player_thirst = 45

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
        empty_length = int((self.max_value - self.current_value) / decimal_conv)
        filled_length = int(self.current_value / decimal_conv) # Should change later to be any unfilled space out of the declared bar_length.
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
