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
    codigo_numerico=1,
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
    codigo_numerico=2,
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
    codigo_numerico=3,
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
    codigo_numerico=4,
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
    codigo_numerico=7,
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
    codigo_numerico=8,
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
    codigo_numerico=5,
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
    codigo="COL",
    codigo_numerico=6,
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
    nombres_nativos={"Tepehuán": "Korian", "Náhuatl": "Tepēhuahcān"},
    abrev="DUR",
    nombre_pronunciacion_local="du'.ɾaŋ.ɡo",
    codigo="DUR",
    codigo_numerico=10,
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
    codigo_numerico=11,
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
        "Chilpantsinko (Náhuatl)",
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
    codigo_numerico=12,
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
    codigo_numerico=13,
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
    huso_horario=timezone("America/Mexico_City"),
)

JAL = Subdivision(
    nombre="Jalisco",
    nombre_comun="Jalisco",
    nombres_nativos={"Náhuatl": "Tlahtohcayotl Xalixco"},
    abrev="JAL",
    nombre_pronunciacion_local="xa'.lis.ko",
    codigo="JAL",
    codigo_numerico=14,
    capital=guadalajara,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=guadalajara.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 23),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Guadalajara": guadalajara},
)

toluca = Ciudad(
    nombre="Toluca de Lerdo",
    nombre_comun="Toluca",
    otros_nombres=[
        "Tollohcan (Náhuatl)",
        "Nzehñi (Otomí)",
        "Imbomáani (Matlatzinca)",
        "Tsindijets (Tlahuica)",
        "Zúmi (Mazahua)",
    ],
    abrev="TOL",
    nombre_pronunciacion_local="to'.lu.ka",
    latlong=(19.29, -99.66),
    fecha_de_fundacion=dt.date(1812, 12, 13),
    huso_horario=timezone("America/Mexico_City"),
)

EM = Subdivision(
    nombre="Estado de México",
    nombre_comun="Estado de México",
    nombres_nativos={"Náhuatl": "Mēxihco"},
    abrev="EdoMex",
    nombre_pronunciacion_local="es'.ta.ðo ðe 'me.xi.ko",
    codigo="MEX",
    codigo_numerico=15,
    capital=toluca,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=toluca.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 20),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Toluca": toluca},
)

ciudad_de_mexico = Ciudad(
    nombre="Ciudad de México",
    nombre_comun="Ciudad de México",
    otros_nombres=[
        "Āltepētl Mēxihco (Náhuatl)",
    ],
    abrev="CDMX",
    nombre_pronunciacion_local="sju'.ða(ð) ðe 'me.xi.ko",
    latlong=(19.43, -99.13),
    fecha_de_fundacion=dt.date(1325, 3, 13),
    huso_horario=timezone("America/Mexico_City"),
)

CDMX = Subdivision(
    nombre="Ciudad de México",
    nombre_comun="Ciudad de México",
    nombres_nativos={"Náhuatl": "Āltepētl Mēxihco"},
    abrev="CDMX",
    nombre_pronunciacion_local="sju'.ða(ð) ðe 'me.xi.ko",
    codigo="CMX",
    codigo_numerico=9,
    capital=ciudad_de_mexico,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=ciudad_de_mexico.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(2016, 1, 29),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Ciudad de México": ciudad_de_mexico},
)

morelia = Ciudad(
    nombre="Morelia",
    nombre_comun="Morelia",
    otros_nombres=[
        "Valladolid",
    ],
    abrev="MOR",
    nombre_pronunciacion_local="mo'.ɾe.lja",
    latlong=(19.77, -101.19),
    fecha_de_fundacion=dt.date(1541, 1, 1),  # Día y mes desconocidos.
    huso_horario=timezone("America/Mexico_City"),
)

