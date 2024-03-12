import mysql.connector


database_name = 'mydbone'


# def get_image_catalog():

#    global database_name
#    connection = mysql.connector.connect(
#       host="localhost",
#       user="root",
#       database=database_name
#    )

#    if connection.is_connected():
#       # get
#       print("Connected to MySQL database")
#       cursor = connection.cursor()
#       # Table
#       table_name = 'image_catalog'
#       cursor.execute(f"SELECT * FROM {table_name}")
#       image_catalog = cursor.fetchall()
#       print(image_catalog)
#       # close
#       cursor.close()
#       connection.close()
#       print("Connection closed")

#       return image_catalog
#    else:
#       print("Failed to connect to MySQL database")


# def if_exist(username):

#    for old_user in get_image_catalog():
#       if old_user[0] == username:
#          return True

#    return False


def only_keep_id(full_list):

   id_list = []

   for i in full_list:
      id_list.append(i[0])

   return id_list


def select_image_catalog(date, resort, only_id=False):

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

      # table
      table_name = 'image_catalog'
      cursor.execute(f"SELECT * FROM {table_name} WHERE date = '{date}' and resort = '{resort}'")
      image_catalog = cursor.fetchall()
      # print(image_catalog)

      # close
      cursor.close()
      connection.close()
      print("Connection closed")

      # only id
      if only_id:
         return only_keep_id(image_catalog)
      else:
         return image_catalog

   else:
      print("Failed to connect to MySQL database")

      
if __name__ == "__main__":

   # get_image_catalog()
   date = '2024-02-23'
   resort = 'wanlong'
   index = select_image_catalog(date, resort, True)
   print(index)