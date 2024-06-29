import re

with open("row.txt", 'r') as file:
  text = file.read()

def first_problem():
    pattern = r"a(b*)"
    print(re.findall(pattern,text))
first_problem()
import re

def match_a_followed_by_zero_or_more_b(text):
  """Matches strings with 'a' followed by zero or more 'b's using regex."""
  pattern = r"a(b*)"
  matches = re.findall(pattern, text)
  print(matches)  # Print the array of matches

def match_a_followed_by_two_to_three_b(text):
  """Matches strings with 'a' followed by 2 to 3 'b's using regex."""
  pattern = r"a(bb|bbb)"
  matches = re.findall(pattern, text)
  print(matches)  # Print the array of matches

def find_lowercase_letter_sequences(text):
  """Matches sequences of lowercase letters joined with an underscore using regex."""
  pattern = r"[a-z]+_[a-z]+"
  matches = re.findall(pattern, text)
  print(matches)  # Print the array of matches

def find_uppercase_followed_by_lowercase(text):
  """Matches sequences of an uppercase letter followed by lowercase letters using regex."""
  pattern = r"[A-Z][a-z]+"
  matches = re.findall(pattern, text)
  print(matches)  # Print the array of matches

def match_a_followed_by_anything_ending_in_b(text):
  """Matches strings with 'a' followed by anything, ending in 'b' using regex."""
  pattern = r"a.*b"  # Use .* for any character zero or more times
  matches = re.findall(pattern, text)
  print(matches)  # Print the array of matches

def replace_punctuation_with_colon(text):
  """Replaces all occurrences of space, comma, or dot with a colon using regex."""
  pattern = r"[ ,\.]"  # Match space, comma, or dot
  replacement = ":"
  new_text = re.sub(pattern, replacement, text)
  print(new_text)  # Print the modified text

def convert_snake_to_camel(text):
  """Converts a snake case string to camel case using regex (not guaranteed for all cases)."""
  pattern = r"(?:^|_)([a-z0-9])"
  def replace_with_uppercase(match):
    return match.group(1).upper()
  new_text = re.sub(pattern, replace_with_uppercase, text)
  print(new_text)  # Print the camel case string

def split_at_uppercase(text):
  """Splits a string at uppercase letters using regex."""
  pattern = r"[A-Z]"
  split_text = re.split(pattern, text)
  print(split_text)  # Print the array of split words

def insert_spaces_before_uppercase(text):
  """Inserts spaces between words starting with capital letters using regex."""
  pattern = r"(?=[A-Z])"  # Positive lookahead for uppercase letter
  new_text = re.sub(pattern, " ", text)
  print(new_text)  # Print the text with spaces added

def convert_camel_to_snake(text):
  """Converts a camel case string to snake case using regex."""
  pattern = r"[A-Z]"  # Match uppercase letters
  def replace_with_underscore(match):
    return "_" + match.group(0).lower()
  new_text = re.sub(pattern, replace_with_underscore, text)
  print(new_text)  # Print the snake case string

# Example usage
text = "This is a_sequence Abc BBba helloWorld someText"

match_a_followed_by_zero_or_more_b(text)
match_a_followed_by_two_to_three_b(text)
find_lowercase_letter_sequences(text)
match_a_followed_by_anything_ending_in_b(text)
replace_punctuation_with_colon(text)
convert_snake_to_camel(text)  # May not work for all cases
split_at_uppercase(text)
insert_spaces_before_uppercase(text)
convert_camel_to_snake(text)