MICH = Subdivision(
    nombre="Michoacán de Ocampo",
    nombre_comun="Michoacán",
    nombres_nativos={"Náhuatl": "Michhuahcān"},
    abrev="MICH",
    nombre_pronunciacion_local="mi.tʃoa'.kan de o'.kam.po",
    codigo="MIC",
    codigo_numerico=16,
    capital=morelia,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=morelia.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 22),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Morelia": morelia},
)

cuernavaca = Ciudad(
    nombre="Cuernavaca",
    nombre_comun="Cuernavaca",
    otros_nombres=["La ciudad de la eterna primavera", "Cuauhnāhuac (Nahuatl)"],
    abrev="CUE",
    nombre_pronunciacion_local="kweɾ.na'.βa.ka",
    latlong=(18.92, -99.23),
    fecha_de_fundacion=dt.date(
        1529, 6, 6
    ),  # Fundada como Villa del Marquesado del Valle de Oaxaca
    huso_horario=timezone("America/Mexico_City"),
)

MOR = Subdivision(
    nombre="Morelos",
    nombre_comun="Morelos",
    nombres_nativos={},
    abrev="MOR",
    nombre_pronunciacion_local="mo'.ɾe.los",
    codigo="MOR",
    codigo_numerico=17,
    capital=cuernavaca,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=cuernavaca.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1869, 4, 17),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Cuernavaca": cuernavaca},
)

tepic = Ciudad(
    nombre="Tepic",
    nombre_comun="Tepic",
    otros_nombres=[],
    abrev="TEP",
    nombre_pronunciacion_local="te'.pik",
    latlong=(21.51, -104.89),
    fecha_de_fundacion=dt.date(1531, 11, 18),
    huso_horario=timezone("America/Hermosillo"),
)

NAY = Subdivision(
    nombre="Nayarit",
    nombre_comun="Nayarit",
    nombres_nativos={},
    abrev="NAY",
    nombre_pronunciacion_local="na.ʝa'.ɾit",
    codigo="NAY",
    codigo_numerico=18,
    capital=tepic,
    capital_horario=timezone("America/Hermosillo"),
    capital_latlong=tepic.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1917, 1, 26),
    husos_horarios=[timezone("America/Hermosillo")],
    ciudades_grandes={"Tepic": tepic},
)

monterrey = Ciudad(
    nombre="Monterrey",
    nombre_comun="Monterrey",
    otros_nombres=[
        "La sultana del norte",
        "La Ciudad de las Montañas",
        "La Capital Industrial de México.",
    ],
    abrev="MTY",
    nombre_pronunciacion_local="mon.te'.rej",
    latlong=(25.67, -100.30),
    fecha_de_fundacion=dt.date(1529, 9, 20),
    huso_horario=timezone("America/Mexico_City"),
)

NL = Subdivision(
    nombre="Nuevo León",
    nombre_comun="Nuevo León",
    nombres_nativos={},
    abrev="NL",
    nombre_pronunciacion_local="'nwe.βo le.'on",
    codigo="NLE",
    codigo_numerico=19,
    capital=monterrey,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=monterrey.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1824, 5, 17),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Monterrey": monterrey},
)

oaxaca = Ciudad(
    nombre="Oaxaca de Juárez",
    nombre_comun="Oaxaca",
    otros_nombres=[
        "Huaxyacac (Nahuatl)",
        "La Verde Antequera",
    ],
    abrev="OAX",
    nombre_pronunciacion_local="wa'.xa.ka",
    latlong=(7.08, -96.75),
    fecha_de_fundacion=dt.date(1532, 4, 25),
    huso_horario=timezone("America/Mexico_City"),
)

OAX = Subdivision(
    nombre="Oaxaca",
    nombre_comun="Oaxaca",
    nombres_nativos={"Nahuatl": "Huāxyacac"},
    abrev="OAX",
    nombre_pronunciacion_local="wa'.xa.ka",
    codigo="OAX",
    codigo_numerico=20,
    capital=oaxaca,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=oaxaca.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 21),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Oaxaca": oaxaca},
)

