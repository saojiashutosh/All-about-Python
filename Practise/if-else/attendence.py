"""A student will not be allowed to sit in exam if his/her attendance is
less than 75%.
Take following input from user
QUESTIONS 23-26
IF - ELSE
info@codeanddebug.in Code and Debug codeanddebug.in
Number of classes held
Number of classes attended.
1. Print percentage of class attended
2. Print Is student is allowed to sit in exam or not."""

x = int(input("Enter number of classes held = "))
y = int(input("Enter number of classes attended = "))

pca = (y/x)*100 

print(f"Percentage of class attended = {pca}")

if(pca < 75):
    print("Student will not be allowed to sit in exam")
else  :
    print("Student will be allowed to sit in exam")