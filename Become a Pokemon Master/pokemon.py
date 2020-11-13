from random import choice


# POKEMON CLASS
class Pokemon:

    ## Constructor methods
    # initializing pokemon with required attributes
    def __init__(self, name, type, level = 5):
        if type not in supported_types:
            print('Error creating pokemon!')
            return
        self.name = name
        self.type = type
        self.level = level
        self.health = level * 4
        self.max_health = level * 5
        self.is_knocked = False

    # string representation of pokemon
    def __repr__(self):
        return f"This is a level {self.level} {self.name} pokemon with {self.health} hitpoints remaining. They are {self.type} type Pokemon."

    ## Helper methods
    # revive pokemon if it is gaining health and was knocked out
    def revive(self):

        self.is_knocked = False

        # revived pokemon should have some health
        if self.health == 0:
            self.health = 1
        
        print(f'{self.name} was revived!')

    # evolving pokemon if it has reached max health
    def evolve(self):

        # increasing level, health and max health
        self.level += 1
        self.max_health = self .level * 5
        self.health = self.max_health

        print(f'{self.name} has evolved to Level {self.level} with {self.max_health} hitpoints.')
    
    # knocking out pokemon if health is 0 or less
    def knock_out(self):

        self.is_knocked = True

        # knocked out pokemon should have only 0 health
        if self.health != 0:
            self.health = 0
        
        print(f'{self.name} was knocked out!')

    ## Main methods
    # losing health if attacked
    def lose_health(self, damage):

        self.health -= damage

        # Calling .knock_out() helper method
        if self.health <= 0:
            self.knock_out()

        else:
            print(f'{self.name} now has {self.health} health points.')

    # gaining health if potion is used
    def gain_health(self, heal):

        # if knocked out then revive
        if self.health == 0:
            self.revive()
        
        self.health += heal
        
        # if health more than max health than evolve
        if self.health >= self.max_health:
            self.evolve()
        
        print(f'{self.name} now has health {self.health} health points.')

    # attacking another pokemon
    def attack_pokemon(self, enemy):

        # if the pokemon is knocked out then can't attack
        if self.is_knocked:
            print(f'{self.name} is knocked out and unable to attack {enemy.name}!')
            return
        
        # if the pokemon has advantage, then deal damage double its level
        if (self.type == 'Fire' and (enemy.type == 'Grass' or enemy.type == 'Ice')) or (self.type == 'Water' and enemy.type == 'Fire') or (self.type == 'Electric' and enemy.type == 'Water') or (self.type == 'Grass' and enemy.type == 'Water') or (self.type == 'Ice' and enemy.type == 'Grass'):

            print(f'{self.name} attacked {enemy.name} for {round(self.level * 2)}.')
            print('HIGH DAMAGE GIVEN!')
            enemy.lose_health(round(self.level * 2))
        
        # If the pokemon has disadvantage then deal damage half the level
        elif (self.type == 'Fire' and enemy.type in ['Fire', 'Water']) or (self.type == 'Water' and enemy.type in ['Water', 'Grass']) or (self.type == 'Electric' and enemy.type in ['Electric', 'Grass']) or (self.type == 'Grass' and enemy.type in ['Fire', 'Grass']) or (self.type == 'Ice' and enemy.type in ['Fire', 'Water', 'Ice']):

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
    
    ## Constructor methods
    # initializing trainer with it's pokemons, number of potions and it's name
    def __init__(self, pokemon_list, num_potions, trainer_name):
        self.pokemons = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = trainer_name

    # string representation of trainer
    def __repr__(self):
        print(f"The trainer {self.name} has following pokemons: ")
        for pokemon in self.pokemons:
            print(pokemon)
        return f"The currently active pokemon is{self.pokemons[self.current_pokemon].name}"

    # helper method to print all the pokemons of trainer
    def print_pokemons(self):
        print('You have: ')
        for pokemon in self.pokemons:
            print(pokemon)
    
    # switching currently active pokemon of trainer
    def switch_active_pokemon(self, pok_idx):

        # Check if the index passed is valid with respect to the number of pokemons of trainer
        if 0 <= pok_idx < len(self.pokemons):

            # if the pokemon at index, which is passed in, is knocked out then do not change current pokemon
            if self.pokemons[pok_idx].is_knocked:
                print(f"{self.name}, {self.pokemons[pok_idx].name} is knocked out. You cannot switch to knocked out pokemons.")

            # if the pokemon at index, which is passed in, is the current pokemon then do not change current pokemon
            elif self.current_pokemon == pok_idx:
                print(f"{self.name}, {self.pokemons[pok_idx].name} is already your active pokemon.")
            
            # if the index is valid and pokemon at index is neither knocked nor current pokemon then change current pokemon
            else:
                self.current_pokemon = pok_idx
                print(f"{self.name}, your active pokemon switched to {self.pokemons[self.current_pokemon].name}.")
        
        # If the index is not a valid index
        else:
            print('No pokemon exist at that place!')
    
    # method to use potion
    def use_potion(self):

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
    
    # attacking enemy trainer
    def attack_trainer(self, enemy_trainer):
        
        # saving value of the trainer's pokemon and enemy trainer's pokemon
        mine = self.pokemons[self.current_pokemon]
        theirs = enemy_trainer.pokemons[enemy_trainer.current_pokemon]

        # using our pokemon to attack enemy's pokemon
        mine.attack_pokemon(theirs)