puebla = Ciudad(
    nombre="Heroica Puebla de Zaragoza",
    nombre_comun="Puebla",
    otros_nombres=[
        "Cuetlaxcoapan (Nahuatl)",
        "El relicario de América",
        "La ciudad de los Ángeles",
        "La Angelópolis",
    ],
    abrev="PUE",
    nombre_pronunciacion_local="'pwe.βla",
    latlong=(19.03, -98.18),
    fecha_de_fundacion=dt.date(1531, 4, 16),
    huso_horario=timezone("America/Mexico_City"),
)

PUE = Subdivision(
    nombre="Puebla",
    nombre_comun="Puebla",
    nombres_nativos={"Nahuatl": "Cuetlaxcoapan"},
    abrev="PUE",
    nombre_pronunciacion_local="'pwe.βla",
    codigo="PUE",
    codigo_numerico=21,
    capital=puebla,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=puebla.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 21),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Puebla": puebla},
)

queretaro = Ciudad(
    nombre="Santiago de Queretaro",
    nombre_comun="Queretaro",
    otros_nombres=[
        "Dähnini Maxei (Otomí)",
    ],
    abrev="QRO",
    nombre_pronunciacion_local="ke'.ɾe.ta.ɾo",
    latlong=(20.59, -100.39),
    fecha_de_fundacion=dt.date(1531, 7, 25),
    huso_horario=timezone("America/Mexico_City"),
)

QRO = Subdivision(
    nombre="Querétaro de Arteaga",
    nombre_comun="Queretaro",
    nombres_nativos={"Otomí": "Hyodi Ndämxei"},
    abrev="QRO",
    nombre_pronunciacion_local="ke'.ɾe.ta.ɾo",
    codigo="QUE",
    codigo_numerico=22,
    capital=queretaro,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=queretaro.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 23),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Queretaro": queretaro},
)

chetumal = Ciudad(
    nombre="Chetumal",
    nombre_comun="Chetumal",
    otros_nombres=[
        "Chactemàal (Maya Yucateco)",
    ],
    abrev="CHE",
    nombre_pronunciacion_local="tʃe.tu.'mal",
    latlong=(18.50, -88.31),
    fecha_de_fundacion=dt.date(1898, 5, 5),
    huso_horario=timezone("America/Cancun"),
)

QR = Subdivision(
    nombre="Quintana Roo",
    nombre_comun="Queretaro",
    nombres_nativos={},
    abrev="QR",
    nombre_pronunciacion_local="kin'.ta.na 'roo",
    codigo="ROO",
    codigo_numerico=23,
    capital=chetumal,
    capital_horario=timezone("America/Cancun"),
    capital_latlong=chetumal.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1974, 10, 8),
    husos_horarios=[timezone("America/Cancun")],
    ciudades_grandes={"Chetumal": chetumal},
)

san_luis_potosi = Ciudad(
    nombre="San Luis Potosí",
    nombre_comun="San Luis Potosí",
    otros_nombres=[
        "San Luis de la Patria",
        "La Ciudad de los Jardines",
    ],
    abrev="SLP",
    nombre_pronunciacion_local="san 'lwis po.to.'si",
    latlong=(22.15, -100.99),
    fecha_de_fundacion=dt.date(1592, 11, 3),
    huso_horario=timezone("America/Mexico_City"),
)

SLP = Subdivision(
    nombre="San Luis Potosí",
    nombre_comun="San Luis Potosí",
    nombres_nativos={},
    abrev="SLP",
    nombre_pronunciacion_local="san 'lwis po.to.'si",
    codigo="SLP",
    codigo_numerico=24,
    capital=san_luis_potosi,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=san_luis_potosi.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 22),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"San Luis Potosí": san_luis_potosi},
)

