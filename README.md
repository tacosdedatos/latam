# latam

<div align="center">

[![Build status](https://github.com/tacosdedatos/latam/workflows/build/badge.svg?branch=master&event=push)](https://github.com/tacosdedatos/latam/actions?query=workflow%3Abuild)
[![Documentation Status](https://readthedocs.org/projects/python-latam/badge/?version=latest)](https://python-latam.readthedocs.io/es/latest/?badge=latest)
[![Python Version](https://img.shields.io/pypi/pyversions/latam.svg)](https://pypi.org/project/latam/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/tacosdedatos/latam/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Security: bandit](https://img.shields.io/badge/security-bandit-green.svg)](https://github.com/PyCQA/bandit)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/tacosdedatos/latam/blob/master/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%F0%9F%9A%80-semantic%20versions-informational.svg)](https://github.com/tacosdedatos/latam/releases)
[![License](https://img.shields.io/github/license/tacosdedatos/latam)](https://github.com/tacosdedatos/latam/blob/master/LICENSE)

Un paquete para trabajar facilmente con metadatos de paises en latinoamerica.
</div>

## ¿Qué trae?

`latam` viene con 3 tipos de entidades: `Ciudad`, `Subdivision` y `Pais`.

Un `Pais` viene con la siguiente información:
```json
{
  "nombre": "Estados Unidos Mexicanos",
  "nombre_comun": "México",
  "abrev": "Mex",
  "nombre_pronunciacion_local": "'me.xi.ko",
  "alpha_2": "MX",
  "alpha_3": "MEX",
  "codigo": "484",
  "capital": "Ciudad de México",
  "capital_horario": "<class 'pytz.tzfile.America/Mexico_City'>",
  "capital_latlong": [
    19.43,
    -99.13
  ],
  "es_independiente": true,
  "fecha_independencia": "<class 'datetime.date'>",
  "es_isla": false,
  "husos_horarios": [
    "<class 'pytz.tzfile.America/Tijuana'>",
    "<class 'pytz.tzfile.America/Hermosillo'>",
    "<class 'pytz.tzfile.America/Mexico_City'>",
    "<class 'pytz.tzfile.America/Cancun'>"
  ],
  "subdivisiones": {
    "Aguascalientes": "<class 'latam.entidades.Subdivision'>",
    "Baja California": "<class 'latam.entidades.Subdivision'>",
    "Baja California Sur": "<class 'latam.entidades.Subdivision'>",
    "Campeche": "<class 'latam.entidades.Subdivision'>",
    "Chiapas": "<class 'latam.entidades.Subdivision'>",
    "Cihuahua": "<class 'latam.entidades.Subdivision'>",
    "Coahuila": "<class 'latam.entidades.Subdivision'>",
    "Colima": "<class 'latam.entidades.Subdivision'>",
    "Durango": "<class 'latam.entidades.Subdivision'>",
    "Guanajuato": "<class 'latam.entidades.Subdivision'>",
    "Guerrero": "<class 'latam.entidades.Subdivision'>",
    "Hidalgo": "<class 'latam.entidades.Subdivision'>",
    "Jalisco": "<class 'latam.entidades.Subdivision'>",
    "Estado de México": "<class 'latam.entidades.Subdivision'>",
    "Ciudad de México": "<class 'latam.entidades.Subdivision'>",
    "Michoacán": "<class 'latam.entidades.Subdivision'>",
    "Morelos": "<class 'latam.entidades.Subdivision'>",
    "Nayarit": "<class 'latam.entidades.Subdivision'>",
    "Nuevo León": "<class 'latam.entidades.Subdivision'>",
    "Oaxaca": "<class 'latam.entidades.Subdivision'>",
    "Puebla": "<class 'latam.entidades.Subdivision'>",
    "Queretaro": "<class 'latam.entidades.Subdivision'>",
    "Quintana Roo": "<class 'latam.entidades.Subdivision'>",
    "San Luis Potosí": "<class 'latam.entidades.Subdivision'>",
    "Sinaloa": "<class 'latam.entidades.Subdivision'>",
    "Sonora": "<class 'latam.entidades.Subdivision'>",
    "Tabasco": "<class 'latam.entidades.Subdivision'>",
    "Tamaulipas": "<class 'latam.entidades.Subdivision'>",
    "Tlaxcala": "<class 'latam.entidades.Subdivision'>",
    "Veracrz": "<class 'latam.entidades.Subdivision'>",
    "Yucatán": "<class 'latam.entidades.Subdivision'>",
    "Zacatecas": "<class 'latam.entidades.Subdivision'>"
  },
  "df": "<class 'pandas.core.frame.DataFrame'>",
  "subdivisiones_df": "<class 'pandas.core.frame.DataFrame'>"
}
```

Una `Subdivision` viene con la siguiente información:
```json
{
  "nombre": "Baja California",
  "nombre_comun": "Baja California",
  "nombres_nativos": {},
  "abrev": "BC",
  "nombre_pronunciacion_local": "'ba.xa. ka.li'.for.nja",
  "codigo": "BCN",
  "codigo_numerico": 2,
  "capital": "<class 'latam.entidades.Ciudad'>",
  "capital_horario": "<class 'pytz.tzfile.America/Tijuana'>",
  "capital_latlong": [
    32.67,
    -115.47
  ],
  "es_contigua": true,
  "es_isla": false,
  "fecha_de_fundacion": "<class 'datetime.date'>",
  "husos_horarios": [
    "<class 'pytz.tzfile.America/Tijuana'>"
  ],
  "ciudades_grandes": {
    "Tijuana": "<class 'latam.entidades.Ciudad'>"
  }
}
```
Una `Ciudad` viene con la siguiente información:
```json
{
  "nombre": "Mexicali",
  "nombre_comun": "Mexicali",
  "otros_nombres": [
    "Chicali"
  ],
  "abrev": "Mxli",
  "nombre_pronunciacion_local": "me.xi.'ka.li",
  "latlong": [
    32.67,
    -115.47
  ],
  "fecha_de_fundacion": "<class 'datetime.date'>",
  "huso_horario": "<class 'pytz.tzfile.America/Tijuana'>"
}
```
Entre otras cosas latam toma ventaja de ciertos estandares.

* Utilizamos `pytz` para incluir los husos horarios de cada `Ciudad`, `Subdivision` y `Pais`.
* Utilizamos objetos `datetime.date` para las fechas de fundación
* Utilizamos el formato EPSG:4326 o WSG84 para la latitud y longitud de cada `Ciudad`.
* Utilizamos el Alfabeto Fonético Internacional (AFI) para el atributo `.nombre_pronunciacion_local`.
* Cada `Subdivision` tiene el atributo `.codigo` y `.codigo_numerico` (las columnas `alpha_2` y `codigo_numerico` en `.subdivisiones_df`, respectivamente). El código (o `alpha_2` esta basado en la norma [ISO-3611-2](https://es.wikipedia.org/wiki/ISO_3166-2) para las subdivisiones y [ISO-3611-1](https://es.wikipedia.org/wiki/ISO_3166-1) para los paises.

## 📃 Citeishon

```
@misc{latam,
  author = {tacosdedatos},
  title = {Un paquete para trabajar facilmente con metadatos de países de Latinoamérica.},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/tacosdedatos/latam}}
}
```

> Este proyecto fue generado con [`python-package-template`](https://github.com/TezRomacH/python-package-template).
