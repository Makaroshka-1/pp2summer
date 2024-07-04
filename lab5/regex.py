import re

with open("row.txt") as file:
  text = file.read()

def first_problem(text):
  pattern = r'a(b*)'
  return re.findall(pattern, text)

def second_problem(text):
  pattern = r'ab{2,3}'
  return re.findall(pattern, text)

def third_problem(text):
  pattern = r'[a-z]+_[a-z]+'
  return re.findall(pattern, text)

def fourth_problem(text):
  pattern = r'[A-Z][a-z]+'
  return re.findall(pattern, text)

def fifth_problem(text):
  pattern = r'a.*?b'
  return re.findall(pattern, text)

def sixth_problem(text):
  pattern = r'[ ,.]'
  return re.sub(pattern, ':', text)

def seventh_problem(text):
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def eighth_problem(text):
    pattern = r'[A-Z][a-z]*'
    return re.findall(pattern, text)

def ninth_problem(text):
    pattern = r'(?<!^)(?=[A-Z])'
    return re.split(pattern, text)

def tenth_problem(text):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return snake_case_string  

string1 = "ayoNumber1"
print((third_problem(text)))





