''' Sequence Assignments '''

nudge = 1
wink = 2
A,B = nudge,wink #Tuple Assignments
print(A,B)
[C,D] = [nudge,wink] # List Assignment
print(C,D)

# Advanced sequence assignment patterns
string = 'SPAM'
a,b,c,d = string
print(a,b)
a , b , c = string[0],string[1],string[2]
print(a,b,c)

#with the help of loop
for (a,b,c) in [(1,2,3),(4,5,6)]:
    print(a,b,c)

# Extended Sequence Unpacking in Python 3

'''Extended Unpacking in action '''
seq = [1,2,3,4]
a,b,c,d = seq
print(a,b,c,d)

''' Boundary cases'''
print(seq)
a,b,c,*d = seq
print(a,b,c,d)

# Applications to for loops
for (a,*b,c) in [(1,2,3,4),(5,6,7,8)]:
    print(a,b,c)

#Multiple-Target Assignments

a=b=c='Spam'
print(a,b,c)

'''Augmented Assignments'''

x = 1
x=x+1 # Traditional
print(x)

x += 1
print(x) #Augmented

'''Expression Statements'''

span(eggs,ham) #Function calls
spam.ham(eggs) #Method calls
spam          #printing variables in the interactive interpreter
print('a,b,c,sep=''') #printing operations in Python 3.0
yield x**2  # Yield expression Statements


''' Expression statements and in Place changes '''
L = [1,2]
L.append(3)
print(L)
