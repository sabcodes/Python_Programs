monday_temp = [9.1, 8.8, 7.6]

for i in monday_temp:
    print(round(i))
    print('done')
for letter in 'hello':
    print(letter.title())

#colors = [11, 34, 98, 43, 45, 54, 54]
#for i in colors:
#    print(i)

#colors = [11, 34, 98, 43, 45, 54, 54]
#for i in colors:
#    if i>50:
#        print(i)

#colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
#for i in colors:
#    if isinstance(i, int):
#        print(i)

#colors = [11, 34.1, 98.2, 43, 45.1, 54, 54]
#for i in colors:
#    if isinstance(i, int) and i>50:
#       print(i)
print('----------------------------------------------------------------')
#grades ={"barno": 10, "marry":20, "ash": 30}
#for i in grades.items():
#    print(i)

#phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
#for key, value in phone_numbers.items():
#    print('{}: {}'.format(key, value))

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for value in phone_numbers.values():
    print('{}'.format(value.replace('+', '00')))

print('--------------while loop---------------------')

a = 3
while a > 0:
    print(a)
    a = a-1

#username = ''
#while username != 'pypy':
#    username = input("enter usernae: ")

#while True:
#    user = input("Enter: ")
#    if user == 'barno':
#        break
#    else:
#        continue

('----------------------------set example--------------------')
a = [1,1,2,3]
print(set(a))

response = ''

def sentece_maker(s):
    words = ("how", "what", "when")
    cap = s.capitalize()
    if s.startswith(words):
        return '{}? '.format(cap)
    else:
        return '{}. '.format(cap)

while True:
    user = input("Enter: ")
    if user == '\end':
        break
    else:
        response = response +sentece_maker(user)

print(response)

