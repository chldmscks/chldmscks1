구름 파이썬 2급 기출문제 문9) 위험한 지역~  

height = [[3, 6, 2, 8], [7, 3, 4, 2], [8, 6, 7, 3], [5, 3, 2, 9]]
data1 = [[9 for x in range(6)] for x in range(6)]
print(data1)

for i in range(4):
    for x in range(4):
        data1[i+1][x+1] = height[i][x]

print(data1)


for i in range(1, 5):
    for x in range(1, 5):
        if (data1[i][x] < data1[i+1][x]) and (data1[i][x] < data1[i-1][x]):



  def solution(height):
      count = 0
	for i in range(1, 5):
		for x in range(1, 5):
			if (data1[i][x] < data1[i+1][x]) and (data1[i][x] < data1[i-1][x]) and (data1[i][x] < data1[i][x+1]) and (data1[i][x] < data1[i][x-1]):
				count += 1
	return count

# The code was missing a colon (:) at the end of the if statement.

      
