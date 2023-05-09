- 👋 Hi, I'm currently making breaking and healing my code.
- 👀 I’m interested in ML and Cyber Security.
- 🌱 I’m currently learning ML and Datascience.
- 💞️ I’m looking to collaborate on ...
- 📫 How to reach me [Twitter](www.twitter.com/@Mr___CS)

<!---
Charles-Shaju/Charles-Shaju is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
Aim :
Develop a program for plotting cross validated predictions. Algorithm :
1. Import datasets and linear_model from sklearn. 2. Import cross_val_predict from sklearn.model_selection. 3. Import matplotlib.pyplot. 4. Initialize lr as linear regression parameter. 5. Load diabetes dataset to the variable x and y. 6. Predict the cross validation for the variable x and y. 7. Design the plot using plt.figure(). 8. Use plt.show() to display the figure. Program Code :
From sklearn import datasets
model_selection import cross_val_predict
import linear_model
import matplotlib.pyplot as plt
lr = linear_model.LinearRegression()
X, y = datasets.load_diabetes(return_X_y=True)
predicted = cross_val_predict(lr, X, y, cv=10)
fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show


Aim:
Develop a program to implement The Digit Dataset. Algorithm:
1. Import matplotlib.pyplot. 2. Import datasets from sklearn. 3. Load digits dataset. 4. Design the plot using plt.figure(). 5. Use plt.imshow() to display digit dataset in the form of image and set the interpolation as
nearest. 6. Use plt.show() to display the figure. Program Code:
from sklearn import datasets
import matplotlib.pyplot as plt
digits = datasets.load_digits()
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()



Develop a program to implement the decision tree regression. Algorithm:
1. Import numpy and matplotlib.pyplot. 2. Import DecisionTreeRegressor from sklearn.tree. 3. Create a random dataset using np.random.RandomState() and pass x and y parameters. 4. Create a split node with maximum depth of 2 using DecisionTreeRegressor() and fit the
model as regr_1.fit(). 5. Create a split node with maximum depth of 5 using DecisionTreeRegressor() and fit the
model as regr_2.fit(). 6. Now predict x and y values using regr_1.predict() and regr_2.predict(). 7. Design the plot using plt.figure() and create a scatter plot using plt.scatter() with the title
‘Decision Tree Regression’ using plt.title(). 8. Plot the results of regr_1 and regr_2 using plt.plot() and set legends for both using
plt.legend(). 9. Set labels using xlabel() and ylabel(). 10. Use plt.show() to display the figure. Program Code:
import numpy as np
from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
rng = np.random.RandomState(1)
X = np.sort(5 * rng.rand(80, 1), axis=0)
y = np.sin(X).ravel()
y[::5] += 3 * (0.5 - rng.rand(16))
regr_1 = DecisionTreeRegressor(max_depth=2)
regr_2 = DecisionTreeRegressor(max_depth=5)
regr_1.fit(X, y)
regr_2.fit(X, y)
X_test = np.arange(0.0, 5.0, 0.01)[:, np.newaxis]
y_1 = regr_1.predict(X_test)
y_2 = regr_2.predict(X_test)
plt.figure()
plt.scatter(X, y, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_1, color="cornflowerblue",label="max_depth=2", linewidth=2)
plt.plot(X_test, y_2, color="yellowgreen", label="max_depth=5", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Decision Tree Regression")




Aim:
Develop a program to plot validation curves. Algorithm:
1. Import numpy and matplotlib.pyplot. 2. Import load_digits from sklearn.datasets. 3. Import svc from sklearn.svm. 4. Import validation_curve from sklearn.model_selection. 5. Set the parameters x and y for digit dataset and specify parameter range using np.logspace(). 6. Determine training and test scores for varying parameter values using validation_curve(svc()
by specifying parameter name as gamma. 7. Compute the mean and standard deviation of training and test scores using np.mean() and
np.std(). 8. Plot the graph and set the title as ‘Validation Curve with SVM’ using plt.title() and set
legend using plt.legend(). 9. Set labels for x-axis and y-axis using xlabel() and ylabel(). 10. Set the limit for y-axis using ylim() and for x-axis use plt.semilogx() to convert it into
log format. 11. Use plt.fill_between() to fill the areas between test and training scores. 12. Use plt.show() to display the figure. Program Code:
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
X, y = load_digits(return_X_y=True)
param_range = np.logspace(-6, -1, 5)
train_scores, test_scores = validation_curve(SVC(), X, y, param_name="gamma", param_range=param_range, scoring="accuracy", n_jobs=1)
train_scores_mean = np.mean(train_scores, axis=1)
train_scores_std = np.std(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
test_scores_std = np.std(test_scores, axis=1)
plt.title("Validation Curve with SVM")
plt.xlabel(r"$\gamma$")
plt.ylabel("Score")
plt.ylim(0.0, 1.1)
lw = 2
plt.semilogx(param_range, train_scores_mean, label="Training score",

color="darkorange", lw=lw)
plt.fill_between(param_range, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std, alpha=0.2, color="darkorange", lw=lw)
plt.semilogx(param_range, test_scores_mean, label="Cross-validation score", color="navy", lw=lw)
plt.fill_between(param_range, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std, alpha=0.2, color="navy", lw=lw)
plt.legend(loc="best")
plt.show()

Aim:
Develop a program to implement isolation forest example. Algorithm:
1. Import numpy and matplotlib.pyplot. 2. Import IsolationForest from sklearn.ensemble. 3. Generate a random set of numbers using np.random.RandomState. 4. Generate training data using X = 0.3 * rng.randn(100, 2) and concatenate it along the first
and last two axes using np.r_(). 5. Generate regular novel observations which is the test dataset using
X = 0.3 * rng.randn(20, 2) and concatenate it along the first and last two axes using np.r_(). 6. Generate some abnormal novel observations that are outiers from rng.uniform(). 7. Fit the model for returning anomaly score using IsolationForest(). 8. Predict the scores for training set,test set and outlier using clf.predict(). 9. Create a rectangular grid to plot the data using np.meshgrid() and plot the samples and
nearest vectors to the plane using clf.decision_function(). 10. Create a scatter plot using plt.scatter() and specify the parameters. 11. Use plt.contourf() to create a filled 3-D surface in a 2-D array. 12. Set a tight layout for the plot using plt.axis() and set limits for both x-axis and y-axis. 13. Provide legends and title using plt.legend(0 and plt.title(). 14. Use plt.show() to display the figure. Program Code:
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest
rng = np.random.RandomState(42)
X = 0.3 * rng.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X = 0.3 * rng.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
X_outliers = rng.uniform(low=-4, high=4, size=(20, 2))
clf = IsolationForest(max_samples=100, random_state=rng)
clf.fit(X_train)
y_pred_train = clf.predict(X_train)
y_pred_test = clf.predict(X_test)
y_pred_outliers = clf.predict(X_outliers)
xx, yy = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.title("IsolationForest")
plt.contourf(xx, yy, Z, cmap=plt.cm.Blues_r)
b1 = plt.scatter(X_train[:, 0], X_train[:, 1], c='white', s=20, edgecolor='k')
b2 = plt.scatter(X_test[:, 0], X_test[:, 1], c='green',s=20, edgecolor='k')
c = plt.scatter(X_outliers[:, 0], X_outliers[:, 1], c='red', s=20, edgecolor='k')
plt.axis('tight')
plt.xlim((-5, 5))
plt.ylim((-5, 5))
plt.legend([b1, b2, c], ["training observations", "new regular observations", "new
abnormal observations"], loc="upper left")
plt.show(
