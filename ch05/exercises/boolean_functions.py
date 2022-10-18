letter_grade = ''

def percentage_to_letter(score):
  if score >= 90:
    letter_grade = 'A'
  elif score >= 80:
    letter_grade = 'B'
  elif score >= 70:
    letter_grade = 'C'
  elif score >= 60:
    letter_grade = 'D'
  else:
    letter_grade = 'F'
  return letter_grade

def is_passing(letter=None):
  if (letter == 'A') or (letter == 'B') or (letter == 'C'):
    return True
  else:
    return False

print(is_passing(percentage_to_letter(float(input('Enter a score: ')))))