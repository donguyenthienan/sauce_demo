import re


def convert_string_to_float(string):
  try:
    return float(re.findall("\d+\.\d+", string)[0])
  except:
    return 0.0
