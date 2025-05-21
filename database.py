import sqlite3

def init_db():
    conn = sqlite3.connect("waybill.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            license_number TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT,
            model TEXT,
            type TEXT,
            mileage INTEGER
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Routes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            point_a TEXT,
            point_b TEXT,
            distance INTEGER,
            route_type TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Waybills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            driver TEXT,
            vehicle TEXT,
            route TEXT,
            date_created TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_to_database(waybill):
    conn = sqlite3.connect("waybill.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO Waybills (driver, vehicle, route, date_created) VALUES (?, ?, ?, ?)",
                (waybill["driver"], waybill["vehicle"], waybill["route"], waybill["date"]))

    conn.commit()
    conn.close()
