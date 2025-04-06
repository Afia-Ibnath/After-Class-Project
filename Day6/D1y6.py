from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
import warnings
from sklearn.exceptions import ConvergenceWarning



digits = load_digits()
x = digits.data / 16.0 
y = digits.target

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(xtrain, ytrain)

ypred = model.predict(xtest)
accuracy = metrics.accuracy_score(ytest, ypred)
print(f"Test Accuracy: {accuracy:.2%}")

for i in range(5):
    plt.imshow(xtest[i].reshape(8, 8), cmap=plt.cm.binary)
    plt.title(f"Predicted: {ypred[i]}, Actual: {ytest[i]}")
    plt.axis('off')
    plt.show()
