# 按本章顺序执行全部 Python 代码段。

import numpy as np

leaves = np.array([[4.0, 1.0],
                   [6.0, 2.0],
                   [8.0, 3.0]])
print(leaves.shape)
print(leaves.ndim)
print(leaves.size)

print(leaves[:, 0].shape)
print(leaves[:, 0:1].shape)
print(leaves[leaves[:, 0] >= 6])

a = np.array([1, 2, 3])
part = a[:2]
part[0] = 9
print(a)
independent = a[:2].copy()
independent[0] = 7
print(a)

A = np.array([[2, 1, 3], [0, 4, 1]])
w = np.array([1, 2, 1])
print(A * w)
print(A @ w)

true_values = np.array([10.0, 10.0, 10.0])
predictions = np.array([8.0, 11.0, 12.0])
errors = predictions - true_values
mae = np.mean(np.abs(errors))
mse = np.mean(errors ** 2)
print(round(mae, 4), round(mse, 4))

offsets = np.array([1.0, 0.5])
corrected = leaves - offsets
print(corrected)

row_offsets = np.array([[10.0], [20.0], [30.0]])
print(leaves + row_offsets)

numbers = np.arange(1, 7).reshape(3, 2)
print(numbers.reshape(2, 3))
print(numbers.T)

import pandas as pd

df = pd.DataFrame({
    "id": ["A", "B", "C", "C"],
    "length": [4.0, None, 8.0, 8.0],
    "width": [1.0, 2.0, 3.0, 3.0],
    "kind": ["甲", "乙", "甲", "甲"]
})
print(df.shape)
print(df.head(2))

from io import StringIO

csv_text = "id,length,width\nA,4.0,1.0\nB,6.0,2.0\n"
small_table = pd.read_csv(StringIO(csv_text))
print(small_table["length"].mean())

clean = df.drop_duplicates().copy()
print(clean["length"].isna().sum())
mean_length = clean["length"].mean()
clean["length"] = clean["length"].fillna(mean_length)
selected = clean.loc[clean["length"] >= 6,
                     ["id", "length", "width"]]
print(selected)

temperatures = pd.Series([18.0, None, 22.0])
print(temperatures.interpolate().tolist())
print(clean.groupby("kind")["length"].mean())

places = pd.DataFrame({
    "id": ["A", "B"],
    "place": ["温室", "室外"]
})
joined = clean.merge(places, on="id", how="left",
                     validate="one_to_one")
print(joined[["id", "place"]])

new_row = pd.DataFrame({
    "id": ["D"], "length": [5.0],
    "width": [1.5], "kind": ["乙"]
})
combined = pd.concat([clean, new_row], ignore_index=True)
encoded = pd.get_dummies(combined, columns=["kind"],
                         dtype=int)
print(encoded.columns.tolist())

print(selected.iloc[0]["id"])
print(selected.loc[1, "id"])
renumbered = selected.reset_index(drop=True)
print(renumbered.index.tolist())

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter([4, 6, 8], [1, 2, 3], color="#376d84")
ax.set_xlabel("Length / cm")
ax.set_ylabel("Width / cm")
ax.set_title("Leaf measurements")
fig.tight_layout()
fig.savefig("leaf_scatter.png", dpi=160)
plt.show()

fig, ax = plt.subplots(figsize=(6, 4))
days = [1, 2, 3, 4]
ax.plot(days, [20, 35, 30, 50], marker="o",
        color="#376d84", label="Device A")
ax.plot(days, [18, 24, 36, 42], marker="s",
        linestyle="--", color="#73958c", label="Device B")
ax.set_xlabel("Day")
ax.set_ylabel("Processed images")
ax.set_xticks(days)
ax.set_ylim(0, 60)
ax.legend()
fig.tight_layout()
fig.savefig("device_lines.png", dpi=160)
plt.show()

names = ["Plants", "Animals", "Objects"]
counts = [40, 35, 25]
colors = ["#376d84", "#73958c", "#b5a98f"]
fig, axes = plt.subplots(1, 2, figsize=(9, 4))
axes[0].bar(names, counts, color=colors)
axes[0].set_ylabel("Image count")
axes[0].set_ylim(0, 50)
axes[1].pie(counts, labels=names, colors=colors,
            autopct="%.0f%%", startangle=90)
