bill=int(input("Enter your bill amount: "))

def sum_of_digits(number):
    sum_digits=0
    while number>0:
        digit=number%10
        sum_digits+=digit
        number//=10
    return sum_digits
if bill>10000:
    discount_percentage= sum_of_digits(bill)
else:
    discount_percentage=sum_of_digits(bill)/2

discount_amt=(discount_percentage/100) *bill
final_bill=bill-discount_amt
print(f"Bill before discount: ₹{bill}")
print(f"discount percentage: {discount_percentage}%")
print(f"discount amount: ₹{discount_amt}")
print(f"Total amount to be paid: ₹{final_bill}")
print("Program by Diya Bhutani - 0221BCA041")