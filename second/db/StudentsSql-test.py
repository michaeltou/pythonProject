import mysql.connector as mysql


class StudentsSql():
    def __init__(self, host, port,user,passowrd,dbname, charset):
        self.host = host
        self.port = port
        self.user = user
        self.password = passowrd
        self.dbname = dbname
        self.charset = charset
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS students (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), age INT)")

    def connet(self):
        self.db = mysql.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            passwd=self.password,
            database=self.dbname,
            charset=self.charset
        )
        self.cursor = self.db.cursor()

    def close(self):
        self.cursor.close()
        self.db.close()

    def get_one(self, sql):
        res = None
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchone()

        except:
            print("查询失败")
            return res

    def get_all(self, sql):
        res = None
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()

        except:
            print("查询失败")
        return res

    def insert(self, sql):
        return self.__edit(sql)

    def update(self, sql):
        return self.__edit(sql)

    def delete(self, sql):
        return self.__edit(sql)

    def __edit(self, sql):
        count = 0
        try:
            count = self.cursor.execute(sql)
            self.db.commit()

        except:
            print("事务提交失败")
            self.db.rollback()
        return count


studentsSql = StudentsSql('localhost', 3306,'root', 'tm123456', 'test', 'utf8')
studentsSql.connet()

studentsSql.create_table()

studentsSql.insert("INSERT INTO students (name, age) VALUES ('Tom', 20)")

studentsSql.update("UPDATE students SET age = 25 WHERE id = 1")


res = studentsSql.get_all("SELECT * FROM students")

print(res)

studentsSql.close()
