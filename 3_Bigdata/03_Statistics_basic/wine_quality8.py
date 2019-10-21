# 목적: 종속변수값 예측하기
# 경고 뜨는 건 ix 때문. 프로그램 수행과는 무관.

import pandas as pd
from statsmodels.formula.api import ols, glm

print("7.2.7 예측하기")
wine = pd.read_csv('winequality-both.csv', sep=',', header=0)
wine.columns = wine.columns.str.replace(' ', '_')

my_formula = 'quality ~ alcohol + chlorides + citric_acid + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
# my_formula = 'quality ~ alcohol + chlorides + density + fixed_acidity + free_sulfur_dioxide + pH + residual_sugar + sulphates + total_sulfur_dioxide + volatile_acidity'
lm = ols(my_formula, data=wine).fit()

dependent_variable = wine['quality']
independent_variables = wine[wine.columns.difference(['quality','type'])]

new_observations = wine.ix[:, independent_variables.columns]
y_predicted = lm.predict(new_observations)
y_predicted_rounded = [round(score) for score in y_predicted]

total_count = 0
index = 0
total_number = len(y_predicted_rounded)
total_correct = 0
while index < total_number:
    print(f'{index+1}   |{y_predicted_rounded[index]}|{dependent_variable[index]}')
    if y_predicted_rounded[index] == dependent_variable[index]:
        total_correct += 1
    index += 1

print(f"\n전체 관찰 계수: {total_number}")
print(f"정답수: {total_correct}")
print(f'정답률: {(total_correct/total_number)*100} %')