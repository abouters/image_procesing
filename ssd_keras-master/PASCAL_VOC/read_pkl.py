
# pklファイルの中を見るためのプログラム

import pickle
f = open('VOC20XX.pkl', 'rb')
data = pickle.load(f)
print(data.keys())
#############################################
# dict_keys(['000005.jpg', ..., '006739.jpg', ...]) ...
# みたいな感じで画像名のリストが表示されます。
#############################################

print(data['007571.jpg'])