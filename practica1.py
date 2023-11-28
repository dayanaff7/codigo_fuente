def cabecera():
    titulo="""

██╗  ██╗ █████╗ ███████╗██╗  ██╗
██║  ██║██╔══██╗██╔════╝██║  ██║
███████║███████║███████╗███████║
██╔══██║██╔══██║╚════██║██╔══██║
██║  ██║██║  ██║███████║██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
        by Dayanna Flores                     

    """
    print(titulo) 

def cadena_texto(var):
 print("EL hash de la frase es: " + str(hash(var)))

cabecera()
texto= input("Introduce una frase: ")
cadena_texto(texto)
