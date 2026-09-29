# 按本章顺序执行全部 Python 代码段。

samples = [(1.0, 2.0), (2.0, 3.0), (3.0, 7.0)]
def line_loss(w, b):
    total = 0.0
    for x, y in samples:
        prediction = w * x + b
        total += (prediction - y) ** 2
    return total / len(samples)

print(line_loss(2.5, -1.0))  # 0.5
print(round(line_loss(2.0, 0.0), 4))  # 0.6667

training = [(3.2, 3.0, "乙"), (2.0, 3.0, "甲"),
            (3.0, 2.0, "甲"), (1.0, 1.0, "甲"),
            (5.0, 5.0, "乙")]
def neighbor_vote(point, k):
    distances = []
    for x1, x2, label in training:
        d2 = (point[0] - x1) ** 2
        d2 += (point[1] - x2) ** 2
        distances.append((d2, label))
    distances.sort(key=lambda item: item[0])
    counts = {}
    for d2, label in distances[:k]:
        counts[label] = counts.get(label, 0) + 1
    return max(counts, key=counts.get)

print(neighbor_vote((3.0, 3.0), 1))  # 乙
print(neighbor_vote((3.0, 3.0), 3))  # 甲

points = [1.0, 2.0, 3.0, 8.0, 9.0]
centers = [1.0, 4.0]
for iteration in range(10):
    groups = [[], []]
    for value in points:
        label = min(range(2),
                    key=lambda j: (value - centers[j]) ** 2)
        groups[label].append(value)
    updated = []
    for j in range(2):
        if groups[j]:
            updated.append(sum(groups[j]) / len(groups[j]))
        else:
            updated.append(centers[j])
    if updated == centers:
        break
    centers = updated
print(groups)   # [[1.0, 2.0, 3.0], [8.0, 9.0]]
print(centers)  # [2.0, 8.5]

candidates = [i / 20 for i in range(21)]
def likelihood(p):
    return p ** 3 * (1 - p)
best = max(candidates, key=likelihood)
print(best)  # 0.75

import math
for z in [-2.0, 0.0, 2.0]:
    sigmoid = 1 / (1 + math.exp(-z))
    relu = max(0.0, z)
    print(z, round(sigmoid, 3), relu)
# -2.0 0.119 0.0
#  0.0 0.500 0.0
#  2.0 0.881 2.0

def network(x1, x2):
    h1 = max(0, x1 + x2 - 1)
    h2 = max(0, x1 - x2)
    score = h1 - 2 * h2
    return int(score >= 0.5)

print(network(2, 1))
print(network(1, 2))

def xor_network(x1, x2):
    h1 = max(0, x1 - x2)
    h2 = max(0, x2 - x1)
    return int(h1 + h2 >= 0.5)

for point in [(0, 0), (1, 0), (0, 1), (1, 1)]:
    print(point, xor_network(*point))

w = 0.0
learning_rate = 0.1
for step in range(3):
    gradient = 2 * (w - 2)
    w = w - learning_rate * gradient
    loss = (w - 2) ** 2
    print(round(w, 4), round(loss, 4))

def function_value(x):
    return (2 * x + 1) ** 2

x = 1.0
for h in [0.1, 0.01, 0.001]:
    rate = (function_value(x + h) - function_value(x)) / h
    print(round(rate, 3))
# 12.4
# 12.04
# 12.004

samples = [(1.0, 2.0), (2.0, 4.0)]
w, b = 0.0, 0.0
rate = 0.1
for step in range(3):
    grad_w, grad_b = 0.0, 0.0
    for x, y in samples:
        error = w * x + b - y
        grad_w += 2 * error * x / len(samples)
        grad_b += 2 * error / len(samples)
    w -= rate * grad_w
    b -= rate * grad_b
    loss = sum((w * x + b - y) ** 2
               for x, y in samples) / len(samples)
    print(round(w, 4), round(b, 4), round(loss, 6))
# 1.0 0.6 1.06
# 1.32 0.78 0.1732
# 1.426 0.828 0.083458

feature = [[1, 3, 2, 0], [2, 0, 1, 4],
           [0, 1, 5, 2], [3, 2, 1, 0]]
pooled = []
for row in range(0, 4, 2):
    output_row = []
    for col in range(0, 4, 2):
        window = [feature[row][col],
                  feature[row][col + 1],
                  feature[row + 1][col],
                  feature[row + 1][col + 1]]
        output_row.append(max(window))
    pooled.append(output_row)
print(pooled)  # [[3, 4], [3, 5]]
