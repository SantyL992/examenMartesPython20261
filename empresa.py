import random

# ==========================================================
# 1. ESTRUCTURAS DE DATOS GLOBALES (LISTAS)
# ==========================================================
# Lista para el proceso de Registro e Ingreso del empleado
usuarios_sistema = []   

# Lista principal para gestionar los 10 usuarios del servicio
usuarios_servicio = []  

# ==========================================================
# 2. FUNCIONES DE REGISTRO E INGRESO (SEGÚN TU IMAGEN)
# ==========================================================

def registrar_empleado():
    """Paso 1 del diagrama: Inicio -> Registro"""
    print("\n========================================")
    print("      REGISTRO DE NUEVO EMPLEADO        ")
    print("========================================")
    
    correo_creado = input("Cree su correo electrónico: ")
    password_creada = input("Cree su contraseña (ID): ")
    
    # Creamos un diccionario para el empleado
    empleado_nuevo = {
        "correo": correo_creado,
        "password": password_creada
    }
    
    # MÉTODO DE LISTA: append (Requisito)
    usuarios_sistema.append(empleado_nuevo)
    print("\n[SISTEMA]: Empleado registrado con éxito.")


def ingreso_login():
    """Paso 2 del diagrama: Ingreso (con 3 intentos)"""
    print("\n========================================")
    print("           INGRESO AL SISTEMA           ")
    print("========================================")
    
    intentos_disponibles = 3
    
    while intentos_disponibles > 0:
        usuario_ingreso = input("Correo: ")
        clave_ingreso = input("Contraseña: ")
        
        # Validación contra el primer empleado registrado
        primer_empleado = usuarios_sistema[0]
        
        if usuario_ingreso == primer_empleado["correo"] and clave_ingreso == primer_empleado["password"]:
            print("\n>>> Login exitoso. Bienvenido al sistema.")
            return True
        else:
            intentos_disponibles = intentos_disponibles - 1
            if intentos_disponibles > 0:
                print(f"Credenciales incorrectas. Intentos restantes: {intentos_disponibles}")
            else:
                print("Cuenta bloqueada temporalmente. Programa finalizado.")
                return False

# ==========================================================
# 3. GENERACIÓN DE DATOS (LECTURAS Y DATOS BÁSICOS)
# ==========================================================

def generar_datos_servicio():
    """Genera 10 diccionarios y 500 registros numéricos totales"""
    print("\n... Generando 500 lecturas numéricas y datos básicos ...")
    
    lista_nombres = ["Andrés", "Beatriz", "Carlos", "Dora", "Esteban", "Flor", "Gerardo", "Helena", "Ítalo", "Janet"]
    
    for i in range(10):
        # Requisito: Crear 50 lecturas por usuario (50 * 10 = 500 registros totales)
        lecturas_mes = []
        for _ in range(50):
            valor_kwh = random.randint(100, 900)
            lecturas_mes.append(valor_kwh)
        
        # Requisito: Estado Activo o Suspendido (Alternado)
        if i % 2 == 0:
            estado_cliente = "ACTIVO"
        else:
            estado_cliente = "SUSPENDIDO"
            
        # Creamos el Diccionario con la Estructura Mínima Requerida
        datos_usuario = {
            "id": i + 1,
            "nombre": lista_nombres[i],
            "documento": random.randint(1010101, 9999999),
            "estrato": random.randint(1, 6),
            "consumoEnergetico": lecturas_mes, # Lista de 50 números
            "estado": estado_cliente
        }
        
        # Guardamos el diccionario en la lista principal
        usuarios_servicio.append(datos_usuario)
    
    print(f"[EXITO]: {len(usuarios_servicio)} Usuarios cargados con 50 lecturas cada uno.")

# ==========================================================
# 4. FUNCIONES DE GESTIÓN Y RESULTADOS (MENÚ)
# ==========================================================

def mostrar_usuarios_ordenados():
    """Muestra la tabla ordenada por consumo de menor a mayor"""
    print("\n" + "="*85)
    print(f"{'ID':<5} | {'NOMBRE':<12} | {'ESTRATO':<8} | {'CONS. TOTAL':<15} | {'ESTADO':<12}")
    print("-" * 85)
    
    # MÉTODO DE LISTA: sort (Requisito)
    # Ordenamos sumando el contenido de la lista 'consumoEnergetico'
    usuarios_servicio.sort(key=lambda x: sum(x["consumoEnergetico"]))
    
    for u in usuarios_servicio:
        total_consumo = sum(u["consumoEnergetico"])
        print(f"{u['id']:<5} | {u['nombre']:<12} | {u['estrato']:<8} | {total_consumo:<15} | {u['estado']:<12}")
    print("="*85)

