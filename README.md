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
The objective of this project is to predict whether a customer will leave the bank based on historical data. Understanding the predictors of customer churn can help the bank in designing effective retention programs and improving customer satisfaction.

- Expected Outcomes
  - We expect to identify key factors contributing to customer churn
  - We will develop a predictive model that accurately classifies customers at risk of churning
  - We will enhance skills in data analysis, machine learning, and problem-solving within a bank industry context

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
- Remove irrelevant features: `RowNumber`, `CustomerId`, `Surname`
- Handle missing values: all columns are free with missing values
- Feature Encoding: We need to convert features like `Geography`, `Gender`, `NumberOfProducts`, `HasCrCard`, `Tenure`, `IsActiveMember` using one-hot encoding or label encoding.

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


