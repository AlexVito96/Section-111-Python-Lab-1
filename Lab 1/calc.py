def separator():
    print("-" * 30)
    
def print_menu():
    print('\n' * 5)
    # is there a way to clear console
    separator()
    print("Welcome to PyCalc")
    separator()

    print('[1] - Add')
    print('[2] - Substract')
    print('[3] - Multiply')
    print('[4] - Divide')


    print('[x] - Close')

    separator()

def sum(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

opc = ''
while(opc != 'x'):
    print_menu()
    opc = input('Please select an option: ')
    if(opc == 'x'):
        break # breal = finish loop
    
    num1 = float(input('First Number: ' ))
    num2 = float(input('Second Number: ' ))

    if(opc == '1'):
        res = sum(num1, num2)
        print("Result:" + str(res))
    elif(opc == '2'):
        res = subtract(num1, num2)
        print("Result:" + str( subtract(num1, num2)))
    elif(opc == '3'):
        res = multiply(num1, num2)
        print("Result:" + str(res))
    elif(opc == '4'):
        res= divide(num1, num2)
        print("Result:" + str(res))
    

    input("Press Enter to continue...")

print("Byte Byte!")

# on division, show an error if the user tries to devide by 0
# return 0 from the fn

