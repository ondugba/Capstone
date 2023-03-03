
print("Welcome to Perscholas Banking terminal!")
print("Please enter 1 to view transactions by zipcode, year and month.")
print("Please enter 2 to view transactions by transaction type and total value")
print("Please enter 3 to view transactions by transaction value total by branch and state")
print("Please enter 4 to view transactions by transaction value total by state")
print("Please enter 5 to view existing customer details")
print("Please enter 6 to modify existing customer details")
print("Please enter 7 to generate a customer's monthly bill")
print("Please enter 8 to view customer transactions in a given time period ")



while True: 
    selection= input("Please enter your selection based on the numeric values above: ")
    try: 
        selection= int(selection)
    except: 
        print("Please choose one of the numeric values above")
        continue

    if selection < 1: 
        print("Please enter a number that is greater than 0")
        continue
    break

if selection == 1:
    
    
    #use 22180, 2018, 5
    zipcode = input("Please enter your 5 digit zipcode: " )
    year = input("Please enter your 4 digit year: " )
    month = input("Please choose a month from 1 through 12: " )
    get_transactions_by_zipcode(zipcode, year, month)
    
    
elif selection == 2:
    
    
    transaction_type = input("Please choose transaction type from the following - Education, Entertainment\
  Healthcare, Grocery, Test, Gas, Bills: " )
    get_transaction_by_type(transaction_type)

    
elif selection == 3: 
    
    
    state_name = input("Please choose a state from the following list (NY, GA, PA, FL, IL, MI, MD, NJ, CA, OH, \
 NC, VA, MA, TX, WI, SC, MN, MS, KY, WA, IA, CT, IN, MT, AR, AL): " )
    transactions_by_state(state_name)
 
    
elif selection == 4:
    
    
    state = input("Please choose a state from the following list (NY, GA, PA, FL, IL, MI, MD, NJ, CA, OH,\
NC, VA, MA, TX, WI, SC, MN, MS, KY, WA, IA, CT, IN, MT, AR, AL): ")
    get_branch_transaction_info(state)
    
    
elif selection == 5:
    
    
    #Use 123459988
    customer_ssn = input("Please enter your social security number: ")
    get_customer_information(customer_ssn)
      
    
elif selection == 6: 
    
    
    #Use 123456100
    ssn = input("Please enter your social security number: ")
    field = input("Please enter in the field you would like to change (Credit_card_no, CUST_CITY, CUST_COUNTRY, \
 CUST_EMAIL, CUST_PHONE, CUST_STATE, CUST_ZIP, FIRST_NAME, LAST_NAME, MIDDLE_NAME, SSN): ")
    new_value = input("Please enter the changed information: ")    
    update_customer_info(ssn, field, new_value)
   
    
elif selection == 7:
    
    
    #Use  4210653349028689,  2  2018
    cc_number = input("Please enter your credit card number: ")
    year = input("Please enter the year you would like to view the bill for: ")
    month = input("Please enter the month you would like to view the bill for: ")
    get_customer_bill(cc_number, year, month)


elif selection == 8:
    

    #Use 123452490 2018-01-01 2018-12-31
    ssn = input("Please enter your social security number: ")
    start_date = input("Please enter your transaction start date as (YYYY-MM-DD): ")
    end_date = input("Please enter your transaction end date as (YYYY-MM-DD): ")
    get_customer_transactions(ssn, start_date, end_date)
    
    
else:
    print("Please make a valid selection")