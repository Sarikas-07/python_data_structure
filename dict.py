#task 4 dictionary: take a string from user, count frequency of each character, store it in dict and print
string = input("Enter a string :")
my_dict = {}
for ch in string:
    if ch in my_dict:
        my_dict[ch] += 1
    else :
        my_dict[ch] = 1
print("Frequency of characters are :",my_dict) 
print("---------------------------------------------------------------------------------------")