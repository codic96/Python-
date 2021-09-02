print('Hello String') #Single quote
print("Hello String") #double quote

title = 'Meaning of life'
print(title)

# String backslash characters

'''
\newline    Ignored (continuation line)
\\             Backslash(store one)
\'              Single quote
\"              Double quote
\a              Bell
\b              Backspace
\f              Formfeed
\n              Newline
\r              Carriage return
\t              Horizontal tab
\v              Vertical tab
\xhh            characters with hex value hh(at most 2 digits)
\ooo             Character with octal value ooo
\O               Null:binary 0 character
\N{id}           Unicode database ID
\uhhh            Unicode 16-bit hex
\Uhhhhhh         Unicode 32-bit hex
\other           Not an escape
'''

# Raw Strings Suppress Excapes

myfile = open('C:\new\text.dat','w')
print(myfile)

myfile = open(r'C:\new\text.dat','w')
print(myfile)


#Triple Quotes Code Multiline Block Strings

mantra = """ Always look on the bright side of the life."""
print(mantra)


# String in Actions

 '''Basic Operation '''
 len('abc') #length Operation

 'abc'+'def'  # Concatenation

 'Ni1'*4 #Repetition

 myname = 'Hacker'
 for c in myname:print(c,end='')

 # Indexing and Slicing


 S = 'Spam'
 S[0],S[-2] #Indexing from front or end
 S[1:3],S[1:],S[:-1] #Slicing:extact a section


St = 'abcdefghijklmnopqrstuvwxyz'
St[1:12:0]
St[1:0:-1]
St[::1]
St[::12]


#String Conversion Tools

int('12'),str(12)

#Character code Conversion

ord('Hello')
chr(12)

#Changing Strings
''' The immutable part means that you can't change a string in-place'''
S='Spam'
S[0]='x' #error

S = S+'Hello' #Concatenation
print(S)

S = S[:4]+'Burger' # Slicing

print(S)

#String methods


#Changing Strings

S ='spammy'
S = S[:3]+'xx'+S[5:]
print(S)

S1 = 'String Methods'
S1 = S1.replace('Methods','Data User')
print(S1)

S2 = 'The find method returns the offset where the substring appears'
where = S2.find('find')
print(where)

#Convert the list String

S = 'The immutable part means that you cant change a string'
L = list(S)
print(L)

print(L[0])

#Other comman String Methods in Action

line = "The knights who say Ni!"
line.rstrip()
line.upper()
line.isalpha()
line.endswith('Ni')
line.startswith('The')

# The Original String Module

#X.method(arguments)
#string.method(X,arguments)

import string
S ='a+b+c'
y = string.replace(S,'+','Spam')
print(y)

# String Formatting Expressions

'''s       Strings
r          uses repr
c          character
d          Decimal
i          Integer
u          Same as d
o          Octal Integer
x          Hex Integer
X          but print uppercase
e          Floating-point
E          print uppercase
f          Floating point
F          Floating point decimal
g          Floating-point e or f
G          Floating-point E or F
%          Literal%       '''
