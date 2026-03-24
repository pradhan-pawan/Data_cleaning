import sqlite3

def get_connection(db_path):
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except Exception as e:
        print(f"DB Connection Error: {e}")
        return None


def save_to_csv(df, path):
    try:
        df.to_csv(path, sep=';', index=False)
        print(f"File saved: {path}")
    except Exception as e:
        print(f"File Write Error: {e}")