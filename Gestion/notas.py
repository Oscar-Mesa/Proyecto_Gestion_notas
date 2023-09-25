import os


list_nombres = []
list_notas = []

def fnt_limpiar():
    os.system('cls')
    print('Autor: Oscar Mesa')
    print('Fecha: 25 de septiembre del 2023')
    print('\n')

def fnt_selector(opcion):
    fnt_limpiar()
    if opcion == '1':
        nombre = input('Nombre <ENTER>')
        nota = input('Nota <ENTER>')

def fnt_registrar(nombre,nota):
    if nombre == '' or nota == '':
        enter = input('Debe ingresar la información solicitada <ENTER>')
    else:
        list_nombres.append(nombre)
        list_notas.append(nota)
        enter = input('Nota registrada con éxito <ENTER>') 

def fnt_menu(m):
    while m == True:
        op = input('<<< MENU PRINCIPAL >>>\
                   \n1. Registrar nota\
                   \n2. Consultar Notas\
                   \n3. Salir\n->')

