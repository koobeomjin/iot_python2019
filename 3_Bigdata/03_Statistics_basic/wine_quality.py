import pandas as pd

wine = pd.read_csv('winequality-both.csv', sep=',',header=0)
wine.columns = wine.columns.str.replace(' ','_')

print(wine.head(10))

print('변수별 요약통계')
print(wine.describe())

print('\n특정 열의 유일값 찾기')
print(sorted(wine.quality.unique))

print('\n빈도 찾기')
print(wine.quality.value_counts())