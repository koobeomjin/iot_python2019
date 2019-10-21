import pandas as pd
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split

# 붓꽃의 CSV 데이터 읽어들이기 --- (※1)
csv = pd.read_csv('preprocessed_data.csv')
# 필요한 열 추출하기 --- (※2)
csv_data = csv[csv.columns.difference(['Winner'])]
csv_label = csv["Winner"]
# 학습 전용 데이터와 테스트 전용 데이터로 나누기 --- (※3)
train_data, test_data, train_label, test_label = train_test_split(csv_data, csv_label)
# 데이터 학습시키고 예측하기 --- (※4)
clf = svm.SVC()
clf.fit(train_data, train_label)
pre = clf.predict(test_data)
# 정답률 구하기 --- (※5)
ac_score = metrics.accuracy_score(test_label, pre)
count = metrics.accuracy_score(test_label, pre, normalize=False)
print("전체 데이터 수: %d"%len(csv_data))
print("학습 전용 데이터 수: %d"%len(train_data))
print("테스트 데이터 수: %d"%len(test_data))
print(f"정답률 : {ac_score *100} %")