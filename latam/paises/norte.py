import datetime as dt

from pytz import timezone

from ..entidades import Ciudad, Pais, Subdivision

tjjuana = Ciudad(
    nombre="Tijuana",
    nombre_comun="Tijuana",
    otros_nombres=["Rancho Tía Juana"],
    abrev="Tj",
    nombre_pronunciacion_local="Tijuana",
    latlong=(32.52, -117.05),
    fecha_de_fundacion=dt.date(1889, 7, 11),
    huso_horario=timezone("America/Tijuana"),
)

mexicali = Ciudad(
    nombre="Mexicali",
    nombre_comun="Mexicali",
    otros_nombres=["Chicali"],
    abrev="Mxli",
    nombre_pronunciacion_local="Mejicali",
    latlong=(32.67, -115.47),
    fecha_de_fundacion=dt.date(1903, 3, 14),
    huso_horario=timezone("America/Tijuana"),
)

BC = Subdivision(
    nombre="Baja California",
    nombre_comun="Baja California",
    abrev="BC",
    nombre_pronunciacion_local="Baja California",
    codigo="BCN",
    capital=mexicali,
    capital_horario=timezone("America/Tijuana"),
    capital_latlong=(32.64, -115.45),
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1952, 1, 16),
    husos_horarios=[timezone("America/Tijuana")],
    ciudades_grandes={"Tijuana": tjjuana},
)

Mexico = Pais(
    nombre="Estados Unidos Mexicanos",
    nombre_comun="México",
    nombre_pronunciacion_local="Méjico",
    abrev="Mex",
    alpha_2="MX",
    alpha_3="MEX",
    codigo="484",
    capital="Ciudad de México",
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=(19.43, -99.13),
    es_independiente=True,
    fecha_independencia=dt.date(1810, 9, 16),
    es_isla=False,
    husos_horarios=[
        timezone("America/Tijuana"),
        timezone("America/Hermosillo"),
        timezone("America/Mexico_City"),
    ],
    subdivisiones={"Baja California": BC},
)
