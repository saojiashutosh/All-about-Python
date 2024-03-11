# Calculate how many numbers are divisible by 7 from 1 to 100.

i=1
count=0
while(i<=100):
    if(i%7==0):
        count+=1
    i+=1
print(count)    