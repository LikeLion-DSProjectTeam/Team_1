# Team_1

Mentor: John Oh, Arden Kim  
Member: Beomseong Kim, Ikjoo Oh

## Table of Contents
1. [Overview](#overview)
2. [Problem Statement](#Problem-Statement)
3. [Data Description](#Data-Description)
4. [Data Preprocessing](#Data-Preprocessing)
5. [Exploratory Data Analysis](#Exploratory-Data-Analysis)
6. [Feature Engineering](#Feature-Engineering)
7. [Model Selection](#Model-Selection)   
8. [Model Training and Evaluation](#Model-Training-and-Evaluation)
9. [Hyperparameter Tuning](#Hyperparameter-Tuning)
10. [Conclusion](#Conclusion)

## Overview

This is a Data Science project by Beomseong Kim and Ikjoo Oh under the guidance of mentors John Oh and Arden Kim. 

Used Kaggle Dataset: [Bank Chustomer Churn](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data)

## Problem Statement
The objective of this project is to utilize reinforcement learning to develop a predictive model that identifies optimal strategies for retaining customers who are at risk of leaving the bank. By leveraging historical data and understanding the factors influencing customer churn, the bank can implement targeted retention programs and enhance overall customer satisfaction.

- Expected Outcomes
  - We will develop a reinforcement learning model that learns optimal actions to take in order to reduce customer churn rates effectively.

## Data Description
1. CreditScore(`int`) — Customer credit score
2. Age(`int`) — Customer age
3. Tenure(`int`) — Duration of the customer relationship with the bank
4. NumOfProducts(`int`) — number of products that a customer has purchased through the bank.
5. HasCrCard(`int`) — denotes whether or not a customer has a credit card
6. IsActiveMember(`int`) — Indicator of active membership status
7. Complain(`int`) — Indicator of customer complaints
8. Satisfaction Score(`int`) — Score provided by the customer for their complaint resolution
9. Points Earned(`int`) — Points earned by the customer through credit card usage
10. Balance(`float`) — Account balance
11. EstimatedSalary(`float`) — Customer Salary
12. Geography(`object`) — Customer location
13. Card Type(`object`) — Type of card hold by the customer.
14. Gender(`object`) — Gender of the customer
15. **Exited**(`int`) — **Target feature** that indicate whether the customer left the bank

- Target Variable
  - Exited: `1` = the customer left, `0` = the customer stayed

- Unneeded Variables
1. RowNumber - indicates the row number and this feature doesn't affect analysis
2. CustomerId - A random identifier for customers, which also doesn't influence customer churn
3. Surname - The customer's surname has no impact on their decision to leave the bank

## Data Preprocessing
- There were no missing values across all features.
- We dropped irrelevant features `RowNumber`, `CustomerId`, `Surname`
- We also dropped the `Complain` feature due to its perfect correlation of 1 with the target variable Exited. Because this redundancy could potentially lead to overfitting
- We converted categorical features like `Geography`, `Gender`, `Card Type`, `NumOfProducts`, and `Satisfaction Score` into one-hot encoded variables to create binary columns representing each category. And we `drop_first = True` because it helps to avoid multicollinearity in our model by dropping one of the binary columns.
- We created the `Zero_Balance` feature by checking if a customer's balance is equal to zero based on the `Balance` feature. Because a significant number of customers had a balance of zero in `Balance` feature. And this binary variable would be crucial in understanding customer behavior.
- Standard Scaling: Applied to `CreditScore` and `Age` to normalize these features around a mean of 0 and standard deviation of 1.
- Min-Max Scaling: Used for `EstimatedSalary` to scale values to a range of 0 and 1.
- Robust Scaling: Implemented for `Point Earned` and `Balance` to mitigate the influence of outliers by using the median and interquartile range.

## Exploratory Data Analysis
- Data Visualization: Use plots such as histograms, bar plots, and box plots to explore relationships between variables. 
- Correlation Analysis: We will identify correlations between features and customer churn to select the most relevant predictors. Use `sns.heatmap`

## Feature Engineering

## Model Selection
1. Baseline Model: Logistic Regression
    - Logistic Regrssion is fundamemntal binary classification algorithm.

## Model Training and Evaluation
- With the 10,000 instances of dataset, we will split the dataset into 70% training, 15% validation, and 15% test sets. 

## Hyperparameter Tuning

## Conclusion


