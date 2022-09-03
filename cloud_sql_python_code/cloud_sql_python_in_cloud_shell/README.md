# 前提
1. 需先建立好 Cloud SQL 資料庫
2. 建立一個測試用的 mydb 資料庫
3. 建立一個使用者

# 使用流程
1. 須先建立 venv 並進入虛擬環境
```
<!-- 於 Cloud Shell 此專案資料夾為工作路徑，於 Terminal 執行 -->
<!-- 生成 venv 資料夾 -->
python -m venv venv
<!-- 進入 venv -->
source venv/bin/activate
```

2. 更新並安裝套件
```
<!-- 更新 pip 安裝套件 -->
python -m pip install --upgrade pip
<!-- 安裝 python sql 所需 API 套件 -->
pip3 install -r requirements.txt
```

3. 更新 env
更新 .env 內的資訊為個人所建立資料庫所設定的資訊

4. python test.py 做測試
```
python test.py
<!-- 執行成功後，印出 DB 資訊 -->
```

5. 依序執行
```
<!-- 建立資料表 -->
python create_table.py
python read_table.py

<!-- 新增一列 -->
python add_row.py
python read_table.py

<!-- 新增多列 -->
python add_rows.py
python read_table.py

<!-- 刪除特定條件的列 -->
python delete_row.py
python read_table.py

<!-- 更新特定條件的列 -->
python update_row.py
python read_table.py

<!-- 刪除所有列數 -->
python delete_all_rows.py
python read_table.py

```