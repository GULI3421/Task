try:
    a = int(input("a = "))
    def even_odd():
        if a == 0:
            print("на ноль делить нельзя")           
        elif a % 2 == 0:
            print("четное число")
        else:
            print("нечетное число")
    even_odd()
except:
    print("ошибка символов")
    
