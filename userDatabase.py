import mysql.connector


database_name = 'mydbone'


def get_user():

   global database_name
   connection = mysql.connector.connect(
      host="localhost",
      user="root",
      database=database_name
   )

   if connection.is_connected():
      # get
      print("Connected to MySQL database")
      cursor = connection.cursor()
      # Table
      cursor.execute("SELECT * FROM user")
      users = cursor.fetchall()
      print(users)
      # close
      cursor.close()
      connection.close()
      print("Connection closed")

      return users
   else:
      print("Failed to connect to MySQL database")


def if_exist(username):

   for old_user in get_user():
      if old_user[0] == username:
         return True

   return False


def add_user(username, password):

   if if_exist(username):
      return 'error'
   
   else:
      global database_name
      connection = mysql.connector.connect(
         host="localhost",
         user="root",
         database=database_name
      )

      if connection.is_connected():
         print("Connected to MySQL database")
         cursor = connection.cursor()

         # 准备 SQL 插入语句
         table_name = 'user'
         column1 = 'username'
         column2 = 'password'
         sql_insert = f"INSERT INTO {table_name} ({column1}, {column2}) VALUES (%s, %s)"

         # 插入数据
         add_data = (username, password)
         cursor.execute(sql_insert, add_data)
         connection.commit()

         cursor.close()
         connection.close()
         print("Connection closed")

         return 'success'
      
      else:
         return "Failed to connect to MySQL database"
      
      
if __name__ == "__main__":

   get_user()
   # print(if_exist('Harden'))
   print(add_user('James', 'iamjames'))
   get_user()