import math
import sys
import argparse

parser = argparse.ArgumentParser(description='Loan calculator')
parser.add_argument('--type', type=str, help='Type of Payment')
parser.add_argument('--principal', type=float, help='The Principal amount')
parser.add_argument('--periods', type=int, help='No. of months needed to repay the loan')
parser.add_argument('--interest', type=float, help='Interest on Loan')
parser.add_argument('--payment', type=float, help='Monthly Payment')
args = parser.parse_args()


def calculate_annuity_payment():
    nominal_rate = args.interest / (12 * 100)
    monthly_payment = math.ceil(args.principal / ((math.pow(1 + nominal_rate, args.periods) - 1) / (
            nominal_rate * (math.pow(1 + nominal_rate, args.periods)))))
    print(f"Your annuity payment = {monthly_payment}!")
    print(f"Overpayment = {monthly_payment * args.periods - args.principal}")


def calculate_annuity_principal():
    nominal_rate = args.interest / (12 * 100)
    principal = (args.payment * (math.pow(1 + nominal_rate, args.periods) - 1)) / (
            nominal_rate * (math.pow(1 + nominal_rate, args.periods)))
    print(f"Your loan principal = {int(principal)}!")
    print(f'Overpayment = {int((args.payment * args.periods) - int(principal))}')


def calculate_annuity_period():
    nominal_rate = args.interest / (12 * 100)
    n = math.ceil(math.log((args.payment / (args.payment - (nominal_rate * args.principal))), 1 + nominal_rate))
    if n % 12 == 0:
        print(
            f"It will take {int(n / 12)} years to repay this loan!" if n / 12 > 1 else f"It will take {int(n / 12)} months to repay this loan!")
    else:
        print(f"It will take {n // 12} years and {n - (n // 12)} months to repay this loan!")
    print(f"Overpayment = {int((args.payment * n) - args.principal)}")


def calculate_diff():
    nominal_rate = args.interest / (12 * 100)
    principal = 0
    for month in range(1, (args.periods + 1)):
        expression = (args.principal / args.periods) + nominal_rate * (
                args.principal - ((args.principal * (month - 1)) / args.periods))
        print(f"Month {month}: payment is {math.ceil(expression)}")
        principal += math.ceil(expression)
    print(f"Overpayment = {math.ceil(principal - args.principal)}")


if (len(sys.argv) < 5) or (args.type != 'annuity' and args.type != 'diff'):
    print('Incorrect parameters')
elif args.type == 'annuity':
    if args.periods is None:
        calculate_annuity_period()
    elif (args.principal is None) and (args.interest is not None):
        calculate_annuity_principal()
    elif (args.payment is None) and (args.principal is not None):
        calculate_annuity_payment()
elif args.type == 'diff' and (args.interest is not None):
    calculate_diff()
else:
    print("Incorrect parameter")
