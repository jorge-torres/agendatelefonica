#! /usr/bin/python
# -*- coding: utf-8 -*-

import modulo
import sys

volver = 1

while volver == 1:
    opcion = modulo.bienvenida()
    modulo.decidir(opcion)
    volver = input("si deseas volver al inicio presiona 1 sino presiona 2 \n> ")
    if volver == 2:
        break










