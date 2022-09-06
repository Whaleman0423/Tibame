"""
此 py 用來快速建立5筆假資料至 firestore 資料庫
"""
from google.cloud import firestore

# 建立客戶端物件
db = firestore.Client() 

# 假資料
users = {
    "2": {
        "名字": "小黃",
        "姓氏": "黃",
        "興趣": "唱歌"
    },
    "3": {
        "名字": "麥可",
        "愛好": "爬山",
        "惡習": "偷看女生"
    },
    "4": {
        "Name": "Coco",
        "身家": "上億",
        "年紀": 17,
        "平均成績": 86.5
    },
    "5": {
        "姓名": "王小紅",
        "性別": "女性",
        "最喜歡的食物": "紅豆餅",
        "最討厭的食物": "苦瓜"
    }, 
    "6": {
        "full_name": "王子病",
        "惡習":"找媽咪"
    }
}

# 迴圈假資料
for user in users.keys():
    # 使用客戶端物件, 建立索引
    doc_ref = db.collection(u'users').document(user)

    # 基於此索引, 用 set 方法添加資料至資料庫
    doc_ref.set(users[user])