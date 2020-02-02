02/01/2020

Define a function max() that takes two numbers as arguments and returns the largest of them. Use the if-then-else construct available in Python. (It is true that Python has the max() function built in, but writing it yourself is nevertheless a good exercise ).
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
Define a function that computes the length of a given list or string. ( It is true that Python has the len()function built in, but writing it yourself is nevertheless a good exercise ).  [note : you can’t use inbuilt len() function]
Write a function that takes a character ( i.e. a string of length 1 ) and returns True if it is a vowel, Falseotherwise.
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
Define a function reverse() that computes the reversal of a string. For example, reverse( "I am testing" )should return the string "gnitset ma I".
Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards). For example, is_palindrome( "radar" ) should return True.
Write a function is_member() that takes a value ( i.e. a number, string, etc ) x and a list of values a, and returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator). [note : you can’t use inbuilt is function]
Define a function overlapping() that takes two lists and returns True if they have at least one member in common, False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, you should (also) write it using two nested for-loops.
Print the following ( using two for loops )
	
# # # # #
# # # #
# # #
# # 
#

Shiven & Sanju has to create a github account and share

1.def max(a,b):
    if(a<b):
        print(a)
    else:
        print(b)
        
2.        def max_of_three(a,b,c):
    if(a>b and a>c):
        print(a)
    elif(b>a and b>c):
        print(b)
    else:
        print(c)
        
 3.       def func(name):
    a=0
    for i in name:
        a=a+1
    print(a)
    
    3.str=input("Enter Name:")
func(str)

4.def vowel(vow):
    i=['a','e','i','o','u']
    vow=input("Enter Letter:")
    if (vow in i):
        print("True")
    else:
        print("False")
        
        4.vowel(name)
        
6.def str_reverse(name):
    name=input("Enter Name:")
    for i in range(len(name)-1,-1,-1):
            print(name[i])
            
            6.str_reverse(name)
