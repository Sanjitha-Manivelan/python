02/01/2020	

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
	

5.def sum(s):
    num=0
    for j in range(0,4,1):
        num=num+s[j]
    print(num)

5.n=[]
for i in range(0,4,1):
    s=int(input("Enter Number:"))
    n.append(s)
sum(n)
print(n)

5.def mult(s):
    num=1
    for j in range(0,4,1):
        num=num*s[j]
    print(num)

5.n=[]
for i in range(0,4,1):
    s=int(input("Enter Number:"))
    n.append(s)
mult(n)

6.def str_reverse(name):
    for i in range(len(name)-1,-1,-1):
            print(name[i])
            
            6.str_reverse(name)
	
7.def palindrome(word):
    word=[]
    word2=[]
    word=input("Enter Name:")
    print(word)
    word2=word[::-1]
    print(word2)
    if(word==word2):
        print("True")
    else:
        print("False")
	
	7.palindrome("madam")
	
8.def is_member(a):
    a=[]
    for i in range(0,4,1):
        num=input("Enter Number:")
        a.append(num)
    print(" ")
    s=input("Enter Number To Check:")
    if(s in a):
        print("Yes")
    else:
        print("No")
	
	8.is_member(2)
	
9.a=[]
s=[]
for i in range(0,4,1):
    num=input("Enter Number:")
    a.append(num)
print(" ")
for j in range(0,4,1):
    sa=input("Enter Number To Check:")
    s.append(sa)

for g in range(0,4,1):
    for f in range(0,4,1):
        if(a[g]==s[f]):
            print(" ")
            print("Yes")
            break; 
	
10.for i in range(5,0,-1):
    for s in range(i,0,-1):
        print("#", end = " ")
    print("\n")
