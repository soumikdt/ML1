__Fraud detection from kaggle data__

Project Description: In present times, increased number of transaction frauds has enhanced need for fraud detection and prevention systems. Transaction fraud detection is now known as critical process for identification and prevention of fraudulent activities in financial transactions. This process involves use of advanced ML algorithms, data analytics, analysis of transaction patterns, and anomalies in transaction data. Using these advanced approaches, various parameters such as location, transaction amount, and frequency can be monitored to detect any unusual behaviour indicating frauds. Real-time monitoring and adaptive algorithms contribute to the effectiveness of fraud detection, enabling swift intervention to prevent unauthorized transactions and protect both consumers and financial institutions from potential losses.

__Data Description__

Dataset Dataset used in this project was provided by Vesta Corporation in 2019 for a compeition on Kaggle.com. It contains real-time transaction details such as user details (device type, OS system), location, transaction amount, and other above 300 features for each transaction. The whole data set is broken into two files: identity and transaction files. These files are mergered using Transaction ID.



TransactionDT: timedelta from a given reference datetime (not an actual timestamp)

TransactionAMT: Dollar Amount of transaction payments

ProductCD: Each transaction product Code

card1 - card6: Card details: type, category, bank name, issuing country & other details.

addr: User address

dist: distance (dist1 & dist2)

P_emaildomain: purchaser email domain

R_emaildomain: receiptionist email domain

C1-C14: counting n of addresses

D1-D15: timedelta considering previous transaction.

M1-M9: Information match (card address and name)

V1-V339: Vesta engineered rich features, including ranking, counting, and other entity relations.

