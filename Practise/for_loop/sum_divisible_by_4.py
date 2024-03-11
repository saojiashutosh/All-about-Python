# Write a program to calculate the sum of all the numbers divisible by 4
# from 20 to 50.

sum=0
for i in range(20,51):
    if(i%4==0):
        sum+=i
        
print(sum)