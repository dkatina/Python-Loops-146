#While loops allow us to repeat code while a condition is true

#It will continue to run until that condition is False or we break out of the loop

#Syntax 

#while (condition):
#   code block

bus = []

#my bus can only fit five people

while len(bus) < 5:
    print('Letting a person on')
    bus.append('Person')


print(bus)

#Need to be careful about infinit loops


#Another thing, failure to launch 
#meaning the loops condition starts as false and never runs


bus = []

#my bus can only fit five people

while len(bus) > 5:
    print('Letting a person on')
    bus.append('Person')


print(bus)
