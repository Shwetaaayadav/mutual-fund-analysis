# Mutual Fund Analysis

## Day 1 Deliverables

### 1. Project Setup

* Created a structured project directory for data analysis and reporting.
* Initialized a Git repository and connected it to GitHub for version control.
* Set up a Python virtual environment and installed all required dependencies.
* Generated a `requirements.txt` file to ensure reproducibility.

### 2. Data Ingestion

* Loaded all 10 provided CSV datasets using Pandas.
* Verified successful loading of each dataset.
* Inspected dataset dimensions, column names, and data types.
* Displayed sample records using `.head()` for initial validation.

### 3. CSV Exploration

* Explored the contents of each dataset to understand its purpose and structure.
* Identified key datasets including Fund Master, NAV History, Scheme Performance, Portfolio Holdings, and Investor Transactions.
* Documented dataset characteristics and potential data issues.

### 4. Mutual Fund NAV API Integration

* Integrated with the MFAPI service (`https://api.mfapi.in`).
* Fetched live NAV data for HDFC Top 100 Direct Fund.
* Retrieved NAV history for five major mutual fund schemes:

  * SBI Bluechip Fund
  * ICICI Bluechip Fund
  * Nippon India Large Cap Fund
  * Axis Bluechip Fund
  * Kotak Bluechip Fund
* Saved API responses as CSV files for further analysis.

### 5. Initial Data Quality Checks

* Checked each dataset for missing values.
* Identified duplicate records where applicable.
* Reviewed data types and column consistency.
* Documented anomalies and observations in a separate report for future cleaning and validation.

## Technologies Installed

* Python
* Pandas
* NumPy
* Requests
* Jupyter Notebook
* Git & GitHub

