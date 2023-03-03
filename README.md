# ScrapingBNA Diario
Herramienta para obtener la cotización de divisas y billetes en forma directa desde la página web del *Banco de la Nación Argentina*

Ideal para tener un `crontab` o tarea programada que diariamente obtenga el valor del tipo de cambio para todas las divisas presentadas en la página.
Por defecto obtiene los valores del Dólar, Euro, Real (dividido por 100) y Libra Esterlina.

Emplea la biblioteca **requests** para realizar un POST de los valores y persistirlos en una base de datos o utilizarlo en un sistema tipo API-REST.


## Requerimientos

- Python >= 3
- [BeautifulSoup]
- requests

## Ejecutar el script!

Ejecutar `./main.py` (o `python main.py`) verificando que la ruta al archivo esté corregida dentro del archivo `main.py`.

De otro modo, ejecutar directamente `scrapCotizacionBna.py`

----
## Lista de cambios
- Reemplazo de [Scrapy] por [BeautifulSoup]

Al ejecutar el script devolverá la información de las cotizaciones obtenidas y la fecha en formato ISO-8601:
```
Fecha:  2023-03-03
Dolar U.S.A  :  197.6700  :  197.8700
Libra Esterlina  :  235.7412  :  236.5734
Euro  :  235.7412  :  209.6037
Real *  :  37.1  :  41.1
```

Si se habilita llamada a la función `postDataToServer()`, la misma enviará los datos por JSON a un servidor, y mostrará en pantalla los datos del JSON enviado y el código de estado de la llamada.
```
=================================================
    POST DATA    
=================================================
DATA -> {"idMoneda": 2, "compra": "197.6700", "venta": "197.8700", "fecha": "2023-03-03", "nombreDivisa": "Dolar"}
200 OK
DATA -> {"idMoneda": 5, "compra": "235.7412", "venta": "236.5734", "fecha": "2023-03-03", "nombreDivisa": "Libra Esterlina"}
200 OK
DATA -> {"idMoneda": 3, "compra": "235.7412", "venta": "209.6037", "fecha": "2023-03-03", "nombreDivisa": "Euro"}
200 OK
DATA -> {"idMoneda": 4, "compra": 37.1, "venta": 41.1, "fecha": "2023-03-03", "nombreDivisa": "Real"}
200 OK
```

[//]: #
   [Scrapy]: <https://scrapy.org>
   [BeautifulSoup]: <https://scrapy.org>
