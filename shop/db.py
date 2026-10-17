import sqlite3

DB_PATH = "shop.db"


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_product(conn: sqlite3.Connection, product_id: int):
    return conn.execute("SELECT id, name, price FROM products WHERE id = ?", (product_id,)).fetchone()
