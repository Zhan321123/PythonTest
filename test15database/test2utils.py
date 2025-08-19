import mysql.connector
from mysql.connector import Error

config = {
  'host': '127.0.0.1',
  'user': 'root',
  'password': '987654321asd',
  'database': 'test',
  'charset': 'utf8mb4',  # 支持所有 Unicode 字符
  'use_unicode': True
}

def close(connection, cursor):
  if connection.is_connected():
    cursor.close()
    connection.close()
    print("数据库连接已关闭。")

if __name__ == '__main__':
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    # 查询列属性
    cursor.execute("show columns from companyNames")
    print("列属性：", cursor.fetchall())

    cursor.execute("select * from companyNames where name like '%武汉%'")
    print("表内容：", cursor.fetchall())