# 按本章顺序执行全部 Python 代码段。

import numpy as np

query = np.array([1.0, 0.0])
keys = np.array([[2.0, 0.0], [0.0, 2.0]])
values = np.array([[2.0, 0.0], [0.0, 4.0]])
scores = keys @ query / np.sqrt(keys.shape[1])
exp_scores = np.exp(scores - scores.max())
weights = exp_scores / exp_scores.sum()
output = weights @ values
print(np.round(weights, 3))
print(np.round(output, 3))
