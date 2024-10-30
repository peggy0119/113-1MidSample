# 創建 10x10 的 map 陣列，並初始化所有元素為 0
map = [[0 for _ in range(10)] for _ in range(10)]

# 定義 rowMap 並賦值
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# 在 map 中根據 rowMap 記錄的索引值標記炸彈
for index in rowMap:
    row = index // 10
    col = index % 10
    map[row][col] = '*'

# 定義方向向量，代表八個方向
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# 更新炸彈旁的數字
for row in range(10):
    for col in range(10):
        if map[row][col] != '*':
            count = 0
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < 10 and 0 <= c < 10 and map[r][c] == '*':
                    count += 1
            map[row][col] = '' if count == 0 else count

# 畫出 map 陣列
for row in map:
    print(" ".join(str(cell) for cell in row))