def gestionar_usuarios_menu():
    """Muestra el menú cíclico después del login"""
    while True:
        print("\n****************************************")
        print("      MENÚ DE GESTIÓN DE SERVICIOS      ")
        print("****************************************")
        print("1. Gestionar usuarios (Ordenar consumo Menor a Mayor)")
        print("2. Eliminar último usuario de la lista (Método .pop)")
        print("3. Insertar usuario de prueba al inicio (Método .insert)")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            mostrar_usuarios_ordenados()
        
        elif opcion == "2":
            # MÉTODO DE LISTA: pop (Requisito)
            if len(usuarios_servicio) > 0:
                eliminado = usuarios_servicio.pop()
                print(f"\n[AVISO]: Se ha eliminado a {eliminado['nombre']} de la lista.")
            else:
                print("\n[ERROR]: La lista ya está vacía.")
        
        elif opcion == "3":
            # MÉTODO DE LISTA: insert (Requisito)
            nuevo_test = {
                "id": 99, "nombre": "TEST", "documento": 000, 
                "estrato": 1, "consumoEnergetico": [0], "estado": "ACTIVO"
            }
            usuarios_servicio.insert(0, nuevo_test)
            print("\n[AVISO]: Usuario TEST insertado en la posición 0.")
            
        elif opcion == "4":
            print("\nCerrando sesión... Gracias por usar el sistema.")
            break
        else:
            print("\n[ERROR]: Opción no válida. Intente de nuevo.")

# ==========================================================
# 5. INICIO DEL PROGRAMA (FLUJO DEL DIAGRAMA)
# ==========================================================

def ejecutar_sistema_completo():
    # Paso 1: Registro
    registrar_empleado()
    
    # Paso 2: Ingreso (Si falla el login, el programa termina)
    if ingreso_login() == True:
        # Paso 3: Generar Lecturas y Datos
        generar_datos_servicio()
        
        # Paso 4: Resultados (Menú)
        gestionar_usuarios_menu()

# Lanzar el sistema
if __name__ == "__main__":
    ejecutar_sistema_completo()



    # // Prompt ayúdame a realizar el siguiente ejercicio, pero... necesito que no utilices POO y uses conceptos básicos de python ya que me encuentro aprendiendo y me gusta poder entender el código


# Contexto

# Una empresa de servicios públicos quiere un prototipo en Python para gestionar lecturas numéricas y datos básicos de usuarios.
# El objetivo del taller es practicar listas, diccionarios, métodos de listas y funciones (def), junto con un flujo simple de registro/login con intentos limitados.
# Objetivo de aprendizaje

# Al finalizar, el estudiante será capaz de:
# Construir soluciones con funciones y flujo de control.
# Gestionar listas con métodos: append, insert, remove, pop, sort.
# Trabajar con lista de diccionarios (mínimo 10 registros).
# Implementar un login/registro con control de intentos e información al usuario.
# Generar y procesar un volumen de datos (500 registros numéricos).
# Requisitos del ejercicio

# 1) Registro y Login (con 3 intentos)

# Implementa un sistema que permita:
# Registro
# Permitir crear un usuario con:correo
# password
# Guardar el usuario registrado en una estructura simple (diccionario o lista de diccionarios).
# Login
# Pedir correo y contraseña.
# Permitir máximo 3 intentos.
# En cada intento fallido debe mostrar:"Credenciales incorrectas. Intentos restantes: X"
# Si inicia sesión correctamente, mostrar:"Login exitoso" y permitir continuar con el menú.
# Si se agotan los intentos:"Cuenta bloqueada temporalmente" y finalizar el programa.
# 2) Registro de N diccionarios (lista de diccionarios)

# Crear una lista llamada usuarios_servicio que contenga 10 diccionarios, cada uno con esta estructura mínima:
# id (int)
# nombre (str)
# documento (str o int)
# estrato (int 1 a 6)
# consumoEnergetico (crear un listado nuemrico de 30 consumos al mes) en KWH
# estado (str: "ACTIVO" o "SUSPENDIDO")
# Debe existir un menú para:
# Ordenar usuarios por consumo de menor a mayor
# Funciones obligatorias

# Tu solución debe estar organizada usando funciones def.
# Menú sugerido (después del login)

# Gestionar usuarios del servicio (lista de diccionarios)
# Salir

# Necesito que todo este ejercicio sea realizado con base en este diagrama que te comparto en la imagen