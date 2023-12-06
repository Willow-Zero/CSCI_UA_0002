import random, math
from game_utilities import *

class die:
    def __init__(self,number_of_sides):
        self.face = random.randint(1,number_of_sides)
        self.number_of_sides = number_of_sides
        self.id = utility.get_id_num()
    def __repr__(self):
        return(str(self.number_of_sides)+'-sided #: '+str(self.id))
    def __str__(self):
        return(str(self.number_of_sides)+'-sided. On:'+str(self.face))
    def roll(self):
        self.face = random.randint(1,self.number_of_sides)
        return(self.face)

class cheat_die1(die):
    def __init__(self,number_of_sides,extra_sides):
        self.hidden_face = random.randint(1,number_of_sides+extra_sides)
        self.face = min(self.hidden_face,number_of_sides)
        self.number_of_sides = number_of_sides
        self.extra_sides = extra_sides
        self.id = utility.get_id_num()
    def roll(self):
        self.hidden_face = random.randint(1,self.number_of_sides+self.extra_sides)
        self.face = min(self.hidden_face,self.number_of_sides)
        return(self.face)
               
class weightedDie(die):
    def __init__(self,number_of_sides):
        self.id = utility.get_id_num()
        self.number_of_sides = number_of_sides
    def roll(self):
        self.roll = random.randint(1,self.number_of_sides*self.number_of_sides)
        self.face = math.ceil(math.sqrt(self.roll))
        return(self.face)
