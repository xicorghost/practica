CARGOS=["Ceo", "Desarrollador", "Borialito"]

def registrar_traba(trabajadores):
    nombre=input("Ingrese nombre del trabajador: ")
    apellido=input("Ingrese apelllido del trabajador: ")
    cargo=input("Ingrese cargo del trabajador (CEO/Desarrollador/Borialito): ").capitalize()
    while cargo not in CARGOS:
        print("Este cargo no existe, intente nuevamente")
        cargo=input("Ingrese cargo del trabajador (CEO/Desarrollador/Borialito): ").capitalize()
    SueldoBruto=int(input("Ingrese sueldo bruto del trabajador: "))

    #calcular los sueldos
    descSalud= SueldoBruto * 0.07
    descAFP= SueldoBruto * 0.12
    liquidPagar= SueldoBruto - descSalud - descAFP

    trabajadores.append({
        "Nombre" : nombre,
        "Apellido" : apellido,
        "Cargo" : cargo,
        "SueldoBruto": SueldoBruto,
        "DescSalud": descSalud,
        "DescAFP" : descAFP,
        "LiquidoPagar" : liquidPagar
    })

def listar_traba(trabajadores):
    print("Lista de trabajadores")
    for trabajador in trabajadores:
        print(trabajador)
        #print(trabajador{"Nombre"})

def imprimir_plantilla(trabajadores):
    CargosSelc=input("ingrese cargo para imprimir planilla o ENTER para todos: ").capitalize()
    if CargosSelc=="":
        trabajadores_a_imprimir= trabajadores
        nombreArchivo="planilla.txt"
    elif CargosSelc in CARGOS:
        trabajadores_a_imprimir=[]
        for trabajador in trabajadores:
            if trabajador["Cargo"] == CargosSelc:
                trabajadores_a_imprimir.append(trabajador)
                nombreArchivo= f"planilla {CargosSelc}.txt"
    else:
        print("cargo no valido")
        return
    
    with open(nombreArchivo, "w") as archivo:
        for trabajador in trabajadores_a_imprimir:
            archivo.write(f"Nombre: {trabajador['Nombre']}\n")
            archivo.write(f"Apellido: {trabajador['Apellido']}\n")
            archivo.write(f"Cargo: {trabajador['Cargo']}\n")
            archivo.write(f"Sueldo Bruto: {trabajador['SueldoBruto']}\n")
            archivo.write(f"Descuento Salud: {trabajador['DescSalud']}\n")
            archivo.write(f"Descuento AFP: {trabajador['DescAFP']}\n")
            archivo.write(f"Liquido a Pagar: {trabajador['LiquidoPagar']}\n\n")

                          
                          
