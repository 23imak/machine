from sklearn import tree
#classifying apples and oranges using features includng weigth(1) and texture(0)
features  = [[140,1],[130,1],[150,0],[170,0]]
lables = [0,0,1,1] #1 for orange , 0 for apple
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,lables)
print clf.predict([[150,0]])