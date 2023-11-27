import random
import unicodedata
import time

bandera = True
while bandera == True:
  jugadores = int(input("QUIERES 1 O 2 JUGADORES: \n"))
  if jugadores == 1 or jugadores == 2:
    break
  else: (print("INGRESA ENTRE 1 Y 2"))

if jugadores == 1:
  def nivel(): #La función nivel, nos permite dar al usuario la libertad de elegir el nivel con el que desea jugar, funciona con un input y un ciclo en el que si el valor no esta en el rango que le solicitamos, seguira ejectuandose.
    print("HOLA BIENVENIDO A AHORCADO CON ANONIMUS CON H,  SOMOS UN DUO DE PRIMIPAROS EL CUAL CREO ESTE JUEGO, COPUESTO DE 4 NIVELES, 3 BONOS DE IDIOMAS, Y \nLA CAPACIDAD DE ELEGIR EL NÚMERO DE INTENTOS, PROBAREMOS SI ERES UN PRO O UN SIMPLE PRIMIPARO QUE AUN NO CONOCE DEL MUNDO DE PYTHON \n")
    print("Estos son los niveles: \nNivel 1 = Primeros pasos PUNTOS : 3 \nNivel 2 = Primiparo PUNTOS: 5 \nNivel 3 = Maestro PUNTOS: 10  \nBonus 1 = Ingles PUNTOS: 5 \nBonus 2 = Frances PUNTOS: 8 \nBonus 3 = Aleman PUNTOS: 10 \n")
    bandera = True
    while bandera == True:
      nivel_Palabras = int(input("Escoge el nivel de las palabras que quieras (solo pon el número, 1 FACIL, 2 MEDIO, 3 DIFICL, si es bonus 1 = 4, bonus 2 = 5, bonus 3 = 6): "))
      if nivel_Palabras in range(1,7):
        break
      else:
        print("Eso no te lo puede dar, ingresa entre 1 y 6")
    return nivel_Palabras

  def intentos(): # La función intentos, cumple exactamente la misma función que la anterior, pero en vez de elegir nivel, esta elegira el número de intentos que tiene el usuario
    bandera = True
    while bandera == True:
      print("SIN CONTAR LOS EXTRA \n0 Intentos: 10 PUNTOS \n1 INTENTO: 8 PUNTOS \n2 INTENTOS: 6 PUNTOS \n3 INTENTOS: 5 PUNTOS \n4 INTENTOS: 4 PUNTOS \n5 INTENTOS: 3 PUNTOS \n6 INTENTOS: 2 PUNTOS \n7 INTENTOS: 1 PUNTO")
      num_intentos = int(input("Escoge el número de intentos,min 0, max 7 (TIENES 3 INTENTOS EXTRA DE BASE,): "))
      if num_intentos in range(0,8):
        break
      else:
        print("Eso no te lo puedo dar, ingresa entre 0 y 7")
        continue
    num_intentos = num_intentos + 3
    print("Tu número de intentos sera: " +str(num_intentos)+ "\n")
    return num_intentos

  def palabra(): # Esta función dependiendo del nivel que ingreso el usuario, tomara una lista dadas las condiciones ya dichas, y tomara un elemento aleatorio de esta, utilizamos el unicodedata para quitarle tildes, y retornamos esta palabra que sera la que permitira ejecutar el juego
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
  ]
      elemento_aleatorio = random.choice(lista)
      elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
      return(elemento_aleatorio)
    if nivel_ == 5:
      print("Quelle élégance de France \n")
      lista = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche", "automne", "hiver", "printemps", "pronunciaton","mois", "janvier", "mars", "avril", "mai", "juin", "juillet", "septembre", "octobre", "novembre", "decembre", "coleurs", "noir", "violet", "blanc", "rouge", "rose", "vert", "bleu", "orange", "marron", "gris", "beige", "turquoise", "famille", "soeur", "fils", "fille", "oncle", "tante", "cousine", "cousin", "enfants", "neveu","verbes", "avoir", "pronominaux", "aller", "manger", "courir", "danser", "chanter", "voler", "vouloir", "pouvoir", "garder", "jouer", "nager", "contruire", "penser", "ajouter", "sortir", "entrer", "monter", "descendre", "partir", "retourner", "rentrer", "rester", "tomber", "venir", "arriver", "mourir","permettre", "permis", "mettre", "mis", "dormir", "mentir", "sentir", "exprimer", "emotions", "hereuse", "triste", "aimer", "destester", "partager","rage" "servir", "sourire", "traduire", "conduire", "produire", "attendre", "battre", "animaux", "chien", "chat", "cheval", "souris", "poisson", "lion"]
      elemento_aleatorio = random.choice(lista)
      elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
      return(elemento_aleatorio)
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

  def img_ahoracado(): # La función de la cual sacamos los muñequitos es la siguiente. Esta permite guardar en una lista, el diccionario con cada muñequito, que estan ordenados secuencialmente para encajarlos con el número de intentos gastados, ademas de eso dependiendo del número de intentos que ingreso el usuario, se tiene configurado que lista sera retornada, para que tenga coherencia.

    if num_intento == 3:
      ahorcado_ = [
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   / \  |',
              '5': '=========',
              }
                ]
    elif num_intento == 4:
      ahorcado_ = [
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   / \  |',
              '5': '=========',
              }
                ]
    elif num_intento == 5:
      ahorcado_ = [
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   / \  |',
              '5': '=========',
              }
                ]
    elif num_intento == 6:
      ahorcado_ = [
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '    |   |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   / \  |',
              '5': '=========',
          }
      ]
    elif num_intento == 7:
      ahorcado_ = [
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
              },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '    |   |',
              '4': '        |',
              '5': '=========',
              },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '        |',
              '5': '=========',
              },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   / \  |',
              '5': '=========',
              }
      ]
    elif num_intento == 8:
      ahorcado_ = [
        {
            '0': '    +---+',
            '1': '        |',
            '2': '        |',
            '3': '        |',
            '4': '        |',
            '5': '=========',
        },
        {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
        {
            '0': '    +---+',
            '1': '    |   |',
            '2': '        |',
            '3': '        |',
            '4': '        |',
            '5': '=========',
        },
        {
            '0': '    +---+',
            '1': '    |   |',
            '2': '    O   |',
            '3': '        |',
            '4': '        |',
            '5': '=========',
        },
        {
            '0': '    +---+',
            '1': '    |   |',
            '2': '    O   |',
            '3': '    |   |',
            '4': '        |',
            '5': '=========',
        },
        {
            '0': '    +---+',
            '1': '    |   |',
            '2': '    O   |',
            '3': '   /|\  |',
            '4': '        |',
            '5': '=========',
        },
        {
            '0': '    +---+',
            '1': '    |   |',
            '2': '    O   |',
            '3': '   /|\  |',
            '4': '   / \  |',
            '5': '=========',
        }
      ]
    elif num_intento == 9:
      ahorcado_ = [
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '    |   |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|   |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   / \  |',
              '5': '=========',
          }
      ]
    elif num_intento == 10:
      ahorcado_ = [
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '    |   |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|   |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   /    |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   / \  |',
              '5': '=========',
          }
          ]
    return ahorcado_

  def juego():
    lista = []
    gastados = 0
    for l in palabra:
      lista.append("_ ")
    print("ESTA SERA LA PALABRA A ADIVINAR, TIENES 90 SEGUNDOS A PARTIR DE YA: ")
    print(str(lista)+ "\n")
    inicio_tiempo = time.time()
    tiempo_transcurrido = 0
    tiempo_max = 90
    while gastados < num_intento and tiempo_transcurrido < tiempo_max:
      if ''.join(lista) == palabra:
        print("LO LOGRASTE " +str(palabra.upper())+ "\n")
        return True
      ingresa_ = str(input("Ingresa una letra: "))
      ingresa_ = ingresa_.lower()
      if len(ingresa_) == 1:
        if ingresa_ in palabra:
          upper = ingresa_.upper()
          print(str(upper)+ " ES CORRECTO")
          contador_ = 0
          if contador_ == 0:
            for m in lista:
              posicion = 0
              if m != ("_ "):
                posicion += 1
                continue
              if m == ("_ "):
                contador = 0
                if contador == 0:
                  for n in palabra:
                    if n == ingresa_:
                      lista[posicion] = ingresa_
                      posicion += 1
                    elif n!= ingresa_:
                      posicion += 1
                else:
                  contador = 0
                  continue
            contador_ += 1
            print("Te quedan " +str(num_intento-gastados)+ " intentos")
            print(str(lista)+ "\n")
          else:
            posicion = 0
            continue
        else:
          upper = ingresa_.upper()
          print(str(upper)+ " ES INCORRECTO INTENTA NUEVAMENTE")
          contador = 0
          gastados += 1
          print("Has gastado " +str(gastados)+ " intentos, te quedan " +str(num_intento-gastados)+ "\n")
          print(str(lista)+ "\n")
        print("AHORCADO: \n")
        for u in range(len(ahorcado)):
          if u == gastados:
            for v, w in ahorcado[u].items():
              print(w)
        print("\n")
        tiempo_transcurrido = time.time() - inicio_tiempo
        print("Te quedan:" +str(tiempo_max - tiempo_transcurrido//1)+ " segundos \n")
      elif len(ingresa_) > 1:
        if ingresa_ == palabra:
          print("LO LOGRASTE ADIVINASTE " +str(palabra)+ "\n")
          return True
        elif ingresa_ != palabra:
          print(str(ingresa_)+ " ES INCORRECTO INTENTA NUEVAMENTE")
          gastados += 1
          for u in range(len(ahorcado)):
            if u == gastados:
                for v, w in ahorcado[u].items():
                    print(w)
          print("\n")
          continue
    if gastados == num_intento:
      print("HAS PERDIDO, LA PALABRA ERA " +str(palabra.upper())+  " ,suerte para la proxima")
      return False
    print("SE HA TERMINADO EL TIEMPO, LA PALABRA ERA: " +str(palabra) +"\n")
    return False

  def puntos(): # En esta Función podemos ver que dependiendo del nivel y del número de intentos que eligio el usuario esta retornara un número de puntos determinado. 
    if nivel_ == 1:
      punto_niv = 3
    elif nivel_ == 2:
      punto_niv = 5
    elif nivel_ == 3:
      punto_niv = 10
    elif nivel_ == 4:
      punto_niv = 5
    elif nivel_ == 5:
      punto_niv = 8
    elif nivel_ == 6:
      punto_niv = 10
    if num_intento == 3:
      punto_int= 10
    if num_intento == 4:
      punto_int = 8
    elif num_intento == 5:
      punto_int = 6
    elif num_intento == 6:
      punto_int = 5
    elif num_intento == 7:
      punto_int = 4
    elif num_intento == 8:
      punto_int = 3
    elif num_intento == 9:
      punto_int = 2
    elif num_intento == 10:
      punto_int = 1
    total = punto_niv + punto_int
    return total

  puntos_ = 0

  if __name__ == "__main__":
    nivel_ = nivel()
    print("AHORA YA ESCOGIDO EL NIVEL VAMOS CON INTENTOS \n")
    num_intento = intentos()
    palabra = palabra()
    ahorcado = img_ahoracado()
    juego = juego()
    if juego == True:
      puntos = puntos()
      puntos_ = puntos_ + puntos
      print(" EL JUGADOR TIENE " +str(puntos_)+ " puntos")
    elif juego == False:
      print("El jugador tiene " +str(puntos_)+ " puntos")

elif jugadores == 2:
  puntos_jugador_1 = 0 
  puntos_jugador_2 = 0 
  for n in range (0,6):
    jugador_act = n % 2 + 1
    def nivel(): # La función nivel, nos permite dar al usuario la libertad de elegir el nivel con el que desea jugar, funciona con un input y un ciclo en el que si el valor no esta en el rango que le solicitamos, seguira ejectuandose.
      print("JUGADOR " +str(jugador_act)+ " BIENVENIDO A AHORCADO CON ANONIMUS CON H, SOMOS UN DUO DE PRIMIPAROS EL CUAL CREO ESTE JUEGO, COPUESTO DE 4 NIVELES, 3 BONOS DE IDIOMAS, Y \nLA CAPACIDAD DE ELEGIR EL NÚMERO DE INTENTOS, PROBAREMOS SI ERES UN PRO O UN SIMPLE PRIMIPARO QUE AUN NO CONOCE DEL MUNDO DE PYTHON \n")
      print("JUGADOR " +str(jugador_act)+ " Estos son los niveles: \nNivel 1 = Primeros pasos PUNTOS : 3 \nNivel 2 = Primiparo PUNTOS: 5 \nNivel 3 = Maestro PUNTOS: 10  \nBonus 1 = Ingles PUNTOS: 5 \nBonus 2 = Frances PUNTOS: 8 \nBonus 3 = Aleman PUNTOS: 10 \n")
      bandera = True
      while bandera == True:
        nivel_Palabras = int(input("JUGADOR " +str(jugador_act)+ " Escoge el nivel de las palabras que quieras (solo pon el número, 1 FACIL, 2 MEDIO, 3 DIFICL, si es bonus 1 = 4, bonus 2 = 5, bonus 3 = 6): "))
        if nivel_Palabras in range(1,7):
          break
        else:
          print("Eso no te lo puede dar, ingresa entre 1 y 6")
      return nivel_Palabras

    def intentos(): # La función intentos, cumple exactamente la misma función que la anterior, pero en vez de elegir nivel, esta elegira el número de intentos que tiene el usuario
      bandera = True
      while bandera == True:
        print("JUGADOR " +str(jugador_act)+ " ,SIN CONTAR LOS EXTRA \n0 Intentos: 10 PUNTOS \n1 INTENTO: 8 PUNTOS \n2 INTENTOS: 6 PUNTOS \n3 INTENTOS: 5 PUNTOS \n4 INTENTOS: 4 PUNTOS \n5 INTENTOS: 3 PUNTOS \n6 INTENTOS: 2 PUNTOS \n7 INTENTOS: 1 PUNTO")
        num_intentos = int(input("Escoge el número de intentos,min 0, max 7 (TIENES 3 INTENTOS EXTRA DE BASE,): "))
        if num_intentos in range(0,8):
          break
        else:
          print("JUGADOR " +str(jugador_act)+ " Eso no te lo puedo dar, ingresa entre 0 y 7")
          continue
      num_intentos = num_intentos + 3
      print("JUGADOR " +str(jugador_act)+ " Tu número de intentos sera: " +str(num_intentos)+ "\n")
      return num_intentos

    def palabra(): #Esta función dependiendo del nivel que ingreso el usuario, tomara una lista dadas las condiciones ya dichas, y tomara un elemento aleatorio de esta, utilizamos el unicodedata para quitarle tildes, y retornamos esta palabra que sera la que permitira ejecutar el juego
      if nivel_ == 1:
        print("JUGADOR " +str(jugador_act)+ " Vamos con primeros pasos \n")
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
      "vida""yama"
        ]
        elemento_aleatorio = random.choice(lista)
        elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
        return(elemento_aleatorio)
      if nivel_ == 2:
        print("JUGADOR " +str(jugador_act)+ " Vamos con Primiparo \n")
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
      if nivel_ == 3:
        print("JUGADOR " +str(jugador_act)+ " Vamos con maestro \n")
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
      if nivel_ == 4:
        print("PLAYER " +str(jugador_act)+ " Let's do IT \n")
        lista = [
    "cat", "dog", "bee", "run", "hat", "red", "sun", "box", "joy", "sky", "key", "car", "egg", "ice", "owl", "pen", "zip", "yoy", "fog", "wax",
    "jet", "log", "mud", "nut", "pie", "rag", "sea", "van", "web", "zen", "air", "animal", "basket", "camera", "danger", "energy", "flower",
    "garden", "health", "island", "jungle", "kettle", "ladder", "market", "nature", "orange", "palace", "quarry", "rescue", "spirit", "travel",
    "unique", "wallet", "xyloph", "yellow", "accord", "breeze", "castle", "donate", "emblem", "flight", "gravel", "harbor", "injury", "jumper",
    "adventure", "brilliant", "chocolate", "dangerous", "fantastic", "gratitude", "hospital", "important", "handsome", "knowledge", "landscape",
    "machinery", "nutrition", "operation", "neumatic", "question", "radiology", "spherical", "telescope", "umbrella", "vibration", "warehouse",
    "xenophobe", "zealously", "afternoon", "biography", "candidate", "education", "frequency", "generator", "marketing" , "nightfall",
    "overboard", "wallpaper", "satellite", "underwear", "blueberry", "homework", "morning", "elephant"
    ]
        elemento_aleatorio = random.choice(lista)
        elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
        return(elemento_aleatorio)
      if nivel_ == 5:
        print("JUGADOR " +str(jugador_act)+ " Quelle élégance de France \n")
        lista = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche", "automne", "hiver", "printemps", "pronunciaton","mois", "janvier", "mars", "avril", "mai", "juin", "juillet", "septembre", "octobre", "novembre", "decembre", "coleurs", "noir", "violet", "blanc", "rouge", "rose", "vert", "bleu", "orange", "marron", "gris", "beige", "turquoise", "famille", "soeur", "fils", "fille", "oncle", "tante", "cousine", "cousin", "enfants", "neveu","verbes", "avoir", "pronominaux", "aller", "manger", "courir", "danser", "chanter", "voler", "vouloir", "pouvoir", "garder", "jouer", "nager", "contruire", "penser", "ajouter", "sortir", "entrer", "monter", "descendre", "partir", "retourner", "rentrer", "rester", "tomber", "venir", "arriver", "mourir","permettre", "permis", "mettre", "mis", "dormir", "mentir", "sentir", "exprimer", "emotions", "hereuse", "triste", "aimer", "destester", "partager","rage" "servir", "sourire", "traduire", "conduire", "produire", "attendre", "battre", "animaux", "chien", "chat", "cheval", "souris", "poisson", "lion"]
        elemento_aleatorio = random.choice(lista)
        elemento_aleatorio_ = ''.join((c for c in unicodedata.normalize('NFD', elemento_aleatorio) if unicodedata.category(c) != 'Mn'))
        return(elemento_aleatorio)
      if nivel_ == 6:
        print("JUGADOR " +str(jugador_act)+ " Das ist Liebe zum Essen von Scheiße \n")
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

    def img_ahoracado(): # La función de la cual sacamos los muñequitos es la siguiente. Esta permite guardar en una lista, el diccionario con cada muñequito, que estan ordenados secuencialmente para encajarlos con el número de intentos gastados, ademas de eso dependiendo del número de intentos que ingreso el usuario, se tiene configurado que lista sera retornada, para que tenga coherencia.
      if num_intento == 3:
        ahorcado_ = [
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '   / \  |',
                '5': '=========',
                }
                  ]
      elif num_intento == 4:
        ahorcado_ = [
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '   / \  |',
                '5': '=========',
                }
                  ]
      elif num_intento == 5:
        ahorcado_ = [
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '   / \  |',
                '5': '=========',
                }
                  ]
      elif num_intento == 6:
        ahorcado_ = [
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '    |   |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '   / \  |',
                '5': '=========',
            }
        ]
      elif num_intento == 7:
        ahorcado_ = [
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
                },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '    |   |',
                '4': '        |',
                '5': '=========',
                },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '        |',
                '5': '=========',
                },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '   / \  |',
                '5': '=========',
                }
        ]
      elif num_intento == 8:
        ahorcado_ = [
          {
              '0': '    +---+',
              '1': '        |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '        |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '        |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '    |   |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '        |',
              '5': '=========',
          },
          {
              '0': '    +---+',
              '1': '    |   |',
              '2': '    O   |',
              '3': '   /|\  |',
              '4': '   / \  |',
              '5': '=========',
          }
        ]
      elif num_intento == 9:
        ahorcado_ = [
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '    |   |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|   |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '   / \  |',
                '5': '=========',
            }
        ]
      elif num_intento == 10:
        ahorcado_ = [
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '        |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '        |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '        |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '    |   |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|   |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '        |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '   /    |',
                '5': '=========',
            },
            {
                '0': '    +---+',
                '1': '    |   |',
                '2': '    O   |',
                '3': '   /|\  |',
                '4': '   / \  |',
                '5': '=========',
            }
            ]
      return ahorcado_

    def juego():
      lista = []
      gastados = 0
      for l in palabra:
        lista.append("_ ")
      print("JUGADOR " +str(jugador_act)+ " ESTA SERA LA PALABRA A ADIVINAR, TIENES 90 SEGUNDOS A PARTIR DE YA: ")
      print(str(lista)+ "\n")
      inicio_tiempo = time.time()
      tiempo_transcurrido = 0
      tiempo_max = 90
      while gastados < num_intento and tiempo_transcurrido < tiempo_max:
        if ''.join(lista) == palabra:
          print("JUGADOR " +str(jugador_act)+ " LO LOGRASTE, ADIVINASTE " +str(palabra.upper())+ "\n")
          return True
        ingresa_ = str(input("JUGADOR " +str(jugador_act)+ " Ingresa una letra: "))
        ingresa_ = ingresa_.lower()
        if len(ingresa_) == 1:
          if ingresa_ in palabra:
            upper = ingresa_.upper()
            print(str(upper)+ " ES CORRECTO")
            contador_ = 0
            if contador_ == 0:
              for m in lista:
                posicion = 0
                if m != ("_ "):
                  posicion += 1
                  continue
                if m == ("_ "):
                  contador = 0
                  if contador == 0:
                    for n in palabra:
                      if n == ingresa_:
                        lista[posicion] = ingresa_
                        posicion += 1
                      elif n!= ingresa_:
                        posicion += 1
                  else:
                    contador = 0
                    continue
              contador_ += 1
              print("Te quedan " +str(num_intento-gastados)+ " intentos")
              print(str(lista)+ "\n")
            else:
              posicion = 0
              continue
          else:
            upper = ingresa_.upper()
            print("JUGADOR " +str(jugador_act)+ " , " +str(upper)+ " ES INCORRECTO INTENTA NUEVAMENTE")
            contador = 0
            gastados += 1
            print("JUGADOR " +str(jugador_act)+ " Has gastado " +str(gastados)+ " intentos, te quedan " +str(num_intento-gastados)+ "\n")
            print(str(lista)+ "\n")
          print("AHORCADO: \n")
          for u in range(len(ahorcado)):
            if u == gastados:
              for v, w in ahorcado[u].items():
                print(w)
          print("\n")
          tiempo_transcurrido = time.time() - inicio_tiempo
          print("JUGADOR " +str(jugador_act)+ " Te quedan:" +str(tiempo_max - tiempo_transcurrido//1)+ " segundos \n")
        elif len(ingresa_) > 1:
          if ingresa_ == palabra:
            print("JUGADOR " +str(jugador_act)+ " LO LOGRASTE, ADIVINASTE " +str(palabra)+ "\n")
            return True
          elif ingresa_ != palabra:
            print("JUGADOR " +str(jugador_act)+  +str(ingresa_)+ " ES INCORRECTO INTENTA NUEVAMENTE")
            gastados += 1
            for u in range(len(ahorcado)):
                if u == gastados:
                    for v, w in ahorcado[u].items():
                        print(w)
            print("\n")
            continue
      if gastados == num_intento:
        print("JUGADOR " +str(jugador_act)+ " HAS PERDIDO, LA PALABRA ERA " +str(palabra.upper())+  " ,suerte para la proxima")
        return False
      print("JUGADOR " +str(jugador_act)+ " SE HA TERMINADO EL TIEMPO, LA PALABRA ERA: " +str(palabra) +"\n")
      return False

    def puntos(): # En esta Función podemos ver que dependiendo del nivel y del número de intentos que eligio el usuario esta retornara un número de puntos determinado. 
      if nivel_ == 1:
        punto_niv = 3
      elif nivel_ == 2:
        punto_niv = 5
      elif nivel_ == 3:
        punto_niv = 10
      elif nivel_ == 4:
        punto_niv = 5
      elif nivel_ == 5:
        punto_niv = 8
      elif nivel_ == 6:
        punto_niv = 10
      if num_intento == 3:
        punto_int= 10
      if num_intento == 4:
        punto_int = 8
      elif num_intento == 5:
        punto_int = 6
      elif num_intento == 6:
        punto_int = 5
      elif num_intento == 7:
        punto_int = 4
      elif num_intento == 8:
        punto_int = 3
      elif num_intento == 9:
        punto_int = 2
      elif num_intento == 10:
        punto_int = 1
      total = punto_niv + punto_int
      return total

    if jugador_act == 1:
      if __name__ == "__main__":
        puntos_1 = 0
        nivel_ = nivel()
        print("JUGADOR " +str(jugador_act)+ " AHORA YA ESCOGIDO EL NIVEL VAMOS CON INTENTOS \n")
        num_intento = intentos()
        palabra = palabra()
        ahorcado = img_ahoracado()
        juego = juego()
        if juego == True:
          puntos = puntos()
          puntos_1 = puntos_1 + puntos
        elif juego == False:
          puntos_1 = puntos_1
        puntos_jugador_1 = puntos_jugador_1 + puntos_1
        print("EL JUGADOR " +str(jugador_act)+ " TIENE " +str(puntos_jugador_1)+ " PUNTOS \n")

    elif jugador_act == 2:
      if __name__ == "__main__":
        puntos_2 = 0
        nivel_ = nivel()
        print("JUGADOR " +str(jugador_act)+ " AHORA YA ESCOGIDO EL NIVEL VAMOS CON INTENTOS \n")
        num_intento = intentos()
        palabra = palabra()
        ahorcado = img_ahoracado()
        juego = juego()
        if juego == True:
          puntos = puntos()
          puntos_2 = puntos_2 + puntos
        elif juego == False:
          puntos_2 = puntos_2
        puntos_jugador_2 = puntos_jugador_2 + puntos_2
        print("EL JUGADOR " +str(jugador_act)+ " TIENE " +str(puntos_jugador_2)+ " puntos \n")

  if puntos_jugador_1 > puntos_jugador_2:
    print("HA GANADO EL JUGADOR 1 CON " +str(puntos_jugador_1)+ " , JUGADOR 2 " +str(puntos_jugador_2)+ " puntos")
  elif puntos_jugador_1 < puntos_jugador_2:
    print("HA GANADO EL JUGADOR 2 CON " +str(puntos_jugador_2)+ " , JUGADOR 1 " +str(puntos_jugador_1)+ " puntos")
  elif puntos_jugador_1 == puntos_jugador_2:
    print("HAN EMPATADO EL JUGADOR 1 CON " +str(puntos_jugador_1)+ " Y EL JUGADOR 2 " +str(puntos_jugador_2)+ " puntos")