# Description - A program designed for One Stop Insurance Company to Calculate New insurance Policy information for its Customers.
# Author - Christian Rose
# Date - July 16th 2024 - July 22nd 2024. 

# Define Required Libraries:
import datetime
import time
import sys

# Function to read constants from file:
def read_constants():
    try:
        with open(r"Const.dat", "r") as f: # The file path was giving me some issues, would only run as C:\Users\chris\OneDrive\Desktop\PythonQAP\Const.dat, I have changed to Const.dat in hopes it works on your end!.
            constants = f.readlines()
        return constants
    except FileNotFoundError:
        print("Const.dat file not found. Please ensure the file exists in the specified location.")
        return None

# Define program constants:
constants = read_constants()
NEXT_POLICY_NUMBER = int(constants[0].strip())
BASIC_PREMIUM = float(constants[1].strip())
DISCOUNT_RATE = float(constants[2].strip())
COST_EXTRA_LIABILITY = float(constants[3].strip())
COST_GLASS_COVERAGE = float(constants[4].strip())
COST_LOANER_CAR = float(constants[5].strip())
HST_RATE = float(constants[6].strip())
PROCESSING_FEE_MONTHLY = float(constants[7].strip())

VALID_PROVINCES = ['ON', 'QC', 'BC', 'AB', 'MB', 'SK', 'NS', 'NB', 'NL', 'PE', 'NT', 'NU', 'YT']


# Define Program Functions:

# Function to format values:
def format_values(value):
    return str(value).title()

# Function to get current date:
def get_current_date():
    return datetime.date.today()

# Function to validate province input:
def validate_province(province):
    return province.upper() in VALID_PROVINCES

# Function to validate 'Y'/'N' inputs:
def validate_yn_input(input_str):
    return input_str.upper() in ['Y', 'N']

# Function to save progress with a blinking message:
def save_progress():
    for _ in range(5):  
        print("Saving policy data...   ", end="\r")
        time.sleep(0.3)
        print("                      ", end="\r")
        time.sleep(0.3)
    print("Policy data saved.")

# Function to write processed data to a file for future use:
def write_to_file(customers):
    filename = 'Claim Records.dat'
    with open(filename, 'a') as file:
        for customer in customers:
            file.write(f"Customer: {customer['First Name']} {customer['Last Name']}\n")
            file.write(f"Address: {customer['Address']}, {customer['City']}, {customer['Province']}, {customer['Postal Code']}\n")
            file.write(f"Phone Number: {customer['Phone Number']}\n")
            file.write(f"Number of Cars: {customer['Number of Cars to be Insured']}\n")
            file.write(f"Extra Liability Coverage: {'Yes' if customer['Extra Liability'] else 'No'}\n")
            file.write(f"Glass Coverage: {'Yes' if customer['Glass Coverage'] else 'No'}\n")
            file.write(f"Loaner Car Coverage: {'Yes' if customer['Loaner Car'] else 'No'}\n")
            file.write(f"Payment Method: {customer['Payment Method']}\n")
            file.write(f"Total Insurance Premium (Pretax): ${customer['Total Insurance Premium']:.2f}\n")
            file.write("Claims:\n")
            for claim in customer['Claims']:
                claim_number, claim_date, claim_amount = claim
                file.write(f"    Claim Number: {claim_number}, Claim Date: {claim_date}, Amount: ${claim_amount:.2f}\n")
            file.write("============================================================\n")
    print(f"Processed data has been saved to '{filename}'.")

# Function to calculate receipt totals:
def calculate_receipt_totals(customer):
    # Calculation for total additional coverage costs:
    total_additional_costs = 0
    if customer['Extra Liability']:
        total_additional_costs += customer['Number of Cars to be Insured'] * COST_EXTRA_LIABILITY
    if customer['Glass Coverage']:
        total_additional_costs += customer['Number of Cars to be Insured'] * COST_GLASS_COVERAGE
    if customer['Loaner Car']:
        total_additional_costs += customer['Number of Cars to be Insured'] * COST_LOANER_CAR

    # Calculation for total insurance premium including the additional coverages:
    total_insurance_premium = customer['Total Insurance Premium'] + total_additional_costs

    # Calculation for subtotal:
    subtotal = total_insurance_premium

    # Calculation for HST:
    taxes = subtotal * HST_RATE

    # Calculation for total amount:
    total_amount = subtotal + taxes

    return {
        'Subtotal': subtotal,
        'Taxes': taxes,
        'Total Amount': total_amount
    }

