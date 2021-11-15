# def binary_base(a):
#     if a < 2:
#         print(a)
#     else:
#         binary_base(a // 2)
#         print(a % 2)
#
# binary_base(int(input()))

# 개행으로 인하여 수정

def binary_base(a):
    if a < 2:
        return str(a)
    else:
        return (str(binary_base(a // 2)) + str(a % 2))

print(binary_base(int(input())))
