import sqlite3


class PerfumesDBHelper:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)

    def setup(self):
        c = self.conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS perfumes (brand TEXT, perfume TEXT, launch_year TEXT, "
                  "main_accords TEXT, notes TEXT, longevity TEXT, sillage TEXT)")
        # c.execute("CREATE INDEX perfume_index ON perfumes (name)")
        self.conn.commit()

    def add_record(self, args):
        c = self.conn.cursor()
        c.execute("INSERT INTO perfumes (brand, perfume, launch_year, main_accords, notes, longevity, sillage) "
                  "VALUES (?, ?, ?, ?, ?, ?, ?)", args)
        self.conn.commit()

    def number_of_records(self):
        c = self.conn.cursor()
        c.execute("SELECT COUNT(*) FROM perfumes")
        result = c.fetchone()
        return result[0]
