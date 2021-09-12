# Tuples

'''Tuples in actions'''
(1,2,3,4)+(5,6,7,8) # Concatenation

(1,2,3)*5 # Repetition

T = (1,2,3,4,5) #Indexing slicing
T[0],T[1:2]

#Conversions methods and immutability

T = ('aa','bb','cc','dd','ee')
print(T)

temp = list(T)
print(temp)
temp.sort()

print(temp)

T = tuple(temp)
print(T)

'''List Comprehension tuple Conversions'''

T = (1,2,3,4,5,6,7,8,9)
L =[x+12 for x in T]
print(L)


myfile = open('mytextfile.txt','w')  #Open for text output:create/empty
myfile.write('File methods tell you that you have reached the end of the file') #Write a line of text:string

myfile.close() #Flush output buffers to disk

myfile.open('mytextfile.txt') # Open for text input: 'r' is default
myfile.readline() #Read the lines back
myfile.readline()

open('mytextfile.txt').read()  # Read all at once into string

print(open('mytextfile.txt').read()) #user-friendly display

for line in open('myfile'):
    print(line,end='')
    
