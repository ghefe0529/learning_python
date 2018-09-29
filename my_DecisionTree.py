# 决策树
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
iris = load_iris()
data = iris.data
target = iris.target
print(iris.feature_names)
print(iris.target_names)
print(data[:10])
print(data.shape)
print(target[:10])
tree_clf = DecisionTreeClassifier()
tree_clf.fit(data,target)

from sklearn.tree import export_graphviz
eg = export_graphviz(tree_clf,out_file='iris_tree1.dot',
                    feature_names=iris.feature_names,
                    class_names=iris.target_names,
                    rounded=True,
                    filled=True)

#dot -Tpng iris_tree.dot -o iris_tree.png