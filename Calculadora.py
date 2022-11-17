num1=int(input("Ingrese un número: "))
num2=int(input("Ingrese un número: "))


Menú = 0

while Menú != 5:
    print("""
    Seleccione una operación:
    
    1) Suma
    2) Resta
    3) Multiplicación
    4) División
    5) Salir
    """)
    
    Menú = int(input())

    if Menú == 1:
        print("Resultado: ", num1,"+", num2,"=", num1+num2)
    
    elif Menú == 2:
        print("Resultado: ", num1,"-", num2,"=", num1-num2)
    
    elif Menú == 3:
        print("Resultado: ", num1,"*", num2,"=", num1*num2)
    
    elif Menú == 4:
        print("Resultado: ", num1,"/", num2,"=", num1/num2)
    elif Menú == 5:
        break

    