# Fire Pokemon subclasses
class MegaCharizardX(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Mega Charizard X", "Fire", level)

class MegaCharizardY(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Mega Charizard Y", "Fire", level)

class Charmander(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Chamander", "Fire", level)


# Water Pokemon subclasses
class Blastoise(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Blastoise", "Water", level)
    
class Wartortle(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Wartortle", "Water", level)


# Electric Pokemon subclasses
class Pikachu(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Pikachu", "Electric", level)

class Golem(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Golem", "Electric", level)

class Toxtricity(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Toxtricity", "Electric", level)


# Grass Pokemon subclasses
class Bulbasaur(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Bulbasaur", "Grass", level)

class Venusaur(Pokemon):
    def __init__(self, level = 5):
        super.__init__("Venusaur", "Grass", level)


# Ice Pokemon subclasses
class Cloyster(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Cloyster", "Ice", level)

class Jynx(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Jynx", "Ice", level)

class Vulpix(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Vulpix", "Ice", level)

class Lapras(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Lapras", "Ice", level)

class Glaceon(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Glaceon", "Ice", level)


# supported types of pokemons
supported_types = ['Fire', 'Water', 'Electric', 'Grass', 'Ice']

# All the variables have been moved to Project Extension part

### Project Extension
# playing game based on user input.

## helper functions
# function to check if the trainer passed as parameter has lost the match
def trainer_lost(trainer):

    # If the num of potions are equal to 0 then return True as trainer lost
    if trainer.potions == 0:
        return True

    # Iterating over every pokemon in the list of trainer's pokemon
    for pokemon in trainer.pokemons:

        # If any of the pokemon is not knocked then return false as all pokemons are not knocked
        if not pokemon.is_knocked:
            return False
    
    # If the function reached till here then return True as trainer lost and all it's pokemon's are knocked out
    return True

# function to check if anyone of trainer1 or trainer2 has lost
def check_winner(trainer1, trainer2):

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

# function to randomly decide who will go first
def random_choice(trainer1, trainer2):

    if choice([0, 1]) == 0:
        return trainer1.name
    
    return trainer2.name

# Getting trainer's input and ensuring that it's valid integer
def trainer_input():

    # looping to keep prompting again if wrong input passed
    while True:
        print('Here is what you can do: \n[0] Attack\n[1] Use Potion\n[2] Switch Pokemon')
        
        # try except block to avoid errors while explicitly converting input to integer
        try:
            res = int(input('Enter respective number (0 - 2): \n>>> '))
        
        # If error occured during conversion then inform the player
        except:
            print('You didn\'t enter a number! Try again.\n')
        
        # If no error occured then check if the integer is valid
        else:

            # If the integer is not valid
            if res not in [0, 1, 2]:
                print('Your input didn\'t match 0, 1 or 2. Try again.\n')
                continue
            
            else: # if the integer is valid then return it
                return res

# Function to input index while switching pokemon
def switch_pokemon_idx():

    # looping to keep prompting again if wrong input passed
    while True:

        # try except block to avoid errors while explicitly converting input to integer
        try:
            res = int(input('Enter which pokemon\'s index to change with: '))

        # If error occurred while converting
        except:
            print('Please enter a numerical value!')

        # If no error occured! It's not required to check if it's valid because that's dealt inside pokemon's class method
        else:
            return res

# Function to ask if the user wants to replay
def replay():

    choice = ''
    
    # looping till player enters Y or N
    while choice not in ['Y', 'N']:
        
        choice = input('Do you want to play again (Y - N): ')
        
        if choice not in ['Y', 'N']:
            
            print('Invalid Input!\nRetry: ')
    
    # return true if want to play again
    if choice == 'Y':
        return True

    return False # return false if don't want to play again

# Function to display welcome message and instructions
def welcome_message():
    print('''Welcome to Pokemon Master!

This is a 2-player game where you can play with anyone else you want (he/she would be your enemy).

You and your enemy would play as pokemon trainers.
By default, pokemons, names and number of potions are assigned to you and your enemy but you can change them above.

A total of 15 pokemons have been used in this game, which are of 5 types
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

# function to reset every variable to defaults
def reset():
    global mega_charizard_x, mega_charizard_y, charmander, blastoise, wartortle, pikachu, golem, toxtricity, bulbasaur, cloyster 
    global jynx, vulpix, lapras, glaceon, trainer_two, trainer_one

    # reseting variables to defaults
    mega_charizard_x = MegaCharizardX(4)
    mega_charizard_y = MegaCharizardY(6)
    charmander = Charmander()
    blastoise = Blastoise(8)
    wartortle = Wartortle()
    pikachu = Pikachu(3)
    golem = Golem(11)
    toxtricity = Toxtricity(4)
    bulbasaur = Bulbasaur(3)
    venusaur = Venusaur(6)
    cloyster = Cloyster()
    jynx = Jynx(7)
    vulpix = Vulpix(15)
    lapras = Lapras(6)
    glaceon = Glaceon(9)

    trainer_one = Trainer([
        mega_charizard_y,
        glaceon,
        charmander,
        toxtricity,
        wartortle,
        golem,
        venusaur,
        jynx
    ], 20, "Alex")

    # Trainer 2 object
    trainer_two = Trainer([
        mega_charizard_y,
        blastoise,
        pikachu,
        vulpix,
        bulbasaur,
        cloyster,
        lapras
    ], 20, "Sarah")



# Game Variables
# creating 1 object per pokemon subclass with different levels
# Fire pokemon objects
mega_charizard_x = MegaCharizardX(4)
mega_charizard_y = MegaCharizardY(6)
charmander = Charmander()

# Water pokemon objects
blastoise = Blastoise(8)
wartortle = Wartortle()

# Electric pokemon objects
pikachu = Pikachu(3)
golem = Golem(11)
toxtricity = Toxtricity(4)

# Grass pokemon object
bulbasaur = Bulbasaur(3)
venusaur = Venusaur(6)

# Ice pokemon objects
cloyster = Cloyster()
jynx = Jynx(7)
vulpix = Vulpix(15)
glaceon = Glaceon(9)


# Trainer 1 object
trainer_one = Trainer([
    mega_charizard_y,
    glaceon,
    charmander,
    toxtricity,
    wartortle,
    golem,
    venusaur,
    jynx
], 20, "Alex")

# Trainer 2 object
trainer_two = Trainer([
    mega_charizard_y,
    blastoise,
    pikachu,
    vulpix,
    bulbasaur,
    cloyster,
    lapras
], 20, "Sarah")


### Main Game
running = True

# looping the game to ensure the game doesn't ends unless the players want
while running:

    # displaying welcome message and instructions
    welcome_message()

    # determing who would go first
    player = random_choice(trainer_one, trainer_two)
    print(f'{player} will go first')

    # while the battle is on
    game_on = True
    while game_on:

        # if the player is trainer_one
        if player == trainer_one.name:

            # display current trainer
            print(f'\nCurrent active trainer {player}')

            # getting trainer's input
            player_choice = trainer_input()

            # performing tasks based on trainer's input
            if player_choice == 0:
                trainer_one.attack_trainer(trainer_two)
            
            elif player_choice == 1:
                trainer_one.use_potion()

            else:

                trainer_one.print_pokemons()

                idx = switch_pokemon_idx()
                trainer_one.switch_active_pokemon(idx)
            
            # Checking if someone lost
            game_end = check_winner(trainer_one, trainer_two)

            if game_end: # changing values to break loop
                game_on = False

            else: # if game didn't end then changing current player
                player = trainer_two.name
        
        # If the current player is trainer_two
        else:

            # display current trainer
            print(f'\nCurrent active trainer {player}')

            # getting trainer's input
            player_choice = trainer_input()

            # performing tasks based on trainer's input
            if player_choice == 0:
                trainer_two.attack_trainer(trainer_one)
            
            elif player_choice == 1:
                trainer_two.use_potion()

            else:
                trainer_two.print_pokemons()

                idx = switch_pokemon_idx()
                trainer_two.switch_active_pokemon(idx)
            
            # Checking if someone lost
            game_end = check_winner(trainer_two, trainer_one)

            if game_end: # changing values to break loop
                game_on = False

            else: # if game didn't end then changing current player
                player = trainer_one.name

    # if the player's dont want to play again
    if not replay():
        print('Thanks for playing!')
        break
    
    # Else resting variables to defaults and playing again
    reset()
