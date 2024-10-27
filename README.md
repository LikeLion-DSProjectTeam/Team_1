# Team_1

Mentor: John Oh, Arden Kim  
Member: Beomseong Kim, Ikjoo Oh

## Table of Contents
1. [Overview](#overview)
2. [Problem Statement](#problem-statement)
3. [Data Description](#data-description)
4. [Data Preprocessing](#data-preprocessing)
5. [Exploratory Data Analysis](#exploratory-data-analysis)
6. [Reinforcement Learning Environment Setup](#reinforcement-learning-environment-setup)
7. [Feature Engineering](#feature-engineering)
8. [Model Selection](#model-selection)
9. [Model Training and Evaluation](#model-training-and-evaluation)
10. [Hyperparameter Tuning](#hyperparameter-tuning)
11. [Performance Analysis](#performance-analysis)
12. [Deployment](#deployment)
13. [Conclusion](#conclusion)

## Overview

This is a Data Science project by Beomseong Kim and Ikjoo Oh under the guidance of mentors John Oh and Arden Kim. 

Used Kaggle Dataset: [Bank Chustomer Churn](https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn/data)

## Problem Statement
The objective of this project is to leverage reinforcement learning to develop an intelligent decision-making model that identifies and implements optimal strategies for retaining customers at risk of churning. By analyzing historical customer data and understanding the key factors influencing churn, the model will learn to take targeted actions such as offering promotions, personalized financial products, or enhanced customer service that would effectively reduce churn rates. Additionally, the project includes the design and implementation of a interface that allows user (most likely bank staff) to interact with the model, visualize predictions, and deploy retention strategies efficiently. This integrated approach aims to enable the bank to deploy dynamic and adaptive retention programs, thereby increasing customer satisfaction, loyalty, and operational efficiency.

- Expected Outcomes
  - Development of a Reinforcement Learning Model: We will create a reinforcement learning-based agent capable of learning and executing optimal actions to retain at-risk customers.
  - User-Friendly Interface Implementation: We will design and develop an intuitive and interactive user interface that allows bank staff to easily interact with the reinforcement learning model, visualize customer churn predictions, and deploy retention strategies with minimal effort.
  - Performance Benchmarking: We will compare the reinforcement learning model’s performance against machine learning baseline models (ex, Logistic, Linear) to demonstrate its effectiveness and superiority in churn prevention.


## Data Description
1. CreditScore(`int`) — Customer credit score
2. Age(`int`) — Customer age
3. Tenure(`int`) — Duration of the customer relationship with the bank
4. NumOfProducts(`int`) — number of products that a customer has purchased through the bank.
5. HasCrCard(`int`) — denotes whether or not a customer has a credit card
6. IsActiveMember(`int`) — Indicator of active membership status
7. Satisfaction Score(`int`) — Score provided by the customer for their complaint resolution
8. Points Earned(`int`) — Points earned by the customer through credit card usage
9. Balance(`float`) — Account balance
10. EstimatedSalary(`float`) — Customer Salary
11. Geography(`object`) — Customer location
12. Card Type(`object`) — Type of card hold by the customer.
13. Gender(`object`) — Gender of the customer
14. **Exited**(`int`) — **Target feature** that indicate whether the customer left the bank

- Target Variable
  - Exited: `1` = the customer left, `0` = the customer stayed

- Unneeded Variables
1. RowNumber - indicates the row number and this feature doesn't affect analysis
2. CustomerId - A random identifier for customers, which also doesn't influence customer churn
3. Surname - The customer's surname has no impact on their decision to leave the bank
4. Complain - This feature has perfect correlation of 1 with `Exited', which could lead to overfitting

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

## Reinforcement Learning Environment Setup

## Feature Engineering (later)

## Model Selection

## Model Training and Evaluation

## Hyperparameter Tuning

## Performance Analysis 

## Deployment 

## Conclusion


