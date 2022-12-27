height=float(input("请输入你的身高（米）："))
weight=float(input("请输入你的体重（千克）："))
BMI=weight/height**2
if BMI>=18.5:
    print("你的体重指数 BMI 为:",BMI,"符合标准！")
else:
    print("你的体重指数 BMI 为:",BMI,"不符合标准！")