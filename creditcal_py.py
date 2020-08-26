import math


def cal_principal():
    print('Enter the annuity payment:')
    ann_pay = float(input())
    print('Enter the count of periods:')
    n = int(input())
    print('Enter the credit interest:')
    rate = float(input())
    i = rate / (12 * 100)
    ann_rate = (i * pow(1 + i, n)) / (pow(1 + i, n) - 1)
    cred_pr = math.floor(ann_pay / ann_rate)
    print(f'Your credit principal = {cred_pr}!')
    overpay = round(ann_pay * n - cred_pr)
    print(f'Overpayment = {overpay}')


def cal_different():
    print('Enter the credit principal:')
    cred_pr = int(input())
    print('Enter the number of periods:')
    n = int(input())
    print('Enter the credit interest:')
    rate = float(input())
    i = rate / (12 * 100)
    diff_tot = 0
    for m in range(1, n+1):
        diff = math.ceil(cred_pr / n + i * (cred_pr - cred_pr*(m-1) / n))
        print(f'Month {m}: paid out {diff}')
        diff_tot += diff
    overpay = diff_tot - cred_pr
    print(f'\nOverpayment = {overpay}')


def cal_emi():
    print('Enter the credit principal:')
    cred_pr = int(input())
    print('Enter the number of periods:')
    n = int(input())
    print('Enter the credit interest:')
    rate = float(input())
    i = rate / (12 * 100)
    ann_rate = (i * pow(1+i, n)) / (pow(1+i, n) - 1)
    ann_pay = math.ceil(cred_pr * ann_rate)
    print(f'Your annuity payment = {ann_pay}!')
    overpay = ann_pay * n - cred_pr
    print(f'Overpayment = {overpay}')


def cal_tenure():
    print('Enter the credit principal:')
    cred_pr = int(input())
    print('Enter the monthly payment:')
    ann_pay = int(input())
    print('Enter the credit interest:')
    rate = float(input())
    i = rate / (12 * 100)
    lgbase = ann_pay / (ann_pay - i * cred_pr)
    tenure = math.ceil(math.log(lgbase, 1+i))
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
    print(prt_msg)
    cal_typ = input().strip()

    if cal_typ == 'n':
        cal_tenure()
    elif cal_typ == 'a':
        cal_emi()
    elif cal_typ == 'p':
        cal_principal()
    elif cal_typ == 'd':
        cal_different()
    else:
        print(f'Error!! type "{cal_typ}" does not exist')

# Main Body
prt_msg = '''What do you want to calculate?
type "n" for the number of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal:
type "d" for differentiated payment:'''
main()
