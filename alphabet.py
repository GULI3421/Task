def Alphabet():
    try:
        s = "abcdefghiklmnopqrstuvwxz"
        ch = ''
        ch = input("Введите символ:")
        index = s.index(ch)
        print(f"символ '{ch}' индекс символа {index}")
    except:
        print("Ошибка символа")
        print("Введите только одну символ англиского алфавита")
(Alphabet())
