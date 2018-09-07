# 다음 행렬과 같은 행렬이 있다.
# m = np.array([[ 0,  1,  2,  3,  4],
#               [ 5,  6,  7,  8,  9],
#               [10, 11, 12, 13, 14]])
# 1.이 행렬에서 값 7 을 인덱싱한다.
# 2.이 행렬에서 값 14 을 인덱싱한다.
# 3.이 행렬에서 배열 [6, 7] 을 슬라이싱한다.
# 4.이 행렬에서 배열 [7, 12] 을 슬라이싱한다.
# 5.이 행렬에서 배열 [[3, 4], [8, 9]] 을 슬라이싱한다.

import numpy as np
m = np.array([[ 0,  1,  2,  3,  4],
               [ 5,  6,  7,  8,  9],
               [10, 11, 12, 13, 14]])
s=m[m%7==0]
print(s[1])
print(s[2])

print(m[1,1:3])
print(m[[1,2],[2,2]])
print(m[0:2, 3:])