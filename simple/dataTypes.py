import datetime
#this is ex of var
time = datetime.datetime.now()
print(time)

#mynum = 6
#print(mynum)
#mynum='hello'
#print(mynum)
#num = 10
#word = 'word'
#print(num,word)

#ex of different var
x=10
y='barno'
sum1=x+x
sum2=y+y
z= 10.1 #float
print(sum1)
print(sum2.upper())
print(type(x), type(y), type(z))

print('-----------------LIST EXAMPLES---------------------')
grades = [9.1, 5.5, 10.1]
print(grades)
print(list(range(10, 100, 5)))

grades=[75, 10.5, 100, 70]
mysum= sum(grades)
length= len(grades)
ave=mysum/length
print(ave)

print('-----------------DICTIONARY EXAMPLE---------------------')
grades={'Barno':10, 'Arno':9, 'Ash': 8}
print(grades.values())
print(grades.keys())
mysum= sum(grades.values())
length= len(grades)
ave=mysum/length
print(ave)

print('-----------------TUPLE EXAMPLE---------------------')
temp=(1,4,'hello')
print(temp)