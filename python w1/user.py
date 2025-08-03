#Get user input
num1 = int(input("Enter the first number:  "))
num2 = int(input("Enter the second number: "))

# choose an operator
operation = input("Enter the operation (+,-,*,/): ")

#perform the operation
 
                      #Addition
if operation == '+':
  result = num1 + num2
  print(f"{num1} + {num2} = {result}")


                      #Substration
elif operation == '-':
  result = num1 - num2
  print(f"{num1} - {num2} = {result}")


                       #multiplication
elif operation == '*':
  result = num1 * num2
  print(f"{num1} * {num2} = {result}")


                        #Divison
elif operation == '/':
  result = num1 / num2
  print(f"{num1} / {num2} = {result}")



