# QAP-4-Files-CR

# One Stop Insurance Policy Management Program

## Overview
This program is designed for One Stop Insurance Company to manage and calculate new insurance policies for its customers. It allows users to input customer information, select insurance options, calculate premiums, generate receipts, and store policy details for future reference.

## Features
- **Customer Information Input**: Capture customer details including name, address, contact information, and number of cars to be insured.
- **Insurance Options**: Choose from additional coverage options such as extra liability, glass coverage, and loaner car.
- **Payment Methods**: Supports full payment, monthly payment, or down payment options with appropriate calculations.
- **Claims Management**: Ability to input multiple claims associated with each customer.
- **Receipt Generation**: Generates detailed receipts with policy information, costs breakdown (subtotal, taxes), and payment details.
- **Data Persistence**: Saves customer policy data to a file (`Claim Records.dat`) for record-keeping.
- **Error Handling**: Validates user inputs to ensure data integrity and provides feedback for incorrect entries.
- **File Handling**: Reads program constants from `Const.dat` file and writes processed data to `Claim Records.dat`.

## Dependencies
- Python 3.x
- Standard libraries: `datetime`, `time`, `sys`

## Setup
1. Clone the repository or download the source code.
2. Ensure Python 3.x is installed on your system.
3. Place `Const.dat` in the same directory as the program for constant values.

## Usage
1. Run the program (`PythonQAP4.py`) in your terminal or IDE.
2. Follow the prompts to enter customer information, coverage preferences, and payment details.
3. Input claims information as necessary.
4. View and print generated receipts for each customer.
5. Optionally, continue entering new customer information until finished.

## Files
- `PythonQAP4.py`: Main program file containing the insurance policy management logic.
- `Const.dat`: Contains constant values used in the program (e.g., NEXT_POLICY_NUMBER, BASIC_PREMIUM, etc.).
- `Claim Records.dat`: Output file where customer policy data is appended for record-keeping.

## Notes
- Ensure `Const.dat` is correctly formatted with necessary constants on each line.
- Review and modify validation functions (`validate_province`, `validate_yn_input`) if additional checks are required.
- Modify receipt formatting in `print_receipt()` function to match specific requirements or branding.

## Contributors
- Author: Christian Rose
