import PyplotGraphic as pg

if __name__ == '__main__':
    graphic = pg.PyplotGraphic("PyplotGraphic Window", "Graphic", "axis X", "axis Y")

    isRuning = True
    while isRuning:
        print("Main-menu:")
        print("1) Draw graphic.")
        print("2) Show funcs list.")
        print("3) Add func.")
        print("4) Remove func.")
        print("5) Clear.")
        print("6) Exit.")

        try:
            i = str(input("Input: "))
            if (i == "6"):
                isRuning = False
            elif (i == "5"):
                graphic.clear()
            elif (i == "4"):
                i = str(input("Введите порядковый номер или название функции: ")).replace(" ", "")
                if i.isdigit():
                    i = int(i)
                graphic.remove(i)
            elif (i == "3"):
                f = str(input("Введите функцию: "))
                graphic.add(f)
            elif (i == "2"):
                print(graphic.get_funcs())
            elif (i == "1"):
                graphic.draw()
        except Exception as error:
            print(f"{error=}, {type(error)=}")
