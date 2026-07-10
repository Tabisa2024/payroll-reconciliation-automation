import pandas as pd

# Load datasets
payroll_data = pd.read_csv("payroll_data.csv")
branch_data = pd.read_csv("branch_data.csv")

# Convert EmployeeID to string to avoid matching issues
payroll_data["EmployeeID"] = payroll_data["EmployeeID"].astype(str)
branch_data["EmployeeID"] = branch_data["EmployeeID"].astype(str)

# Merge both datasets using EmployeeID
merged_data = payroll_data.merge(
    branch_data,
    on="EmployeeID",
    how="outer",
    suffixes=("_Payroll", "_Branch"),
    indicator=True
)

exceptions = []

for _, row in merged_data.iterrows():
    employee_id = row["EmployeeID"]

    if row["_merge"] == "left_only":
        exceptions.append({
            "EmployeeID": employee_id,
            "EmployeeName": row["EmployeeName_Payroll"],
            "IssueType": "Missing in Branch Data",
            "PayrollValue": "Exists",
            "BranchValue": "Missing",
            "Status": "Review Required"
        })

    elif row["_merge"] == "right_only":
        exceptions.append({
            "EmployeeID": employee_id,
            "EmployeeName": row["EmployeeName_Branch"],
            "IssueType": "Missing in Payroll Data",
            "PayrollValue": "Missing",
            "BranchValue": "Exists",
            "Status": "Review Required"
        })

    else:
        employee_name = row["EmployeeName_Payroll"]

        if row["Salary_Payroll"] != row["Salary_Branch"]:
            exceptions.append({
                "EmployeeID": employee_id,
                "EmployeeName": employee_name,
                "IssueType": "Salary Mismatch",
                "PayrollValue": row["Salary_Payroll"],
                "BranchValue": row["Salary_Branch"],
                "Status": "Review Required"
            })

        if row["Department_Payroll"] != row["Department_Branch"]:
            exceptions.append({
                "EmployeeID": employee_id,
                "EmployeeName": employee_name,
                "IssueType": "Department Mismatch",
                "PayrollValue": row["Department_Payroll"],
                "BranchValue": row["Department_Branch"],
                "Status": "Review Required"
            })

# Create exception report
exception_report = pd.DataFrame(exceptions)

# Save report
exception_report.to_csv("exception_report.csv", index=False)

print("Payroll reconciliation completed successfully.")
print(f"Total exceptions found: {len(exception_report)}")
print("Exception report saved as: exception_report.csv")
`
