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

El juego es como el de toda la vida: Hay una palabra oculta del cual tiene que adivinarse mediante el acierto de letras que van redescubriendo dicha palabra, de lo contrario bajo una cantidad de 11 intentos fallidos, el juego acabara.

Hemos destinado 5 niveles de dificultad elegidos a gusto del jugador. Su dificultad radicara en la cantidad de letras de la que este compuesta dicha palabra y/ su idioma en el que este predispuesta. 

Dichos niveles enfatizados mejor seria asi:

# Nivel 1: # Pala

