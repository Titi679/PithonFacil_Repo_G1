

usuarios = []  # Lista de Usuarios global
usuarios_nc=[]

def registrar_usuario():


    usuario = {}  # Este diccionario almacenara la infomracion del nombre y la contraseña

    print("Comencemos con el proceso de registro!")
    print("No tomará más de 5 minutos, no te preocupes!")
    print("Necesitaremos un Nombre de Usuario y una Contraseña")
    print("-----------------------------------------------------------------")

    # Pide el nombre de Usuario
    while True:
        usuario_input = input("Nombre de usuario: ")
        usuario_input=usuario_input.strip()
        usuario_input=usuario_input.lower()
        if usuario_input in usuarios:
            print("El usuario ya está registrado, intenta con otro nombre.")
        else:
            break 

    # Pide la contraseña
    contraseña = input("Contraseña: ")

    # Este porceso guarda los datos
    usuario["nombre"] = usuario_input
    usuario["contraseña"] = contraseña  # Nota: No es seguro almacenar contraseñas en texto plano
    usuarios.append(usuario_input)
    usuarios_nc.append(usuario)

    print("Usuario registrado con éxito!")
    return usuario

def eliminar_usuario():
    print("Eliminar usuario registrado")
    usuario_input = input("Ingrese el nombre de usuario a eliminar: ")
    usuario_input=usuario_input.strip()
    usuario_input=usuario_input.lower()

    if usuario_input in usuarios:
        usuarios.remove(usuario_input)  # Eliminara el usuario registrado
        print(f"Usuario '{usuario_input}' eliminado correctamente.")
    else:
        print("El usuario no está registrado.")

def modificar_usuario():
    print("Modificar usuario registrado")
    usuario_actual = input("Ingrese el nombre de usuario a modificar: ")
    usuario_actual=usuario_actual.strip()
    usuario_actual=usuario_actual.lower()

    # Verificara si el usuario esta o no registrado
    if usuario_actual not in usuarios:
        print("El usuario no está registrado.")
        return 

    contraseña = input("Ingrese la contraseña para modificar el usuario: ")

    if usuarios[usuario_actual] == contraseña:
        nuevo_usuario = input("Ingrese el nuevo nombre de usuario: ").strip().lower()

        if nuevo_usuario in usuarios:
            print("El nuevo nombre de usuario ya está registrado. Intente con otro.")
        else:
            usuarios[nuevo_usuario] = usuarios.pop(usuario_actual)
            print(f"Usuario '{usuario_actual}' ha sido cambiado a '{nuevo_usuario}' correctamente.")
    else:
        print("Contraseña incorrecta. No se puede modificar el usuario.")

def quiosco():
    print("Bienvenido a Nuestro Quiosco")
    print("En este apartado puede comprar varios productos, consultar el precio y los mas vendidos")
    print("Tambien puede podificar su usuario si ya esta registrado o registrarse si aun no lo está")
    print("Que desea hacer? ")
    print("Iniciar Sesión [1]")
    print("Registrar Usuario [2]")
    print("Eliminar Usuario [3]")
    print("Modificar Usuario Registrado [4]")
    print(usuarios)
    #print(usuario)
    eleccion=int(input())
    

    if eleccion == 1:
        print(...)
    elif eleccion == 2:
        registrar_usuario();
    elif eleccion == 3:
        eliminar_usuario();
    elif eleccion == 4:
        modificar_usuario();

def main():
    while True:
        quiosco()  # Llamamos la función quiosco que presenta el menú
        otra_acción = input("\n¿Quieres realizar otra acción? (s/n): ").strip().lower()
        if otra_acción != "s":
            print("Gracias por usar el quiosco. ¡Hasta luego!")
            break  # Salir del bucle si la respuesta no es 's'

if __name__ == "__main__":
    main()