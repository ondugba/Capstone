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
- you will also need to download and install MySQL and Tableau

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

## Technical Challenges
- there are some issues with connecting to the sql database using pyspark.
- I was able to connect and load all my cleaned dataframes into the mysql database I was using but I did get a lot of warnings.



![](images/married_men.png)

Top branch by total transaction value for Healthcare

![](images/top_3_branch_healthcare.png)
![](images/top_branch_healthcare.png)

Top 3 months by total transactions

![](images/top3months.png)



