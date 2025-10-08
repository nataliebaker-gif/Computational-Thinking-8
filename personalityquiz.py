athlete_points = 0 
teacher_points = 0
doctor_points = 0
entrepreneur_points = 0
business_points = 0
Janitor_points = 0
Unemployed_points = 0

input ("Hi! And welcome to my personality quiz! Today we will be finding out which job suits you best! Press enter to continue... ")
input ("To play this quiz, you will answer each question according to your preference. Always answer with capital A, B, or C. Lastly, press enter after you have answered each question. Enjoy! ")
input ("")
answer = input ("Would you rather do A) math work, or B) play your favorite sport, or C) give a lesson on one of your passions? {Answer: ")
if answer == "A" :
    business_points += 1
elif answer == "B" :
    athlete_points += 1
elif answer == "C" :
    teacher_points += 1
print ("********************************************************************************")

answer = input ("Do you like to clean? A) Yes, or B) No {Answer: ")
if answer == "A" :
    Janitor_points += 1
print ("****************************************************************************************")

answer = input ("Would you rather spend a summer day A) making money, or B) swimming in the lake {Answer: ")
if answer == "A" :
    entrepreneur_points += 1
elif answer == "B" :
    Unemployed_points += 1
print("****************************************************************************************")

answer = input ("Would you rather A) Have 10 younger siblings, or B) Be an only child? {Answer: ")
if answer == "A" :
    teacher_points += 2
print ("****************************************************************************************")

answer = input ("Would you rather go to A) math class, or B) health class? {Answer: ")
if answer == "A" :
    business_points += 1
elif answer == "B" :
    doctor_points += 1
print ("****************************************************************************************")

answer =  input ("Which do you find more relaxing? A) video games, or B) cleaning your room, or C) both are very disorienting {Answer: ")
if answer == "A" :
    Unemployed_points += 1
elif answer == "B" :
    Janitor_points += 1
print ("****************************************************************************************")

answer =  input ("In science class, would you rather A) learn about the human body, or B) play on the roof top? {Answer: ")
if answer == "A" :
    doctor_points += 2
elif answer == "B" :
    athlete_points += 1
print ("****************************************************************************************")

answer =  input ("Do you feel motivated to start a business to make money? Example: Car washing, dog walking, baby sitting, etc. A) Yes, or B) No, or C) Not sure yet. {Answer: ")
if answer == "A" :
    entrepreneur_points += 2
elif answer == "B" :
    Unemployed_points += 1
elif answer == "C" :
    Unemployed_points += 1
print ("****************************************************************************************")

answer =  input ("If you were a parent, would you be okay with raising your voice to kids so they obey? A) Yes, or B) No {Answer: ")
if answer == "A" :
    teacher_points += 1
print ("****************************************************************************************")

answer =  input ("Which statement is true about you: A) I find the human body very fascinating. B) I dont care about what goes on in the human body. C) The human body grosses me out. D) Other. {Answer:  ")
if answer == "A" :
    doctor_points += 1
print ("****************************************************************************************")

answer =  input ("Do you play a sport 6 or more days a week? A) Yes, or B) No {Answer: ")
if answer == "A" :
    athlete_points += 1
print ("****************************************************************************************")

answer =  input ("Do you ever clean for fun, or to calm yourself? A) No, or B) Yes {Answer: ")
if answer == "B" :
    Janitor_points += 1
print ("****************************************************************************************")

answer =  input ("In your future Job, are you okay with doing lots of math? A) No, or B) Yes {Answer: ")
if answer == "B" :
    business_points += 1
print ("****************************************************************************************")
    
answer =  input ("Would you rather A) Be your own boss with lots of responsibility, and control, or B) Have a boss, with less control, yet also less responsibility? {Answer: ")
if answer == "A" :
    entrepreneur_points += 1
print ("****************************************************************************************")
#end

if athlete_points>teacher_points and athlete_points>doctor_points and athlete_points>entrepreneur_points and athlete_points>business_points and athlete_points>Janitor_points and athlete_points>=Unemployed_points :
 print("You made it to the end! Based on your results, you would be an amazing athlete!")

elif teacher_points>=athlete_points and teacher_points>=doctor_points and teacher_points>=entrepreneur_points and teacher_points>=business_points and teacher_points>=Janitor_points and teacher_points>=Unemployed_points :
 print("You made it to the end! Based on your results, you would be a great teacher!")

elif doctor_points>=athlete_points and doctor_points>=teacher_points and doctor_points>=entrepreneur_points and doctor_points>=business_points and doctor_points>=Janitor_points and doctor_points>=Unemployed_points :
 print("You made it to the end! Based on your results, you would be an amazing doctor!")

elif entrepreneur_points>=athlete_points and entrepreneur_points>=teacher_points and entrepreneur_points>=doctor_points and entrepreneur_points>=business_points and entrepreneur_points>=Janitor_points and entrepreneur_points>=Unemployed_points :
 print("You made it to the end! Based on your results, you would be an entrepreneur!")

elif business_points>=athlete_points and business_points>=teacher_points and business_points>=entrepreneur_points and business_points>=Janitor_points and business_points>=Unemployed_points :
 print("You made it to the end! Based on your results, you would work in business!")

elif Janitor_points>=athlete_points and Janitor_points>=teacher_points and Janitor_points>=entrepreneur_points and Janitor_points>=business_points and Janitor_points>=Unemployed_points :
 print("You made it to the end! Based on your results, you would be an amazing Janitor!")

elif Unemployed_points>=athlete_points and Unemployed_points>=teacher_points and Unemployed_points>=entrepreneur_points and Unemployed_points>=business_points and Unemployed_points>=Janitor_points : print("You made it to the end! Based on your results, you would be Unemployed! Congrats! (: ")



