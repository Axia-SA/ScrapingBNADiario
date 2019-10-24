#!/usr/bin/python3
# -*- encoding: utf-8 -*-
# -*- coding: utf-8 -*- 
import scrapy
import json
#import requests  <-- Descomentar para enviar los datos obtenidos por POST

class Moneda:
    compra = ''
    venta = ''
    idMoneda = ''
    fecha = ''
    def __init__(self, idD, c, v, f, nD):
        self.idMoneda = idD
        self.compra = c
        self.venta = v
        self.fecha = f
        self.nombreDivisa = nD

# Obtiene de la página del Banco Nación las cotizaciones de las divisas, y la cotización
# de billetes del Real (dividido por 100).
# Posteriormente realiza un POST al backend del sistema de Axia para guardar los datos

class BootstrapTableSpider(scrapy.Spider):
    name = "tabla"

    def start_requests(self):
        urls = [
            'https://www.bna.com.ar',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        fecha = ''
        m = []

        for row in response.xpath('//*[@id="divisas"]//thead/tr'):
            fecha = row.xpath('th[1]//text()').extract_first()

        for row in response.xpath('//*[@id="divisas"]//tbody/tr'):
            divisa = row.xpath('td[1]//text()').extract_first()
            compra = row.xpath('td[2]//text()').extract_first()
            venta = row.xpath('td[3]//text()').extract_first()
            compra = compra.replace(',', '.')
            venta = venta.replace(',', '.')

            idDivisa = 0
            agregar = 0
            nombreDivisa = ''
            if divisa == "Dolar U.S.A":
                idDivisa = 2
                nombreDivisa = 'Dolar'
                agregar = 1
            if divisa == "Real (*)":
                idDivisa = 4
                agregar = 1
                nombreDivisa = 'Real'
                compra = float(compra)/100
                venta = float(venta)/100
            if divisa == "Euro":
                idDivisa = 3
                agregar = 1
                nombreDivisa = 'Euro'
            if divisa == "Libra Esterlina":
                idDivisa = 5
                agregar = 1
                nombreDivisa = 'Libra Esterlina'

            if agregar:
                tmp = Moneda(idDivisa, float(compra), float(venta), fecha, nombreDivisa)
                m.append(tmp)


        for row in response.xpath('//*[@id="billetes"]//thead/tr'):
            fecha = row.xpath('th[1]//text()').extract_first()

        # Como la cotizacion de divisas no posee el Real, este se obtiene de la cotizacion de billetes
        for row in response.xpath('//*[@id="billetes"]//tbody/tr'):
            divisa = row.xpath('td[1]//text()').extract_first()
            compra = row.xpath('td[2]//text()').extract_first()
            venta = row.xpath('td[3]//text()').extract_first()
            compra = compra.replace(',', '.')
            venta = venta.replace(',', '.')

            idDivisa = 0
            agregar = 0
            if divisa == "Real *":
                idDivisa = 4
                agregar = 1
                nombreDivisa = 'Real'
                compra = float(compra)/100
                venta = float(venta)/100

            if agregar:
                tmp = Moneda(idDivisa, float(compra), float(venta), fecha, nombreDivisa)
                m.append(tmp)


        for row in m:
            s = json.dumps(row.__dict__)
            print('DATA -> ' + s)
            # Enviar los datos obtenidos por POST al backend de un sistema
            # headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}  <- Cabeceras
            # r = requests.post("http://url.com/backend/my_endpoint", data=s, headers=headers)
            # print(r.status_code, r.reason)

