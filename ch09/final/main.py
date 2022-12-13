import CatFactAPI
import QuoteAPI

def main():
  score = 0
  number_of_qs = 5
  qapi = QuoteAPI.QuoteAPI()
  quote_result = qapi.get()
  insp_quote = quote_result['advice']
  for num in range(0, number_of_qs):
    capi = CatFactAPI.CatFactAPI()
    cat_q_result = capi.get()
    cat_fact = cat_q_result[0]
    if "not " in cat_fact:
      falsified_fact = cat_fact.replace("not ", " ")
      answer = 'f'
      print(f'true or false: {falsified_fact}')
    elif " can " in cat_fact:
      falsified_fact = cat_fact.replace(" can ", " cannot ")
      answer = 'f'
      print(f'true or false: {falsified_fact}')
    elif " is " in cat_fact:
      falsified_fact = cat_fact.replace(" is ", " is not ")
      answer = 'f'
      print(f'true or false: {falsified_fact}')
    elif "n't " in cat_fact:
      falsified_fact = cat_fact.replace("n't ", " ")
      answer = 'f'
      print(f'true or false: {falsified_fact}')
    elif " are " in cat_fact:
      falsified_fact = cat_fact.replace(" are ", " aren't ")
      answer = 'f'
      print(f'true or false: {falsified_fact}')
    else:
      answer = 't'
      print(f'true or false: {cat_fact}')
    if input('type t/f: ') == answer:
      score = score + 1
      print('correct')
    else:
      print('incorrect')
        
    
    
  if score >3:
    print(f'you won with a score of {score}/5! here is a random inspirational quote for you:')
    print(insp_quote)
  else:
    print(f'try again to get 4/{number_of_qs} of the questions correct for an inspirational quote!')


main()