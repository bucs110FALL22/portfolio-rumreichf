print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15)
  #this last one is technically wrong because it rounds down, and the real value of the expression would go on infinitely.

rate = float(input("What is the current exchange rate of Euros to USD?"))
amount = float(input("How much currency would you like to exchange?"))

total = rate * amount
result = total - 3

print(result)