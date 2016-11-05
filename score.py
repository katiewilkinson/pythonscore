
print "Scores and Grades"
#creates a range from 0-10
for count in range(0,10):
    #sets variable score from 70-100
    score = (70,100)
# if score is less than or equal to 70 than the grade is d
    if(score <= 70):
      grade = "D"
      # if the score is less than or equal to 80 than the score is c
    elif(score <= 80):
      grade = "C"
    elif(score <= 90):
      grade = "B"
      #otherwise for all others the grade is A
    else:
      grade = "A"
      #print end
    print "end of program bye"
