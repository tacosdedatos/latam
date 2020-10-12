"""Estados Unidos Mexicanos"""
import datetime as dt

from pytz import timezone

from ..entidades import Ciudad, Pais, Subdivision

aguascalientes = Ciudad(
    nombre="Ciudad de Aguascalientes",
    nombre_comun="Aguascalientes",
    otros_nombres=["Ciudad de la gente buena"],
    abrev="AGS",
    nombre_pronunciacion_local="a.ɣ̞was.ka'.ljen̟.tes",
    fecha_de_fundacion=dt.date(1575, 10, 22),
    huso_horario=timezone("America/Mexico_City"),
    latlong=(21.88, -102.29),
)

AGU = Subdivision(
    nombre="Aguascalientes",
    nombre_comun="Aguascalientes",
    abrev="AGS",
    nombre_pronunciacion_local="a.ɣ̞was.ka'.ljen̟.tes",
    codigo="AGU",
    capital=aguascalientes,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=aguascalientes.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1857, 2, 5),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Ciudad de Aguascalientes": aguascalientes},
)

tjjuana = Ciudad(
    nombre="Tijuana",
    nombre_comun="Tijuana",
    otros_nombres=["Rancho Tía Juana"],
    abrev="Tj",
    nombre_pronunciacion_local="ti.'xwa.na",
    latlong=(32.52, -117.05),
    fecha_de_fundacion=dt.date(1889, 7, 11),
    huso_horario=timezone("America/Tijuana"),
)

mexicali = Ciudad(
    nombre="Mexicali",
    nombre_comun="Mexicali",
    otros_nombres=["Chicali"],
    abrev="Mxli",
    nombre_pronunciacion_local="me.xi.'ka.li",
    latlong=(32.67, -115.47),
    fecha_de_fundacion=dt.date(1903, 3, 14),
    huso_horario=timezone("America/Tijuana"),
)

BC = Subdivision(
    nombre="Baja California",
    nombre_comun="Baja California",
    abrev="BC",
    nombre_pronunciacion_local="'ba.xa. ka.li'.for.nja",
    codigo="BCN",
    capital=mexicali,
    capital_horario=timezone("America/Tijuana"),
    capital_latlong=mexicali.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1952, 1, 16),
    husos_horarios=[timezone("America/Tijuana")],
    ciudades_grandes={"Tijuana": tjjuana},
)

la_paz = Ciudad(
    nombre="La Paz",
    nombre_comun="La Paz",
    otros_nombres=[],
    abrev="LAP",
    nombre_pronunciacion_local="la 'pas",
    latlong=(24.14, -110.31),
    fecha_de_fundacion=dt.date(1535, 5, 3),
    huso_horario=timezone("America/Hermosillo"),
)

BCS = Subdivision(
    nombre="Baja California Sur",
    nombre_comun="Baja California Sur",
    abrev="BCS",
    nombre_pronunciacion_local="'ba.xa. ka.li'.for.nja 'sur",
    codigo="BCS",
    capital=la_paz,
    capital_horario=timezone("America/Hermosillo"),
    capital_latlong=la_paz.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1974, 10, 8),
    husos_horarios=[timezone("America/Hermosillo")],
    ciudades_grandes={"La Paz": la_paz},
)

campeche = Ciudad(
    nombre="San Francisco de Campeche",
    nombre_comun="Campeche",
    otros_nombres=["Ahk'ìin Pech (Maya Yucateco)"],
    abrev="CPE",
    nombre_pronunciacion_local="kam'.pe.tʃe",
    latlong=(19.85, -90.53),
    fecha_de_fundacion=dt.date(1540, 10, 4),
    huso_horario=timezone("America/Mexico_City"),
)
CAM = Subdivision(
    nombre="Campeche",
    nombre_comun="Campeche",
    abrev="CAM",
    nombre_pronunciacion_local="kam'pe.tʃe",
    codigo="CAM",
    capital=campeche,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=campeche.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1863, 4, 29),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Campeche": campeche},
)

tuxtla_gutierrez = Ciudad(
    nombre="Tuxtla Gutiérrez",
    nombre_comun="Tuxtla Gutiérrez",
    otros_nombres=[],
    abrev="TUX",
    nombre_pronunciacion_local="tuks'.tla ɣ̞w.tie'.řeθ",
    latlong=(16.75, -93.12),
    fecha_de_fundacion=dt.date(1848, 5, 31),
    huso_horario=timezone("America/Mexico_City"),
)

CHIS = Subdivision(
    nombre="Chiapas",
    nombre_comun="Chiapas",
    abrev="CHIS",
    nombre_pronunciacion_local="tʃjap'.as",
    codigo="CHP",
    capital=tuxtla_gutierrez,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=tuxtla_gutierrez.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1824, 9, 14),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Tuxtla Gutiérrez": tuxtla_gutierrez},
)

chihuahua = Ciudad(
    nombre="Chihuahua",
    nombre_comun="Chihuahua",
    otros_nombres=[],
    abrev="Chih",
    nombre_pronunciacion_local="tʃi'.wa.wa",
    latlong=(28.64, -106.09),
    fecha_de_fundacion=dt.date(1709, 10, 12),
    huso_horario=timezone("America/Chihuahua"),
)

CHIH = Subdivision(
    nombre="Chihuahua",
    nombre_comun="Chihuahua",
    abrev="CHIH",
    nombre_pronunciacion_local="tʃi'.wa.wa",
    codigo="CHH",
    capital=chihuahua,
    capital_horario=timezone("America/Chihuahua"),
    capital_latlong=chihuahua.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1824, 7, 6),
    husos_horarios=[timezone("America/Chihuahua")],
    ciudades_grandes={"Chihuahua": chihuahua},
)

saltillo = Ciudad(
    nombre="Saltillo",
    nombre_comun="Saltillo",
    otros_nombres=["Las Antenas de México"],
    abrev="SAL",
    nombre_pronunciacion_local="sal'.ti.ʝo",
    latlong=(25.43, -101.00),
    fecha_de_fundacion=dt.date(1577, 7, 25),
    huso_horario="America/Chihuahua",
)

COAH = Subdivision(
    nombre="Coahuila de Zaragoza",
    nombre_comun="Coahuila",
    abrev="COAH",
    nombre_pronunciacion_local="koa'.wj.la ðe θa.ra'.ɣ̞o.θa",
    codigo="COA",
    capital=saltillo,
    capital_horario=timezone("America/Chihuahua"),
    capital_latlong=saltillo.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1824, 5, 7),
    husos_horarios=[timezone("America/Chihuahua")],
    ciudades_grandes={"Salitllo": saltillo},
)

MEX = Pais(
    nombre="Estados Unidos Mexicanos",
    nombre_comun="México",
    nombre_pronunciacion_local="'me.xi.ko",
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
    subdivisiones={
        "Aguascalientes": AGU,
        "Baja California": BC,
        "Baja California Sur": BCS,
        "Campeche": CAM,
        "Chiapas": CHIS,
        "Cihuahua": CHIH,
        "Coahuila": COAH,
    },
)
