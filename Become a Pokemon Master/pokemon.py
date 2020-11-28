'''
This is a Pokemon game simulator program
'''
from random import choice


# POKEMON CLASS
class Pokemon:
    '''
    Pokemon class to give a blueprint for each pokemon
    '''

    ## Constructor methods
    # initializing pokemon with required attributes
    def __init__(self, name, pokemon_type, level = 5):
        if pokemon_type not in supported_types:
            print('Error creating pokemon!')
            return
        self.name = name
        self.pokemon_type = pokemon_type
        self.level = level
        self.health = level * 4
        self.max_health = level * 5
        self.is_knocked = False

    def __repr__(self):
        line1 = f"This is a level {self.level} {self.name} pokemon with {self.health} hitpoints remaining."
        line2 = f"\nThey are {self.pokemon_type} type Pokemon."
        return line1 + line2

    ## Helper methods
    def revive(self):
        '''
        This method is used to revive a pokemon when it is gaining health and was knocked out
        '''

        self.is_knocked = False

        # revived pokemon should have some health
        if self.health == 0:
            self.health = 1
        print(f'{self.name} was revived!')

    def evolve(self):
        '''
        This method is used to evolving a pokemon if it has reached max health
        '''

        # increasing level, health and max health
        self.level += 1
        self.max_health = self .level * 5
        self.health = self.max_health

        print(f'{self.name} has evolved to Level {self.level} with {self.max_health} hitpoints.')

    def knock_out(self):
        '''
        This method is used to knock out a pokemon if health is 0 or less
        '''

        self.is_knocked = True

        # knocked out pokemon should have only 0 health
        if self.health != 0:
            self.health = 0

        print(f'{self.name} was knocked out!')

    ## Main methods
    def lose_health(self, damage):
        '''
        This function is used to decrease health if pokemon has been attacked
        '''

        self.health -= damage

        # Calling .knock_out() helper method
        if self.health <= 0:
            self.knock_out()

        else:
            print(f'{self.name} now has {self.health} health points.')

    def gain_health(self, heal):
        '''
        This method is used to gain health if pokemon has attacked
        '''

        # if knocked out then revive
        if self.health == 0:
            self.revive()

        self.health += heal

        # if health more than max health than evolve
        if self.health >= self.max_health:
            self.evolve()

        print(f'{self.name} now has health {self.health} health points.')

    def attack_pokemon(self, enemy):
        '''
        This method is used to attack other pokemon
        '''

        # if the pokemon is knocked out then can't attack
        if self.is_knocked:
            print(f'{self.name} is knocked out and unable to attack {enemy.name}!')
            return

        # if the pokemon has advantage, then deal damage double its level
        if (self.pokemon_type == 'Fire' and (enemy.pokemon_type == 'Grass' or enemy.pokemon_type == 'Ice')) or (self.pokemon_type == 'Water' and enemy.pokemon_type == 'Fire') or (self.pokemon_type == 'Electric' and enemy.pokemon_type == 'Water') or (self.pokemon_type == 'Grass' and enemy.pokemon_type == 'Water') or (self.pokemon_type == 'Ice' and enemy.pokemon_type == 'Grass'):

            print(f'{self.name} attacked {enemy.name} for {round(self.level * 2)}.')
            print('HIGH DAMAGE GIVEN!')
            enemy.lose_health(round(self.level * 2))

        # If the pokemon has disadvantage then deal damage half the level
        elif (self.pokemon_type == 'Fire' and enemy.pokemon_type in ['Fire', 'Water']) or (self.pokemon_type == 'Water' and enemy.pokemon_type in ['Water', 'Grass']) or (self.pokemon_type == 'Electric' and enemy.pokemon_type in ['Electric', 'Grass']) or (self.pokemon_type == 'Grass' and enemy.pokemon_type in ['Fire', 'Grass']) or (self.pokemon_type == 'Ice' and enemy.pokemon_type in ['Fire', 'Water', 'Ice']):

            print(f'{self.name} attacked {enemy.name} for {round(self.level * .5)}.')
            print('LOW DAMAGE GIVEN!')
            enemy.lose_health(round(self.level * .5))

        # If pokemon has neither disadvantage nor  advantage then deal damage equal to level
        else:

            print(f'{self.name} attacked {enemy.name} for {self.level}.')
            print('NORMAL DAMAGE GIVEN!')
            enemy.lose_health(self.level)



