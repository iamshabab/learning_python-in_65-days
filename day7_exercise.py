# 1. Use a for loop to print all even numbers from 1 to 20

for number in range(1,20):
    if number % 2==0:
        print(number)

# 2. Use a for loop to calculate the sum of all numbers from 1 to 100
#    Print the result
print("\n sum \n ")
sum=0
for a in range(100):
    print(f"{sum}+{a}={a+sum}")
    sum=a+sum
print(sum)


# 3. Given this list of scores:
scores = [55, 82, 91, 47, 73, 88, 60, 95]
#    Use a loop to print:
#    - Each score
#    - Whether each score is "Pass" (>=60) or "Fail" (<60)
#    - Count how many passed and how many failed
tpass=0
tfail=0
for score in scores:
    print(score)
    if score>=60:
        print("pass")
        tpass=tpass+1
    else:
        print("fail")
        tfail=tfail+1
print(f"number of pass subject is {tpass} and number of fail subject is {tfail}")


# 4. Use a while loop to simulate a countdown from 10 to 1
#    then print "Blast off!"
num=11
while num>0:
    num=num-1
    print(num)
print("blast off!")
# 5. Use a nested loop to print this pattern:
# *
# * *
# * * *
# * * * *
# * * * * *
row=5
for a in range(1,row+1): 
    for b in range(a): 
        print("*",end="")
    print()

    
# 6. ML Challenge — simulate 8 training epochs:
#    Start with loss = 1.0
#    Each epoch, reduce loss by 0.12
#    Print the epoch number and current loss (rounded to 2 decimals)
#    If loss drops below 0.20, print "Converged!" and stop
t_epochs=8
loss=1.0
epoch=0.12

for a in range(1,t_epochs+1):
    loss-=0.12
    print(f"epoch number :{a} and current loss :{loss : .2} ")
    if loss<0.20:
        print("converged!")
        break

    

