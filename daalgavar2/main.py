from module1_names import get_name
from module2_classes import get_class
from module3_gpa import get_gpa
def main():
    try:
        code = int(input("Сурагчийн код оруулна уу: "))
    except ValueError:
        print("Зөвхөн 0-3 хоорондын бүхэл тоо оруулна уу.")
        return
    if 0 <= code < 4:
        print("Мэдээлэл")
        print(f"Нэр       : {get_name(code)}")
        print(f"Анги      : {get_class(code)}")
        print(f"Голч дүн  : {get_gpa(code)}")
    else:
        print("Ийм индекс байхгүй 0-3 хоорондын код оруулна уу.")
if __name__ == "__main__":
    main()
