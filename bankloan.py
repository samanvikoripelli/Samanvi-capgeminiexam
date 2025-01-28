def check_bank_loan_eligibility(salary,age,credit_score):
    if salary < 25000:
        return "loan rejected"
    if age < 21 or age > 60:
        return "loan rejected"
    if credit_score < 600:
        return "loan rejected"
    return "loan approved"
def main():
    salary = float(input("enter your salary"))
    age = int(input("enter your age"))
    credit_score = int(input("enter your credit_score"))
    result = check_bank_loan_eligibility(salary,age,credit_score)
    print(result)
main()