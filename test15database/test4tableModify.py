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

connection = mysql.connector.connect(**config)
cursor = connection.cursor()
cursor.execute("alter table companyNames add pinyin varchar(1024)")