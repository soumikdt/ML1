__Fraud detection from kaggle data__

Project Description: In present times, increased number of transaction frauds has enhanced need for fraud detection and prevention systems. Transaction fraud detection is now known as critical process for identification and prevention of fraudulent activities in financial transactions. This process involves use of advanced ML algorithms, data analytics, analysis of transaction patterns, and anomalies in transaction data. Using these advanced approaches, various parameters such as location, transaction amount, and frequency can be monitored to detect any unusual behaviour indicating frauds. Real-time monitoring and adaptive algorithms contribute to the effectiveness of fraud detection, enabling swift intervention to prevent unauthorized transactions and protect both consumers and financial institutions from potential losses.

__Data Description__

Dataset Dataset used in this project was provided by Vesta Corporation in 2019 for a compeition on Kaggle.com. It contains real-time transaction details such as user details (device type, OS system), location, transaction amount, and other above 300 features for each transaction. 


## Dataset
- **Source**: Vesta Corporation
- **Files**:
  - `train_transaction.csv`: training transaction data
  - `train_identity.csv`: training identity data
  - `test_transaction.csv`: testing transaction data
  - `test_identity.csv`: testing identity data

### Feature Overview
- **TransactionDT**: Time delta from a reference datetime (not actual timestamp)
- **TransactionAmt**: Dollar amount of transaction
- **ProductCD, card1–card6**: Product and card details
- **addr1, addr2**: User address information
- **dist1, dist2**: Distance features
- **P_emaildomain, R_emaildomain**: Email domain features
- **C1–C14**: Count features
- **D1–D15**: Time delta features
- **M1–M9**: Match features (e.g., card and address)
- **V1–V339**: Rich engineered features provided by Vesta

## Dependencies
- Python 3.7+
- pandas
- numpy
- scikit-learn
- imbalanced-learn (SMOTE)
- xgboost
- matplotlib
- seaborn
- statsmodels
- prettytable
- scipy


2. Open `ML_FraudDetection.ipynb` and run cells sequentially to reproduce the analysis.

### Workflow Steps
1. **Data Loading & Merging**: Combine transaction and identity files by TransactionID.
2. **Exploratory Data Analysis (EDA)**: Initial data profiling and visualization.
3. **Data Preprocessing**: Handle missing values, encode categorical features.
4. **Feature Engineering**: Create new features and select relevant ones.
5. **Model Training**: Train Logistic Regression, Random Forest, and XGBoost classifiers.
6. **Evaluation**: Assess performance with accuracy, precision, recall, F1-score, and ROC-AUC.

## Project Structure
```text
├── data/
│   ├── train_transaction.csv
│   ├── train_identity.csv
│   ├── test_transaction.csv
│   └── test_identity.csv
├── ML_FraudDetection.ipynb
├── requirements.txt
└── README.md
```

## Methodology
Detailed explanation of data preprocessing steps, feature selection strategies, and modeling choices can be found in the notebook.

## Model Evaluation
Performance of each model (cross-validated) is summarized with metrics and visualizations in the notebook.

## Results
- **Best Model**: XGBoost achieved the highest ROC-AUC score of _X.XX_
- **Comparison**: Random Forest and Logistic Regression results are also provided for benchmarking.

