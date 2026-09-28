# RFM Analysis

A beginner-friendly customer segmentation project using **RFM Analysis** with Python and Pandas.

## 📌 Project Objective

The goal of this project is to analyze customer purchasing behavior and divide customers into different segments based on their purchase history.

RFM stands for:

* **Recency** – How recently a customer made a purchase
* **Frequency** – How often a customer makes a purchase
* **Monetary** – How much money a customer has spent

## 🧠 RFM Concepts

### Recency

Recency measures the number of days since the customer's most recent purchase.

**Lower Recency = Better**

Example:

A customer who purchased 5 days ago is more recent than a customer who purchased 100 days ago.

### Frequency

Frequency represents the number of purchases made by a customer.

**Higher Frequency = Better**

### Monetary

Monetary represents the total amount spent by a customer.

**Higher Monetary = Better**

## 📊 RFM Scoring

Each customer receives a score from **1 to 5** for:

* Recency
* Frequency
* Monetary

For Recency, the scoring direction is reversed because a lower number of days is better.

The three scores are combined to create an overall RFM score.

Example:

```text
R = 5
F = 3
M = 5

RFM Score = 535
```

## 👥 Customer Segmentation

Customers are divided into segments based on their RFM scores.

The current project identifies:

* **Loyal Customers**
* **At Risk**
* **Champions**
* **Potential Loyalists**
* **Need Attention**

The sample dataset resulted in:

* **3 Loyal Customers**
* **2 At Risk Customers**

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Jupyter Notebook
* VS Code

## 📁 Project Structure

```text
RFM-Analysis/
│
├── Data/
│   └── customer_sales.csv
│
├── Notebooks/
│   └── rfm_analysis.ipynb
│
├── Outputs/
│   └── rfm_customer_segments.csv
│
├── README.md
└── create_dataset.py
```

## 🔍 Key Python Concepts Practiced

* Creating a DataFrame
* Reading and writing CSV files
* `groupby()`
* `max()`
* `count()`
* `sum()`
* `pd.qcut()`
* `apply()`
* Custom functions
* `astype()`
* Customer segmentation
* Data visualization

## 📈 Project Workflow

```text
Customer Sales Data
        ↓
Data Preparation
        ↓
Calculate Recency
        ↓
Calculate Frequency
        ↓
Calculate Monetary
        ↓
Create RFM Scores
        ↓
Customer Segmentation
        ↓
Export Results
```

## 🎯 Learning Outcome

This project provides a practical introduction to **customer segmentation** and demonstrates how business data can be converted into meaningful customer insights using Python.

It also introduces the basic concepts behind RFM analysis that are commonly used in areas such as:

* Retail
* E-commerce
* Banking
* Marketing
* Customer Relationship Management (CRM)
