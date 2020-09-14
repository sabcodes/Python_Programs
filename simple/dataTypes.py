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

print('-----------------MORE LISTS EXAMPLE---------------------')
monday_temp = [9.1,10.2,11.2]
monday_temp.append(8.1)
print(monday_temp)
monday_temp.clear()
print(monday_temp)
monday_temp = [9.1, 10.2, 11.1, 5.0, 10.5]
#del monday_temp[1:2]
print(monday_temp[1])
print(monday_temp[2:])
#negative index
print(monday_temp[-4:-1])

print('-----------------STRING EXAMPLE---------------------')
mystring= 'hello'
print(mystring[1])
print(mystring[-1])
crazyList = ['hello', 5, 10]
print(crazyList[0][-2])

print('-----------------MORE DICT EXAMPLE---------------------')
student_grades = {"marry":10, "josh":5, "ash": 6}
print(student_grades['josh'])
