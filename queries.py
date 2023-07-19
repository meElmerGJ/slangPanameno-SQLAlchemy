import sqlalchemy
from tabulate import tabulate
from sqlalchemy.exc import IntegrityError
from base import Session, engine, Base
from slangPanameno import SlangPanameno

session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


class Program:
    words_generated = False


# Function to print a done task correctly message with a specified format
def msg_done(message):
    print(f"\n-----> {message} <-----")


# Function create a slang object
def add_word():
    try:
        new_slang = SlangPanameno(input("Ingrese la palabra: "), input("Ingresa el significado: "))
        session.add(new_slang)
        session.commit()
        msg_done("Palabra agregada")
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        print("\nERROR - La palabra ya existe")


# Function to update a word
def edit_word():
    value_requested = input("\nPresiones 0 para ver palabras\n\nIngrese el numero (#) o la palabra a eliminar: ")
    if value_requested == "0":
        get_words()
        edit_word()
    elif exist(value_requested):
        if value_requested.isnumeric():
            new_word = input(f"Ingrese nueva palabra: ")
            new_meaning = input(f"Ingrese el significado: ")
            row = session.query(SlangPanameno).filter_by(id=value_requested).first()
            row.word = new_word
            row.meaning = new_meaning
        else:
            new_word = input(f"Ingrese nueva palabra: ")
            new_meaning = input(f"Ingrese el significado: ")
            row = session.query(SlangPanameno).filter_by(word=value_requested).first()
            row.word = new_word
            row.meaning = new_meaning
        msg_done("Palabra editada")
    else:
        print("\nERROR: El valor ingresado no existe en la base de datos")
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        print("\nERROR - La palabra ya existe")


# Function to delete a word
def del_word():
    value_requested = input("\nPresiones 0 para ver palabras\n\nIngrese el numero (#) o la palabra a eliminar: ")
    if value_requested == '0':
        get_words()
        del_word()
    elif exist(value_requested):
        if value_requested.isnumeric():
            session.query(SlangPanameno).filter_by(id=value_requested).delete()
        else:
            session.query(SlangPanameno).filter_by(word=value_requested).delete()
        msg_done("Palabra eliminada")
        session.commit()
    else:
        print("\nERROR: El valor ingresado no existe en la base de datos")


# Function to get all records
def get_words():
    result = session.query(SlangPanameno)
    table = []
    for row in result:
        table.append([row.id, row.word, row.meaning])
    print(tabulate(table, headers=["#", "Palabra", "Significado"], tablefmt="psql"))
    input('"Presione ENTER para continuar"')


# Function to get a specific word meaning
def get_meaning():
    try:
        value_requested = input("\nIngrese la palabra: ")
        result = session.query(SlangPanameno).filter_by(word=value_requested).first()
        print(f"\n{result.word}, significa: {result.meaning}")
    except AttributeError:
        print("\nERROR: El valor ingresado no existe en la base de datos")


# Function to generate 10 records to test functions. (TEST USAGE ONLY)


def generate_data():
    if Program.words_generated:
        print("\nWARNING - Los registros ya han sido creados")
    else:
        slang_objects = [
            SlangPanameno("Chombo", "Amigo cercano o compañero"),
            SlangPanameno("Jato", "Casa o hogar"),
            SlangPanameno("Pana", "Amigo o camarada"),
            SlangPanameno("Que xopa!", "El clasico saludo de nosotros"),
            SlangPanameno("Taquilla", "Alguna historia o relato que puede ser falsa"),
            SlangPanameno("Quilla", "Dinero"),
            SlangPanameno("Tirar la posta", "Contar una historia o chisme"),
            SlangPanameno("Taquear", "Comer en exceso"),
            SlangPanameno("Chiri", "Frío"),
            SlangPanameno("Pelea de gallos", "Competencia o disputa acalorada")]
        session.add_all(slang_objects)
        session.commit()
        msg_done("Se han ingresado 10 registros")
        Program.words_generated = True


# Function to delete all records (TEST USAGE ONLY)
def delete_all_data():
    session.query(SlangPanameno).delete()
    print("\n ------> Todos los registros han sido eliminados <------")


def exist(value_requested):
    result = session.query(SlangPanameno).filter_by(word=value_requested).first() \
             or session.query(SlangPanameno).filter_by(id=value_requested).first()
    if result is None:
        return False
    else:
        return True
