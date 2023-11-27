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
- Listado de palabras a jugar
- Imagen de muñequito siendo ahorcado
- Limite de tiempo
- Juego final

### Importe de librerias

Para el despliegue adecuado de nuestro codigo, importamos "random", "unicodedata" y "time", ya que estos nos sentaron las bases para un uso indicado del juego

```

import random
import unicodedata
import time

```

### Instrucciones y nivel de juego

El juego es como el de toda la vida: Hay una palabra oculta del cual tiene que adivinarse mediante el acierto de letras que van redescubriendo dicha palabra, de lo contrario bajo una cantidad (que el mismo usuarios elegirá) de intentos fallidos, el juego acabara.

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



