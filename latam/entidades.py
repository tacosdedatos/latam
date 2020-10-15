"""Módulo con las clases base de cada entidad: `Ciudad`, `Subdivision`, `Pais`."""

from typing import Dict, List, Optional, Tuple

import datetime as dt
from dataclasses import dataclass

import pandas as pd


@dataclass
class Ciudad:
    """Clase base para una Ciudad.

    Atributos
    ---------
    nombre: str
        El nombre oficial de la ciudad. Por ejemplo, Ciudad Autónoma de Buenos Aires en lugar de Buenos Aires.
    nombre_comun: str
        El nombre de la ciudad (puede ser el mismo que el oficial). Por ejemplo, Buenos Aires en lugar de Ciudad Autónooma de Buenos Aires.
    otros_nombres: Optional[List[str]]
        Lista de otros nombres por los que se le conoce a la ciudad. Por ejemplo, a Lima, Perú se le conoce como Ciudad de los Reyes y La Perla del Pacīfico.
    abrev: str
        Abreviación del nombre.
    nombre_pronunciacion_local: str
        Pronunciación (fonética) del nombre en el idioma local.
    latlong: tuple
        Latitud y longitud de la ciudad. En ESPG:4326.
    fecha_de_fundacion; datetime.date
        Fecha en la que la ciudad fue fundada.
    huso_horario: pytz.timezone
        Huso horario en el que se encuentra la ciudad.
    """

    nombre: str
    nombre_comun: str
    otros_nombres: Optional[List[str]]
    abrev: str
    nombre_pronunciacion_local: str
    latlong: Tuple[float, float]
    fecha_de_fundacion: dt.date
    huso_horario: dt.tzinfo

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.nombre_comun}>"


@dataclass
class Subdivision:
    """Clase base para una Subdivisión. Estas son entidades subnacionales como estados, distritos, provincias, etc.

    Atributos
    ---------
    nombre: str
        El nombre oficial de la ciudad. Por ejemplo, Ciudad Autónoma de Buenos Aires en lugar de Buenos Aires.
    nombre_comun: str
        El nombre de la ciudad (puede ser el mismo que el oficial). Por ejemplo, Buenos Aires en lugar de Ciudad Autónooma de Buenos Aires.
    nombres_nativos: Dict[str, str]
        Nombre otorgado a la subdivisión por los nativos de la región. Por ejemplo, el estado de Durango, México es conocido como Korian en Tepehuán y Tepēhuahcān en Nahuatl.
        El diccionario tiene como llave (key) la lengua nativa y el valor (value) es el nombre de la subdivisión en dicha lengua.
        Ejemplo:
            DUR = Subdivision(..., nombres_nativos={"Tepehuán": "Korian", "Nahuatl": "Tepēhuahcān"}, ...)
    abrev: str
        Abreviación del nombre.
    nombre_pronunciacion_local: str
        Pronunciación (fonética) del nombre en el idioma local.
    codigo: str
        Código de 3 caracteres según el formato ISO-3611-2.
    codigo_numerico: int
        Código númerico asociado con esta subdivisión. Estos se utilizarán para servir los datos geográficos. Por ejemplo, el código ISO-3611-2 de Baja California, México es MX-BCN y su código númerico sería el código de México (484) y el de Baja California (002), o sea 484002.
    capital: Ciudad
        La capital en forma de objeto latam.entidades.Ciudad.
    capital_horario: pytz.timezone
        Huso horario de la capital.
    capital_latlong: tuple
        Latitud y longitud de la capital. En ESPG:4326.
    es_contigua: bool
        Si la subdivisión es parte de la masa terrestre principal del país. De lo contrario sería una isla. Por ejemplo, Cuba tiene 15 provincias contiguas (parte de la isla principal) y una provincia que en sí es isla.
    es_isla: bool
        Si la subdivisión es una isla por si sola.
    fecha_de_fundacion; datetime.date
        Fecha en la que la ciudad fue fundada.
    husos_horarios: List[pytz.timezone]
        Huso horarios de la subdivisión. En general, cada subdivisión tiene un solo huso horario pero no siempre.
    ciudades_grandes: Dict[str, Ciudad]
        Diccionario de ciudades grandes en esta subdivisión.
    """

    nombre: str
    nombre_comun: str
    nombres_nativos: Dict[str, str]
    abrev: str
    nombre_pronunciacion_local: str
    codigo: str
    codigo_numerico: int
    capital: Ciudad
    capital_horario: dt.tzinfo
    capital_latlong: Tuple[float, float]
    es_contigua: bool
    es_isla: bool
    fecha_de_fundacion: dt.date
    husos_horarios: List[dt.tzinfo]
    ciudades_grandes: Dict[str, Ciudad]

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.nombre_comun}>"


