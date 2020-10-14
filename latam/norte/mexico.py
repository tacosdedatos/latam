"""Estados Unidos Mexicanos.

|       Estado (Abrev.)       |        Capital      |
|:---------------------------:|:--------------------|
| Aguascalientes (AGS)        |   Aguascalientes    |
| Baja California (BC)        |   Mexicali          |
| Baja California Sur (BCS)   |   La Paz            |
| Campeche (CAM)              |   Campeche          |
| Chiapas (CHIS)              |   Tuxtla Gutiérrez  |
| Chihuahua (CHIH)            |   Chihuahua         |
| Coahuila (COAH)             |   Saltillo          |
| Colima (COL)                |   Colima            |
| Durango (DUR)               |   Durango           |
| Guanajuato (GTO)            |   Guanajuato        |
| Guerrero (GRO)              |   Chilpancingo      |
| Hidalgo (HGO)               |   Pachuca           |
| Jalisco (JAL)               |   Guadalajara       |
| Estado de México (EM)       |   Toluca            |
| Ciudad de México (CDMX)     |   Mexico City       |
| Michoacán (MICH)            |   Morelia           |
| Morelos (MOR)               |   Cuernavaca        |
| Nayarit (NAY)               |   Tepic             |
| Nuevo León (NL)             |   Monterrey         |
| Oaxaca (OAX)                |   Oaxaca            |
| Puebla (PUE)                |   Puebla            |
| Querétaro (QRO)             |   Querétaro         |
| Quintana Roo (QR)           |   Chetumal          |
| San Luis Potosí (SLP)       |   San Luis Potosí   |
| Sinaloa (SNL)               |   Culiacán          |
| Sonora (SON)                |   Hermosillo        |
| Tabasco (TAB)               |   Villahermosa      |
| Tamaulipas (TAMPS)          |   Victoria          |
| Tlaxcala (TLAX)             |   Tlaxcala          |
| Veracruz (VER)              |   Xalapa            |
| Yucatán (YUC)               |   Mérida            |
| Zacatecas (ZAC)             |   Zacatecas         |
"""

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
    nombres_nativos={},
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
    nombres_nativos={},
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
    nombres_nativos={},
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
    nombres_nativos={},
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
    nombres_nativos={},
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
    nombres_nativos={},
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
    huso_horario=timezone("America/Chihuahua"),
)

COAH = Subdivision(
    nombre="Coahuila de Zaragoza",
    nombre_comun="Coahuila",
    nombres_nativos={},
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

colima = Ciudad(
    nombre="Colima",
    nombre_comun="Colima",
    otros_nombres=["La Ciudad de las Palmeras"],
    abrev="COL",
    nombre_pronunciacion_local="ko'.li.ma",
    latlong=(19.24, -103.73),
    fecha_de_fundacion=dt.date(1527, 1, 20),
    huso_horario=timezone("America/Mexico_City"),
)

manzanillo = Ciudad(
    nombre="Manzanillo",
    nombre_comun="Manzanillo",
    otros_nombres=["Capital Mundial del Pez Vela", "Esmeralda del Pacífico"],
    abrev="MZO",
    nombre_pronunciacion_local="man.sa'.ni.jo",
    latlong=(19.05, -104.31),
    fecha_de_fundacion=dt.date(1537, 7, 24),
    huso_horario=timezone("America/Mexico_City"),
)

COL = Subdivision(
    nombre="Colima",
    nombre_comun="Colima",
    nombres_nativos={},
    abrev="COL",
    nombre_pronunciacion_local="ko'.li.ma",
    codigo="Col",
    capital=colima,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=colima.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1856, 12, 9),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Colima": colima, "Manzanillo": manzanillo},
)

durango = Ciudad(
    nombre="Victoria de Durango",
    nombre_comun="Durango",
    otros_nombres=["La Perla del Guadiana", "La Tierra del Cine"],
    abrev="DUR",
    nombre_pronunciacion_local="du'.ɾaŋ.ɡo",
    latlong=(24.02, -104.67),
    fecha_de_fundacion=dt.date(1563, 7, 8),
    huso_horario=timezone("America/Mexico_City"),
)

DUR = Subdivision(
    nombre="Durango",
    nombre_comun="Durango",
    nombres_nativos={"Tepehuán": "Korian", "Nahuatl": "Tepēhuahcān"},
    abrev="DUR",
    nombre_pronunciacion_local="du'.ɾaŋ.ɡo",
    codigo="DUR",
    capital=durango,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=durango.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1824, 5, 22),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Durango": durango},
)

guanajuato = Ciudad(
    nombre="Guanajuato",
    nombre_comun="Guanajuato",
    otros_nombres=[
        "Lugar montañoso de ranas",
        "Mo-o-ti (Chichimecas)",
        "Paxtitlan (Mexicas)",
        "Kuanasïuatu (Purépecha)",
    ],
    abrev="GTO",
    nombre_pronunciacion_local="gwa.na'.xwa.to",
    latlong=(21.02, -101.26),
    fecha_de_fundacion=dt.date(1546, 1, 1),  # Desconocido dia y mes.
    huso_horario=timezone("America/Mexico_City"),
)

