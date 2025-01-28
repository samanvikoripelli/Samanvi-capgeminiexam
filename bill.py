def bill_splitter():
    total_bill = float(input("enter the bill"))
    number_of_people = int(input("enter the number of people"))
    tip_percent = float(input("enter the tip_percent"))
    total_with_tip = total_bill + (total_bill * tip_percent / 100)
    amount_per_person = total_with_tip / number_of_people
    print(f"each person need to pay {amount_per_person:.2f}")
def main():
    bill_splitter()
main()