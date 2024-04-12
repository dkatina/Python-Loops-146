#There are 3 main ways to exit a while loop
# Break condition, False Flags, Control Variable State Change


#------ Break, break terminates the loop immediately

while True:
    fav_food = input('Whats your favorite food?')

    if fav_food == 'tacos':
        print('That is the correct answer. Enjoy The Fiesta!')
        break
    else:
        print('WRONG ANSWER TRY AGAIN!!!')


#----- Flags, allow the rest of the code block to execute, but terminate the loop after
#can be nice for grand exits

searching = True
hours = 0

while searching:
    found = input('Has anyone found my keys? yes or no ')
    if found == 'yes':
        searching = False
    hours += 1
    if not searching:
        print('Thank you all for helping me find my keys.')
        print('It only took us', hours, 'hours!')


#--- Control Variables state changes so the condition is eventually false

count = 0

while count <= 10:
    print('running my code!')
    count += 5


alist = ['this', 'that', 'the other']
index = 0

while index < len(alist):
    print('Doing', alist[index])
    index += 1

