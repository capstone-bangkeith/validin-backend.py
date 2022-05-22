import sqlite3


class Database:
    def __init__(self, db_name: str | None = "kodewilayah.db"):
        self.con = sqlite3.connect(db_name)

    def close(self):
        self.con.close()

    def __del__(self):
        self.close()

    def get_kode_wilayah(self, kode: str | None = None):
        cur = self.con.cursor()
        if kode is None:
            cur.execute("SELECT * FROM kodewilayah")
        else:
            cur.execute(
                "SELECT * FROM kodewilayah WHERE kodewilayah=:kode", {"kode": kode}
            )
        return cur.fetchall()
