import os
import csv
import random
import statistics
os.system('cls')

def menu(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

#lista empleados dado por la prueba
empleados=["Juan Perez","María García","Carlos Lopez","Ana Martinez","Pedro Rodriguez","Laura Hernandez","Miguel Sanchez","Isabel Gómez","Francisco Díaz","Elena Fernandez"]

sueldos={} #esta es mi lista de sueldos entonces

#1 asignas sueldos aleatorios
def asig_sueldo_alea():
    for empleado in empleados:
        sueldos[empleado] = random.randint(300000, 2500000)
    print("Sueldos asignados.")
#funciona
    
def clasificar_sueldos():
      
    total_sueldos = 0
    sueldo_menor = {}
    sueldo_entre = {}
    sueldo_mayor = {}

    for empleado, sueldo in sueldos.items():
        total_sueldos += sueldo
        if sueldo < 800000:
            sueldo_menor[empleado] = sueldo
        elif 800000 <= sueldo <= 2000000:
            sueldo_entre[empleado] = sueldo
        else:
            sueldo_mayor[empleado] = sueldo

        print("\nSueldos menores a $800.000 TOTAL: ", len(sueldo_menor))
        print("Nombre empleado:          Sueldo: ")
        for empleado, sueldo in sueldo_menor.items():
            print(f"{empleado:25} ${sueldo}")
        print("==========================================")

        print("\nSueldos entre $800.000 y $2.000.000 TOTAL: ", len(sueldo_entre))
        print("Nombre empleado:          Sueldo:")
        for empleado, sueldo in sueldo_entre.items():
            print(f"{empleado:25} ${sueldo}")
        print("==========================================")

        print("\nSueldos superiores a $2.000.000 TOTAL: ", len(sueldo_mayor))
        print("Nombre empleado:          Sueldo:")
        for empleado, sueldo in sueldo_mayor.items():
            print(f"{empleado:25} ${sueldo}")
        print("==========================================")

    print(f"TOTAL SUELDOS: ${total_sueldos}")
    #YAFUNCIONAAAAPORFINNNNNNNNNNNNNNNN

#3 Ver estadísticas
def ver_estadisticas():
    sueldos_lista = list(sueldos.values()) #values devuelve la lista con los valores asociados a las "claves"
    #aqui va el sueldo más alto
    sueldo_alto = max(sueldos_lista)
    #aqui va el sueldo más bajo
    sueldo_bajo = min(sueldos_lista)
    #aqui va el promedio de los suelditos
    promedio_sueldos = statistics.mean(sueldos_lista)
    #aqui va la media geometrica
    media_geometrica = statistics.geometric_mean(sueldos_lista)
    #imprimno
    print(f"Sueldo más alto: ${sueldo_alto}")
    print(f"Sueldo más bajo: ${sueldo_bajo}")
    print(f"Promedio de sueldos: ${promedio_sueldos}")
    print(f"Media geométrica: ${media_geometrica:}")

#4Reporte de sueldos
def reporte_sueldos():
    #si el descuento de salud es 7%, debo multiplicar por 0,07
    #el descuento de afp es de 12%, debo multiplicar los sueldos base por 0,12
    #sueldo-liquido=sueldobase-descuentosalud-descuentoafp
    with open('reporte_sueldos.csv','w') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud (fonasa)", "Descuento AFP", "Sueldo líquido"])
        for trabajador, sueldo_base in sueldos.items():
            descuento_salud = round(sueldo_base * 0.07)
            descuento_afp = round(sueldo_base * 0.12)
            sueldo_liquido = round(sueldo_base - descuento_salud - descuento_afp)
            writer.writerow([trabajador, f"${sueldo_base}", f"${descuento_salud}", f"${descuento_afp}", f"${sueldo_liquido}"])
            #no me queda bien....el excel se ve todo pegado