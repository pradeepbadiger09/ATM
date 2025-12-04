import sys

if len(sys.argv) == 4:
    withdraw = int(sys.argv[1])
    balance = int(sys.argv[2])
    pin = sys.argv[3]
else:
    print("Arguments are default values.")
    withdraw = 0
    balance = 1000
    pin = 0000

correct_pin = "1234"

if pin != correct_pin:
    print("Transaction Declined: Incorrect PIN")
elif withdraw > balance:
    print("Transaction Declined: Insufficient Balance")
else:
    print("Transaction Approved")
