
# This is comment  when the hastage has been put in the code it will readed as a comment 

"""
this is the multi line comment used for 
some explanation in the code whisch ahsmore explanaion

"""
 
# Case senstive 

"""
Case Sestive  ABC abc Abc

"""
# Key Words 

"""
reserved word for python eg : True False

"""
# Variables 

"""
variable that starts with alphabet or an underscore (abc, __)

"""
"""
a = 10
sanju = rthgf
rea# = 45

"""
# Data Types
"""
Integer = 100 ( numbers are dentoed as number in the variable represents )
Float = 10.3 ( when comes with decimal form its a float data types)
Complex = 50j ( when j comes after the  number (j)= square root of -1)
String = ("hi this price is 400$ )string is used for store any type of data inside the value of "" or '')
boolean = key words reservedin python libraries

"""

#Print()-function
"""
two types of function in this sequence 
that is print(a) that print the variabl that stored in the variable a 
another one is print("a") actualy prints an a is the output.
"""
"""
a = 10
saanju = "name in it"
print(a,saanju)
print("defenition")
""" 
#  Escape Sequence 
"""
print("hi sanju \\'how are you \"iam fine about u\"") 


print("hi da \tmapla \"epadi \niruka\"")
"""
#type casting 
"""



a=10
b=10.5
c=10+4j
d="hisanju"
e= False 
print(a,type(a),b,type(b),c,type(c),d,type(d),e,type(e))


"""
"""
total=0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
         total += i
print("Sum of all multiples of 3 or 5 below 1000 is:", total)
"""

#A rithmetic operators
"""
print(100 + 100)    # its addition
print(100 - 100)    # its a subraction 
print(100 * 100)    # its a multiplication
print(100 / 100)    # its a division
print(89 ** 15) # r os the value example 100 to the power of 100 
print(100 // 100)   # quotient
print(100 % 100)    # reminder

"""
# Assignment Operator

"""
a = 55              # a = 55 it perfoms like this 
print(a)

a += 59             # a = a + 59
print(a)

a **=76             # a = a ** 76
print(a)

a //= 65            # a = a //= 65
print(a)

a %= 15             # a = a %= 15
print(a)
 
a *= 46             # a = a * 46
print(a)

a /= 89             # a = a / 89
print(a)

a -= 56             # a = a - 56 
print(a)

"""

# Comparison Operator
"""
a = 56
b  = 58

print(a == b)
print(a != b)
print(a > b)
print(a>=b)  
print(a<b, a<=b)
"""
# Python Collectio 
"""
List is collection collection of multiple data types are been stored in a single variable  for
 eg :  a=[10,"sanu", 5.667, 6j, ]
 called as list variable

sanju = [5,"sju" ,4.5, 6j ]
print(sanju, type(sanju))
 """

# list will indicates in a three typr
# List []
"""
sanju = ["sefr","def",45,6.7,"gello"]
print(sanju[2])                 #--> its an ordered tpye and it changable & it allows duplicate members
sanju[3] = "true"
print(sanju,type(sanju))
"""
# Tuple ()
"""
sanju = ("sefr","def",45,6.7,"gello",1,1,1,1,1,1,1,1)
print(sanju[2])                 #-->  tuple an ordered tpye and it unchangable & it allows duplicate members
print(sanju,type(sanju))
"""
# set{}
"""
sanju = {"sefr","def",45,6.7,"gello",1,1,1,1,1,1,1,1}
               #-->  Set allows an multiple duplicate  entries  but it will reflect on the resule and it will  changes the result as per the py libs
print(sanju,type(sanju))
"""

# Dictonary
"""
sanju = {
    "hi " : "how can i help " ,
    "how" : "you  out for youi",      #  --> its an un ordered and changable no duplicate entries willbe perfomed  
    "fine da buddy"  : "today"}       #  --> it will be denoted as {:} using this value only it assigned as a dict
sanju[4] = "kick you"
print(sanju,type(sanju))
"""

# immutable and mutable data types  
# in immutable samae value stores an ind of the value like a=1 means 1254254155412  while b=1 in the sense  the id will be remains the same  1254254155412
# in  mutabl;e data type  same value that store an seperate seperate valuse inthe location lib a=1 45124512454 b=1 1215154154251451 id will be differ from one another 

#example immmutable
"""
a=1
b=1
print(id(a))
print(id(a))

# muttable  [denotes by this bracket]
a=[1,2,3,4,5,6]
b=[1,2,3,4,5,6]
print(id(a))
print(id(b))
"""
#Identify Operators
 #it checks the momory address of the value stord in the lib 

a=34
b=34
print(a == b)  # --> comparision operator has been used 
print(a is not b)   #--> identify operator has been used it checks the varable address that stored in the lib

a=1
b=1
print(a == b)  # --> comparision operator has been used 
print(a is b)  

#Membership operator
 
#get ab input foem an use and print the functions

toll1 = int(input("Chennai toll1 collected amount rs: "))
toll2 = int(input("Vellore toll2 collected amount rs: "))
toll3 = int(input("Ambur toll3 collected amount rs: "))
toll4 = int(input("Gudiyatham the toll4 collected amount rs: "))
if(toll1 > 100):
    print(toll1, "Charged an higher Price as per the norms of RTO")
    if(toll1<100):
        print(toll1, "Chennai Charged an Valuable amount and \"Good\"")
        if(toll1> 300):
            print("Too much amount has been Collected in Chennai ")
    elif(toll1 > 1000):
        print("Rais an complaint against an \"RTO\" in chennai and inform to the the owner")
if(toll2 > 150):
    print(toll2, "Charged an higher Price and inform to owner")
    if(toll2<120):
        print(toll2, "Vellore Charged an Valuable amount and \"Good\"")
        if(toll1> 300):
            print("Too much amount has been Collected in Vellore ")
    elif(toll2 > 700):
        print("Rais an complaint against an \"RTO\" and inform to the the owner")
if(toll3 > 50):
    print(toll3, "Charged an higher Price and inform to owner")
    if(toll3<30):
        print(toll3, "Charged an Valuable amount and \"Good\"")
        if(toll1> 300):
            print("Too much amount has been Collected in Ambur ")
    elif(toll3 > 1000):
        print("Rais an complaint against an \"RTO\" and inform to the the owner")
if(toll4 > 100):
    print(toll4, "Charged an higher Price and inform to owner")
    if(toll1<100):
        print(toll4, "Charged an Valuable amount and \"Good\"")
        if(toll1> 300):
            print("Too much amount has been Collected in Gudiyatham ")
    elif(toll4 > 500):
        print("Rais an complaint against an \"RTO\" and inform to the the owner")
sum = toll1 + toll2 + toll3 + toll4
print("THe trip has been complted sucessfully and the total spent inthe tool amount would be \n :" , sum)

"""
#  Loop Statement 
"""
"""i. For Loop 
ii. while Loop
"""
"""
a = 1
while a>0:
    print(a)
    a=a + 1
"""
"""

num =35
symbol = "%"

counter =1
b=1
while b<=num:
    a=1
    while a<=counter:
        print(symbol, end="Y")
        a+=1
    print()
    b+=1
    counter +=1
print("loope ended here")
"""