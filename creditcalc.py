import math
import sys
import argparse


def cal_principal():
    ann_pay = args.payment
    n = args.periods
    rate = args.interest
    i = rate / (12 * 100)
    ann_rate = (i * pow(1 + i, n)) / (pow(1 + i, n) - 1)
    cred_pr = math.floor(ann_pay / ann_rate)
    print(f'Your credit principal = {cred_pr}!')
    overpay = round(ann_pay * n - cred_pr)
    print(f'Overpayment = {overpay}')


def cal_different():
    cred_pr = args.principal
    n = args.periods
    rate = args.interest
    i = rate / (12 * 100)
    diff_tot = 0
    for m in range(1, n+1):
        diff = math.ceil(cred_pr / n + i * (cred_pr - cred_pr*(m-1) / n))
        print(f'Month {m}: paid out {diff}')
        diff_tot += diff
    overpay = diff_tot - cred_pr
    print(f'\nOverpayment = {overpay}')


def cal_emi():
    cred_pr = args.principal
    n = args.periods
    rate = args.interest
    i = rate / (12 * 100)
    ann_rate = (i * pow(1+i, n)) / (pow(1+i, n) - 1)
    ann_pay = math.ceil(cred_pr * ann_rate)
    print(f'Your annuity payment = {ann_pay}!')
    overpay = ann_pay * n - cred_pr
    print(f'Overpayment = {overpay}')


def cal_tenure():
    cred_pr = args.principal
    ann_pay = args.payment
    rate = args.interest
    i = rate / (12 * 100)
    lg_base = ann_pay / (ann_pay - i * cred_pr)
    tenure = math.ceil(math.log(lg_base, 1+i))
    yy = tenure // 12
    mm = tenure % 12
    if yy == 0:
        print(f'You need {mm} months to repay this credit!')
    elif mm == 0:
        print(f'You need {yy} years to repay this credit!')
    else:
        print(f'You need {yy} years {mm} months to repay this credit!')
    overpay = ann_pay * tenure - cred_pr
    print(f'Overpayment = {overpay}')

def main():
    if len(sys.argv) != 5:
        print('Incorrect parameters')
        return
    if args.type is None or args.interest is None:
        print('Incorrect parameters')
        return
    pr = args.principal
    er = args.periods
    it = args.interest
    ay = args.payment
    if (pr is not None and pr < 0) or (er is not None and er < 0) or \
            (it is not None and it < 0) or (ay is not None and ay < 0):
        print('Incorrect parameters')
        return
    if args.type == 'annuity':
        if args.periods is None:
            cal_tenure()
        if args.payment is None:
            cal_emi()
        if args.principal is None:
            cal_principal()
    elif args.type == 'diff' and args.payment is None:
        cal_different()
    else:
        print('Incorrect parameters')

# Main Body
prt_msg = '''type "annuity" for the annuity monthly payment,
type "diff" for differentiated payment'''

parser = argparse.ArgumentParser(description="Credit Calculator", epilog="Enjoy the Program!")
parser.add_argument("--type", type=str, help=prt_msg)
parser.add_argument("--principal", type=int, help="Credit Principal Amount")
parser.add_argument("--periods", type=int, help="Number of periods in Months")
parser.add_argument("--interest", type=float, help="Annual Interest Rate %%")
parser.add_argument("--payment", type=float, help="Annuity Payment Amount")
args = parser.parse_args()
main()