# Calculation to total insurance premium based on number of cars:
def calculate_total_insurance_premium(num_cars):
    total_premium = BASIC_PREMIUM + (num_cars - 1) * BASIC_PREMIUM * (1 - DISCOUNT_RATE)
    return total_premium

# Calculation to total cost including HST:
def calculate_total_cost(total_insurance_premium):
    total_cost = total_insurance_premium * (1 + HST_RATE)
    return total_cost

# Calculation for monthly payment:
def calculate_monthly_payment(total_cost, down_payment=None):
    if down_payment:
        remaining_balance = total_cost - down_payment
    else:
        remaining_balance = total_cost
    
    monthly_payment = (remaining_balance + PROCESSING_FEE_MONTHLY) / 8
    return monthly_payment

# Function to print receipt for a customer:
def print_receipt(customer):
    # Function to format phone number:
    formatted_phone = f"({customer['Phone Number'][:3]:<3})-{customer['Phone Number'][3:6]:<3}-{customer['Phone Number'][6:]:<4}"

    # Calculation of receipt totals:
    totals = calculate_receipt_totals(customer)

    # Printing of Receipt:
    print()
    print()
    print("                                      CUSTOMER COPY")
    print("                                 -------------------------")
    print()
    print("                                One Stop Insurance Company")
    print("                               --INSURANCE POLICY RECEIPT--")
    print()
    print("                                 -------------------------")
    print()
    print(f"                                                          Invoice Date:  {customer['Invoice Date']}")
    print(f"                                                          Policy Number: {NEXT_POLICY_NUMBER}")
    print(f"   {customer['First Name']} {customer['Last Name']}")
    print(f"   {customer['Address']}")
    print(f"   {customer['City']}, {customer['Province']: <2}, {customer['Postal Code']:<6}")
    print(f"   {formatted_phone}                                         Number of Vehicles to be Insured:      {customer['Number of Cars to be Insured']:<3}")
    print(f"                                                          Payment Option Selected:            {customer['Payment Method']:<16}")
    print(f"   Additional Coverage Options:                           Down Payment:                       {customer['Down Payment']}")
    print("                                                          ------------------------------------------")
    print(f"   Extra Liability Coverage:   {'Yes' if customer['Extra Liability'] else 'No': <3}                        Cost:                              ${customer['Number of Cars to be Insured'] * COST_EXTRA_LIABILITY if customer['Extra Liability'] else 0:.2f}")
    if customer['Glass Coverage']:
        print(f"   Glass Coverage:             {'Yes'}                        Cost:                              ${customer['Number of Cars to be Insured'] * COST_GLASS_COVERAGE:.2f}")
    else:
        print(f"   Glass Coverage:             {'No': <3}                        Cost:                              ${0:.2f}")
    if customer['Loaner Car']:
        print(f"   Loaner Car Coverage:        {'Yes'}                        Cost:                              ${customer['Number of Cars to be Insured'] * COST_LOANER_CAR:.2f}")
    else:
        print(f"   Loaner Car Coverage:        {'No': <3}                        Cost:                              ${0:.2f}")
    print("                                                          ------------------------------------------")
    print(f"                                                          Total Insurance Premium (Pretax):  ${totals['Subtotal']:.2f}")
    print(f"                                                          Taxes (HST {HST_RATE * 100}%):                 ${totals['Taxes']:.2f}")
    print("                                                          ------------------------------------------")
    print(f"                                                          Total Amount (including taxes):    ${totals['Total Amount']:.2f}")
    print()
    print("                               --------------------------")
    print()
    print(f"                             Your Monthly Payment Rate is: ")
    print(f"                                        ${customer['Monthly Payment']:.2f}")
    print(f"                               FIRST PAYMENT DATE IS ON:")
    print(f"                                      {customer['First Payment Date']}")
    print()

    # Printing previous claims if any:
    if len(customer['Claims']) == 0:
        print("Customer has no previous claims.")
    else:
        print("\nPrevious Claims:")
        print("                      Claim #         Claim Date       Amount")
        print("                      ----------------------------------------")
        for claim in customer['Claims']:
            claim_number, claim_date, claim_amount = claim
            print(f"                        {claim_number:<10}    {claim_date}    ${claim_amount:,.2f}")

