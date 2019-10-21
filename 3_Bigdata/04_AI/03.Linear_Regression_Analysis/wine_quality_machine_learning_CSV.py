import pandas as pd
import operator
from sklearn import metrics, svm
from itertools import combinations

print("결과 예측하기")
wine = pd.read_csv('white_winequality.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

match_dic = {}

columns_list = ['alcohol','chlorides', 'citric_acid', 'density', 'fixed_acidity',
                'free_sulfur_dioxide', 'pH', 'residual_sugar', 'sulphates',
                'total_sulfur_dioxide', 'volatile_acidity']
label = wine['quality']

# 최적의 독립변수 식별
for num in range(7,12):
    combi_list = list(combinations(columns_list, num))
    for tup in combi_list:
        # 종속 변수 식별
        data_header_list = list(tup)
        clf = svm.SVC()
        clf.fit(wine[data_header_list], label)
        pre = clf.predict(wine[data_header_list])
        accuracy = metrics.accuracy_score(label, pre)
        # scores =
        # model_selection.cross_val_score(clf, wine[data_header_list], label, cv=5)
        # accuracy = scores.mean()
        data_header_name = ' '.join(data_header_list)
        match_dic[data_header_name] = accuracy*100
        print(f'\n데이터 행 조합: {data_header_name}')
        print(f'>> C:\Python_Workspace\3_Bigdata\04_AI\01.Machine_Learning 정답률: {accuracy*100} %%')

# 정답률 최대값 찾기
match_dic = sorted(match_dic.items(), key = operator.itemgetter(1), reverse=True)

print("\n\n 독립변수 최적화 분석 결과")
print("총 조합 갯수: %d" %len(match_dic))
print("MAX 조합: %s >> %.2f %%"%(match_dic[0][0], match_dic[0][1]))