culiacan = Ciudad(
    nombre="Culiacán Rosales",
    nombre_comun="Culiacán",
    otros_nombres=["La Perla del Humaya", "Colhuacán (Nahuatl)"],
    abrev="CUL",
    nombre_pronunciacion_local="ku.lja.'kan",
    latlong=(24.81, -107.39),
    fecha_de_fundacion=dt.date(1531, 9, 29),
    huso_horario=timezone("America/Hermosillo"),
)

SNL = Subdivision(
    nombre="Sinaloa",
    nombre_comun="Sinaloa",
    nombres_nativos={},
    abrev="SNL",
    nombre_pronunciacion_local="si.na'.loa",
    codigo="SIN",
    codigo_numerico=25,
    capital=culiacan,
    capital_horario=timezone("America/Hermosillo"),
    capital_latlong=culiacan.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1830, 10, 14),
    husos_horarios=[timezone("America/Hermosillo")],
    ciudades_grandes={"Culiacán": culiacan},
)

hermosillo = Ciudad(
    nombre="Hermosillo",
    nombre_comun="Hermosillo",
    otros_nombres=["La Ciudad del Sol"],
    abrev="HER",
    nombre_pronunciacion_local="eɾ.mo'.si.ʝo",
    latlong=(29.09, -110.95),
    fecha_de_fundacion=dt.date(1700, 5, 18),
    huso_horario=timezone("America/Hermosillo"),
)

SON = Subdivision(
    nombre="Sonora",
    nombre_comun="Sonora",
    nombres_nativos={},
    abrev="SON",
    nombre_pronunciacion_local="so'.no.ɾa",
    codigo="SON",
    codigo_numerico=26,
    capital=hermosillo,
    capital_horario=timezone("America/Hermosillo"),
    capital_latlong=hermosillo.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1824, 1, 10),
    husos_horarios=[timezone("America/Hermosillo")],
    ciudades_grandes={"Hermosillo": hermosillo},
)

villahermosa = Ciudad(
    nombre="Villahermosa",
    nombre_comun="Villahermosa",
    otros_nombres=["La Esmeralda del Sureste"],
    abrev="VIL",
    nombre_pronunciacion_local="ˌbi.ʝa.eɾ'.mo.sa",
    latlong=(17.99, -92.93),
    fecha_de_fundacion=dt.date(1564, 6, 24),
    huso_horario=timezone("America/Mexico_City"),
)

TAB = Subdivision(
    nombre="Tabasco",
    nombre_comun="Tabasco",
    nombres_nativos={},
    abrev="TAB",
    nombre_pronunciacion_local="ta.'βas.ko",
    codigo="TAB",
    codigo_numerico=27,
    capital=villahermosa,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=villahermosa.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1824, 2, 7),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Villahermosa": villahermosa},
)

ciudad_victoria = Ciudad(
    nombre="Ciudad Victoria",
    nombre_comun="Ciudad Victoria",
    otros_nombres=[],
    abrev="CDV",
    nombre_pronunciacion_local="sju'.ðað βik'.to.ɾja",
    latlong=(23.73, -99.13),
    fecha_de_fundacion=dt.date(1750, 10, 6),
    huso_horario=timezone("America/Mexico_City"),
)

TAMPS = Subdivision(
    nombre="Tamaulipas",
    nombre_comun="Tamaulipas",
    nombres_nativos={},
    abrev="TAMPS",
    nombre_pronunciacion_local="ta.maw'.li.pas",
    codigo="TAM",
    codigo_numerico=28,
    capital=ciudad_victoria,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=ciudad_victoria.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1824, 2, 7),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Ciudad Victoria": ciudad_victoria},
)

tlaxcala = Ciudad(
    nombre="Tlaxcala de Xicohténcat",
    nombre_comun="Tlaxcala",
    otros_nombres=[],
    abrev="TLAX",
    nombre_pronunciacion_local="tla(k)s'.ka.la",
    latlong=(19.31, -98.24),
    fecha_de_fundacion=dt.date(1525, 10, 3),
    huso_horario=timezone("America/Mexico_City"),
)

