a = 12
b = 13
# Expression operator
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a>>b)
print(a**b)
print(a&b)

# Built-in mathematical functions
'''pow,abs,round,int,hex,bin'''
# Utility modules
'''random,math etc.'''

# python Expression operator

'''
yield x                     Generator function send protocol
lambda args:expression      Anonymous function generation
x if y else z               Ternary selection
x or y                      Logical OR
x and y                     LOgical AND
not x                       Logical negation
x in y,x not in y           Membership(iterables,sets)
x is y,x not y              Object Indentity tests
x<y,x<=y,x>y,x>=y,x==y,x!=y  Magnitude comparsion
x bitwise OR y               Bitwise OR
x^y                          Bitwise XOR
x&y                          Bitwise AND
x<<y,x>>y                    Shift x left or right by y bitwise
x+y                          Addition,concatenation
x-y                          Subtraction,set difference
x*y                          Multiplication,repetition
x%y                          Remainder,format
x/y,x//y                     Division
-x,+x                        Negation,Indentity
~X                           Bitwise NOT
X**Y                         Power(exponentiation)
x[i]                         Indexing(sequence,mapping,others)
x[i:i:k]                     Slicing
x(...)                       call(function,method,class)
x.attr                       Attribute referance
(...)                        Tuple,expression,generator Expression
[...]                        List,list comprehension
{...}                        Dictionary,set,ser and dictionary comprehensions
'''

# Mixed operator follow operator presedence
#Parenthese group subexpressions
#Mixed types are converted up


# Numbers in Actions

c = 100
d = 200

e = (a+b)*c
print(e)

print(c+b)
print(a+d)
print(d-c)
print(a<b)
print(a==b)
print(a/b)
print(a//b)
print(a>>b)
print(a<<b)
print(a!=b)

#Math function
import math
math.floor(2.5)
math.floor(-30.6)

#Decimal functions
from decimal import Decimal
Decimal('0.1')+ Decimal('0.1')+Decimal('0.1')-Decimal('0.3')

#Fraction function

from fractions import Fraction
x = Fraction(1,3)
y = Fraction(4,6)
print(x,y)


# Sets

x = set('abcdef')
y = set('bdxyz')
print(x)
print(y)

'e' in x  # Membership
x-y       # difference
#x union y # union
x & y      #Intersection
x^y        #Symmetric difference
x>y , x<y  #Superset,subset

