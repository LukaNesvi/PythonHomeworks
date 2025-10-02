balance = 1000
withdraw = int(input("Input the amount you want to withdraw: "))

if withdraw <= 1000:
    print ("Withdrawal successful")
    print (f"Your new balance is - {balance - withdraw}")
elif withdraw > 1000:
    print ("Insuficient funds")
else:
    print ("Error")
