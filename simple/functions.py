def mean(val):
    if isinstance(val, dict):
        the_mean=sum(val.values()) / len(val)
    else:
        the_mean = sum(val)/len(val)
    return the_mean

sample = [0, 3, 4]
student_grades ={"b":10, 'a':5, "c":10}
print(mean(student_grades))
print(mean(sample))

x = 3
y = 1
if x > y:
    print('x is greater than y')
elif x == y:
    print('x is same as y')
else:
    print('x is less than y')

def temp(t):
    if t>7:
        return "Warm"
    else:
        return 'Cold'

print('-------------------user input-----------------------')
#user_input = float(input('Enter Temp: '))
#print(user_input.lower())
#print(temp(user_input))

print('-------------------more input-----------------------')
first = input("Enter your name: ")
last = input("Enter your name: ")
message = "Hello %s %s!!" % (first, last)
message = f"Hello {first} {last}"
print(message)
