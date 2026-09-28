import pandas as pd
data = {
    "Customer_ID": [
        "C001", "C001", "C001",
        "C002", "C002",
        "C003", "C003", "C003", "C003",
        "C004",
        "C005", "C005", "C005"
    ],

    "Order_Date": [
        "2026-09-01", "2026-09-10", "2026-09-20",
        "2026-08-15", "2026-09-05",
        "2026-06-10", "2026-07-15", "2026-08-10", "2026-09-15",
        "2026-05-20",
        "2026-09-02", "2026-09-12", "2026-09-22"
    ],

    "Sales": [
        5000, 7500, 10000,
        4000, 6000,
        3000, 4500, 5000, 7000,
        2500,
        8000, 9000, 12000
    ]
}
df = pd.DataFrame(data)

df.to_csv("data/customer_sales.csv", index=False)

print("Customer sales dataset created successfully!")
print(df)