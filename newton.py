import numpy as np

# def sqrt(x):
#     a = x
#     for i in range(100):
#         delta =  -(a**2 - x)/(2*a)
#         if abs(a**2 - x)/(2*a) < 1e-10:
#             return a
#         a = a + delta
#         print("iteration:", i, "a:", a)
#     return a

# sqrt(10)

N = 3
df_dx = np.tile(np.eye(4), (N, 1, 1))
print("df_dx:\n", df_dx)
df_dx_trans = df_dx.transpose(1, 2, 0)
print("df_dx_trans:\n", df_dx_trans)

c_dot = np.array([1., 0.])
print(c_dot)
c_dot_reshaped = c_dot[:, np.newaxis]
print(c_dot_reshaped)


df_dx.transpose(1, 2, 0)