om ="""___________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""
print(om)
print()







#add
def add(n1, n2):
  return n1 + n2

#sub
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

#operation
operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
num1 = int(input('Enter Your first word:- '))
for symboll in operation:
  print(symboll)
operation_symbol = input("Enter operation:- ")
num2 = int(input("enter your second number here:- "))
calculate_fun = operation[operation_symbol]
answer = calculate_fun(num1, num2)
print(f"{num1} {operation_symbol} {num2} =  {answer}")
