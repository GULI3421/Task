import math#
def area(figure):
    try:
        if figure=="треугольник":#
            a=float(input("Введите сторону a ="))#
            b=float(input("Введите сторону b ="))#
            c=float(input("Введите сторону c ="))#
            p=(a+b+c)/2#
            s=math.sqrt((p*(p-a)*(p-b)*(p-c)))#
            print("площадь треугольника",s)
        elif figure=="прямоугольник":#
            a=float(input("Введите сторону a ="))#
            b=float(input("Введите сторону b ="))#
            s=a*b#
            print("площадь прямоугольника",s)
        elif figure=="круг":#
            r=float(input("Введите радиус r ="))#
            s=math.pi*(r**2)#
            print("площадь круга",s)
        elif figure=="квадрат":#
            a=float(input("Введите одну сторону а="))#
            s = a**2#
            print("площадь квадрата",s)
        elif figure=="трапеция":#
            a=float(input("Введите длину большего основания а: "))#
            b=float(input("Введите длину меньшего основания b: "))#
            c=float(input("Введите угол при большем основании в градусах: "))#
            z=c*math.pi/180#
            s=(a**2-b**2)/4*math.tan(z)#
            print("площадь трапеция",s)
        elif figure=="длина гипотенузы":#
            a = float(input ("Введите катет 1: "))# 
            b = float(input ("Введите катет 2: "))#
            s = math.sqrt(a**2 + b**2)#
            print("длина гипотенузы",s)
        elif figure=="длина окружности":#
            r=float(input("Введите радиус r="))#
            s=2*math.pi*r#
            print("длина окружности",s)
    except:
        print("ошибка ввода")
        
    
figure = input('фигура -')
print(area(figure))

    

    

