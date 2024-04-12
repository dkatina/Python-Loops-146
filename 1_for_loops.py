#Intro to For Loops

#Allow us to execute a code block for every item in an iterable ('string', 'list')

#They allow us to repeat code a limited number of times (numbers of times is determined by the iterable)

#Syntax of for loop

#for item in iterable:
#   code block


flavors = ['Vanilla', 'Chocolate', 'Mint', 'Caramel']

for flavor in flavors:
    # print('Running Code Block')
    # print(flavor)
    print('Tasting the', flavor, 'flavor')

guest_list = ['Dylan', 'Travis', 'Christian', 'Sarah', 'Shoha']

line = ['Adam', 'Craig', 'Dylan', 'Travis', 'Billy Bob']

#door man for loop

for person in line:
    print('*',person,'walks up *')
    if person in guest_list:
        print('Welcome to the Party!', person)
    else:
        print('SCRAAAAMMMM')



nums = [12,5436,2345,45678,145,4568,13245,]

for num in nums:
    if num % 2 == 0:
        print(num, 'is even')
    else:
        print(num, 'is odd')