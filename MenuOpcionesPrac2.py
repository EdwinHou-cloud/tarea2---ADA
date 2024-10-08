"""
Hou, Edwin	        8-1021-1916
Arosemena, Miguel	8-1016-2330
Corrales, Diego		8-1001-1890
Camaño, Edward		8-1010-515
Pino, Josué		    8-1012-688
"""

# InicioAlgoritmo
import math

# Función que muestra la presentación del programa
def Presentacion():
    # Uso del formato centrar (^70) para alinear los textos de presentación
    print("\n{:^70}".format("UNIVERSIDAD TECNOLÓGICA DE PANAMÁ"))
    print("{:^70}".format("FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES"))
    print("{:^70}".format("DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS"))
    print("{:^70}".format("TRABAJO GRUPAL 2"))
    print("{:^70}".format("Integrantes: Miguel Arosemana 8-1016-2330"))
    print("{:^78}".format("Edward Camaño 8-1010-515"))
    print("{:^80}".format("Diego Corrales 8-1001-1890"))
    print("{:^76}".format("Edwin Hou 8-1021-1916"))
    print("{:^76}".format("Josue Pino 8-1012-688"))

# Función para calcular la hipotenusa, área y perímetro de un triángulo rectángulo
def Catetos_TrianguloR():
    try:
        # Solicita al usuario el valor del primer cateto
        while True:
            cateto_1 = float(input("Ingrese el valor del primer cateto (c1): "))
            if cateto_1 <= 0: # Valida que no sea cero o negativo
                print("Ingrese un valor correcto, un cateto no puede ser 0 o negativo")
            else:
                break # Sale del ciclo si la entrada es válida
        
        # Solicita al usuario el valor del segundo cateto
        while True:
            cateto_2 = float(input("Ingrese el valor del segundo cateto (c2): "))
            if cateto_2 <= 0: # Valida que no sea cero o negativo
                print("Ingrese un valor correcto, un cateto no puede ser 0 o negativo")
            else:
                break # Sale del ciclo si la entrada es válida
            
        # Calcula la hipotenusa, área y perímetro usando las fórmulas dadas
        hipotenusa = math.sqrt(cateto_1**2 + cateto_2**2)  # Fórmula de la hipotenusa
        area = (cateto_1 * cateto_2) / 2  # Fórmula del área
        perimetro = hipotenusa + cateto_1 + cateto_2  # Fórmula del perímetro

        # Muestra los resultados con dos decimales
        print(f"Hipotenusa (h): {hipotenusa:.2f}")
        print(f"Área (A): {area:.2f}")
        print(f"Perímetro (p): {perimetro:.2f}")
    
    # Muestra error en caso de insertar valores no númericos   
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos para los catetos.")

def Ventas_Refrescos():
    try:
        # Lista de productos inicializados con valores en cero para los precios, ventas y el total
        productos = ["Agua", "Cerveza", "Agua saborizante", "Sodas", "Jugos naturales"]
        precios = [0, 0, 0, 0, 0]
        ventas = [0, 0, 0, 0, 0]
        total = [0, 0, 0, 0, 0]

        # Itera sobre los productos para solicitar el precio y la cantidad vendida
        for i in range(len(productos)):
            print(f"\nProducto: {productos[i]}")
            while True:
                try:
                    ventas[i] = int(input("Ingrese la cantidad vendida (máximo 300): "))
                    if ventas[i] < 0: #Verifica que las ventas no sean negativas
                        print("La cantidad vendida no puede ser negativa.")
                        continue
                    if ventas[i] > 300: #Verifica que las ventas no sean mayores a 300
                        print("La cantidad vendida no puede ser mayor a 300.")
                        continue
                    break
                except ValueError:
                    print("Error, el valor es incorrecto. Intente nuevamente.")
            while True:
                try:
                    precios[i] = float(input("Ingrese el precio del producto: "))
                    if precios[i] <= 0: #Verifica que el precio no sea negativo o cero
                        print("El precio no puede ser negativo o cero.")
                        continue
                    break
                except ValueError:
                    print("Error, el valor es incorrecto. Intente nuevamente.")

        # Calcula las ventas totales de cada producto
        for i in range(len(productos)):
            total[i] = ventas[i] * precios[i]

        # Suma total de ventas y total monetario
        totalVentas = sum(ventas)
        totalTotal = sum(total)
        
        # Muestra el informe de ventas en forma de tabla
        print("\nInforme de Ventas:")
        print("+----------------------+--------------------+--------+--------------+")
        print("| {:<20} | {:<18} | {:<6} | {:<12} |".format("Productos", "Ventas", "Precio", "Total"))
        print("+----------------------+--------------------+--------+--------------+")
        for i in range(len(productos)):
            print(f"| {productos[i]:<20} | {ventas[i]:<18} | {precios[i]:<6} | {total[i]:<13.1f}|")
        print("+----------------------+--------------------+--------+--------------+")    
        print(f"| Total                | {totalVentas:<18} |        | {totalTotal:<13}|")
        print("+----------------------+--------------------+--------+--------------+")
        
        # Muestra mensajes de acuerdo con el total de ventas
        if totalVentas > 1000:
            print("\nUsted ha tenido un limite de venta superior, ha ganado una membresia")
        elif totalVentas > 500 and totalVentas < 1000:
            print("\nTe felicitamos, te falta poco para llegar a la meta")
        elif totalVentas < 500:
            print("\nAnimo, pronto lo lograras")
    
    # Muestra error en caso de insertar valores no númericos o valores fuera del rango
    except ValueError:
        print("Error: Ingrese una cantidad válida de productos.")

