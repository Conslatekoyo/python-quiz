# Q1. Write a program in Python to remove duplicate items from a list.
def remove_duplicate(list):
    list2=[]
    for i in list:
        if i not in list2:
            list2.append(i)
    return list2
print(remove_duplicate([1,22,22,33,44,44,5,6,7,8,8,8,10]))

# # Q2. Write a program, to sum up, all the elements of a list.
def sum_elements(given):
    sum=0
    next=1
    for num in given:
        next+=1
        sum+=num
    print(sum)
sum_elements([1,2,3,4,5])

# # Q3. Write a program to sum all the values of a dictionary.
def sum_values():
    a={"school":14,"cities":10,"towns":47}
    c=a.values()
    sum=0
    for num in c:
        sum+=num
    print(sum)
# sum_values()

# # Q4. Use a dictionary to store antonyms of words. E.g.- 'Right':'Left', 'Up':'Down', etc. Display all words and then ask the user to enter a word and display the antonym of it.
def atonym():
    c={'Right':'Left','Up':'Beneath','Top':'Down'}
    print(c)
    d=str(input("Enter a word:"))
    for d in c:
        if d in c:
            print(d.value())
atonym()
    

# Q5: Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are squares of keys.
# def squared_values(dict):
#     product=
# Q6: Write a Python program to create a dictionary from two lists without losing duplicate values.


    

# Q7:  Write a Python program to convert more than one list to a nested dictionary.
# Q8. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Q9:  Write a Python program to move all zero digits to the end of a given list of numbers.e
#    Ie;  Original_list=[1,30,2,0,4,21,0,45,23,78,0,12,0,5]
#          Expected_Outcome=[1,30,2,4,21,45,23,78,12,5,0,0,0,0]
# Q10: Write a Python program to remove consecutive duplicates of a given list.
def remove_duplicates():
    a=[3,4,5,6,7,8,8,8,8,8,5,5,5,6,6,6,6,8,9]
    b=[]
    for num in a:
        if num not in b:
            b.append(num)
    print(b)
remove_duplicates()
    

# Q11:  Write a Python program to check whether an element exists within a tuple.
def existence():
    r=(2,3,4,5,6,7)
    int(input("Enter number:"))
    for num in r:
        if num in r:
            return True
        else:
            return False
print(existence())


# Q12: Write a Python program to convert a given string list to a tuple.
def convert_string():
    w=['1','2','3','4','5','6']
    print(tuple(w))
convert_string()

