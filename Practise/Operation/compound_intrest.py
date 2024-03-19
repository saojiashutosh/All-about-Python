P=int(input("enter initial principal balance = "))
r=int(input("enter intrest rate = "))
t=int(input("enter number of time period = "))

CI=P*((1+(r/100))**(t))

print(f"Compound Intrest for entered data is {CI}")