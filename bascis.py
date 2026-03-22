
# bill Caclulator 
print("Welcome to Calculator")
#converting input data type into float as default data type is str
totalBill = float(input(" What was the todal Bill - "))
tip = float(input("How much tin would you like to pay - "))
split = float(input ("In how many ppl you would like to split the bill - "))
share = (totalBill + tip)/split

print(f"Each person's share = {share:.2f}")  # Formats to 2 decimal places
