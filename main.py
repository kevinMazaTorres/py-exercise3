"""
Exercise 1: Guess the number
Exercise 2: Multiplication table
Exercise 3: Basic calculator
"""

import random

def guess_the_number():
  """
    Using loops, implement a guessing game.
    Guess the number (1-10):
    messages: Too low, Too high, Try again, Congratulations!
  """
  # fix code
  print("Guess the number (1-10):")


def multiplication_table():
  """
    Using a while/for loops, implement a multiplication table.
  """
  # fix code
  print("multiplication_table for {number}")


def basic_calculator():
    """
    Using a while/for loops, implement a basic calculator.
    1. Enter the first number: 10
    2. Enter an operator (+, -, *, /): +
    3. Enter the second number: 20
    4. print 10 + 20 => Result: 30
    """
    num1 = float(input("Ingrese el primer número: "))
    operador = input("Ingrese un operador (+, -, *, /): ")
    num2 = float(input("Ingrese el segundo número: "))

    resultado = None

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Error: No se puede dividir por cero.")
            return
    else:
        print("Error: Operador no válido.")
        return

    print(f"{num1} {operador} {num2} => Resultado: {resultado}")


def main():
  # input choice between 1-3 function
  # call the function
  choice = int(input(f"""
    1. Guess the number
    2. Multiplication table
    3. Basic calculator
    Enter a number (1-3): """))
  if choice == 1:
    guess_the_number()
  elif choice == 2:
    multiplication_table()
  elif choice == 3:
    basic_calculator()
  else:
    print("Invalid choice.")

main()