# cs_practice
def calculate_rectangle_area(length, width):
    area = length * width
    return area

# 输入长和宽
length = float(input("请输入长方形的长度: "))
width = float(input("请输入长方形的宽度: "))

# 调用函数计算面积
result = calculate_rectangle_area(length, width)

# 显示结果
print(f"长方形的面积是: {result}")
