#Nested Loops

#A loop inside of a loop

#because the inner loop is in the code block of the outter loop
#the inner loop will run to completion every to the outter loop iterates once

nums = [1,2,3,4]

for num1 in nums:
    print('Outter loop iteration:', num1)
    for num2 in nums:
        print('Inner loop iteration:', num2)


#-- Topping Combination

toppings = ['Pepperoni', 'Sausage', 'Ham', 'Pineapple', 'Olives']

for topping_1 in toppings:
    for topping_2 in toppings:
        if topping_1 == topping_2:
            print('Double', topping_1)
        else:
            print(topping_1, topping_2)