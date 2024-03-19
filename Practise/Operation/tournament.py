win = int(input("Enter number of wins = "))
loss = int(input("Enter number of loss = "))
tie = int(input("Enter nuber of tied matches ="))

score = 4*win + 2*tie + 0*loss

print(f"Total score of a team is {score}")
print("Total number of win points = ",4*win)
print("Total number of tie points = ",2*tie)