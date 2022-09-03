"""
此執行檔僅用於 Cloud Shell ，若使用於本地或是 VM 環境，有修改的必要

功能：讀取資料表
Reference：https://github.com/PyMySQL/PyMySQL

測試結果：在 mydb 資料庫, 成功讀取 my_table 資料表
"""

# 引入套件
import os
import pymysql

from dotenv import load_dotenv

# # 載入環境變數檔案 (.env)
load_dotenv()

# # 取得環境變數
my_host = os.getenv("MY_DB_HOST")
my_port = int(os.getenv("PORT"))
my_user = os.getenv("DB_USER")
my_passwd = os.getenv("DB_USER_PASSWORD")
my_db = os.getenv("DB_NAME")

# # 印出來看看
print("my_host: %s"%my_host)
print("my_port: %s"%my_port)
print("my_user: %s"%my_user)
print("my_passwd: %s"%my_passwd)
print("my_db: %s"%my_db)

# 建立連線
conn = pymysql.connect(host=my_host, port=my_port, user=my_user, passwd=my_passwd, db=my_db)

# 客戶端物件
# cur = conn.cursor()
with conn:
    with conn.cursor() as cursor:
        # 執行語句 - 讀取 my_table 所有值
        result = cursor.execute("""SELECT * From my_table;""")

        # 印出結果
        print()
        print(cursor)

        # 全部列出來
        for row in cursor:
            print(row)
