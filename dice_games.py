from dice import *
from game_utilities import *


## At minimum, a class consists of the declaration of the class
## which requires the creation of a block
class game:
    None
    ## minimal definition for a class (we won't really use this one)

class dice_game(game):
    ## class for dice games between
    ## a player and the computer
    def __init__(self,game_name):
        self.score = 0
        self.game_name = game_name
        self.die = die(6)
    def __repr__(self):
        return('Game: ' + self.game_name + str(utility.get_id_num()))
    def __str__(self):
        return('Game: ' + self.game_name)
    def game_over_who_wins(self):
        None
    def print_score(self):
        print(self.score)
    def one_turn(self):
        ## this method represents a single round of the game
        print('Next Turn')
    def play_game(self):
        ## This method is invoked to play the game.
        ## As long as nobody has won the game, it continues.
        while not(self.game_over_who_wins()):
            self.one_turn()
            self.print_score()

class war_dice_game(dice_game):
    ## In a basic war dice game, the player competes
    ## against the computer (each has its own score).
    ## The player wins if they reach end_score before the
    ## computer (and vice versa).
    def __init__(self, game_name, end_score, cheating=False):
        self.score = 0
        self.computer_score = 0
        self.end_score = end_score
        if cheating:
            self.die = cheat_die1(6,4)
        else:
            self.die = die(6)
        self.computer_die = die(6)
        print('***This is',game_name+'!')
    def print_score(self):
        print('Computer has', self.computer_score,'points.')
        print('You have',self.score,'points.')
    def game_over_who_wins(self):
        if self.computer_score > self.end_score:
            self.print_score()
            print('Computer Wins!')
            return(True)
        elif self.score > self.end_score:
            self.print_score()
            print('You Win!')
            return(True)
        else:
            return(False)


class single_dice_war_simple(war_dice_game):
    ## In this game, one_turn involves the player
    ## and the computer each rolling one dice and comparing.
    def one_turn(self):
        computer_roll = self.computer_die.roll()
        player_roll = self.die.roll()
        print('You rolled',player_roll,'and the computer rolled',computer_roll)
        self.score = self.score+player_roll
        self.computer_score = self.computer_score+computer_roll

class single_dice_war_with_pot(war_dice_game):
    ## Adds computer_score and pot attributes
    ## One_turn is defined so that:
    ## (1) Scores of player and computer only increase when one roll is higher than the other
    ## (2) The winner of a round's score increases by the difference between the two scores plus
    ##     whatever is in the "pot"
    ## (3) When the player and computer scores tie, their die rolls are added to the pot.
    ##     The pot is empty whenever it is added to a player (or computer) score.
    def __init__(self, game_name, end_score,cheating=False):
        self.game_name = game_name
        self.score = 0
        self.computer_score = 0
        self.end_score = end_score
        if cheating:
            self.die = cheat_die1(6,4)
        else:
            self.die = die(6)
        self.computer_die = die(6)
        self.pot = 0
    def one_turn(self):
        computer_roll = self.computer_die.roll()
        player_roll = self.die.roll()
        difference = player_roll-computer_roll
        print('You rolled',player_roll,'and the computer rolled',computer_roll)
        if difference > 0:
            difference = difference + self.pot
            print('You gain',difference,'points.')
            self.score=self.score+difference
            self.pot = 0
        elif difference < 0:
            difference = (-1 *difference)+self.pot
            print('You lose',difference,'points')
            self.computer_score=self.computer_score+difference
            self.pot = 0
        else:
            print('It is a tie!,Do you want to put',computer_roll+player_roll,'in the pot?')
            if utility.yes_or_no():
                self.pot=self.pot+computer_roll+player_roll


class boomDiceGame(war_dice_game):
    def __init__(self,game_name,weighted=False):
        self.game_name = game_name
        self.end_score = 0
        self.weighted = weighted
        self.score = 0
        self.computer_score = 0
        self.computerScore = 0
        self.diceArray = [1,2,3,4,5,6,7,8,9,10]
        self.computerDiceArray = [die(1),die(2),die(3),die(4),die(5),die(6),die(7),die(8),die(9),die(10)]
    def one_turn(self):
        computerDie = random.randrange(len(self.computerDiceArray))
        computerRoll = self.computerDiceArray[computerDie].roll()
        self.computerDiceArray.pop(computerDie)
        print("Computer's roll is " + str(computerRoll))
        diceString = "Your remaining dice are: "
        for remainingDie in self.diceArray:
            diceString += str(remainingDie) + " "
        playerDice = input(("Which die would you like to roll? "))
        i = 1
        while i == 1:
            try:
                self.diceArray.remove(int(playerDice))
                playerDice = int(playerDice)
                i = 0
            except:
                playerDice = input("ERROR: invalid dice number")
        if self.weighted:
            playerRoll = weightedDie(playerDice).roll()
        else:
            playerRoll = die(playerDice).roll()
        print("Your roll is " + str(playerRoll))
        if computerRoll > playerRoll:
            self.computerScore += computerRoll
            print("You lose! Computer score is " + str(self.computerScore) + ", your score is " + str(self.score)) 
        if playerRoll > computerRoll:
            self.score += playerRoll
            print("You win! Computer score is " + str(self.computerScore) + ", your score is " + str(self.score)) 
        else:
            print("Tie! No points! Computer score is " + str(self.computerScore) + ", your score is " + str(self.score)) 
        self.end_score = self.score
        self.computer_score = self.computerScore
    def playGame(self):
        while len(self.diceArray)>0:
            self.one_turn
    def game_over_who_wins(self):
        if len(self.diceArray) == 0:
            if self.computerScore > self.score:
                self.print_score()
                print('Computer Wins!')
                return(True)
            elif self.score > self.computerScore:
                self.print_score()
                print('You Win!')
                return(True)
            elif self.score == self.computerScore:
                self.print_score()
                print("Tie!")
                return(True)
        else:
            return(False)
