##在银行里, 银行年利息 3.7%,小明几年能存够?请填空完善该程序，帮小张计算几年后可以环游中国。
money=5000
year=0
while money<30000:
    money=money*(1+0.037)
    year=year+1
print(year,"年后可以环游中国")
input("运行完毕，请按回车键退出...")