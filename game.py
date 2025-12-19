import random

def generate_secret():
  digits = list(range(10))
  random.shuffle(digits)
  return ''.join([str(digit) for digit in digits[:4]])


if __name__ == '__main__':
  main()
