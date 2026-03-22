#task 5 :take 5 students name from user in list, take marks and store it into dict, and print student with highest marks
my_dict = {}
for i in range(5):
    name = input(f"Enter a name of student { i+1 }:") #f" is used to format a sting called formatted string 
    marks = int(input(f"Enter marks of student {name}:"))
    my_dict[name] = marks
print("All students and their marks :")
for name,marks in my_dict.items():
    print(name ," : " ,marks)

max_marks = list(my_dict.values())[0]
top_student = ""
for name,marks in my_dict.items():
    if marks > max_marks:
        max_marks = marks
        top_student = name
print("***********Top student************")
print(name," with marks :",max_marks)
