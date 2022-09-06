from google.cloud import firestore

# 建立客戶端物件
db = firestore.Client() 

# 使用客戶端物件, 建立索引
doc_ref = db.collection(u'users').document(u'0')

# set 與 update 的差別
# 若 資料存在, 則不管是 set 或 update 都會更新資料
# 若 資料不存在，則 set 會建立資料, update 則會報錯

# 基於此索引, 用 set 方法添加資料至資料庫
doc_ref.set({
    'name': 'Ada',
    'height': 175,
    'date_of_birth': '1995-06-05',
    'gender': 'female',
    'cell-phone': '09123456789',
    'address': '台北市中山區中山路1號',
    'job_position': 'Data Engineer'
})