@dataclass
class Pais:
    """Clase base para un País.

    Atributos
    ---------
    nombre: str
        El nombre oficial de la ciudad. Por ejemplo, Ciudad Autónoma de Buenos Aires en lugar de Buenos Aires.
    nombre_comun: str
        El nombre de la ciudad (puede ser el mismo que el oficial). Por ejemplo, Buenos Aires en lugar de Ciudad Autónooma de Buenos Aires.
    abrev: str
        Abreviación del nombre.
    nombre_pronunciacion_local: str
        Pronunciación (fonética) del nombre en el idioma local.
    alpha-2: str
        Código de dos letras para el país según el formato ISO-3611-1.
    alpha-3: str
        Código de tres letras para el país según el formato ISO-3611-1.
    codigo: str
        Código de 3 dígitos según el formato ISO-3611-2.
    capital: Ciudad
        La capital en forma de objeto latam.entidades.Ciudad.
    capital_horario: pytz.timezone
        Huso horario de la capital.
    capital_latlong: tuple
        Latitud y longitud de la capital. En ESPG:4326.
    es_independiente: bool
        Si la nación es independiente. Por ejemplo, Puerto Rico es parte del *commonwealth* de los Estados Unidos.
    fecha_de_independencia: Optional[datetime.date]
        Fecha de independencia de la nación.
    es_isla: bool
        Si el país es una isla.
    husos_horarios: List[pytz.timezone]
        Huso horarios de la subdivisión. En general, cada subdivisión tiene un solo huso horario pero no siempre.
    subdivisiones: Dict[str, Subdivision]
        Diccionario de subdivisiones que comprenden el país.
    df: pandas.DataFrame
        Un DataFrame de pandas de una fila con la información del país.
    subdivisiones_df: pandas.DataFrame
        Un DataFrame de pandas con la información de cada subdivision el país.
    """

    nombre: str
    nombre_comun: str
    abrev: str
    nombre_pronunciacion_local: str
    alpha_2: str
    alpha_3: str
    codigo: str
    capital: str
    capital_horario: dt.tzinfo
    capital_latlong: Tuple[float, float]
    es_independiente: bool
    fecha_independencia: Optional[dt.date]
    es_isla: bool
    husos_horarios: List[dt.tzinfo]
    subdivisiones: Dict[str, Subdivision]

    def __repr__(self):
        return f"<{self.__class__.__name__}:{self.nombre_comun}>"

    def _pais_df(self) -> pd.DataFrame:
        pais_data = {
            "abrev": self.abrev,
            "alpha_2": self.alpha_2,
            "alpha_3": self.alpha_3,
            "capital": self.capital,
            "capital_horario": self.capital_horario,
            "capital_lat": self.capital_latlong[0],
            "capital_long": self.capital_latlong[1],
            "codigo": self.codigo,
            "es_independiente": self.es_independiente,
            "es_isla": self.es_isla,
            "fecha_independencia": self.fecha_independencia,
            "huso_horario": self.husos_horarios,
            "nombre": self.nombre,
            "nombre_comun": self.nombre_comun,
            "nombre_pronunciacion_local": self.nombre_pronunciacion_local,
            "subdivisiones": [
                subdivision.nombre
                for subdivision in self.subdivisiones.values()
            ],
        }
        return pd.DataFrame(data=[pais_data])

    def _subdivision_df(self) -> pd.DataFrame:
        subdivision_data = []
        for key, subdivision in self.subdivisiones.items():
            subdivision_data.append(
                {
                    "abrev": subdivision.abrev,
                    "capital": subdivision.capital.nombre,
                    "capital_horario": subdivision.capital_horario,
                    "capital_lat": subdivision.capital_latlong[0],
                    "capital_long": subdivision.capital_latlong[1],
                    "alpha_2": subdivision.codigo,
                    "codigo_numerico": subdivision.codigo_numerico,
                    "es_contigua": subdivision.es_contigua,
                    "es_isla": subdivision.es_isla,
                    "fecha_de_fundacion": subdivision.fecha_de_fundacion,
                    "huso_horario": subdivision.husos_horarios[0],
                    "nombre": subdivision.nombre,
                    "nombre_comun": subdivision.nombre_comun,
                    "nombre_pronunciacion_local": subdivision.nombre_pronunciacion_local,
                    "nombres_nativos": ",".join(
                        [
                            f"{value} ({key})"
                            for key, value in subdivision.nombres_nativos.items()
                        ]
                    ),
                }
            )
        return pd.DataFrame(subdivision_data)

    def __post_init__(self):
        self.df = self._pais_df()
        self.subdivisiones_df = self._subdivision_df()
