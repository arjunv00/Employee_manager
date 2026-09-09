import mysql.connector


class Dbconnect:
    def get_connection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Arjunvinayak@123",
                database="company_db"
            )
            return self.connection
        except Exception as e:
            return None

class EmployeeManagement(Dbconnect):
    def get(self):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee"
            self.cursor.execute(query)
            record = self.cursor.fetchall()
            for data in record:
                print(data)
        except Exception as e:
            print(e)

    def post(self, **kwargs):
        self.connect = super().get_connection()
        self.cursor = self.connect.cursor()
        query = """
                INSERT INTO employee
                (name, place, mobile, email, department, salary, joining_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        values = [v for v in kwargs.values()]
        self.cursor.execute(query, values)
        self.connect.commit()
        print("New employee added successfully")

    def retrieve(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            if record == None:
                print("Employee not found")
            print(record)
        except Exception as e:
            print(e)

    def get_object(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "select * from employee where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None

    def delete(self, id=None):
        try:
            self.connect = super().get_connection()
            self.cursor = self.connect.cursor()
            query = "delete from employee where id = %s"
            values = (id,)
            self.cursor.execute(query, values)
            if self.cursor.rowcount > 0:
                self.connect.commit()
                print("Employee deleted successfully")
            else:
                print("Employee not found")
        except Exception as e:
            print(e)


    def put(self, id=None, **kwargs):
        try:
            record = self.get_object(id=id)
            if record != None:
                self.connect = super().get_connection()
                self.cursor = self.connect.cursor()
                placeholder = ""
                for k in kwargs.keys():
                    placeholder += k + "=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update employee set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query, values)
                self.connect.commit()
                print("Employee details updated successfully......")
            else:
                print("Employee not found.....")
        except Exception as e:
            print(e)


connection_instance = Dbconnect()

print(connection_instance.get_connection())

employee_instance = EmployeeManagement()


#POST
# employee_instance.post(
#      name="Anitha",
#      place="Perumbavoor",
#      mobile="7546983465",
#      email="anithadileep@gmail.com",
#      department="Finance",
#      salary=35000,
#      joining_date=datetime.now()
#  )


# GET ALL
#employee_instance.get()


# RETRIEVE BY ID
# employee_instance.retrieve(id=2)


# GET OBJECT
# print(employee_instance.get_object(id=1))


# DELETE
# employee_instance.delete(id=2)


# PUT
# employee_instance.put(
#     id=2,
#     name="Arjun Vinayak",
#     place="Perumbavoor",
#     salary=35000
# )

