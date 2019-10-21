# 쌍별 이변량 산점도
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(color_codes=True)

# 쌍별 이변량 산점도 (Pairwise bivariate)
iris = sns.load_dataset("iris")
print(iris.head(100))
sns.pairplot(iris)
# sns.pairplot(iris, hue="species")
plt.show()
