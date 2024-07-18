from FUNCIONES_EXAMEN_FANTINI import *
while True:
    opc=menu('menu principal',['Asignar sueldos aleatorios','Clasificar sueldos','Ver estadísticas','Reporte de sueldos'])
    if opc==1:
        asig_sueldo_alea()
    elif opc==2:
        clasificar_sueldos()
    elif opc==3:
        ver_estadisticas()
    elif opc==4:
        reporte_sueldos()
    elif opc==5:
        print("Finalizando programa...")
        print("Desarrollado por María Victoria Fantini Palma")
        print("Rut: 21.037.734-4")
        break
    else:
        print("Opción inválida, intente nuevamente.")