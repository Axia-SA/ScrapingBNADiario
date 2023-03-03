#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup


class Moneda:
    compra = 0
    venta = 0
    idMoneda = ''
    fecha = ''
    def __init__(self, idDivisa, valorCompra, valorVenta, fecha, nombreDivisa):
        self.idMoneda = idDivisa
        self.compra = valorCompra
        self.venta = valorVenta
        self.fecha = fecha
        self.nombreDivisa = nombreDivisa

def buildClass(nombreDivisa, valorCompra, valorVenta, fecha):
    idDivisa = 0
    agregar = 0
    if nombreDivisa == "Dolar U.S.A":
        idDivisa = 2
        nombreDivisa = 'Dolar'
        agregar = True
    if nombreDivisa == "Real (*)":
        idDivisa = 4
        agregar = True
        nombreDivisa = 'Real'
    if nombreDivisa == "Euro":
        idDivisa = 3
        agregar = True
        nombreDivisa = 'Euro'
    if nombreDivisa == "Libra Esterlina":
        idDivisa = 5
        agregar = True
        nombreDivisa = 'Libra Esterlina'
    if nombreDivisa == "Real *":
        idDivisa = 4
        agregar = True
        nombreDivisa = 'Real'
    if (agregar is True):
        return Moneda(idDivisa, valorCompra, valorVenta, fecha, nombreDivisa)
    else:
        return None

def postDataToServer(vectorMoneda):
     for row in vectorMoneda:
        s = json.dumps(row.__dict__)
        print('DATA -> ' + s)
        headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
        # Completar la URL de envío
        # r = requests.post("__my_url__", data=s, headers=headers)
        # print(r.status_code, r.reason)

# Realizar solicitud GET a la URL
url = "https://www.bna.com.ar/Personas"
response = requests.get(url)

# Analizar el contenido HTML de la respuesta
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar la tabla de cotizaciones
table_divisa = soup.find('div', {'id': 'divisas'})
table_billete = soup.find('div', {'id': 'billetes'})

# Obtener la segunda fila de la tabla
rows = table_divisa.find_all('tr')
row2 = rows[1]
row3 = rows[2]
row4 = rows[3]

rows_billete = table_billete.find_all('tr')
row_billete = rows_billete[3]

# Obtener el valor de las filas
column1_usd = row2.find_all('td')[0].text
column2_usd = row2.find_all('td')[1].text.replace(",",".")
column3_usd = row2.find_all('td')[2].text.replace(",",".")

column1_eur = row3.find_all('td')[0].text
column2_eur = row3.find_all('td')[1].text.replace(",",".")
column3_eur = row3.find_all('td')[2].text.replace(",",".")

column1_gbp = row4.find_all('td')[0].text
column2_gbp = row3.find_all('td')[1].text.replace(",",".")
column3_gbp = row4.find_all('td')[2].text.replace(",",".")

column1_bra = row_billete.find_all('td')[0].text
column2_bra = row_billete.find_all('td')[1].text.replace(",",".")
column3_bra = row_billete.find_all('td')[2].text.replace(",",".")

# Obtener valor de fecha D/M/YYYY
fecha_cot = soup.find('th', {'class': 'fechaCot'}).text
# Convertir a formato de fecha ISO-8601
fecha_cot = fecha_cot.split("/")[2].zfill(2) + "-" + fecha_cot.split("/")[1].zfill(2) + "-" + fecha_cot.split("/")[0].zfill(2)
print("Fecha: ", fecha_cot)

vectDivisa = []
# Imprimir los valores obtenidos y agregar los valores a un vector de Moneda()
print(column1_usd, " : ", column2_usd, " : ", column3_usd)
res = buildClass(column1_usd, column2_usd, column3_usd, fecha_cot)
if (res is not None):
    vectDivisa.append(res)

print(column1_eur, " : ", column2_eur, " : ", column3_eur)
res = buildClass(column1_eur, column2_eur, column3_eur, fecha_cot)
if (res is not None):
    vectDivisa.append(res)

print(column1_gbp, " : ", column2_gbp, " : ", column3_gbp)
res = buildClass(column1_gbp, column2_gbp, column3_gbp, fecha_cot)
if (res is not None):
    vectDivisa.append(res)

print(column1_bra, " : ", float(column2_bra)/100, " : ", float(column3_bra)/100)
res = buildClass(column1_bra, float(column2_bra)/100, float(column3_bra)/100, fecha_cot)
if (res is not None):
    vectDivisa.append(res)

# print("=================================================")
# print("    POST DATA    ")
# print("=================================================")
# postDataToServer(vectDivisa)
