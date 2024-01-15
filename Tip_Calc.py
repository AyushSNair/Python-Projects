print("Welcome To the Tip calculator")
print("What was the Actual Bill?")
bill = float(input())
print("What percentage of tip would you like to give? 10, 12 or 15? ")
tip = float(input())
print("How many people are there to split th bill? ")
splt = float(input())

perc = bill * (tip*0.01)

total = perc + bill

ppl = total / splt

p=round(ppl)
print(f"Each person should pay: {p}")