import re


def convert_string_to_float(string):
  try:
    return float(re.findall("\d+\.\d+", string)[0])
  except:
    return 0.0


def add_numbers(*numbers):
  return sum(number for number in numbers)
