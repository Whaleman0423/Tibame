"""
此執行檔僅用於 Cloud Shell ，若使用於本地或是 VM 環境，有修改的必要

功能：增加一列
Reference：https://github.com/PyMySQL/PyMySQL

測試結果：在 mydb 資料庫, 成功在 my_table 資料表增加一列
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

with conn:
    with conn.cursor() as cursor:

        # 執行語句 - 增加 my_table 一列
        result = cursor.execute("""
            INSERT INTO my_table (id,name, gender, cell_phone, email, job_title) 
            VALUES ("0", "王小明", "男性", "09123456789", "abc@cxcxc.io", "工程師");
        """)

        # 印出結果
        print(result)
    # 執行
    conn.commit()

