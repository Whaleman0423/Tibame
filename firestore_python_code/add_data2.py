from google.cloud import firestore

# 建立客戶端物件
db = firestore.Client() 

# 使用客戶端物件, 建立索引
doc_ref = db.collection(u'users').document(u'1')

# 基於此索引, 用 set 方法添加資料至資料庫
doc_ref.set({
    '名字': '小白',
    '身高': 165,
    '生日': '1999-04-25',
    '性別': '男性',
    '手機號碼': '09987654321',
    '住址': '台北市松山區龜山路10號',
    '職稱': 'AI Engineer'
})