
homework1=[['IntroCS', 2, 'Maj', 3],['Botany',4,'Elect',1],\
          ['Calc',5,'Elect',4],['ArtHist',1,'Min',1],['CircArts',7,'Maj',1]]
## homework1 is for a student who is taking a double major
## in Circus Arts and Computer Science, with a minor in Art History.
## the order is [subject, due_in_days, Maj/Min/Elect, hours_to_do]

def score_homework(homework):
          ## a lower score means do this task first
          subject,due_in_days,Maj_min,hours_to_do = homework
          ## favor homework that is quick to do and/or is due sooner
          score = due_in_days*hours_to_do
          ## 
          if Maj_min == 'Maj':
                    score = score*.5
          elif Maj_min == 'Min':
                    score = score*.75
          ## favor homework for major and minor over electives
          return(score)

def sort_homework1(homework_list):
          print(homework_list)
          list_to_sort = []
          for homework in homework_list:
                    scored_list = [score_homework(homework)]
                    scored_list.extend(homework)
                    list_to_sort.append(scored_list)
          list_to_sort.sort()
          return(list_to_sort)

print('version1',sort_homework1(homework1))

def sort_homework2(homework_list):
    ## fancier syntax, but does not include the
    ## score used for sorting in the output
          print(homework_list)
          list_to_sort = []
          homework_list.sort(key=score_homework)
          return(homework_list)

print('version2',sort_homework2(homework1))



