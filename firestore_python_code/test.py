from google.cloud import firestore

# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.

# 建立客戶端物件
# db = firestore.Client(project='my-project-id')
db = firestore.Client() # Cloud Shell 環境上有當前預設的 project 環境變數, 因此可以不用設定

print(db)