def a(**param): #关键字可变参数
    for i ,k in param.items(): #记得加intem()函数 i 是关键字  k 是值
        print(i,k)
a(na="sadas",ag="15")