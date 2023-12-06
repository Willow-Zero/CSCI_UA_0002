def div_w_remainder(dividend,divisor):
    whole = dividend//divisor
    remainder = dividend%divisor
    return(whole,remainder) 

big_total = 0
maximum_share = 0

def share_items(number_of_things,number_of_people):
    global big_total
    global maximum_share
    result = div_w_remainder(number_of_things,number_of_people)
    big_total += number_of_things
    maximum_share += result[0]
    if result[1] > 0:
        maximum_share +=1







def question_1():
    share_items(int(input("First number of things: ")),int(input("First number of people: ")))
    share_items(int(input("Second number of things: ")),int(input("Second number of people: ")))
    share_items(int(input("Third number of things: ")),int(input("Third number of people: ")))
    print("big total:", big_total)
    print("maximum share", maximum_share)



question_1()


