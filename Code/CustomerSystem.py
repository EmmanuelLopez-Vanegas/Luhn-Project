# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import csv
import os
import time

def printMenu():
    """print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')"""
    enterCustomerInfo()
    return 


def enterCustomerInfo():
    print('Welcome to our system')
    print('We will be asking for your personal details and save them into a csv file')
    time.sleep(3)
    while True:
        os.system('cls')
        while True:
            first_name = input('First Name: ')
            if first_name.isalpha() and first_name != '':
                break
            else:
                print('Please enter a valid first name')
        while True:
            last_name = input('Last Name: ')
            if last_name.isalpha() and last_name != '':
                break
            else:
                print('Please enter a valid last name')
        while True:
            city = input('City: ')
            if city.isalpha() and city != '':
                break
            else:
                print('Please enter a valid City')
        while True:
            postal_code = input('Postal Code: ').upper()
            if len(postal_code) == 3 and validatePostalCode(postal_code) == True:
                break
            else:
                print('Invalid postal code. Please enter 3 character postal code.')
                time.sleep(1)
        os.system('cls')
        print(f'Name: {first_name} {last_name}')
        print(f'City: {city}')
        print(f'Postal Code: {postal_code}')
        check = input('Confirmation (yes/no) ')
        if check == 'yes' or 'y':
            break
        elif check == 'no' 'n':
            time.sleep(0.0001)
    while True:
        card_number = input('Card Number: ')
        while len(card_number) > 16 or len(card_number) < 16:
            print('Input a valid card number')
            card_number = input('Card Number: ')
        valid = validateCreditCard(card_number)
        if valid == True:
            credentials = generateCustomerDataFile(first_name, last_name, city, postal_code, card_number)
            if credentials == True:
                print('Customer data file exists already')
                break
            else:
                print('Information has been updated')
                break
        else:
            print('Input a valid card number')
            time.sleep(1)
    return
            

def validatePostalCode(postal_code):
    code = postal_code
    with open('postal_codes.csv', 'r', newline = '', encoding = 'ISO-8859-1') as file:
        read = csv.reader(file, delimiter = '|')
        for row in read:
            if row[0] == code:
                print('Valid Postal Code')
                time.sleep(0.5)
                return True
        else:
            return False
        

def validateCreditCard(card_number):
    card = card_number
    reversed_digits = card[::-1]
    total_sum = 0
    for i, digit in enumerate(reversed_digits):
        digit = int(digit)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:  
                digit -= 9     
        total_sum += digit 
    if  total_sum % 10 == 0:
        return True
    else:
        return False
       

def generateCustomerDataFile(first_name, last_name, city, postal_code, card_number):
    with open('solutions.csv', 'r', newline = '', encoding = 'UTF-8') as file:
        read = csv.reader(file, delimiter = '|')
        for row in read:
            if first_name == row[0]:
                return True
        else:
            with open('solutions.csv', 'r', newline = '', encoding = 'UTF-8') as file:
                read = csv.reader(file, delimiter = '|')
            with open('solutions.csv', 'a', newline = '', encoding = 'UTF-8') as file:
                write = csv.writer(file, delimiter = '|')
                write.writerow([ first_name, last_name, city, postal_code, card_number]) 
            return False

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################
####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

printMenu()
while True:
    userInput = input("Would you like to add any more users? (yes/no) ")
    if userInput == "yes" or userInput == 'y':
        printMenu()
    elif userInput == 'no' or userInput == 'n':
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")        
time.sleep(1)   
os.system('cls') 
print("Program Terminated")
