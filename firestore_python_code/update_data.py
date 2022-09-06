from google.cloud import firestore

# 建立客戶端物件
db = firestore.Client() 

# 建立 索引, 文件名為 2 的索引
doc_ref = db.collection(u'users').document(u'2')

# 基於索引, 將資料集為 users 且 檔案為 2 的資料做更新
doc_ref.update({
    '興趣': '偷看女生洗澡',
    '名字': '色龜',
    '愛好': '睡覺',
    '是否已婚': True,
})

# # 若沒有該索引, 則會報錯
# # 建立 索引, 文件名為 10 的索引
# doc_ref = db.collection(u'users').document(u'10')

# # 基於索引, 將資料集為 users 且 檔案為 10 的資料做更新
# doc_ref.update({
#     '興趣': '偷看女生洗澡',
#     '名字': '色龜',
#     '愛好': '睡覺',
#     '是否已婚': True,
# })