def Pagos_Hipoteca():
    try:
        while True:
            capital = float(input("Ingrese el capital del préstamo: "))
            if capital <= 0:
                print("Error: El capital del préstamo no puede ser negativo.")
                continue # Permite que el usuario vuelva a ingresar el capital si es inválido
            else:
                break # Sale del ciclo cuando se ingresa un capital válido

        while True:
            interes_anual = float(input("Ingrese el interés anual (%): "))
            if interes_anual <= 0:
                print("Error: El interés anual no puede ser cero o negativo.")
                continue # Permite que el usuario vuelva a ingresar un valor correcto
            else:
                break # Sale del ciclo si el interés anual es válido

        while True:
            años = int(input("Ingrese el número de años de la hipoteca: "))
            if años <= 0:
                print("Error: El número de años no puede ser negativo.")
                continue # Permite que el usuario vuelva a ingresar un valor correcto
            else:
                break # Sale del ciclo si el valor ingresado es válido
        
        # Convierte el interés anual a mensual
        interes_mensual = (interes_anual / 100) / 12
        
        # Número total de meses
        meses = años * 12
        # Fórmula para calcular la cuota mensual
        cuota_mensual = capital * (interes_mensual * (1 + interes_mensual) ** meses) / ((1 + interes_mensual) ** meses - 1)
        
        # Muestra los resultados
        print(f"La cuota mensual a pagar es: {cuota_mensual:.2f} ")
    
    # Captura error por división entre cero, que puede ocurrir si el interés es 0
    except ZeroDivisionError:
        print("Error: El interés anual no puede ser cero.")
    
    # Muestra error en caso de insertar valores no númericos 
    except ValueError:
        print("Error: Ingrese valores numéricos válidos.")

# Función del menú principal que permite seleccionar las opciones disponibles
def menu():
    while True:
        # Muestra el menú principal al usuario
        print("\n Menú Principal: ")
        print("1. Presentación")
        print("2. Catetos de un triángulo rectángulo")
        print("3. Compañía de refresco")
        print("4. Pagos mensuales de una hipoteca")
        print("5. Salir")
        
        try:
            # Captura la opción seleccionada por el usuario
            opcion = input("Seleccione una opción (1 al 5): ")
            
            # Ejecuta la función correspondiente según la opción seleccionada
            if opcion == '1':
                Presentacion()
            elif opcion == '2':
                Catetos_TrianguloR()
            elif opcion == '3':
                Ventas_Refrescos()
            elif opcion == '4':
                Pagos_Hipoteca()
            elif opcion == '5':
                print("Gracias por utilizar nuestro programa.")
                break # Sale del bucle y finaliza el programa
            else:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 5.")

        except ValueError:
            # Maneja errores si el usuario ingresa un valor no numérico
            print("Error: Por favor, ingrese un número válido.")

# Inicia el programa llamando a la función del menú
menu() 
# FinAlgoritmo