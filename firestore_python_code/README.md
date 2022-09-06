# 使用前提
1. 已啟用該專案的 Firestore

# 使用流程
1. 在Cloud Shell 建立虛擬環境並安裝套件
```
<!-- 於 Cloud Shell 此專案資料夾為工作路徑，於 Terminal 執行 -->
<!-- 生成 venv 資料夾 -->
python -m venv venv
<!-- 進入 venv -->
source venv/bin/activate

<!-- 更新 pip 安裝套件 -->
python -m pip install --upgrade pip
<!-- 安裝 python sql 所需 API 套件 -->
pip3 install -r requirements.txt
```

2. 執行 test.py 進行測試
```
python test.py
<!-- 若沒報錯, 即成功 -->
```

3. 依序測試以下對 Firestore 功能的 API
```
<!-- 添加資料 -->
python add_data1.py
<!-- 添加後, 至 Firestore 查閱 -->

<!-- 再添加一筆 document -->
python add_data2.py
<!-- 添加後, 至 Firestore 查閱 -->

<!-- 添加 多筆資料 -->
python add_many_data.py
<!-- 添加後, 至 Firestore 查閱 -->

<!-- 查閱並印出資料 -->
python read_data.py

<!-- 更新資料 -->
python update_data.py

<!-- 查閱並印出資料 -->
python read_data.py

<!-- 刪除資料 -->
python delete_data.py

<!-- 查閱並印出資料 -->
python read_data.py
```

# 參考文件

https://cloud.google.com/firestore/docs/create-database-server-client-library#firestore_setup_dataset_pt2-python

https://pypi.org/project/google-cloud-firestore/