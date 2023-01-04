'''
Name : Prashant Rawat
Date : 4/01/2023	
'''


import random

#function to print list 
def printer(ssc):
	print(lst,'\n ','   '*(ssc),'^',sep='')
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
	sn=step-1
	print('\n\nStep : ',step)
	#shorting list
	for i in range(0,8):
		if lst[i+1]<lst[i] and lst[i+1]<lst[sn]:
			sn=i+1
	printer(sn)
	a=lst[step-1]
	lst[step-1]=lst[sn]
	lst[sn]=a
	i=1
	print(lst)
	sorted=True
	#cheacking if the list is sorted
	while i<len(lst) and sorted:
		if lst[i]<lst[i-1]:
			sorted=False
		i+=1
	step+=1
	
print(lst)