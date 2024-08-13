import math

def calculate_factorial(n):
  """Вычисляет факториал числа n с использованием библиотеки math.

  Args:
    n: Целое положительное число.

  Returns:
    Факториал числа n.

  Raises:
    ValueError: Если n не является целым положительным числом.
  """
  if not isinstance(n, int) or n < 0:
    raise ValueError("Число должно быть целым положительным числом.")
  return math.factorial(n)

while True:
  try:
    number = int(input("Введите положительное целое число: "))
    if number < 0:
      raise ValueError
    factorial = calculate_factorial(number)
    print(f"Факториал {number} равен {factorial}")
    break
  except ValueError:
    print("Ошибка! Введите положительное целое число.")