axes[1].set_aspect("equal")
fig.tight_layout()
fig.savefig("category_charts.png", dpi=160)
plt.show()

sample_ids = np.array([1, 2, 3])
observed = np.array([2, 4, 6])
predicted = np.array([3, 4, 4])
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(sample_ids, observed,
           marker="o", label="Observed")
ax.scatter(sample_ids, predicted,
           marker="x", label="Predicted")
ax.vlines(sample_ids, observed, predicted,
          color="gray", linestyle="--")
ax.set_xticks(sample_ids)
ax.set_xlabel("Sample")
ax.set_ylabel("Value")
ax.set_ylim(0, 7)
ax.legend()
fig.tight_layout()
fig.savefig("prediction_errors.png", dpi=160)
plt.show()

from sklearn.linear_model import LinearRegression

X_small = np.array([[1.0], [2.0], [3.0]])
y_small = np.array([2.0, 4.0, 6.0])
regressor = LinearRegression()
regressor.fit(X_small, y_small)
print(regressor.coef_)
print(regressor.intercept_)
print(regressor.predict([[4.0]]))

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

polynomial_model = make_pipeline(
    PolynomialFeatures(degree=2, include_bias=False),
    LinearRegression()
)
polynomial_model.fit(
    [[1.0], [2.0], [3.0]], [2.0, 5.0, 10.0]
)
print(polynomial_model.predict([[4.0]]))

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
train_column = np.array([[10.0], [20.0], [30.0]])
scaled_train = scaler.fit_transform(train_column)
scaled_new = scaler.transform([[40.0]])
print(np.round(scaled_train.ravel(), 3))
print(np.round(scaled_new.ravel(), 3))
print(scaler.mean_)

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X = iris.data
y = iris.target
(X_train, X_remaining,
 y_train, y_remaining) = train_test_split(
    X, y, test_size=0.4, random_state=7, stratify=y
)
X_valid, X_test, y_valid, y_test = train_test_split(
    X_remaining, y_remaining, test_size=0.5,
    random_state=7, stratify=y_remaining
)
print(X_train.shape, X_valid.shape, X_test.shape)

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

candidates = {
    "KNN_3": KNeighborsClassifier(n_neighbors=3),
    "KNN_7": KNeighborsClassifier(n_neighbors=7),
    "Tree_3": DecisionTreeClassifier(
        max_depth=3, random_state=7
    )
}
best_model = None
best_score = -1.0
best_name = ""

for name, classifier in candidates.items():
    model = make_pipeline(
        SimpleImputer(strategy="mean"),
        StandardScaler(),
        classifier
    )
    model.fit(X_train, y_train)
    valid_prediction = model.predict(X_valid)
    score = accuracy_score(y_valid, valid_prediction)
    print(name, round(score, 3))
    if score > best_score:
        best_score = score
        best_model = model
        best_name = name

test_prediction = best_model.predict(X_test)
print("Selected:", best_name)
print("Test accuracy:",
      round(accuracy_score(y_test, test_prediction), 3))
print(confusion_matrix(y_test, test_prediction,
                       labels=[0, 1, 2]))

new_measurement = np.array([[5.1, 3.5, 1.4, 0.2]])
new_label = best_model.predict(new_measurement)[0]
print(int(new_label), iris.target_names[new_label])

wrong_positions = np.flatnonzero(y_test != test_prediction)
for position in wrong_positions:
    actual_name = iris.target_names[y_test[position]]
    predicted_label = test_prediction[position]
    predicted_name = iris.target_names[predicted_label]
    print(int(position), actual_name, predicted_name)

from sklearn.neural_network import MLPClassifier

mlp = make_pipeline(
    StandardScaler(),
    MLPClassifier(hidden_layer_sizes=(8,), solver="lbfgs",
                  alpha=0.01, max_iter=2000, random_state=7)
)
mlp.fit(X_train, y_train)
mlp_prediction = mlp.predict(X_valid)
print(round(accuracy_score(y_valid, mlp_prediction), 3))

from sklearn.cluster import KMeans

cluster_model = KMeans(
    n_clusters=2, n_init=10, random_state=7
)
cluster_ids = cluster_model.fit_predict([[1.0], [2.0],
                                        [8.0], [9.0]])
print(cluster_ids)
print(cluster_model.cluster_centers_)

import jieba

words = jieba.lcut("我喜欢学习人工智能")
print(words)
