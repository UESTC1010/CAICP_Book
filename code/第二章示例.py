# 按本章顺序执行全部 Python 代码段。

print("开始处理数据")
print(2 + 3)

width = 28
height = 28
pixel_count = width * height
print(pixel_count)  # 784

sample_count = 80
old_count = sample_count
sample_count = sample_count + 5
print(sample_count, old_count)  # 85 80

print(25 + 5)        # 30
print("25" + "5")    # 255
print(25 > 20)       # True

text = input()
count = int(text)
print("样本数", count, sep="：")

age = 12
allowed = age >= 10 and age <= 15
print(allowed)      # True
print(not allowed)  # False

battery = 15
if battery == 0:
    status = "停止"
elif battery < 20:
    status = "准备充电"
else:
    status = "继续运行"
print(status)  # 准备充电

values = [18, 20, 25]
total = 0
for value in values:
    total = total + value
print(total)  # 63

total = 0
n = 1
while n <= 3:
    total += n
    n += 1
print(total, n)  # 6 4

values = [3, -1, 5]
total = 0
for value in values:
    if value < 0:
        continue
    total += value
print(total)  # 8

values = [4, 7, 10]
index = 0
while index < len(values):
    if values[index] == 7:
        print(index)  # 1
        break
    index += 1
else:
    print("未找到")

word = "Python"
print(word[0], word[-1])  # P n
print(word[1:4])          # yth
print(word[:3])           # Pyt
print(word[::2])          # Pto
print(word[::-1])         # nohtyP

line = "  A17,23.5,正常  "
cleaned = line.strip()
parts = cleaned.split(",")
name = parts[0]
temperature = float(parts[1])
print(name, temperature, parts[2])  # A17 23.5 正常
print(" / ".join(parts))           # A17 / 23.5 / 正常

name = "A17"
temperature = 23.5
print(f"编号：{name}")
print(f"温度：{temperature:.1f}℃")

data = [3, 1]
data.append(4)
data.extend([1, 5])
print(data)              # [3, 1, 4, 1, 5]
ordered = sorted(data)
print(ordered)           # [1, 1, 3, 4, 5]
print(data)              # [3, 1, 4, 1, 5]
data.sort(reverse=True)
print(data)              # [5, 4, 3, 1, 1]

grid = [[2, 4, 6], [1, 3, 5]]
print(grid[1][2])  # 5
grid[0][1] = 8
for row in grid:
    row_total = 0
    for value in row:
        row_total += value
    print(row_total)  # 依次输出 16 和 9

a = [2, 4, 6]
b = a
c = a.copy()
b[0] = 9
print(a)  # [9, 4, 6]
print(c)  # [2, 4, 6]

rows = []
for _ in range(3):
    rows.append([0, 0])
rows[0][0] = 1
print(rows)  # [[1, 0], [0, 0], [0, 0]]

leaves = [[4.0, 1.0], [6.0, 2.0], [8.0, 3.0]]
lengths = []
for row in leaves:
    lengths.append(row[0])
average = sum(lengths) / len(lengths)
print(lengths)  # [4.0, 6.0, 8.0]
print(average)  # 6.0

record = {"编号": "A17", "温度": 23.5}
print(record["编号"])  # A17
record["温度"] = 24.0
record["状态"] = "正常"
print(record["温度"])  # 24.0

labels = ["猫", "狗", "猫"]
counts = {}
for label in labels:
    counts[label] = counts.get(label, 0) + 1
for label, count in counts.items():
    print(label, count)  # 依次输出 猫 2 和 狗 1

def mean(values):
    return sum(values) / len(values)

result = mean([18, 20, 25])
print(result)  # 21.0

def announce():
    print("处理完成")

announce()

def show_total(values):
    print(sum(values))

result = show_total([2, 3])
print(result)

def shift(value, offset=1):
    return value + offset

print(shift(5))            # 6
print(shift(5, 3))         # 8
print(shift(5, offset=3))   # 8

def add_zero(values):
    values.append(0)

data = [3, 5]
add_zero(data)
print(data)  # [3, 5, 0]

print(bin(26))       # 0b11010
print(hex(26))       # 0x1a
print(int("11010", 2))  # 26
print(int("1A", 16))    # 26
print(format(26, "b"))  # 11010

def total_to(n):
    if n == 0:
        return 0
    return n + total_to(n - 1)

print(total_to(3))  # 6

import math

print(math.sqrt(25))   # 5.0
print(math.floor(2.8)) # 2
print(math.ceil(2.2))  # 3

import random

rng = random.Random(7)
print(rng.randint(1, 6))        # 1 到 6 之间的整数，含两端
print(rng.choice(["甲", "乙", "丙"]))  # 从三项中选一项
print(rng.sample([1, 2, 3, 4], 2))   # 抽取两个不同位置

import os

print(os.getcwd())
path = os.path.join("data", "records.txt")
print(os.path.isfile(path))

import os

path = os.path.join("data", "records.txt")
with open(path, encoding="utf-8") as file:
    text = file.read()
print(text)

text = "3.5"
try:
    count = int(text)
except ValueError:
    print("这段文字不能直接转换为整数")

def read_record(line):
    fields = line.split(",")
    code = fields[0].strip()
    length = float(fields[1])
    width = float(fields[2])
    return code, length, width

lines = ["A,4.0,1.0", "B,-2.0,1.5", "C,8.0,3.0"]
total = 0.0
count = 0
for line in lines:
    code, length, width = read_record(line)
    if length > 0 and width > 0:
        total += length
        count += 1
if count > 0:
    print(total / count)  # 6.0
else:
    print("没有有效记录")

values = [-2, 0, 3, 5, -1]
doubled = []
for x in values:
    if x > 0:
        doubled.append(x * 2)
print(doubled)  # [6, 10]

values = [-2, 0, 3, 5, -1]
doubled = [x * 2 for x in values if x > 0]
print(doubled)  # [6, 10]

def double(x):
    return x * 2

result = list(map(double, [3, 5]))
print(result)  # [6, 10]

values = [-2, 0, 3, 5]
positive = filter(lambda x: x > 0, values)
result = list(map(lambda x: x * 2, positive))
print(result)  # [6, 10]

from functools import reduce

names = ["A", "", "B", "A", "C"]
result = reduce(
    lambda kept, x: (
        kept + [x] if x and x not in kept else kept
    ),
    names,
    []
)
print(result)  # ['A', 'B', 'C']

class Device:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery

    def run(self, cost):
        if cost < 0 or cost > self.battery:
            return False
        self.battery -= cost
        return True

first = Device("A", 10)
second = Device("B", 10)
print(first.run(6))      # True
print(first.run(5))      # False
print(first.battery)     # 4
print(second.battery)    # 10

class Box:
    items = []

a = Box()
b = Box()
a.items.append("红")
print(b.items)  # ['红']
a.items = ["蓝"]
print(a.items)  # ['蓝']
print(b.items)  # ['红']
