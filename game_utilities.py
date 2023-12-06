class game_utilities:
    ## all utilities go here
    def __init__(self):
        ## count elements
        ## produced so each has
        ## a unique number
        self.id_num=0
        
    def get_id_num(self):
        # increment utililty id and return it
        self.id_num = self.id_num+1
        return(self.id_num)
        
    def yes_or_no(self):
        answer = 'blah'
        while not answer in 'yn':
            answer = input('Yes or No? ')
            answer = answer.lower()
            answer = answer[0]
        if answer == 'y':
            return(True)
        else:
            return(False)

utility = game_utilities()
