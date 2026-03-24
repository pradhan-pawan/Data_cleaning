import pandas as pd
import os
from utils import get_connection, save_to_csv

def run_pandas_solution(db_path, output_path):
    conn = get_connection(db_path)
    if conn is None:
        return

    try:
        sales = pd.read_sql("SELECT * FROM sales", conn)
        customers = pd.read_sql("SELECT * FROM customer", conn)
        orders = pd.read_sql("SELECT * FROM orders", conn)
        items = pd.read_sql("SELECT * FROM items", conn)

        df = customers.merge(sales, on="customer_id") \
                      .merge(orders, on="sales_id") \
                      .merge(items, on="item_id")

        df = df[(df["age"] >= 18) & (df["age"] <= 35)]

        # Remove NULL quantities
        df = df[df["quantity"].notna()]

        result = df.groupby(
            ["customer_id", "age", "item_name"]
        )["quantity"].sum().reset_index()

        result = result[result["quantity"] > 0]

        result.columns = ["Customer", "Age", "Item", "Quantity"]
        result["Quantity"] = result["Quantity"].astype(int)

        save_to_csv(result, output_path)

    except Exception as e:
        print(f"Pandas Error: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    db_path = os.path.join(BASE_DIR, "sales.db")
    output_path = os.path.join(BASE_DIR, "output", "pandas_output.csv")

    run_pandas_solution(db_path, output_path)