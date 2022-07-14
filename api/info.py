import psycopg2

class Info:
    def __init__(self):
        self.conn = psycopg2.connect(database="telephone",
                        host="localhost",
                        user="postgres",
                        password="0123.",
                        port="5432"
                        )



    def save_info(self,data):
        qs = """INSERT INTO test01 ( name, phone) values(%s,%s);"""
        cur = self.conn.cursor()
        for item in data["items"]:
            cur.execute(qs,(item["name"],item["phone"]))
            self.conn.commit()
        cur.close()
        
# conn.execute("SELECT * FROM test01")