# TRAINER CLASS
class Trainer:
    '''
    Trainer class to give a blueprint for each trainer
    '''

    ## Constructor methods
    def __init__(self, pokemon_list, num_potions, trainer_name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = trainer_name

    def __repr__(self):
        print(f"The trainer {self.name} has following pokemons: ")
        for pokemon in self.pokemons:
            print(pokemon)
        return f"The currently active pokemon is {self.pokemons[self.current_pokemon].name}"

    ### Helper methods
    def print_pokemons(self):
        '''
        This function is used to print all the pokemons of the trainer
        '''
        print('You have: ')
        for pokemon in self.pokemons:
            print(pokemon)

    # switching currently active pokemon of trainer
    def switch_active_pokemon(self, pok_idx):
        '''
        This function is used to switch the current active pokemon
        '''

        # Check if the index passed is valid with respect to the number of pokemons of trainer
        if 0 <= pok_idx < len(self.pokemons):

            # if the pokemon at index passed in is knocked out
            if self.pokemons[pok_idx].is_knocked:
                print("You cannot switch to knocked out pokemons.")

            # if the pokemon at index passed in is the current pokemon
            elif self.current_pokemon == pok_idx:
                print(f"{self.name}, {self.pokemons[pok_idx].name} is already your active pokemon.")

            # if the index is valid and pokemon at index is neither knocked nor current pokemon
            else:
                self.current_pokemon = pok_idx
                pokemon_name = self.pokemons[self.current_pokemon].name
                print(f"{self.name}, your pokemon switched to {pokemon_name}.")

        # If the index is not a valid index
        else:
            print('No pokemon exist at that place!')

    def use_potion(self):
        '''
        This method is used to use a potion on a pokemon
        '''

        # if the number of potions is not equal to 0
        if self.potions > 0:

            # printing info and decreasing num of potions
            print(f"{self.name}, potion used on {self.pokemons[self.current_pokemon].name}")
            self.potions -= 1

            # if no more potions are left
            if self.potions == 0:
                print('No more potions left!')

            # if some potions are still left
            else:
                print(f"You now have {self.potions} potions left!")

            # increasing health of current pokemon
            self.pokemons[self.current_pokemon].gain_health(10)

        # if the number of potions already equal to 0
        else:
            print('You do not have any potions left!')

    def attack_trainer(self, enemy_trainer):
        '''
        This method is used to attack the pokemon of other trainer
        '''

        # saving value of the trainer's pokemon and enemy trainer's pokemon
        mine = self.pokemons[self.current_pokemon]
        theirs = enemy_trainer.pokemons[enemy_trainer.current_pokemon]

        # using our pokemon to attack enemy's pokemon
        mine.attack_pokemon(theirs)


# Fire Pokemon subclasses
class MegaCharizardX(Pokemon):
    '''
    Mega Charizard X pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Mega Charizard X", "Fire", level)

class MegaCharizardY(Pokemon):
    '''
    Mega Charizard Y pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Mega Charizard Y", "Fire", level)

class Charmander(Pokemon):
    '''
    Charmander pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Chamander", "Fire", level)


# Water Pokemon subclasses
class Blastoise(Pokemon):
    '''
    Blastoise pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Blastoise", "Water", level)


class Wartortle(Pokemon):
    '''
    Wartortle pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Wartortle", "Water", level)


# Electric Pokemon subclasses
class Pikachu(Pokemon):
    '''
    Pikachu pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Pikachu", "Electric", level)

class Golem(Pokemon):
    '''
    Golem pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Golem", "Electric", level)

class Toxtricity(Pokemon):
    '''
    Toxtricity pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Toxtricity", "Electric", level)


# Grass Pokemon subclasses
class Bulbasaur(Pokemon):
    '''
    Bulbasaur pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

class Venusaur(Pokemon):
    '''
    Venusaur pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Venusaur", "Grass", level)


# Ice Pokemon subclasses
class Cloyster(Pokemon):
    '''
    Cloyster pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Cloyster", "Ice", level)

class Jynx(Pokemon):
    '''
    Jynx pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Jynx", "Ice", level)

class Vulpix(Pokemon):
    '''
    Vulpix pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Vulpix", "Ice", level)

class Lapras(Pokemon):
    '''
    Lapras pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Lapras", "Ice", level)

class Glaceon(Pokemon):
    '''
    Glaceon pokemon subclass
    '''
    def __init__(self, level = 5):
        super().__init__("Glaceon", "Ice", level)


# supported pokemon_types of pokemons
supported_types = ['Fire', 'Water', 'Electric', 'Grass', 'Ice']

# All the variables have been moved to Project Extension part

### Project Extension
# playing game based on user input.

## helper functions
def trainer_lost(trainer):
    '''
    Function to check if the trainer passed as parameter has lost the match
    '''

    # If the num of potions are equal to 0 then return True as trainer lost
    if trainer.potions == 0:
        return True

    # Iterating over every pokemon in the list of trainer's pokemon
    for pokemon in trainer.pokemons:

        # If any of the pokemon is not knocked then return false as all pokemons are not knocked
        if not pokemon.is_knocked:
            return False

    # return True as trainer lost and all it's pokemon's are knocked out
    return True

def check_winner(trainer1, trainer2):
    '''
    Function to check if anyone of trainer1 or trainer2 has lost
    '''

    # Checking if trainer1 has lost the match
    trainer1_lost = trainer_lost(trainer1)

    # If so then print text and return True as we have a winnner
    if trainer1_lost:
        print(f"{trainer1.name} lost the match.")
        print(f"Congratulations {trainer2.name}!")
        return True
    # Checking if trainer1 has lost the match
    trainer2_lost = trainer_lost(trainer2)

    # If so then print text and return True as we have a winnner
    if trainer2_lost:
        print(f"{trainer2.name} lost the match.")
        print(f"Congratulations {trainer1.name}!")
        return True
    # If no one lost then it means match will go on so returning false
    return False

def random_choice(trainer1, trainer2):
    '''
    Function to randomly decide who will go first
    '''

    if choice([0, 1]) == 0:
        return trainer1.name
    return trainer2.name

def trainer_input():
    '''
    Getting trainer's input and ensuring that it's valid integer
    '''

    # looping to keep prompting again if wrong input passed
    while True:
        print('Here is what you can do: \n[0] Attack\n[1] Use Potion\n[2] Switch Pokemon')

        # try except block to avoid errors while explicitly converting input to integer
        try:
            res = int(input('Enter respective number (0 - 2): \n>>> '))

        # If error occured during conversion then inform the player
        except TypeError:
            print('You didn\'t enter a number! Try again.\n')

        # If no error occured then check if the integer is valid
        else:
            # If the integer is not valid
            if res not in [0, 1, 2]:
                print('Your input didn\'t match 0, 1 or 2. Try again.\n')
            else: # if the integer is valid then return it
                return res

def switch_pokemon_idx():
    '''
    Function to input index while switching pokemon
    '''

    # looping to keep prompting again if wrong input passed
    while True:

        # try except block to avoid errors while explicitly converting input to integer
        try:
            res = int(input('Enter which pokemon\'s index to change with: '))

        # If error occurred while converting
        except TypeError:
            print('Please enter a numerical value!')

        # If no error occured! It's not required to check if it's valid
        else:
            return res

def replay():
    '''
    Function to ask if the user wants to replay
    '''

    user_choice = ''
    # looping till player enters Y or N
    while user_choice not in ['Y', 'N']:

        user_choice = input('Do you want to play again (Y - N): ')

        if user_choice not in ['Y', 'N']:
            print('Invalid Input!\nRetry: ')

    # return true if want to play again
    if user_choice == 'Y':
        return True

    return False # return false if don't want to play again

def welcome_message():
    '''
    Function to display welcome message and instructions
    '''

    print('''Welcome to Pokemon Master!

This is a 2-player game where you can play with anyone else you want (he/she would be your enemy).

You and your enemy would play as pokemon trainers.
By default, pokemons, names and number of potions are assigned to you and your enemy but you can change them above.

A total of 15 pokemons have been used in this game, which are of 5 pokemon_types
Fire, Water, Grass, Electric and Ice.
Pokemons have different level and they evolve when they attain full health.
You can do the following tasks:- 
1) Attack enemy trainers pokemon
2) Use a potion to heal, revive or evolve your current active pokemon
3) Switch your current active pokemon.

As per default values trainer1 (named 'Alex') has 8 pokemons and trainer2 (named 'Sarah') has 7 pokemons.
When switching a pokemon you must ensure that you enter a valid index for next pokemon, else it wont change.
(Indexes begin from 0. For eg, by default valid indexes for trainer1 would be from 0 to 7 (and not 8).)

RULE IS SIMPLE:
The first one to have 0 potions left or all pokemons knocked out is the loser.

(P.S. by default both trainer have 20 potions each.)

Let the Battle Begin!!!

''')

def reset():
    '''
    Function to reset every variable to defaults
    '''

    global MEGA_CHARIZARD_X, MEGA_CHARIZARD_Y, CHARMANDER, BLASTOISE, WARTORTLE, PIKACHU
    global GOLEM, TOXTRICITY, BULBASAUR, CLOYSTER, VENUSAUR
    global JYNX, VULPIX, LAPRAS, GLACEON, TRAINER_ONE, TRAINER_TWO

    # reseting variables to defaults
    MEGA_CHARIZARD_X = MegaCharizardX(4)
    MEGA_CHARIZARD_Y = MegaCharizardY(6)
    CHARMANDER = Charmander()
    BLASTOISE = Blastoise(8)
    WARTORTLE = Wartortle()
    PIKACHU = Pikachu(3)
    GOLEM = Golem(11)
    TOXTRICITY = Toxtricity(4)
    BULBASAUR = Bulbasaur(3)
    VENUSAUR = Venusaur(6)
    CLOYSTER = Cloyster()
    JYNX = Jynx(7)
    VULPIX = Vulpix(15)
    LAPRAS = Lapras(6)
    GLACEON = Glaceon(9)

    TRAINER_ONE = Trainer([
        MEGA_CHARIZARD_X,
        GLACEON,
        CHARMANDER,
        TOXTRICITY,
        WARTORTLE,
        GOLEM,
        VENUSAUR,
        JYNX
    ], 20, "Alex")

    # Trainer 2 object
    TRAINER_TWO = Trainer([
        MEGA_CHARIZARD_Y,
        BLASTOISE,
        PIKACHU,
        VULPIX,
        BULBASAUR,
        CLOYSTER,
        LAPRAS
    ], 20, "Sarah")



# Game Variables
# creating 1 object per pokemon subclass with different levels
# Fire pokemon objects
MEGA_CHARIZARD_X = MegaCharizardX(4)
MEGA_CHARIZARD_Y = MegaCharizardY(6)
CHARMANDER = Charmander()

# Water pokemon objects
BLASTOISE = Blastoise(8)
WARTORTLE = Wartortle()

# Electric pokemon objects
PIKACHU = Pikachu(3)
GOLEM = Golem(11)
TOXTRICITY = Toxtricity(4)

# Grass pokemon object
BULBASAUR = Bulbasaur(3)
VENUSAUR = Venusaur(6)

# Ice pokemon objects
CLOYSTER = Cloyster()
JYNX = Jynx(7)
VULPIX = Vulpix(15)
GLACEON = Glaceon(9)
LAPRAS = Lapras(6)


# Trainer 1 object
TRAINER_ONE = Trainer([
    MEGA_CHARIZARD_X,
    GLACEON,
    CHARMANDER,
    TOXTRICITY,
    WARTORTLE,
    GOLEM,
    VENUSAUR,
    JYNX
], 20, "Alex")

# Trainer 2 object
TRAINER_TWO = Trainer([
    MEGA_CHARIZARD_Y,
    BLASTOISE,
    PIKACHU,
    VULPIX,
    BULBASAUR,
    CLOYSTER,
    LAPRAS
], 20, "Sarah")


### Main Game
RUNNING = True

# looping the game to ensure the game doesn't ends unless the players want
while RUNNING:

    # displaying welcome message and instructions
    welcome_message()

    # determing who would go first
    player = random_choice(TRAINER_ONE, TRAINER_TWO)
    print(f'{player} will go first')

    # while the battle is on
    GAME_ON = True
    while GAME_ON:

        # if the player is TRAINER_ONE
        if player == TRAINER_ONE.name:

            # display current trainer
            print(f'\nCurrent active trainer {player}')

            # getting trainer's input
            player_choice = trainer_input()

            # performing tasks based on trainer's input
            if player_choice == 0:
                TRAINER_ONE.attack_trainer(TRAINER_TWO)

            elif player_choice == 1:
                TRAINER_ONE.use_potion()

            else:

                TRAINER_ONE.print_pokemons()

                idx = switch_pokemon_idx()
                TRAINER_ONE.switch_active_pokemon(idx)

            # Checking if someone lost
            GAME_END = check_winner(TRAINER_ONE, TRAINER_TWO)

            if GAME_END: # changing values to break loop
                GAME_ON = False

            else: # if game didn't end then changing current player
                player = TRAINER_TWO.name

        # If the current player is TRAINER_TWO
        else:

            # display current trainer
            print(f'\nCurrent active trainer {player}')

            # getting trainer's input
            player_choice = trainer_input()

            # performing tasks based on trainer's input
            if player_choice == 0:
                TRAINER_TWO.attack_trainer(TRAINER_ONE)

            elif player_choice == 1:
                TRAINER_TWO.use_potion()

            else:
                TRAINER_TWO.print_pokemons()

                idx = switch_pokemon_idx()
                TRAINER_TWO.switch_active_pokemon(idx)

            # Checking if someone lost
            GAME_END = check_winner(TRAINER_TWO, TRAINER_ONE)

            if GAME_END: # changing values to break loop
                GAME_ON = False

            else: # if game didn't end then changing current player
                player = TRAINER_ONE.name

    # if the player's dont want to play again
    if not replay():
        print('Thanks for playing!')
        break

    # Else resting variables to defaults and playing again
    reset()
