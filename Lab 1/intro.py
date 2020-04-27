

def separator():
    print('_____________________________')
    print ('inside')

print('Hello World!') 

# data types
name = "Alex"
last = "Vito"
age = 23
found = False
average = 2.345

print(name)
print(average)
print(found)

# Operations
print(21 + 21)
print(100 - 50)
print(12 * 321)
print(100 / 10)
print(10 % 3) # % = modulus operator (gives the residue)

print (name + name)
print(age + age)
print(name + str(age))
    
separator()

if(age < 90):
    print("You are still young")
elif(age == 90):
    print('You are on the border line')
else:
    print('Sorry bud, you are getting old:)')