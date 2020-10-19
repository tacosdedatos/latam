"""República de Guatemala. Quauhtlemallan.

|   Departamento      |         Cabecera            |
|:-------------------:|:---------------------------:|
|   Petén             |     Flores                  |
|   Huehuetenango     |     Huehuetenango           |
|   Quiché            |     Santa Cruz del Quiché   |
|   Alta Verapaz      |     Cobán                   |
|   Izabal            |     Puerto Barrios          |
|   San Marcos        |     San Marcos              |
|   Quetzaltenango    |     Quetzaltenango          |
|   Totonicapán       |     Totonicapán             |
|   Sololá            |     Sololá                  |
|   Chimaltenango     |     Chimaltenango           |
|   Sacatepéquez      |     Antigua Guatemala       |
|   Guatemala         |     Ciudad de Guatemala     |
|   Baja Verapaz      |     Salamá                  |
|   El Progreso       |     Guastatoya              |
|   Jalapa            |     Jalapa                  |
|   Zacapa            |     Zacapa                  |
|   Chiquimula        |     Chiquimula              |
|   Retalhuleu        |     Retalhuleu              |
|   Suchitepéquez     |     Mazatenango             |
|   Escuintla         |     Escuintla               |
|   Santa Rosa        |     Cuilapa                 |
|   Jutiapa           |     Jutiapa                 |
"""

import datetime as dt

from pytz import timezone

from ..entidades import Ciudad, Pais, Subdivision

ciudad_flores = Ciudad(
    nombre="Ciudad Flores",
    nombre_comun="Flores",
    otros_nombres=[],
    abrev="FLO",
    nombre_pronunciacion_local="flo'.res",
    fecha_de_fundacion=dt.date(
        1831, 5, 2
    ),  # https://guatehistoria.com/datos-historicos-del-peten/
    huso_horario=timezone("America/Guatemala"),
    latlong=(16.93, -89.88),
)

PE = Subdivision(
    nombre="Petén",
    nombre_comun="Petén",
    nombres_nativos={"Itzá": "Noj Petén"},
    abrev="PET",
    nombre_pronunciacion_local="pet.'en",
    codigo="PE",
    codigo_numerico=17,
    capital=ciudad_flores,
    capital_horario=timezone("America/Guatemala"),
    capital_latlong=ciudad_flores.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(
        1697, 3, 14
    ),  # https://guatehistoria.com/datos-historicos-del-peten/
    husos_horarios=[timezone("America/Guatemala")],
    ciudades_grandes={"Ciudad Flores": ciudad_flores},
)

huehuetenango = Ciudad(
    nombre="Huehuetenango",
    nombre_comun="Huehuetenango",
    otros_nombres=["Xinabajul"],
    abrev="HUE",
    nombre_pronunciacion_local="we.we.te.'nan.ɡo",
    fecha_de_fundacion=dt.date(1866, 11, 23),
    huso_horario=timezone("America/Guatemala"),
    latlong=(15.31, -91.48),
)

HU = Subdivision(
    nombre="Huehuetenango",
    nombre_comun="Huehuetenango",
    nombres_nativos={"Mam": "Xinabajul"},
    abrev="HUE",
    nombre_pronunciacion_local="we.we.te.'nan.ɡo",
    codigo="HU",
    codigo_numerico=13,
    capital=huehuetenango,
    capital_horario=timezone("America/Guatemala"),
    capital_latlong=huehuetenango.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1866, 5, 8),
    husos_horarios=[timezone("America/Guatemala")],
    ciudades_grandes={"Huehuetenango": huehuetenango},
)
