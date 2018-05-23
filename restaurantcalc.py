# -----------------------------------------------------------------------------
# Name:  Resturant Calculator
# Purpose:  This is a calculator that calculates sales tax + tip
#
#
# Author:   Randy Hoang
# -----------------------------------------------------------------------------
"""
This program is a sales and tip calculator for resturants

This program will ask the user to enter the price of four menu items and then
asks you for the tip % you want to pay and then calcuates the subtotal, sales
tax, tip ammount and the total.  We assume that the normal tax rate is 7.25%

The tip is the product of the % input amount and the subtotal (meaning not
including tax)
"""

TAX = .075 # This is the sales tax of 7.5

def main():
    item_one = float(input('Please enter the price of the first menu item: '))
    item_two = float(input('Please enter the price of the second menu item: '))
    item_three = float(input('Please enter the price of the third menu item: '))
    item_four = float(input('Please enter the price of the fourth menu item: '))
    input_tip = float(input('Enter the percent tip in decimal form:  '))
    subtotal = item_one + item_two + item_three + item_four

    tip_amount = (subtotal * input_tip)
    tax_amount = TAX * subtotal
    total_amount = tip_amount + tax_amount + subtotal

    subtotal_sign = f'${subtotal:.2f}' # Adding the $ sign and decimal places
    tip_sign = f'${tip_amount:.2f}'
    tax_sign = f'${tax_amount:.2f}'
    total_sign = f'${total_amount:.2f}'

    subtotal_align = f'Subtotal Amount:{subtotal_sign:>12}' # Aligned numbers
    tip_align = f'Tip Amount:{tip_sign:>16}'
    tax_align = f'Tax Amount:{tax_sign:>16}'
    total_align = f'Total Amount to pay:{total_sign:>8}'

    print(subtotal_align)
    print(tip_align)
    print(tax_align)
    print(total_align)




if __name__ == '__main__':
    main()
