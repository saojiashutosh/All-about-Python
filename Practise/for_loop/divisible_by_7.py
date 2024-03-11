# Calculate how many numbers are divisible by 7 from 1 to 100

count = 0
for i in range(1,101):
    if(i%7==0):
        count+=1
        
print(count)