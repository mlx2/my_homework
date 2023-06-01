
S = eval(input("请输入一个整数:"))
infinitesimal = 0.00000000000000000000000000000000000001
a = S / 2

counter = 1
while True:
    b = S / a
    delta = a - b
   
    
    counter = counter + 1

    if delta < infinitesimal:
        break
    else:
        a = a = (a + b) / 2
print("{}的算数平方根为{:.2f}".format(S,a))