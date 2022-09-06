from google.cloud import firestore

# 建立客戶端物件
db = firestore.Client() 

# 建立 索引, 文件名為 2 的索引
doc_ref = db.collection(u'users').document(u'2')

# 基於索引, 將資料集為 users 且 檔案為 2 的資料做刪除
doc_ref.delete()



