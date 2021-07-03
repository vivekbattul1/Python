#42. [Interactive Coding Exercise] Banker Roulette - Who will pay the bill?
#==>
import random
#split string method
name_string = input("Give me everybody's name, seprated by a comma.\n")
names = name_string.split(", ")

#get the total number of items in list
num_items = len(names)
#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items -1 )
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")