TLAX = Subdivision(
    nombre="Tlaxcala",
    nombre_comun="Tlaxcala",
    nombres_nativos={"Nahuatl": "Tlaxcallān"},
    abrev="TLAX",
    nombre_pronunciacion_local="tla(k)s'.ka.la",
    codigo="TLA",
    codigo_numerico=29,
    capital=tlaxcala,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=tlaxcala.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1856, 12, 9),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Tlaxcala": tlaxcala},
)

xalapa = Ciudad(
    nombre="Xalapa-Enríquez",
    nombre_comun="Xalapa",
    otros_nombres=["La Ciudad de las Flores"],
    abrev="XAL",
    nombre_pronunciacion_local="xa.'la.pa",
    latlong=(19.54, -96.93),
    fecha_de_fundacion=dt.date(1791, 12, 18),
    huso_horario=timezone("America/Mexico_City"),
)

VER = Subdivision(
    nombre="Veracruz de Ignacio de la Llave",
    nombre_comun="Veracruz",
    nombres_nativos={},
    abrev="VER",
    nombre_pronunciacion_local="be.ɾa'.kɾus",
    codigo="VER",
    codigo_numerico=30,
    capital=xalapa,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=xalapa.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 22),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Xalapa": xalapa},
)

merida = Ciudad(
    nombre="Merida",
    nombre_comun="Merida",
    otros_nombres=[],
    abrev="MER",
    nombre_pronunciacion_local="'me.ɾi.ða",
    latlong=(20.97, -89.62),
    fecha_de_fundacion=dt.date(1542, 1, 6),
    huso_horario=timezone("America/Mexico_City"),
)

YUC = Subdivision(
    nombre="Yucatán",
    nombre_comun="Yucatán",
    nombres_nativos={},
    abrev="YUC",
    nombre_pronunciacion_local="ɟʝu.ka.'tan",
    codigo="YUC",
    codigo_numerico=31,
    capital=merida,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=merida.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 23),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Mérida": merida},
)

zacatecas = Ciudad(
    nombre="Zacatecas",
    nombre_comun="Zacatecas",
    otros_nombres=[
        "Civilizadora del Norte",
        "Ciudad de Cantera",
        "Corazón de Plata",
    ],
    abrev="ZAC",
    nombre_pronunciacion_local="sa.ka.'te.kas",
    latlong=(22.77, -102.57),
    fecha_de_fundacion=dt.date(1546, 9, 8),
    huso_horario=timezone("America/Mexico_City"),
)

ZAC = Subdivision(
    nombre="Zacatecas",
    nombre_comun="Zacatecas",
    nombres_nativos={},
    abrev="ZAC",
    nombre_pronunciacion_local="sa.ka.'te.kas",
    codigo="ZAC",
    codigo_numerico=32,
    capital=zacatecas,
    capital_horario=timezone("America/Mexico_City"),
    capital_latlong=zacatecas.latlong,
    es_contigua=True,
    es_isla=False,
    fecha_de_fundacion=dt.date(1823, 12, 23),
    husos_horarios=[timezone("America/Mexico_City")],
    ciudades_grandes={"Zacatecas": zacatecas},
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
        timezone("America/Cancun"),
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
        "Estado de México": EM,
        "Ciudad de México": CDMX,
        "Michoacán": MICH,
        "Morelos": MOR,
        "Nayarit": NAY,
        "Nuevo León": NL,
        "Oaxaca": OAX,
        "Puebla": PUE,
        "Queretaro": QRO,
        "Quintana Roo": QR,
        "San Luis Potosí": SLP,
        "Sinaloa": SNL,
        "Sonora": SON,
        "Tabasco": TAB,
        "Tamaulipas": TAMPS,
        "Tlaxcala": TLAX,
        "Veracrz": VER,
        "Yucatán": YUC,
        "Zacatecas": ZAC,
    },
)
