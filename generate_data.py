import pandas as pd
import numpy as np

n_rows = 100

# ---------------------------------
# Customer Info + Financial Profile
# ---------------------------------
customer_id = [f"CUST{1000+i}" for i in range(n_rows)]
age = np.random.randint(18, 65, size=n_rows)

emp_titles = ['Engineer','Teacher','Manager','Nurse','Sales','Consultant','Student','Technician','Clerk']
emp_title = np.random.choice(emp_titles, size=n_rows)
emp_length = np.random.choice(['< 1 year','1 year','2 years','3 years','4 years','5 years','6 years','7 years','8 years','9 years','10+ years'], size=n_rows)

home_ownership = np.random.choice(['RENT','OWN','MORTGAGE','OTHER'], size=n_rows)
annual_inc = np.random.randint(20000, 150000, size=n_rows)
verification_status = np.random.choice(['Verified','Source Verified','Not Verified'], size=n_rows)

# Stock info
has_stock = [np.random.choice([0,1], p=[0.7,0.3]) if inc<50000 else np.random.choice([0,1], p=[0.4,0.6]) for inc in annual_inc]
stock_value = [0 if hs==0 else int(inc*np.random.uniform(0.5,3.0)) for hs, inc in zip(has_stock, annual_inc)]

# ---------------------------------
# Loan info
# ---------------------------------
loan_amnt = np.random.randint(1000, 40000, size=n_rows)
funded_amnt = loan_amnt - np.random.randint(0, 500, size=n_rows)
funded_amnt_inv = funded_amnt - np.random.randint(0, 200, size=n_rows)

term = np.random.choice(['36 months','60 months'], size=n_rows)
int_rate = np.round(np.random.uniform(5.0, 25.0, size=n_rows), 2)
installment = np.round(loan_amnt * int_rate/1200 + loan_amnt/np.where(term=='36 months',36,60),2)

grade = np.random.choice(list('ABCDEFG'), size=n_rows)
sub_grade = [g+str(np.random.randint(1,6)) for g in grade]

banks = ['Bangkok Bank', 'Kasikorn Bank', 'SCB', 'Krungsri', 'TMB']
bank = np.random.choice(banks, size=n_rows)

purpose_list = ['debt_consolidation','credit_card','home_improvement','major_purchase','small_business','car','medical','wedding','vacation','other']
loan_purpose = np.random.choice(purpose_list, size=n_rows)
title = [p.replace('_',' ').title() for p in loan_purpose]

zip_code = [f"{np.random.randint(10000,99999)}" for _ in range(n_rows)]
addr_state = np.random.choice(['CA','NY','TX','FL','IL','PA','OH','GA','NC','MI'], size=n_rows)

dti = np.round(np.random.uniform(0,40,size=n_rows),2)
delinq_2yrs = np.random.randint(0,5,size=n_rows)
earliest_cr_line = pd.to_datetime(np.random.choice(pd.date_range('1980-01-01','2015-01-01'), size=n_rows))
inq_last_6mths = np.random.randint(0,10,size=n_rows)

open_acc = np.random.randint(1,20,size=n_rows)
pub_rec = np.random.randint(0,5,size=n_rows)
revol_bal = np.random.randint(0,50000,size=n_rows)
revol_util = np.round(np.random.uniform(0,120,size=n_rows),2)
total_acc = np.random.randint(5,50,size=n_rows)

# Payment info
out_prncp = np.random.randint(0,loan_amnt+1,size=n_rows)
out_prncp_inv = out_prncp - np.random.randint(0,500,size=n_rows)
total_pymnt = loan_amnt - out_prncp + np.random.randint(0,5000,size=n_rows)
total_pymnt_inv = total_pymnt - np.random.randint(0,500,size=n_rows)
total_rec_prncp = loan_amnt - out_prncp
total_rec_int = total_pymnt - total_rec_prncp
total_rec_late_fee = np.random.randint(0,500,size=n_rows)
recoveries = np.random.randint(0,5000,size=n_rows)
collection_recovery_fee = np.random.randint(0,1000,size=n_rows)

last_pymnt_d = pd.to_datetime(np.random.choice(pd.date_range('2018-01-01','2025-01-01'), size=n_rows))
last_pymnt_amnt = np.round(total_pymnt/np.random.randint(1,5,size=n_rows),2)
next_pymnt_d = last_pymnt_d + pd.to_timedelta(np.random.randint(28,60,size=n_rows), unit='d')
last_credit_pull_d = pd.to_datetime(np.random.choice(pd.date_range('2019-01-01','2025-01-01'), size=n_rows))

# Credit Score (สมมติสัมพันธ์กับ Income, LoanAmount, Age)
credit_score = [min(850, max(300, int(annual_inc[i]/1000 - loan_amnt[i]/1000 + age[i]/2 + np.random.randint(-50,50)))) 
                for i in range(n_rows)]

# ---------------------------------
# Combine all into DataFrame
# ---------------------------------
df = pd.DataFrame({
    'CustomerID': customer_id,
    'Age': age,
    'EmpTitle': emp_title,
    'EmpLength': emp_length,
    'HomeOwnership': home_ownership,
    'AnnualInc': annual_inc,
    'VerificationStatus': verification_status,
    'HasStock': has_stock,
    'StockValue': stock_value,
    'LoanAmnt': loan_amnt,
    'FundedAmnt': funded_amnt,
    'FundedAmntInv': funded_amnt_inv,
    'Term': term,
    'IntRate': int_rate,
    'Installment': installment,
    'Grade': grade,
    'SubGrade': sub_grade,
    'Bank': bank,
    'Purpose': loan_purpose,
    'Title': title,
    'ZipCode': zip_code,
    'AddrState': addr_state,
    'DTI': dti,
    'Delinq_2yrs': delinq_2yrs,
    'EarliestCrLine': earliest_cr_line,
    'InqLast6Mths': inq_last_6mths,
    'OpenAcc': open_acc,
    'PubRec': pub_rec,
    'RevolBal': revol_bal,
    'RevolUtil': revol_util,
    'TotalAcc': total_acc,
    'OutPrncp': out_prncp,
    'OutPrncpInv': out_prncp_inv,
    'TotalPymnt': total_pymnt,
    'TotalPymntInv': total_pymnt_inv,
    'TotalRecPrncp': total_rec_prncp,
    'TotalRecInt': total_rec_int,
    'TotalRecLateFee': total_rec_late_fee,
    'Recoveries': recoveries,
    'CollectionRecoveryFee': collection_recovery_fee,
    'LastPymntD': last_pymnt_d,
    'LastPymntAmt': last_pymnt_amnt,
    'NextPymntD': next_pymnt_d,
    'LastCreditPullD': last_credit_pull_d,
    'CreditScore': credit_score
})

print(df.head())
excel_file = 'synthetic_financial_loans.xlsx'
df.to_excel(excel_file, index=False)
print(f"Saved Excel file: {excel_file}")

json_file = 'synthetic_financial_loans.json'
df.to_json(json_file, orient='records', date_format='iso')
print(f"Saved JSON file: {json_file}")