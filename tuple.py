#task 2 tuple: create tuple of 5 ele, convert it into list, add new ele,convert back into tuple and print final tuple
#tuple can be modify by converting it into list and then convert it back into tuple 
my_tuple = (10,20,30,40,50) #tuples are immutable (can't update once declared)#list are mutable (can change anytime)
print("Original tuple :",my_tuple)
my_list = list(my_tuple) 
num = int(input("Enter a number to add into list :"))
my_list.append(num)
my_tuple= tuple(my_list)
print("Updated tuple :",my_tuple)
print("----------------------------------------------------------------------------------------")
