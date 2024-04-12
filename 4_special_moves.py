# Special moves

#Break, Continue, and Pass

#---Break : terminates a list prematurly

pay_dirt = ['dirt', 'dirt', 'dirt', 'gold', 'dirt', 'dirt']

for scoop in pay_dirt:
    print('PANNING FOR GOLD!')
    if scoop == 'gold':
        print("WE FOUND OUR GOLD, IM DONE LOOKIN")
        break
    else:
        print('just more dirt, gotta keep lookin')

#--- Continue : continue skips the rest of the code block and moves on to the next iteration

#square odd numbers
nums = [13,256,1146,478,21,3457]

for num in nums:
    if num % 2 == 0:
        continue
    num **= 2
    print(num)


# Pass

my_list = [1,2,3]

for item in my_list:
    pass