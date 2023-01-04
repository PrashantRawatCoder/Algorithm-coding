'''
Name : Prashant Rawat
Date : 3/01/2023	
'''
import random

#function to print list 
def printer(spc):
	print(lst,'\n ','   '*(spc-1),'^  ^',sep='')
lst=[]
if input('Do you want to enter your own list (if yes enter yes) : ')==('yes' or 'Yes'):
	for i in range(1,10):
		lst.append(int(input(f'Enter {i} value : ')))


# making a random list 
while len(lst)<9:
	ran=random.randint(1,9)
	if ran not in lst :
		lst.append(ran)

print('List is : ',lst)
sorted = False
step=1
while not sorted:
	print('\n\nStep : ',step)
	#shorting list
	for i in range(1,9):
		printer(9-i)
		if lst[9-i]<lst[8-i]:
			a=lst[9-i]
			lst[9-i]=lst[8-i]
			lst[8-i]=a
	
	i=1
	sorted=True
	#cheacking if the list is sorted
	while i<len(lst) and sorted:
		if lst[i]<lst[i-1]:
			sorted=False
		i+=1
	step+=1
	
print(lst)
