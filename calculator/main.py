from add import add
from subtract import subtract
from divide import divide
def main():
    try:
        a = int(input("Эхний тоо оруулна уу: "))
        b = int(input("Хоёр дахь тоо оруулна уу: "))
    except ValueError:
        print("Зөвхөн тоон утга оруулна уу.")
        return
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")
if __name__ == "__main__":
    main()
