# Capstone Project for Perscholas Data Engineerig
This is the final project for the Perscholas Data Engineering bootcamp

## Overview
This project requires management of an ETL process, Data Analysis, and Data Visualization for:

-  Loan Application dataset 
-  Credit Card dataset

## Requirements
- there is a yml file which has the required libraries to install to duplicate this project but the core libraries are:
    : Python 
    : Pandas
    : Seaborn
    : Matplotlib
    : PySpark
- this yml file can be run to automatically create a dupicate environment 
- I've also included a requirements.txt file as well.
- you will also need to download and install MySQL and Tableau
- There is a console.py file that needs to be run from inside of the part1 notebook - can run at the end of section 2 or at the end of the notebook(but before stopping the spark session)

## Data Analysis and Visualization

Total transaction Amount by Transaction Type

![](images/transaction_types_amounts.png)

Top 8 states by number of customers 

![](images/top_8_states_by_customer.png)

Top 15 customers by total transactions

![](images/top15_customers_by_total_transaction_amounts.png)

Approval Rate for Self-Employeed individuals

![](images/self_employ1.png)
![](images/self_employ2.png)

Rejection percentage for married male applicants

![](images/married_men.png)

Top branch by total transaction value for Healthcare

![](images/top_3_branch_healthcare.png)
![](images/top_branch_healthcare.png)

Top 3 months by total transactions

![](images/top3months.png)

## Technical Challenges
- there are some issues with connecting to the sql database using pyspark.
- I was able to connect and load all my cleaned dataframes into the mysql database I was using but I did get a lot of warnings.



