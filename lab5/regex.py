import re

with open("row.txt") as file:
  text = file.read()


def first_problem():
  pattern = r'a(b*)'
  matches = []
  for i in range( len(text)):
    if re.fullmatch(pattern, text[i]):
      matches.append(text[i])
  return matches

def second_problem():
  pattern = r'ab{2,3}'
  matches = []
  for i in range( len(text)):
    if re.fullmatch(pattern, text[i]):
      matches.append(text[i])
  return matches

def third_problem():
  pattern = r'[a-z]+_[a-z]+'
  matches = []
  for i in range( len(text)):
    if re.fullmatch(pattern, text[i]):
      matches.append(text[i])
  return matches

def fourth_problem():
  pattern = r'[A-Z]+_[a-z]+'
  matches = []
  for i in range( len(text)):
    if re.fullmatch(pattern, text[i]):
      matches.append(text[i])
  return matches

def fifth_problem():
  pattern = r'a.*b$'
  matches = []
  for i in range(len(text)):
    if re.fullmatch(pattern, text[i]):
      matches.append(text[i])
  return matches

def sixth_problem(text):
  pattern = r'[,.]'
  for i in range(len(text)):
    text[i]=re.sub(pattern,":",text[i])
  text =''.join(text)
  return text 

def seventh_problem(text):
    components = text.split('_')
    camel_case_string = components[0] + ''.join(x.title() for x in components[1:])
    return camel_case_string

def eighth_problem(text):
    split_strings = re.findall('[A-Z][^A-Z]*', text)
    return split_strings

def ninth_problem(text):
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return modified_string

def tenth_problem(text):
    snake_case_string = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
    return snake_case_string  

print(ninth_problem(text))





