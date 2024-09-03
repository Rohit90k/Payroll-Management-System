import sqlite3


def get_row_count():
    db = sqlite3.connect('Employees.db')
    cursor = db.cursor()
    cursor.execute("""SELECT COUNT(*) FROM Database""")
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return rows[0][0]


def get_total_basic():
    db = sqlite3.connect('Employees.db')
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(basic) FROM Database""")
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return rows[0][0]


def get_total_rate_day():
    db = sqlite3.connect('Employees.db')
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(day_rate) FROM Database""")
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return rows[0][0]


def get_total_rate_ot():
    db = sqlite3.connect('Employees.db')
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(ot_rate) FROM Database""")
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return rows[0][0]


def get_total_rate_sun():
    db = sqlite3.connect('Employees.db')
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(sun_rate) FROM Database""")
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return rows[0][0]


def get_total_salary():
    db = sqlite3.connect('Employees.db')
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(total_salary) FROM Database""")
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return rows[0][0]


def get_total_r_off():
    db = sqlite3.connect('Employees.db')
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(r_off) FROM Database""")
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return rows[0][0]


def get_total_net():
    db = sqlite3.connect('Employees.db')
    cursor = db.cursor()
    cursor.execute("""SELECT SUM(net_salary) FROM Database""")
    rows = cursor.fetchall()
    db.commit()
    db.close()
    return rows[0][0]

