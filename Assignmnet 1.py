#1. Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
 
for iteration in range(1,11):
    Sum = iteration + (iteration - 1)
    print(Sum)

#Ans(1,3,5,7,9,11,13,15,17,19)

print("-----------------------------------------------------------------")

#2. Print the following pattern
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5
    
for i in range(1 , 6):
    letters = str(i)* i
    print(*letters,sep=" ")

#ans ->
#1
#2 2
#3 3 3
#4 4 4 4
#5 5 5 5 5


print("-----------------------------------------------------------------")

#3. List is given below:
#numbers = [12, 75, 150, 180, 145, 525, 50]
#Write a program to display only those numbers from a list that satisfy the following conditions:
#i. The number must be divisible by five
#ii. If the number is greater than 150, then skip it and move to the next number
#iii. If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
for index in range(len(numbers)):
    if (numbers[index]%5==0):
        print(numbers[index])
    if (numbers[index] > 150):
        index +=1
    if (numbers[index]>500):
        print(numbers[index])
        
            
print("-----------------------------------------------------------------")

#4. Display Fibonacci series up to 10 terms
#The Fibonacci Sequence is a series of numbers. The next number is found by adding
#up the two numbers before it. The first two numbers are 0 and 1.

terms = 10
n1 , n2 = 0,1
count = 0
while (count < terms):
    print(n1)
    nth = n2+n1
    n1 = n2
    n2 = nth
    count+=1

print("-----------------------------------------------------------------")

#5. Write a program to use the loop to find the factorial of a given number.
#The factorial (symbol: !) means to multiply all whole numbers from the chosen number
#down to 1.
    
num = int(input("Enter an Integer : "))
fac = 1
if (num == 0 or num == 1):
    print (f"The Factorial of {num} is = {1}")
else:
    for integer in range(1,num+1):
        fac = integer * fac
    print(fac)
    

print("-----------------------------------------------------------------")

#6. Write a program to iterate a given list and count the occurrence of each element and
#print to show the count of each element.
#sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
#Expected Output:
#Printing count of each item 11: 2, 45: 3, 8: 1, 23: 2, 89: 1


sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
lst1=[]
i = 0
while i < len(sample_list):
    count = 0
    e = i
    lst = []
    while e < len(sample_list):
        if (sample_list[i]==sample_list[e]):
            count+=1
            save = e
        e+=1
    lst.append(sample_list[save])
    lst.append(count)
    lst1.append(lst)
    i+=1
print(lst1)


print("-----------------------------------------------------------------")


#7. Given two lists, l1 and l2, write a program to create a third list l3 by picking an
#odd-index element from the list l1 and even index elements from the list l2.
#Given:


l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3=[]
for i in range(0,len(l1)):
    if (i%2==0):
        l3.append(l2[i])
    if(i%2!=0):
        l3.append(l1[i])

print(l3)

#Ans -> [4, 6, 12, 12, 20, 18, 28]




















