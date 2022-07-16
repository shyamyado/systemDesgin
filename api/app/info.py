import psycopg2

class Info:
    def __init__(self):
        self.conn = psycopg2.connect(database="telephone",
                        host="192.168.56.1",
                        user="postgres",
                        password="0123.",
                        port="5432"
                        )

    def save_info(self, data):
        qs = """INSERT INTO test01 ( name, phone) values(%s,%s) RETURNING id;"""
        cur = self.conn.cursor()
        res = []
        for item in data["items"]:
            print(item)
            cur.execute(qs,(item["name"],item["phone"]))
            id_of_new_row = cur.fetchone()[0]
            self.conn.commit()
            res.append(id_of_new_row)
        cur.close()
        return res
        
    def get_all_user(self):
        qs = """SELECT name, phone from test01"""
        cur = self.conn.cursor()
        cur.execute(qs)
        users = cur.fetchall()
        cur.close()
        return users

    def get_user_by_phone(self, phone):
        cur = self.conn.cursor()
        cur.execute(f"""SELECT name, phone from test01 WHERE phone = '{phone}'""")
        #cur.execute(qs,(str(phone)))
        user = cur.fetchone()
        cur.close()
        return user

    def update_user_details(self,phone, data):
        print(data)
        name = data["name"]
        new_phone = data["phone"]
        cur = self.conn.cursor()
        sql = """ UPDATE test01
                SET name = %s
                , phone = %s
                WHERE phone = %s"""
        res = cur.execute(sql, (name, new_phone, phone))
        self.conn.commit()
        cur.close()
        return res


#  WORKING ON GIT ONE
#  working on git two
#  working on git three