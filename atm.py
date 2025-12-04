import sys
if len(sys.argv) != 4:
    print("Usage: python atm.py <withdraw_amount> <balance> <PIN>")
    sys.exit()

withdraw = int(sys.argv[1])
balance = int(sys.argv[2])
pin = sys.argv[3]

correct_pin = "1234"

if pin != correct_pin:
    print("Transaction Declined: Incorrect PIN")
elif withdraw > balance:
    print("Transaction Declined: Insufficient Balance")
else:
    print("Transaction Approved")
