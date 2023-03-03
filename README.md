# ScrapingBNA Diario
Herramienta para obtener la cotización de divisas y billetes en forma directa desde la página web del *Banco de la Nación Argentina*

Ideal para tener un `crontab` o tarea programada que diariamente obtenga el valor del tipo de cambio para todas las divisas presentadas en la página.
Por defecto obtiene los valores del Dólar, Euro, Real (dividido por 100) y Libra Esterlina.

Incluye además la biblioteca **requests** para realizar un POST de los valores y persistirlos en una base de datos.


### Requerimientos

- Python >= 3
- [BeautifulSoup]
- requests

### Run the script!

Ejecutar `./main.py` (o `python main.py`) verificando que la ruta al archivo esté corregida.
De otro modo, ejecutar directamente `scrapCotizacionBna.py`

### Lista de cambios
- Reemplazo de [Scrapy] por [BeautifulSoup]


[//]: #
   [Scrapy]: <https://scrapy.org>
   [BeautifulSoup]: <https://scrapy.org>
