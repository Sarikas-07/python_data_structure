#direct input method
numbers = [10,20,30,40,50,60]
print(numbers)
print("-------------------------------------------------------------------------")

#inpuut from user for list
list1 = []
for i in range(5):
    num = int(input(f"Enter {i+1}  number :"))
    list1.append(num)
print(list1)
print("-------------------------------------------------------------------------")

#task 1 list: take 6 no.s from user, store them into list, print sum of all and 2nd largest no.
numbers = [ ]
num = int(input("Enter numbers to find sum of all :"))
numbers.append(num)

total = num
largest = num 
count = 0

for num in range(5) :
    num = int(input("Enter numbers to find sum of all :"))
    numbers.append(num)
    total += num #for finding sum of elements

    if num > largest :
        largest = num #for finding largest number

    if num % 2 == 0:
        count +=1

print("sum of all elememts : ",total)
print("Largest number from above numbers is :",largest)
print("Count of total even numbers present :",count)
print("---------------------------------------------------------------------------------------------")
