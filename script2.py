a = 12 # Integer
a = 12.78 #Floating Numbers
a = 'Span' # String

print(a)

#Object are Garbage Collected

a = 12
a = 'Spam'

print(a)

# Shared Referances

a = 3
b = a
print(b)

a = 3
b = a
a = a+2
print(a)
