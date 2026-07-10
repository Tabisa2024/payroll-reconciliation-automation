# Payroll Reconciliation Automation

This project demonstrates a payroll reconciliation automation workflow designed to reduce manual checking by comparing payroll records against branch records and generating an exception report.

## Project Overview

In many business environments, payroll reconciliation is done manually by comparing employee payroll records against branch-level data. This can be time-consuming and prone to errors.

This automation compares two datasets:
- Payroll data
- Branch data

It identifies:
- Employees found in payroll but missing from branch records
- Employees found in branch records but missing from payroll
- Salary mismatches
- Department mismatches

## Features

- Reads payroll and branch CSV files
- Compares employee records by Employee ID
- Detects missing records
- Detects salary mismatches
- Detects department mismatches
- Generates an exception report
- Saves results into a CSV file

## Tech Stack

- Python
- Pandas
- CSV data processing
- Automation logic
- Data validation

## Business Value

This project shows how repetitive reconciliation work can be automated to improve accuracy, reduce manual effort, and allow teams to focus on resolving exceptions instead of manually comparing records.

## Files in This Project

| File | Description |
|---|---|
| `payroll_data.csv` | Sample payroll system data |
| `branch_data.csv` | Sample branch records |
| `reconciliation.py` | Python script that performs the reconciliation |
| `exception_report.csv` | Output file generated after running the script |

## How to Run

1. Install pandas:

```bash
pip install pandas
