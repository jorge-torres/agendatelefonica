#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys


def bienvenida():

    print ("BIENVENIDO A LA AGENDA TELEFONICA \n")
    print ("""Elige una de las siguientes opciones \n
            1-Para listar los contactos
            2-Para agregar un contacto a la lista
            3-Para buscar un contacto""")
    opcion = int(input(">"))
    if opcion != 1 and opcion != 2 and opcion != 3 :
        print ("lo sentimos escogiste un opciòn invalida")
        sys.exit(0)
    else:
        return opcion


def listar ():

    archivo = open("data/contactos.csv", mode="r")
    texto = archivo.read()
    print (texto.replace(",","\t\t"))
    archivo.close()

def ultimoid():
    archivo = open("data/contactos.csv", "r")
    lineapartida = ("id", "nombre", "telefono")
    while lineapartida[0] != "" and lineapartida[0] != " ":
        linea = archivo.readline()
        lineapartida = linea.split(",")
        if lineapartida[0] != "" and lineapartida[0] != " ":
            id = lineapartida[0]
    return (id)

def agregar():

    num = (int (ultimoid()) + 1 )
    strnum = str(num)
    archivo = open("data/contactos.csv", "a")
    contacto = raw_input("Escriba el nombre del contacto \n>")
    telefono = raw_input("Escriba el numero de telefono del contacto \n>")
    archivo.write(strnum)
    archivo.write(",")
    archivo.write(contacto)
    archivo.write(",")
    archivo.write(telefono)
    archivo.write("\n")
    print ("se ha agragado a la lista el contacto "+contacto+" con el numero de telefono "+telefono+"\n>")
    archivo.close()


def buscar():

    nombre = raw_input("que contacto deseas buscar? \n>")
    existe = False
    archivo = open("data/contactos.csv", "r")
    lineapartida = ("id","nombre","telefono")

    while lineapartida[0] != "" and lineapartida[0] != " ":
        if nombre == lineapartida[1]:
            existe = True
            print (lineapartida[1] + "\t" + lineapartida[2])
        linea = archivo.readline()
        lineapartida = linea.split(",")

    if not existe:
        print ("El contacto " + nombre+" no existe ")



def decidir(opcion):

    if opcion == 1:
        listar()
    elif opcion == 2:
        agregar()
    else:
        buscar()

