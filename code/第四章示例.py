# 按本章顺序执行全部 Python 代码段。

records = [(4.0, 1.5), (-2.0, 1.0), (6.0, 2.0)]
total = 0.0
count = 0
for length, width in records:
    if length > 0 and width > 0:
        total += length
        count += 1
if count == 0:
    print("没有有效记录")
else:
    print(total / count)

pattern = ["红", "蓝", "蓝"]
n = 10
print(pattern[(n - 1) % len(pattern)])

codebook = {"00": "圆", "01": "三角形",
            "10": "正方形", "11": "五角星"}
encoded = "001001"
decoded = []
for start in range(0, len(encoded), 2):
    piece = encoded[start:start + 2]
    decoded.append(codebook[piece])
print(decoded)  # ['圆', '正方形', '三角形']

solutions = []
for a in range(16 // 3 + 1):
    for b in range(16 // 5 + 1):
        if 3 * a + 5 * b == 16:
            solutions.append((a, b))
print(solutions)

solutions = []
for a in range(16 // 3 + 1):
    remaining = 16 - 3 * a
    if remaining % 5 == 0:
        b = remaining // 5
        solutions.append((a, b))
print(solutions)  # [(2, 2)]

def linear_search(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

print(linear_search([8, 3, 9, 5], 9))

def binary_search(values, target):
    left = 0
    right = len(values) - 1
    while left <= right:
        middle = (left + right) // 2
        if values[middle] == target:
            return middle
        if values[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1

print(binary_search([2, 5, 8, 11, 14, 17, 20], 14))

def bubble_sort(values):
    a = values.copy()
    for end in range(len(a) - 1, 0, -1):
        changed = False
        for i in range(end):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                changed = True
        if not changed:
            break
    return a

def selection_sort(values):
    a = values.copy()
    for start in range(len(a) - 1):
        smallest = start
        for i in range(start + 1, len(a)):
            if a[i] < a[smallest]:
                smallest = i
        a[start], a[smallest] = a[smallest], a[start]
    return a

def insertion_sort(values):
    a = values.copy()
    for i in range(1, len(a)):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value
    return a

def quick_sort(values):
    if len(values) <= 1:
        return values.copy()
    pivot = values[len(values) // 2]
    smaller = [x for x in values if x < pivot]
    equal = [x for x in values if x == pivot]
    larger = [x for x in values if x > pivot]
    return quick_sort(smaller) + equal + quick_sort(larger)

experiments = [("A", 1, 3), ("B", 2, 5),
               ("C", 3, 4), ("D", 4, 6)]
ordered = sorted(experiments, key=lambda item: item[2])
chosen = []
last_end = 0
for name, start, end in ordered:
    if start >= last_end:
        chosen.append(name)
        last_end = end
print(chosen)  # ['A', 'C', 'D']

graph = {
    "S": ["A", "B"],
    "A": ["S", "C", "D"],
    "B": ["S", "D"],
    "C": ["A", "T"],
    "D": ["A", "B", "T"],
    "T": ["C", "D"]
}

from collections import deque

def bfs(graph, start):
    queue = deque([start])
    distance = {start: 0}
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in distance:
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return order, distance

order, distance = bfs(graph, "S")
print(order)
print(distance["T"])

def shortest_path(graph, start, goal):
    queue = deque([start])
    parent = {start: None}
    while queue:
        node = queue.popleft()
        if node == goal:
            break
        for neighbor in graph[node]:
            if neighbor not in parent:
                parent[neighbor] = node
                queue.append(neighbor)
    if goal not in parent:
        return []
    path = []
    node = goal
    while node is not None:
        path.append(node)
        node = parent[node]
    return path[::-1]

print(shortest_path(graph, "S", "T"))
# ['S', 'A', 'C', 'T']

def dfs(graph, start):
    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order

print(dfs(graph, "S"))

transition = {
    ("锁定", "有效票"): "放行",
    ("锁定", "推闸"): "锁定",
    ("放行", "有效票"): "放行",
    ("放行", "推闸"): "锁定"
}
state = "锁定"
for event in ["推闸", "有效票", "推闸"]:
    state = transition[(state, event)]
    print(state)

temperature = 10.0
rate = 0.5
history = [temperature]
for step in range(5):
    temperature += rate * (20 - temperature)
    history.append(temperature)
print(history)
# [10.0, 15.0, 17.5, 18.75, 19.375, 19.6875]
