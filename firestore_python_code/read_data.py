from google.cloud import firestore

# 建立客戶端物件
db = firestore.Client() 

# 建立 資料集 索引
users_ref = db.collection(u'users')
# 基於索引, 取出所有此資料集的 document 及他們的欄位
docs = users_ref.stream()

# 迴圈所有此資料集的檔案資料
for doc in docs:
    print(f'{doc.id} => {doc.to_dict()}')