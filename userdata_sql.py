import sqlite3
import datetime as dt


###########################

class SQL_Access:
    def __init__(self):
        self.create_table()

    def create_table(self):
        conn = sqlite3.connect("measurements.db")
        cursor = conn.cursor()

        cursor.execute("""
                CREATE TABLE IF NOT EXISTS measurements (
                    id INTEGER PRIMARY KEY,
                    date DATE,
                    weight DECIMAL,
                    waist_circumference DECIMAL
                )
                """)

        cursor.execute("SELECT date, weight, waist_circumference FROM measurements")

        rows = cursor.fetchall()

        for row in rows:
            print(row)

        conn.commit()
        conn.close()

    def insert_data(self, date, weight, waist):
        conn = sqlite3.connect("measurements.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO measurements ( date, weight, waist_circumference) VALUES (?, ?, ?)",
            (date, weight, waist)
        )

        conn.commit()
        conn.close()

    def insert_weight(self, date, weight):
        conn = sqlite3.connect("measurements.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT 1 FROM measurements WHERE date = ? LIMIT 1",
            (date,)
        )

        exists = cursor.fetchone() is not None

        if exists:
            cursor.execute(
                "UPDATE measurements SET weight = ? WHERE date = ?",
                (weight, date)
            )
        else:
            cursor.execute(
                "INSERT INTO measurements (date, weight) VALUES (?, ?)",
                (date, weight)
            )

        conn.commit()
        conn.close()

    def insert_circumference(self, date, waist):
        conn = sqlite3.connect("measurements.db")
        cursor = conn.cursor()

        cursor.execute(
            "SELECT 1 FROM measurements WHERE date = ? LIMIT 1",
            (date,)
        )

        exists = cursor.fetchone() is not None

        if exists:
            cursor.execute(
                "UPDATE measurements SET waist_circumference = ? WHERE date = ?",
                (waist, date)
            )
        else:
            cursor.execute(
                "INSERT INTO measurements (date, waist_circumference) VALUES (?, ?)",
                (date, waist)
            )

        conn.commit()
        conn.close()

    def get_data(self):
        conn = sqlite3.connect("measurements.db")
        cursor = conn.cursor()

        cursor.execute("SELECT date, weight, waist_circumference FROM measurements")
        rows = cursor.fetchall()

        list_of_lists = [list(row) for row in rows]

        conn.commit()
        conn.close()
        return list_of_lists