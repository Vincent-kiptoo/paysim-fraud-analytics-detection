# PaySim Fraud Analytics and Detection

End-to-end fraud analytics and machine learning project using the PaySim dataset, built as a piece for fraud detection, behavioral analysis, and explainable machine learning.

## Project Overview

This project investigates fraud in digital financial transactions from both an analytical and a machine learning perspective.

My goal is not just to build a model, but to understand fraud as a behavioral problem:
how suspicious transactions look, how fraud patterns differ from normal activity, and how machine learning can support early detection and decision-making.

This project is also informed by my background in criminology and penology. That gives me a useful lens for thinking about fraud as a mix of opportunity, concealment, timing, and exploitation of systems.

## Why This Project

Fraud detection is one of the most important problems in financial services because fraud is costly, adaptive, and often hidden inside a large volume of legitimate transactions.

A strong fraud detection system must:

- detect suspicious transactions early
- minimize false negatives
- avoid overwhelming users with false positives
- explain why a transaction is suspicious
- support decision-making, not just prediction

This project is designed to show those ideas clearly through analytics, modeling, interpretation, and deployment-ready structure.

## Problem Statement

Digital payment systems process millions of transactions, but only a small fraction are fraudulent. This creates a difficult imbalanced classification problem.

The main question for this project is:

> Can we analyze PaySim transaction behavior and build an intelligent system that predicts fraudulent transactions while explaining the patterns behind those predictions?

## Dataset

This project uses the PaySim dataset, a synthetic mobile money transaction dataset modeled on real transaction behavior.

The dataset contains transaction-level information such as:

- transaction step or time unit
- transaction type
- transaction amount
- origin account
- origin balance before and after the transaction
- destination account
- destination balance before and after the transaction
- fraud label
- flagged fraud indicator

The target variable is whether a transaction is fraudulent.

## Previous Work on This Dataset

Before moving into machine learning, I already explored this dataset using SQL-based analysis.

That earlier work included investigations into:

- transaction patterns
- crime discovery
- behavioral risk patterns
- victim profile analysis
- system response
- final conclusions

This machine learning project builds on that foundation. The SQL analysis helped me understand the data from an investigative angle, and now I am turning those insights into predictive modeling and explainable fraud detection.

## Project Goals

The goals of this project are to:

1. Understand the PaySim dataset deeply.
2. Explore fraud and non-fraud transaction behavior.
3. Identify patterns that may indicate suspicious activity.
4. Build baseline and improved machine learning models.
5. Use proper metrics for imbalanced classification.
6. Explain model predictions clearly.
7. Build toward a simple deployment-ready application.

## Why Fraud Detection Is Hard

Fraud detection is challenging because:

- fraud cases are rare compared to legitimate transactions
- fraudsters try to behave like normal users
- accuracy alone can be misleading
- false positives can annoy legitimate users
- false negatives can cause financial loss
- fraud patterns may change over time

Because of this, the project will focus on metrics and explanations that make sense for imbalanced classification.

## Planned Approach

The project will follow a staged workflow:

1. Load and inspect the data
2. Perform exploratory data analysis
3. Clean and validate the dataset
4. Engineer useful fraud-related features
5. Build baseline models
6. Compare model performance
7. Interpret what drives predictions
8. Prepare the project for deployment

## Evaluation Metrics

Because this is an imbalanced classification problem, accuracy is not enough on its own.

The project will evaluate models using:

- precision
- recall
- F1-score
- confusion matrix
- ROC-AUC
- precision-recall AUC

Special attention will be given to the tradeoff between false positives and false negatives.

## Explainability

A good fraud detection system should not only predict fraud. It should also explain why a transaction looks suspicious.

This project will include:

- feature importance analysis
- fraud pattern interpretation
- comparison of fraud and non-fraud behavior
- clear visual explanations
- simple language for model results

## Portfolio Angle

This is a portfolio project, so the presentation matters as much as the modeling.

The final version is intended to show:

- real problem framing
- strong data understanding
- structured coding habits
- analytical thinking
- machine learning fundamentals
- mathematical understanding
- explainability
- communication skill
- deployment readiness

## Project Structure

Fraud-Analytics/
│
├── data/
│   └── raw/
│
├── docs/
│   ├── DATA_DICTIONARY.md
│   ├── DECISIONS.md
│   └── WEEK1_PLAN.md
│
├── notebooks/
│   └── 01_eda_paysim.ipynb
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── logging_config.py
│   └── data_ingestion.py
│
├── tests/
│   └── __init__.py
│
├── README.md
├── requirements.txt
└── .gitignore