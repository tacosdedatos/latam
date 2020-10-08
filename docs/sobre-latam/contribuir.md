# Cómo contribuir

¡Las contribuciones son bienvenidas y muy agradecidas!
Todo ayuda y siempre vas a recibir 

¡Las contribuciones son bienvenidas y son muy apreciadas! Cada
ayuda un poco, y siempre se dará crédito.

Puedes contribuir de muchas maneras:

## Tipos de contribuciones

### Reportar _bugs_ o errores

Reportalos en <https://github.com/tacosdedatos/tacosdedatos-utils/issues>.

Si estas reportando un _bug_, porfa íncluye:

-   El nombre y versión de tu sistema operativo.
-   Cualquier detalle sobre su configuración local que pueda ser útil en
    solución de problemas.
-   Pasos detallados para reproducir el error.

### Corregir _bugs_ o errores

Puedes revistar los _issues_ en GitHub ([tacosdedatos/tacosdedatos-utils](https://github.com/tacosdedatos/tacosdedatos-utils/issues)).
Cualquiera con la etiqute _"bug"_ y _"ayuda pls"_ esta abierto a quien quiera implementar la solución.

### Implementar _Features_ o funciones 

Puedes revistar los _issues_ en GitHub ([tacosdedatos/tacosdedatos-utils](https://github.com/tacosdedatos/tacosdedatos-utils/issues)).
Cualquiera con la etiqute _"mejora"_ y _"ayuda pls"_ esta abierto a quien quiera implementar la solución.


### Escribir documenteishon

`tacosdedatos-utils` siempre puede utilizar más documentación. Ya sea en 
los _docs_ oficiales, en docstrings, o en la web con publicaciónes en blogs, artículos y mucho más.

### Enviar comentarios

La mejor manera de proveer retroalimentación es crear un _issue_ en 
<https://github.com/tacosdedatos/tacosdedatos-utils/issues>.

Si estás proponiendo una mejora:

-   Explica en detallo como va a funcionar.
-   Mantén el enfoque/alcance lo más estrecho posible para que sea más fácil
    implementar. 
-   Recuerde que este es un proyecto impulsado por voluntarixs, y que
    las contribuciones son bienvenidas :)

¡Comencemos!
------------

¿Listx para contribuir? Aquí esta como configurar [tacosdedatos-utils](#tacosdedatos-utils) 
para desarrollo local.

1.  Crea un _fork_ del repositorio en GitHub [tacosdedatos-utils]{#tacosdedatos-utils}.

2.  Clona tu _fork_ localmente:

        $ git clone https://github.com/tu_cuenta_de_github/tacosdedatos-utils.git

3.  Instala tu copia local en un entorno virtual. Con `tacosdedatos-utils` utilizamos `poetry`
    Asumiendo que lo tengas instalado, así es como configurars tu _fork_ para desarrollo local:

        $ cd tacosdedatos-utils/
        $ make install
        $ poetry shell # para activar tu entorno virtual 
    ```{admonition} Si no tienes instalado poetry
    Ejecuta el comando `make download-poetry`
    ```

4.  Crea una _branch_ para el desarrollo local:

        $ git checkout -b nombre-de-tu-mejora-o-correccion

    Ahora puedes hacer cambios locales.

5.  Cuando termines de hacer tus cambios, asegurate que tus cambios pasen
    los _tests_, el estilo de código y las medidas de seguridad que utilizamos en `tacosdedatos-utils`
    esto es fácil de hacer con los siguientes comando:

        $ make codestyle
        $ make tests
        $ make check-safety


6.  Haz _commit_ tus cambios y publicalos en tu _branch_ de GitHub:

        $ git add .
        $ git commit -m "Descripción detallada de tu mejora o arreglo de bug"
        $ git push origin nombre-de-tu-mejora-o-correccion

7.  Envía una _pull request_ a través de GitHub.


## Directríces de las _Pull Request_

Antes de enviar una _pull request_, verifica que cumpla lo siguiente:

1.  La _pull request_ debe incluir tests.
2.  Si tu _pull request_ agrega funcionalidad, la documentación debe ser actualizada.
    Agrega tu nueva funcionalidad en una función con una docstring, y agrega tu mejora
    en la lista en el `README.md`.
3.  La _pull request_ debería funcionar en Python 3.6+


## Tips

Para ejecutar los _tests_

    $ make tests


## Publicación

Un recordatorio para quienes mantienen el paquete. Asegurate que todos tus cambios esten
_cometidos_ (incluyendo una entrada a `sobre-tacosdedatos-utils/historia.md`).

Luego ejecuta:

    $ poetry version patch # opciones: major / minor / patch
    $ git tag -a <LA-NUEVA-VERSION-DEL-PAQUETE> -m "Versión <LA-NUEVA-VERSION-DEL-PAQUETE>"
    $ git push && git push --tags

El paquete será publicado a PyPI a través de GitHub Actions
