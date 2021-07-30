x = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
b = []
n = len(x[0])
for i in range(len(x)):
  b.append([0]*n)  
  for j in range(n):
    b[i][n - 1 - j] = x[i][j]
for i in range(len(x)):
  for j in range(n):
    print(b[i][j])
   
