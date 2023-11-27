# Proyecto_final_PDC

[![BOTONES.png](https://i.postimg.cc/KvLTLtqY/BOTONES.png)](https://postimg.cc/BXStfPGW)

## Integrantes

## Miguel Angel Acevedo Olaya
## Juan Andrés Valderrama Parra


### Proyecto final progamacion de computadores 2023-2 UNAL: Jueguito del ahorcado

Como grupo hemos decidido como proyecto final hacer un juego del famosisimo juego de "el ahorcado", el cual todos jugabamos de peques cuando la vida era bella y nuestra diversion no se limitaba ahora solo a un dispositivo electrónico. Ironicamente, lo vamos a traer a planos digitales bajo progamación y para jugarlo en un dispositivo electrónico (procedo a xdxdd).

Para la realización de este juego lo compusimos bajo estos factores indispensables para la realización del juego

- Importe de librerias
- Instrucciones y niveles de juego
- Puntuación
- Listado de palabras a jugar
- Imagen de muñequito siendo ahorcado
- Limite de tiempo
- Juego final

## Importe de librerias

Para el despliegue adecuado de nuestro codigo, importamos "random", "unicodedata" y "time", ya que estos nos sentaron las bases para un uso indicado del juego

```

import random
import unicodedata
import time

```

## Instrucciones y nivel de juego

El juego es como el de toda la vida: Hay una palabra oculta del cual tiene que adivinarse mediante el acierto de letras que van redescubriendo dicha palabra, de lo contrario bajo una cantidad minima de 3 (y que el mismo usuario puede aumentar si desea)  de intentos fallidos, el juego acabara.

Hemos destinado 6 niveles de dificultad elegidos a gusto del jugador. Su dificultad radicara en la cantidad de letras de la que este compuesta dicha palabra y/ su idioma en el que este predispuesta. 

Dichos niveles enfatizados mejor seria asi:

### Nivel 1: Vamos con primeros pasos
Palabras en español que contengan entre 2 a 4 letras

### Nivel 2: Vamos con primiparo
Palabras en español que contengan entre 5 a 8 letras

### Nivel 3: Vamos con maestro 
Palabras en español que contengan mas de 8 letras

### Nivel 4: Let´s do IT
Palabras en inglés de 3 letras o mas

### Nivel 5: Quelle élégance de France
Palabras en francés de 4 letras o mas

### Nivel 6: Das ist Liebe Essen von Scheiße
Palabras en alemán de 4 letras o mas




Ya con los parametros y las instrucciones bien definidas y establecidas, se traslada a lenguaje de progamación en el cual se le da la posibilidad que el usuario el nivel de juego a su gusto:

```
def nivel():
  print("HOLA BIENVENIDO A AHORCADO CON ANONIMUS CON H, SOMOS UN DUO DE PRIMIPAROS EL CUAL CREO ESTE JUEGO, COPUESTO DE 4 NIVELES, 3 BONOS DE IDIOMAS, Y \nLA CAPACIDAD DE ELEGIR EL NÚMERO DE INTENTOS, PROBAREMOS SI ERES UN PRO O UN SIMPLE PRIMIPARO QUE AUN NO CONOCE DEL MUNDO DE PYTHON \n")
  print("Estos son los niveles: \nNivel 1 = Primeros pasos PUNTOS : 3 \nNivel 2 = Primiparo PUNTOS: 5 \nNivel 3 = Maestro PUNTOS: 10  \nBonus 1 = Ingles PUNTOS: 5 \nBonus 2 = Frances PUNTOS: 8 \nBonus 3 = Aleman PUNTOS: 10 \n")
  bandera = True
  while bandera == True:
    nivel_Palabras = int(input("Escoge el nivel de las palabras que quieras (solo pon el número, 1 FACIL, 2 MEDIO, 3 DIFICL, si es bonus 1 = 4, bonus 2 = 5, bonus 3 = 6): "))
    if nivel_Palabras in range(1,7):
      break
    else:
      print("Eso no te lo puede dar, ingresa entre 1 y 6")
  return nivel_Palabras

def intentos():
  bandera = True
  while bandera == True:
    print("SIN CONTAR LOS EXTRA \n1 INTENTO: 1 PUNTO \n2 INTENTOS: 2 PUNTOS \n3 INTENTOS: 3 PUNTOS \n4 INTENTOS: 4 PUNTOS \n5 INTENTOS: 6 PUNTOS \n6 INTENTOS: 8 PUNTOS \n7 INTENTOS: 10 PUNTOS")
    num_intentos = int(input("Escoge el número de intentos,min 1, max 7 (TIENES 3 INTENTOS EXTRA DE BASE,): "))
    if num_intentos in range(1,8):
      break
    else:
      print("Eso no te lo puedo dar, ingresa entre 1 y 7")
      continue
  num_intentos = num_intentos + 3
  print("Tu número de intentos sera: " +str(num_intentos)+ "\n")
  return num_intentos

```

## Puntuaciones

Bien sea para el nivel de un jugador, o 2 jugadores, el elixir y quien se llevara la copa Piston es aquel que logre la increible hazaña de encontrar la palabra indicada en el menor numero de intentos posible.

Todos los jugadores contaran con una cantidad base de intentos de solamente 3. Previo a la partida se le dara la opción a que el jugador pueda aumentar el número de intentos, pero eso lo volveria mas noob y por ende la cantidad de puntos disminuye paulatinamente. La pertenencia de puntos en función de la cantidad de intentos adicionales seria asi:

## INTENTOS BASE: 3 ----> 10 PUNTOS
### 1 INTENTO EXTRA: 8 PUNTOS
### 2 INTENTOS EXTRA: 6 PUNTOS
### 3 INTENTOS EXTRA: 5 PUNTOS
### 4 INTENTOS EXTRA: 4 PUNTOS
### 5 INTENTOS EXTRA: 3 PUNTOS
### 6 INTENTOS EXTRA: 2 PUNTOS
### 7 INTENTOS EXTRA: 1 PUNTO


## Listado de palabras a jugar

Se seleccionaron manualmente un total de mas de 1000 palabras entre todos los niveles(mas de 300 palabras entre los niveles de español, y mas de 100 en los demás idiomas), enfrascados en sus respectivos niveles y de los cuales le daran ese atributo de siempre tener una palabra nueva por cada juego.

### Progamación:
(Cabe recalcar que la palabra a jugar se seleccionara a lo random de esta galaxia (pero pues en codigo, obvio))


### Nivel 1: Vamos con primeros pasos

```
def palabra():
  if nivel_ == 1:
    print("Vamos con primeros pasos \n")
    lista = [
    "sol", "mar", "luz", "paz", "amor", "rey", "dia", "pan", "flor", "rio", "ojo", "pie", "voz", "hiel", "ley", "te", "rama" ,
    "lago", "mesa", "pato", "cama", "seda", "oro", "nuez", "pino", "ave", "sal", "miel", "cal", "risa", "lima", "vino", "foco" ,
    "ciel", "rana", "lomo", "aro" , "piso", "bote", "fila", "sapo", "gato", "lino", "seta", "tiza", "lobo", "rudo", "lira", "bajo" ,
    "roto", "lago", "puma", "polo", "lima", "lila", "rico", "hueso", "aula", "coco", "bote", "lazo", "lava", "lona", "kilo", "lote", "codo" ,
    "vela", "alto", "rizo", "mora", "sala", "masa", "pila", "taco", "goma", "lima", "luna", "rizo", "lata", "sapo", "rama", "taza","pico",
    "pala" ,"puma", "casa", "vaso", "cima", "tira", "tiro", "mimo", "masa", "rito", "tono", "pesa", "rota", "ropa", "piso", "oso", "alma",
    "gira", "cero", "tela", "hilo", "pera", "tono", "cuna", "saco", "mesa", "cosa", "lado", "pez", "hora", "sola", "tiro", "lupa", "cita",
    "vaso", "rizo", "copa", "vela", "raso", "tapa", "polo", "lote", "lobo", "rato", "rata", "roca", "pila", "lago", "limo", "tira", "rima",
    "tasa", "sopa", "palo", "vino", "lira", "lava", "loma", "puma", "tren", "lira","riel","sosa", "rito", "vaso", "poco", "lazo", "cosa",
    "raso", "pera", "toro", "polo", "lote", "lobo", "pato", "rata", "roca", "pila", "lago", "limo", "tira", "rima", "tasa", "sopa", "palo",
    "vino", "lira", "lava"," loma", "peso", "tren", "lira", "piel", "sosa", "rito", "vaso", "poco", "lazo", "cosa", "raso", "pera", "toro",
    "polo", "lote", "lobo", "rato", "rata", "roca", "pila", "lago", "lima", "tira", "rima", "tasa", "sopa", "palo", "aire", "bote", "cebo",
    "dato", "eco", "fama", "giro", "halo", "idea", "jugo", "kaki", "lote", "masa", "nata", "onda", "paso", "queso", "raza", "seda", "taza",
    "uva", "vida", "wok", "yoga", "zumo", "arte", "boca", "cuna", "don", " eje", "foto", "gris", "hielo", "jarra", "kilo", "lola", "mito",
    "nudo", "oso", "pito", "queso", "rita", "saco", "tuna", "uso", "vela", "web", "yate", "zen", "ave", "bici", "codo", "cuco", "eros",
    "faro","gana", "hola", "jefe", "keko", "lata", "mimo", "nasa", "oro", "pavo", "quiz", "ropa", "sapo", "tajo", "unir", "vez", "wifi",
    "yodo", "zona", "acne", "bote", "cama", "duna", "eje", "foso", "gaza", "halo", "isla", "hale", "kiwi", "lara", "mesa", "nene", "opio",
    "pino", "dama", "rama", "sapo", "tapa", "uñas", "vino", "dedo", "yema", "zumo", "mama", "papa", "ají", "búho", "ceja", "duna", "eje",
    "feo", "gula", "hueso", "jota", "kiwi", "lira", "mole", "nodo", "peso", "rudo", "soso", "tito", "urna", "vale", "jugo", "café, ""aloe",
    "buda", "cima", "duo", "enea", "fofo", "gafe", "haba", "iman", "luca", "lata", "mina", "pavo", "riel", "saco", "tela", "uno", "buho",
    "paz""yama"
    ]
    elemento_aleatorio = random.choice(lista)
    elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
    return(elemento_aleatorio)

```


### Nivel 2: Vamos con primiparo:

```
 if nivel_ == 2:
    print("Vamos con Primiparo \n")
    lista = [
    "abrigo", "balero", "camino", "Detalle", "esfera", "fuerza", "gorila", "humano", "insecto", "jardin", "lapiz", "madera", "narco", "opalo",
    "pajaro", "quimera", "raton", "sabana", "temprano", "utero", "valvula", "xilófono", "yogurt", "zocalo", "afinar", "broche", "calmado",
    "dactil", "ebano", "fabula", "genero", "habito", "indice", "bodega", "lamina", "maquina", "nauseas", "pablo", "quorum", "rabano", "sadico",
    "ulcera", "vandalo", "zangano", "aereo", "barato", "cometa", "dorado", "estilo", "fiesta", "gracia", "hierro", "invierno", "juego", "kawasaki",
    "limon", "manzana", "numero", "olvido", "pezon", "queso", "reloj", "silla", "tiempo", "viento", "aceite", "broma", "cepillo", "dragon",
    "espejo", "frasco", "guitarra", "helado", "iman", "jirafa", "kiosco", "lenteja", "mueble", "naranja", "oruga", "platano", "querido", "resorte"
    "sarten", "tabaco", "util", "vuelo", "yerno", "zafiro", "amarillo", "bicicleta", "claridad", "drogado", "estampa", "fantasma", "gravilla",
    "halcon", "impacto", "jornada", "karate", "llanura", "maraton", "niquel", "octubre""ratente", "quimico", "resumen", "sinfonia", "trabajo",
    "uruguay", "ventana", "yerba", "zanahoria", "acelga", "bufalo", "cosecha", "decibel", "establo", "fabula", "habitante", "ilusion", "jengibre",
    "karaoke", "labrador", "maniaco", "nublado", "obraje", "parpado", "quebrada", "relieve", "salmon", "tabique", "ursula", "viaducto", "waffles",
    "alambre", "caracol", "delfin", "elefante", "frutal", "granero", "hormiga", "incienso", "jacinto", "kilovatio", "linterna", "monarca",
    "naranjo", "acelote", "paraguas", "quirofano", "reserva", "semilla", "telefono", "sombra", "ventilador", "xilografia", "zarcillo", "algodon",
    "brujula", "cenador", "dinosaurio", "escarola", "flamenco", "garganta", "hormigon", "indicador", "jalea", "laberinto", "marmol", "nectar",
    "obelisco""palanca""quimono""retablo""sinfonia""taburete""ulcera""vertigo", "yoduro", "zafiro", "bambu", "caramelo", "dinamita", "estrella",
    "fantasia", "girasol", "helice", "insignia", "jaleo", "kamikaze", "limonero", "maniquí", "nopal", "octagono", "pantera", "quijote",
    "rompecabezas", "sandwich", "taller", "umbra", "vivienda", "yacimiento", "zambomba", "almohada", "bazar", "carpeta", "dromedario", "establo",
    "felino", "gorrion", "helicoptero", "invernadero", "jeringa", "lider", "mariposa", "neumatico", "ovación", "pimienta", "rosaleda", "sardina",
    "terreno", "unicornio", "vainilla", "zapatilla", "alquiler", "bombilla", "clavel", "durazno", "esfera", "furgoneta", "gaviota", "hidrante",
    "infusión", "jazmin", "kilogramo", "linterna", "molino", "neblina""orquídea", "pizarra", "quimica", "rosquilla", "vanadio", "almendra",
    "boceto", "cosecha", "espejismo", "fandango", "gladiolo", "halogeno", "insular", "jocoso", "lombriz", "mochila", "navegador", "ostra",
    "picaporte", "quinoa", "rotonda", "surtidor", "uvula", "vagabundo", "yate", "zambullida", "acrobata", "claro", "bisturi", "cupula",
    "diadema", "enigma", "frijol", "gondola", "harina", "insecto", "jicara", "laser", "mascara", "nomada", "oculto", "paramo", "quiste", "rabano",
    "sotano", "túnel", "ultimo", "vastago", "zodiaco", "acrilico", "boveda", "cesped", "darsena", "ebano", "fosforo", "gargola", "heroe",
    "icaro", "jubilo", "latigo", "mastil", "nectar", "optica", "petalo", "quorum", "regimen", "subdito", "tempano", "unico", "vertice", "xilofono",
    "aereo""baculo""codigo"
    ]
    elemento_aleatorio = random.choice(lista)
    elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
    return(elemento_aleatorio)

```

### Nivel 3: Vamos con maestro:

```
if nivel_ == 3:
    print("Vamos con maestro \n")
    lista = [
"abecedario", "biblioteca", "calefaccion", "democracia", "electricidad", "filosofia", "gastronomia", "hidratacion", "iluminacion",
"jardineria", "kilometraje", "libreria", "matematicas", "neumatico", "orquesta", "paralelogramo", "querubines", "radiografia", "metalurgia",
"telescopio", "ultrasonido", "vagabunderia", "ingenieria", "camioneta", "filosofia", "aprobacion", "arquitectura", "burocracia",
"contaminacion", "desarrollo", "espectaculo", "fraternidad", "geografia", "horticultura", "imaginacion", "justificacion", "kinesiologia",
"luminiscencia", "meteorologia", "navegacion", "oportunidad", "psicología", "quimica", "revolucion", "reconocimiento", "traduccion",
"universitario", "vulcanizacion", "antioquia", "zoologico", "aeronautica", "biologia", "cartografia", "dermatologia", "encefalograma",
"filantropia", "gerontologia", "hidrografia", "iconografia", "jeringuilla", "levitacion", "monocromatico", "nefrologia", "oceanografia",
"paleontologia", "quiropractica", "retroalimentacion", "sismología", "telepatia", "ultravioleta", "verborrea", "entropia", "coqueteria",
"antagonismo", "balistica", "caligrafoa", "diagnóstico", "simbiosis", "filigrana", "glaciacion", "hemisferio", "ilusionismo", "jovialidad",
"kinesioterapia", "locomoción", "magnetismo", "neurologia", "ornitología", "psicopatologia", "queratina", "reciclaje", "simbolismo",
"teocracia", "unificacion", "ventilacion", "histeria", "xenofobo", "zoologia", "arqueologia", "bioquimica", "cinematografia",
"deshidratación", "epistemología", "fisioterapia", "geriatria", "hemoglobina", "idealización", "logaritmo", "microscopio", "neurocirugia",
"oftalmologia", "paleografia", "quiromancia", "radiotelescopio", "serpiente", "taxidermia", "cantautor", "escondidas", "xenofobia",
"zambullirse", "autobiografia", "bacteriologia", "contabilidad", "desinfeccion", "electromagnetismo", "fotografia", "gramatica", "hipotenusa",
"impresionismo", "jurisprudencia", "kinestesia", "litografia", "macadamia", "nostalgia", "oleografia", "fotografia", "quiroptero",
"restauracion""surrealismo""television""aristocracia""beneficencia""comunicacion""deforestacion""electrodomestico""fotocopiadora""gubernamental""hemeroteca""informatica""jurisdiccion"
"kilovoltio", "libreria", "neurociencia", "oftalmologo", "paramedico", "ginecoplastia", "resucitacion", "quirurgico", "ultrasonografia",
"discoteca", "reggaeton", "yerbatero", "zambullidor", "automatizacion", "bioingeniería", "cronometraje", "desoxirribonucleico", "etnografía"
"fonoaudiologia", "horticultor", "embriaguez", "jardineria", "kinesiologia", "lexicografia", "meteorologia", "nefrologia", "otorrinolaringologia",
"petrografia", "quiropractica", "radiotelefonia", "sismografo", "toxicologia", "microscopio", "videocamara", "xenofobo", "yuxtaposicion",
"zoologico", "antropologia", "biomecánica", "computadora", "dermatologia", "espectrofotometria", "filantropia", "hemodinámica", "inmunologia",
"kilogramo", "laringologia", "micologia", "neumonia", "oftalmologia", "paleontologia", "quimioterapia", "radiactividad", "taquicardia",
"ultravioleta", "virologia", "depresion", "zancadilla", "arqueologia", "progamacion", "cardiologia", "depuradora", "electroencefalograma",
"geriatria", "hemoglobina", "infograma", "jardinería", "ludopatia", "microprocesador", "neurotransmisor", "psicopedagogía", "quebradizo",
"radioastronomía", "semiótica", "terapia", "ultraligero", "ventriloquia", "zapatilla", "astronomia", "bronquitis", "caleidoscopio",
"deshidratador", "electroimán", "fisiología", "gerontología", "hemisferio", "indemnizacion", "jeringuilla", "kinesioterapia", "logistica",
"monocromático", "neurocirugia", "osteopatia", "psiquiatria", "quimico", "reciclador", "filologia", "transeúnte", "verosimilitud",
"xilofono", "yerbatero", "zambullida", "antioxidante", "catapulta", "diagnóstico", "electroshock", "fraccionamiento", "astronauta",
"intermediario", "jerarquía", "kinesiterapia", "luminiscencia", "magnetoscopio", "neuroanatomía", "oftalmoscopio", "farmacología", "acuicultura",
"barometro", "camuflaje", "descifrador", "empatia", "fertilizante", "glucosa", "hidroelectrica", "justiciero", "karaoke", "laboratorio",
"microscopio", "neurocirujano", "oftalmoscopio", "paracaidismo", "queratina", "radiacion", "sarcofago", "ultravioleta", "ventrilocuo",
"xenofobia", "zangoloteo", "binocular", "ciberespacio", "desinfectante", "entrenador", "filosofar", "geotermia", "hormigon", "inmunologia",
"jardinero", "caleidoscopio", "luminiscencia", "monocromatico", "navegante", "operacion", "paleontologo", "quimioterapia", "radiotelescopio",
"secuenciador", "termometro", "urbanizacion", "viscosidad", "terremoto"
]
    elemento_aleatorio = random.choice(lista)
    elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
    return(elemento_aleatorio)

```

### Nivel 4: Let´s do IT:

```
 if nivel_ == 4:
    print("Let's do IT \n")
    lista = [
"cat", "dog", "bee", "run", "hat", "red", "sun", "box", "joy", "sky", "key", "car", "egg", "ice", "owl", "pen", "zip", "yoy", "fog", "wax",
"jet", "log", "mud", "nut", "pie", "rag", "sea", "van", "web", "zen", "air", "animal", "basket", "camera", "danger", "energy", "flower",
"garden", "health", "island", "jungle", "kettle", "ladder", "market", "nature", "orange", "palace", "quarry", "rescue", "spirit", "travel",
"unique", "wallet", "xyloph", "yellow", "accord", "breeze", "castle", "donate", "emblem", "flight", "gravel", "harbor", "injury", "jumper",
"adventure", "brilliant", "chocolate", "dangerous", "fantastic", "gratitude", "hospital", "important", "handsome", "knowledge", "landscape",
"machinery", "nutrition", "operation", "neumatic", "question", "radiology", "spherical", "telescope", "umbrella", "vibration", "warehouse",
"xenophobe", "zealously", "afternoon", "biography", "candidate", "education", "frequency", "generator", "marketing" , "nightfall",
"overboard", "wallpaper", "satellite", "underwear", "blueberry", "homework", "morning", "elephant"

```

### Nivel 5: Quelle élégance de France:

```
 if nivel_ == 5:
    print("Quelle élégance de France \n")
    lista = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche", "automne", "hiver", "printemps", "pronunciaton","mois", "janvier", "mars", "avril", "mai", "juin", "juillet", "septembre", "octobre", "novembre", "decembre", "coleurs", "noir", "violet", "blanc", "rouge", "rose", "vert", "bleu", "orange", "marron", "gris", "beige", "turquoise", "famille", "soeur", "fils", "fille", "oncle", "tante", "cousine", "cousin", "enfants", "neveu","verbes", "avoir", "pronominaux", "aller", "manger", "courir", "danser", "chanter", "voler", "vouloir", "pouvoir", "garder", "jouer", "nager", "contruire", "penser", "ajouter", "sortir", "entrer", "monter", "descendre", "partir", "retourner", "rentrer", "rester", "tomber", "venir", "arriver", "mourir","permettre", "permis", "mettre", "mis", "dormir", "mentir", "sentir", "exprimer", "emotions", "hereuse", "triste", "aimer", "destester", "partager","rage" "servir", "sourire", "traduire", "conduire", "produire", "attendre", "battre", "animaux", "chien", "chat", "cheval", "souris", "poisson", "lion"]
    elemento_aleatorio = random.choice(lista)
    elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
    return(elemento_aleatorio)

```

### Nivel 6: Das ist Liebe Essen von Scheiße:

```
  if nivel_ == 6:
    print("Das ist Liebe zum Essen von Scheiße \n")
    lista = [
"haus", "baum", "auto", "weg", "zug", "hund", "katze", "jahr", "tag", "zeit", "mond", "sonne", "meer", "stadt", "berg", "buch", "boot",
"tur", "wand", "bett", "tisch", "stuhl", "licht", "lampe", "bild", "ring", "vogel", "blume", "fluss", "brot", "wein", "milch", "wasser",
"blumen", "fenster", "schrank", "brucke", "vogel", "schule", "kirche", "garten", "strabe", "insel", "freund", "lehrer", "familie", "teller",
"stuhl", "lampe", "buchen", "bilder", "wetter", "sonnen", "sterne", "wolken", "regnen", "schnee", "windig", "sommer", "winterhg",
"fruhling", "herbst", "wasser", "kaffee", "zucker", "pfanne", "messer", "krankenhaus", "universität", "bibliothek", "schokolade",
"geschichten", "wissenschaft", "elektrizität", "kindergarten", "schmetterling", "sonnenschein", "regenschirm", "fruhstück", "arbeitsplatz",
"geburtstag", "fahrradfahren", "geschwindigkeit", "gemusegarten", "feiertag", "Gluckwunsch", "handtuch", "instrument", "journalist",
"kaffeetasse", "landschaft", "mittagessen", "nachmittag", "organisation", "persönlichkeit", "qualifikation", "restaurant", "supermarkt",
"telefonnummer", "umweltschutz", "verantwortung"
]
    elemento_aleatorio = random.choice(lista)
    elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
    return(elemento_aleatorio)

```


# Límite de tiempo 