# Main Program Starts Here:
def main():
    global NEXT_POLICY_NUMBER
    print("Welcome to One Stop Insurance Company")
    customers = []

    while True:
        try:
            # Inputs of customer information:
            first_name = input("Enter customer's first name: ").title()
            last_name = input("Enter customer's last name: ").title()
            address = input("Enter customer's address: ")
            city = input("Enter customer's city: ").title()
            province = input("Enter customer's province: ").upper()
            while not validate_province(province):
                print("Invalid province. Please enter a valid province from the list provided: (ON, QC, BC, AB, MB, SK, NS, NB, NL, PE, NT, NU, YT): ")
                province = input("Enter customer's province: ").upper()
            
            postal_code = input("Enter customer's postal code: ")
            phone_number = input("Enter customer's phone number: ")

            num_cars = int(input("Enter number of cars being insured: "))

            extra_liability = input("Extra liability coverage (Y/N): ").upper()
            while not validate_yn_input(extra_liability):
                print("Invalid input! Please enter Y or N.")
                extra_liability = input("Extra liability coverage (Y/N): ").upper()
            extra_liability = extra_liability == 'Y'

            glass_coverage = input("Glass coverage (Y/N): ").upper()
            while not validate_yn_input(glass_coverage):
                print("Invalid input! Please enter Y or N.")
                glass_coverage = input("Glass coverage (Y/N): ").upper()
            glass_coverage = glass_coverage == 'Y'

            loaner_car = input("Loaner car coverage (Y/N): ").upper()
            while not validate_yn_input(loaner_car):
                print("Invalid input! Please enter Y or N.")
                loaner_car = input("Loaner car coverage (Y/N): ").upper()
            loaner_car = loaner_car == 'Y'

            payment_method = input("Payment method (Full/Monthly/Down Pay): ").title()
            if payment_method == "Down Pay":
                down_payment = float(input("Enter down payment amount: "))
            else:
                down_payment = None

            # Claims information:
            claims = []
            while True:
                claim_number = input("Enter claim number (or 'done' to finish): ")
                if claim_number.lower() == 'done':
                    break
                claim_date = input("Enter claim date: ")
                claim_amount = float(input("Enter claim amount: "))
                claims.append((claim_number, claim_date, claim_amount))

            # Calculation for insurance details:
            total_insurance_premium = calculate_total_insurance_premium(num_cars)

            # Calculation for total extra coverage costs:
            total_extra_costs = 0
            if extra_liability:
                total_extra_costs += num_cars * COST_EXTRA_LIABILITY
            if glass_coverage:
                total_extra_costs += num_cars * COST_GLASS_COVERAGE
            if loaner_car:
                total_extra_costs += num_cars * COST_LOANER_CAR

            # Calculation for total cost including HST:
            total_cost = calculate_total_cost(total_insurance_premium + total_extra_costs)

            # Calculation of monthly payments:
            monthly_payment = calculate_monthly_payment(total_cost, down_payment)

            # Invoice and payment dates:
            invoice_date = get_current_date()
            first_payment_date = datetime.date(invoice_date.year, invoice_date.month + 1, 1)

            # Storing customer data:
            customer_data = {
                'First Name': format_values(first_name),
                'Last Name': format_values(last_name),
                'Address': address,
                'City': format_values(city),
                'Province': province,
                'Postal Code': postal_code,
                'Phone Number': phone_number,
                'Number of Cars to be Insured': num_cars,
                'Extra Liability': extra_liability,
                'Glass Coverage': glass_coverage,
                'Loaner Car': loaner_car,
                'Payment Method': payment_method,
                'Down Payment': down_payment,
                'Claims': claims,
                'Total Insurance Premium': total_insurance_premium,
                'Total Cost': total_cost,
                'Monthly Payment': monthly_payment,
                'Invoice Date': invoice_date,
                'First Payment Date': first_payment_date
            }

            customers.append(customer_data)

            # This will increment next policy number by desired amount:
            NEXT_POLICY_NUMBER += 1

            # Saves progress with the blinking message:
            save_progress()

            # Writes information to file:
            write_to_file([customer_data])

            # Print receipt for the current customer:
            print_receipt(customer_data)

            # This is used to ask if you want to enter another customer:
            print()
            another_customer = input("Do you want to enter another customer? (Y/N): ").upper()
            if another_customer != 'Y':
                break

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Acknowledgement that customer information has been saved successfully:
    print("\nCustomer information has been successfully recorded.")

if __name__ == "__main__":
    main()

# End