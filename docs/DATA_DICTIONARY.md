# Data Dictionary

## Dataset Name

PaySim

## Description

PaySim is a synthetic mobile money transaction dataset designed to simulate real-world payment behavior. It contains transaction-level records that can be used to study fraud patterns and build machine learning models for fraud detection.

## Purpose of the Dataset

The dataset is used to:

- analyze transaction behavior
- identify suspicious patterns
- study fraud in digital financial systems
- build a fraud detection model

## Target Variable

### `isFraud`

Indicates whether a transaction is fraudulent.

- `0` = legitimate transaction
- `1` = fraudulent transaction

## Column Descriptions

### `step`
Represents the time unit of the transaction in the simulation. It can be interpreted as the transaction time step.

### `type`
The type of transaction. Common values include:

- `CASH_IN`
- `CASH_OUT`
- `DEBIT`
- `PAYMENT`
- `TRANSFER`

### `amount`
The amount of money involved in the transaction.

### `nameOrig`
The account ID of the sender or origin account.

### `oldbalanceOrg`
The sender’s balance before the transaction.

### `newbalanceOrig`
The sender’s balance after the transaction.

### `nameDest`
The account ID of the recipient or destination account.

### `oldbalanceDest`
The recipient’s balance before the transaction.

### `newbalanceDest`
The recipient’s balance after the transaction.

### `isFraud`
The fraud label for the transaction.

### `isFlaggedFraud`
A system-generated fraud flag. This indicates whether the transaction was flagged by the simulation logic.

## Initial Interpretation Notes

- Fraud is expected to be rare, so the dataset is likely imbalanced.
- `type` may be highly relevant for fraud analysis.
- Balance columns may help identify suspicious behavior such as inconsistency between transaction amount and balance changes.
- Account identifiers are useful for reference, but may not be directly useful as raw machine learning features.
- `isFlaggedFraud` may help with exploratory analysis, but it should be examined carefully to avoid leakage if used improperly in modeling.

## Important Modeling Note

Before training any model, we must check whether any features create data leakage or reveal fraud in a way that would not be available in a real-world prediction setting.

## Questions to Explore

- Which transaction types are most associated with fraud?
- Do fraudulent transactions have distinctive amount patterns?
- Are there suspicious balance changes before and after transactions?
- Can account behavior over time help improve detection?
- Is the flagged fraud label aligned with the actual fraud label?

## Notes

This data dictionary will be updated as the dataset is explored and the feature set is refined.