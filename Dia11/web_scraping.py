##Buscar en una página de libreria los libros que tienen
## un rating de más de 4 estrellas

import bs4
import requests

#crear url sin numero de pagina
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'


#lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []
#iterar paginas
for pagina in range(1,51):
    #crear sopa en cada pag
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

    #seleccionar datos de los libros
    libros = sopa.select('.product_pod')

    #iterar los libros
    for libro in libros :
        #checker que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0 :
            #guardar titulo
            titulo_libro = libro.select('a')[1]['title']
            #agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

#ver libros recogidos
for t in titulos_rating_alto:
    print(t)





