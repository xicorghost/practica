import funciones as fn

trabajadores=[]

while True:
    print("Bienvenido trabajador a los pagos de sueldo")
    print("1.Registrar trabajador")
    print("2.Lista de los trabajadores")
    print("3.Imprimir planilla de sueldos")
    print("4.Salir del programa")

    opc=int(input("ingrese una opcion: "))

    if opc== 1:
        fn.registrar_traba(trabajadores)
        print("selcciono opc 1")
    elif opc== 2:
        fn.listar_traba(trabajadores)
        print("selcciono opc 2")
    elif opc== 3:
        fn.imprimir_plantilla(trabajadores)
        print("selcciono opc 3")
    elif opc== 4:
        print("saliendo del sistema")
        break
    else:
        print("opcion no valida")
