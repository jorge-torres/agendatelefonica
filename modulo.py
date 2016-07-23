#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys


def bienvenida():

    print ("BIENVENIDO A LA AGENDA TELEFONICA \n")
    print ("""Elige una de las siguientes opciones \n
            1-Para listar los contactos
            2-Para agregar un contacto a la lista""")
    opcion = int(input(">"))
    if opcion > 2:
        print ("lo sentimos escogiste un opciòn invalida")
        sys.exit(0)
    else:
        return opcion


def listar ():
    archivo = open("data/contactos.csv", mode="r")
    texto = archivo.read()
    print (texto.replace(",","\t\t"))
def agregar():
    # archivo = open("data/contactos.csv", "r")
    archivo = open("data/contactos.csv", "a")
    contacto = raw_input("Escriba el nombre del contacto \n>")
    telefono = raw_input("Escriba el numero de telefono del contacto \n>")
    archivo.write(contacto)
    archivo.write(",")
    archivo.write(telefono)
    archivo.write("\n")
    print ("se ha agragado a la lista el contacto "+contacto+" con el numero de telefono "+telefono+"\n>")



def decidir(opcion):
    if opcion == 1:
        listar()
    else:
        agregar()