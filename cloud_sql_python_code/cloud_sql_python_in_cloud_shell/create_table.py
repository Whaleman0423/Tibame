"""
此執行檔僅用於 Cloud Shell ，若使用於本地或是 VM 環境，有修改的必要

功能：創建資料表
Reference：https://github.com/PyMySQL/PyMySQL

測試結果：在 mydb 資料庫, 成功創建出 my_table 資料表
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
cur = conn.cursor()

# 執行語句 - 創建資料表
# 因資料表只能創建一個名字, 所以只能執行一次
# 重複執行，會報錯誤："Table 'my_table' already exists"
cur.execute("""
CREATE TABLE my_table (
    id varchar(255),
    name varchar(255),
    gender varchar(255),
    cell_phone varchar(255),
    email varchar(255),
    job_title varchar(255));
""")

# 關閉物件與連線
cur.close()
conn.close()