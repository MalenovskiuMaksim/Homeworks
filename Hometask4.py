a=input("Введіть значення а!")
b=input("Введіть значення б!")
c=input("Введіть значення с!")
if a>b:
    print("Вітаю!")
elif a<b:
    print("Спробуйте ще раз!")
elif a==b:
    if b>c:
        print("Спробуйте ще раз!")
    elif b<c:
        print("Вітаю!")