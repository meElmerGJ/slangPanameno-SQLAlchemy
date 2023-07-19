from queries import *


if __name__ == "__main__":

    try:
        # Flujos de programa
        print("\nBIENVENIDO AL DICCIONARIO DE SLANG PANAMEÑO\n")

        # Program menu
        menu = """
                1) Agregar nueva palabra
                2) Editar palabra
                3) Eliminar palabra 
                4) Ver palabras
                5) Buscar significado de palabra
                6) Insertar 10 registros(only test usage)
                7) Eliminar todos los registros(only test usage)
                8) Salir
                """

        # Program main loop // Warning! -> Need to use version above Python 3.10 for ***match - case*** Statements.
        end = False

        while not end:
            try:
                print(menu)
                option = int(input(f"Ingresa una opcion: "))
                match option:
                    case 1:
                        add_word()
                    case 2:
                        edit_word()
                    case 3:
                        del_word()
                    case 4:
                        get_words()
                    case 5:
                        get_meaning()
                    case 6:
                        generate_data()
                    case 7:
                        delete_all_data()
                    case 8:
                        session.close()  # Closing session
                        msg_done("El programa ha finalizado")
                        exit(0)
            except ValueError:
                print(f"ERROR - Ingrese una opcion correcta")
    except (KeyboardInterrupt, EOFError):
        msg_done("El programa ha finalizado")
