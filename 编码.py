s =input("输入六位二进制：")#010101
n = len(s)
i = 0
while i <= n-1:
    c =s[i:i+3]
if c == "000": d = "东"
elif c == "001": d = "东南"
elif c == "010": d = "南"
elif c == "011": d = "西南"
elif c == "100": d = "西"
elif c == "101": d = "西北"
elif c == "110": d = "北"
else: d = "东北"
b1 = int(s[i + 3])
b2 = int(s[i + 4])
b3 = int(s[i + 5])
v=b1*4+b2*2+b3#实现三位二进制编码到十进制的转化
print( str(c) +" " + str(v)) #按格式要求打印输出，如：东 7
i+=6 #调整 i