leon = Ciudad(
    nombre="León de Los Aldama",
    nombre_comun="León",
    otros_nombres=[
        "La Perla del Bajío",
        "La Capital Mundial del Calzado",
        "La Ciudad Esmeralda",
    ],
    abrev="LEO",
    nombre_pronunciacion_local="le'on",
    latlong=(21.12, -101.68),
    fecha_de_fundacion=dt.date(1576, 1, 20),
    huso_horario=timezone("America/Mexico_City"),
)

GTO = Subdivision(
    nombre="Guanajuato",
    nombre_comun="Guanajuato",
    nombres_nativos={"Purépecha": "kuanhasï juáta"},
    abrev="GTO",
    nombre_pronunciacion_local="gwa.na'.xwa.to",
    codigo="GUA",
    capital=guanajuato,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=guanajuato.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 20),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Guanajuato": guanajuato, "León": leon},
)

chilpancingo = Ciudad(
    nombre="Chilpancingo de los Bravo",
    nombre_comun="Chilpancingo",
    otros_nombres=[
        "Ciudad Bravo",
        "Lugar de Avispa",
        "Chilpantsinko (Nahuatl)",
    ],
    abrev="CHIL",
    nombre_pronunciacion_local="tʃil.pan'.siŋ.ɡo",
    latlong=(17.55, -99.50),
    fecha_de_fundacion=dt.date(1591, 11, 1),
    huso_horario=timezone("America/Mexico_City"),
)

acapulco = Ciudad(
    nombre="Acapulco de Juarez",
    nombre_comun="Acapulco",
    otros_nombres=["La Perla del Pacífico"],
    abrev="ACA",
    nombre_pronunciacion_local="aka'.pul.ko",
    latlong=(16.86, -99.88),
    fecha_de_fundacion=dt.date(1550, 3, 12),
    huso_horario=timezone("America/Mexico_City"),
)

GRO = Subdivision(
    nombre="Guerrero",
    nombre_comun="Guerrero",
    nombres_nativos={},
    abrev="GRO",
    nombre_pronunciacion_local="ɡe'.re.ɾo",
    codigo="GRO",
    capital=chilpancingo,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=chilpancingo.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1849, 10, 27),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Acapulco": acapulco, "Chilpancingo": chilpancingo},
)

pachuca = Ciudad(
    nombre="Pachuca de Soto",
    nombre_comun="Pachuca",
    otros_nombres=[
        "La Bella Airosa",
        "Nju̱nthe (Mezquital Otomi)",
        "La Novia del Viento",
        "Cuna del Fútbol Mexicano",
        "Tuzolandia",
    ],
    abrev="PAC",
    nombre_pronunciacion_local="pa'.tʃu.ka",
    latlong=(20.12, -98.74),
    fecha_de_fundacion=dt.date(
        1438, 1, 1
    ),  # Dia y Mes desconocidos. Asentamientos humanos previos.
    huso_horario=timezone("America/Mexico_City"),
)

HGO = Subdivision(
    nombre="Hidalgo",
    nombre_comun="Hidalgo",
    nombres_nativos={},
    abrev="HGO",
    nombre_pronunciacion_local="i'.ðal.ɣo",
    codigo="HGO",
    capital=pachuca,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=pachuca.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1869, 1, 16),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Pachuca": pachuca},
)

guadalajara = Ciudad(
    nombre="Guadalajara",
    nombre_comun="Guadalajara",
    otros_nombres=[
        "La Perla de Occidente",
        "La Perla Tapatía",
        "La Ciudad de las Rosas",
        "Ciudad madre imperial",
        "وادي الحجارة (wādī al-ḥajārah)",
    ],
    abrev="Guad",
    nombre_pronunciacion_local="ɡwa.ða.la'.xa.ɾa",
    latlong=(20.67, -103.35),
    fecha_de_fundacion=dt.date(1524, 2, 14),
    huso_horario=timezone("America/Guadalajara"),
)

JAL = Subdivision(
    nombre="Jalisco",
    nombre_comun="Jalisco",
    nombres_nativos={"Nahuatl": "Tlahtohcayotl Xalixco"},
    abrev="JAL",
    nombre_pronunciacion_local="xa'.lis.ko",
    codigo="JAL",
    capital=guadalajara,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=guadalajara.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 23),
    husos_horarios=[timezone("America/Guadalajara")],
    ciudades_grandes={"Guadalajara": guadalajara},
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
        "Colima": COL,
        "Durango": DUR,
        "Guanajuato": GTO,
        "Hidalgo": HGO,
        "Jalisco": JAL,
    },
)
