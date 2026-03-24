import pandas as pd
import os
from utils import get_connection, save_to_csv

def run_sql_solution(db_path, output_path):
    conn = get_connection(db_path)
    if conn is None:
        return

    # Debug: check tables
    print("Tables:", conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table';"
    ).fetchall())

    query = """
    SELECT 
        c.customer_id AS Customer,
        c.age AS Age,
        i.item_name AS Item,
        SUM(o.quantity) AS Quantity
    FROM customer c
    JOIN sales s ON c.customer_id = s.customer_id
    JOIN orders o ON s.sales_id = o.sales_id
    JOIN items i ON o.item_id = i.item_id
    WHERE c.age BETWEEN 18 AND 35
    AND o.quantity IS NOT NULL
    GROUP BY c.customer_id, c.age, i.item_name
    HAVING SUM(o.quantity) > 0
    ORDER BY Customer, Item;
    """

    try:
        df = pd.read_sql_query(query, conn)
        df["Quantity"] = df["Quantity"].astype(int)
        save_to_csv(df, output_path)
    except Exception as e:
        print(f"Query Error: {e}")
    finally:
        conn.close()


if __name__ == "__main__":
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    db_path = os.path.join(BASE_DIR, "sales.db")
    output_path = os.path.join(BASE_DIR, "output", "sql_output.csv")

    run_sql_solution(db_path, output_path)