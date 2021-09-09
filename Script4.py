print(len([1,2,3,4]))

list = [1,2,3,4,5]+[6,7,8,9,10]
print(list)

list1 = [12,78,21,22,12]*12
print(list1)

#list Iteration and Comprehension

3 in [1,2,3] #Membership

for x in [1,2,3,4,5]: #Iteration
    print(x,end='')

res = [c*4 for c in 'HELLO'] # List Comprehension
print(res)


L = ['SPAN','SPAN','JAVA','PYTHON']
L[1]

#Changing Lists In-Place

#index and slice assignments

L = ['spam','Spam','SPAM']
L[1] = 'eggs' # Index assignments
print(L)

L[0:2] = ['eat','more'] #Slice assignments: delete+insert
print(L)

#List method calls

L.append('please')
L
L.sort()
''' You can modify sort behavior by passing in keyword arguments-- a special 'name=value' '''
L = ['abc','ABC','aBe']
L.sort()
L

L = ['abc','ABD','aBe'] # Normalize to lowercase
L.sort(key=str.lower)
L


#Dictionary in Action

D = {'spam':2,'ham':1,'eggs':3}
D['spam']
D['ham'] = ['grill','bake','fry'] # change entry
D ['spam'] = ['hello','java','tech']
print(D)

del D['eggs']  # delete dic.
print(D)

D['brunch'] = 'Bacon'
print(D)

list(D.items())
list(D.keys())
print(D.values())


#Update

D = {'name':'Vipin Kumar','address':'Lucknow'}
print(D)

D1 = {'phone_number':'9199922','email':'pro@12gmail.com'}
D.update(D1)
