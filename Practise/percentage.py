maths = int(input("enter maths marks = "))
eng = int(input("enter english marks = "))
sci = int(input("enter science marks = "))
hist = int(input("enter History marks = "))
civics = int(input("enter Civics marks = "))

per = ((maths+eng+sci+hist+civics)/250)*100

print(f"Percentage is {per}")