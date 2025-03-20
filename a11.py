# radius = float(input("请输入圆的半径："))
# pi = 3.14159
# area = pi * radius ** 2
# perimeter = 2 * pi * radius
# print(f"半径为{radius}的圆，面积为{area:.2f}，周长为{perimeter:.2f}")
# chinese = float(input("请输入语文成绩："))
# math = float(input("请输入数学成绩："))
# english = float(input("请输入英语成绩："))
# total = chinese + math + english
# average = total / 3
# print(f"总分：{total}，平均分：{average:.2f}")
height = float(input("请输入身高（米）："))
weight = float(input("请输入体重（千克）："))
bmi = weight / (height ** 2)
print(f"您的BMI值为：{bmi:.1f}")

if bmi < 18.5:
    print("体质类型：偏瘦")
elif 18.5 <= bmi < 24:
    print("体质类型：正常")
elif 24 <= bmi < 28:
    print("体质类型：偏胖")
else:
    print("体质类型：肥胖")