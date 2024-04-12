#range() creates a sequence of number that we can iterate through

#-- range(stop) the sequence will go from 0 to stop non-inclusive

print(range(10))
print('Range to 10')
for num in range(10):
    print(num) #code block executes ten time because of range(10)



#-- range(start, stop) : creates a sequence from start inclusive to stop non-inclusive
print('Range from 5 to 10')
for num in range(5,10):
    print(num) 


#-- range(start,stop, step) : creates a range from start to stop every step-th number
print('Range from 10 to 100, every 10th digit')
for num in range(10,100,10):
    print(num)



#--- range in combination with len

alist = ['item1','item2','item3','item4']

print(len(alist))

for index in range(len(alist)):
    print(index)
    print(alist[index])


food = ['Tacos', 'Tiramisu', 'Pizza', 'Sushi', 'Burger', 'Caesar Salad', 'Burger', 'Key Lime Pie']

for index in range(len(food)):
    if food[index] == 'Burger':
        print('Burger postion:', index)


#Looping over indices can be very useful when dealing with corresponding lists

students = ['John', 'Jim', 'Jane', 'Jill']
grades = [98, 84, 76, 100]
activities = ['Football', 'Woodshop', 'Art', 'Debate Team']

for index in range(len(students)):
    print(students[index], 'has a grade of', grades[index], 'and their activity is', activities[index])