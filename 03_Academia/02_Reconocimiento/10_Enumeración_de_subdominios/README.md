# Enumeración de subdominios

IMPORTANTE: Recientemente, hemos notado un problema con la herramienta “sublist3r” del repositorio que presentamos en el vídeo: no está mostrando los subdominios del dominio que introduces durante el proceso de reconocimiento.

Aunque es probable que este error se corrija pronto, para quienes necesiten usar la herramienta sin inconvenientes en este momento, os sugiero descargarla desde este repositorio alternativo:

* [https://github.com/huntergregal/Sublist3r](https://github.com/huntergregal/Sublist3r)
 
La enumeración de subdominios es una de las fases cruciales en la seguridad informática para identificar los subdominios asociados a un dominio principal.

Los subdominios son parte de un dominio más grande y a menudo están configurados para apuntar a diferentes recursos de la red, como servidores web, servidores de correo electrónico, sistemas de bases de datos, sistemas de gestión de contenido, entre otros.

Al identificar los subdominios vinculados a un dominio principal, un atacante podría obtener información valiosa para cada uno de estos, lo que le podría llevar a encontrar vectores de ataque potenciales. Por ejemplo, si se identifica un subdominio que apunta a un servidor web vulnerable, el atacante podría utilizar esta información para intentar explotar la vulnerabilidad y acceder al servidor en cuestión.

Existen diferentes herramientas y técnicas para la enumeración de subdominios, tanto pasivas como activas. Las herramientas pasivas permiten obtener información sobre los subdominios sin enviar ninguna solicitud a los servidores identificados, mientras que las herramientas activas envían solicitudes a los servidores identificados para encontrar subdominios bajo el dominio principal.

Algunas de las herramientas pasivas más utilizadas para la enumeración de subdominios incluyen la búsqueda en motores de búsqueda como Google, Bing o Yahoo, y la búsqueda en registros DNS públicos como PassiveTotal o Censys. Estas herramientas permiten identificar subdominios asociados con un dominio, aunque no siempre son exhaustivas. Además, existen herramientas como CTFR que utilizan registros de certificados SSL/TLS para encontrar subdominios asociados a un dominio.

También se pueden utilizar páginas online como Phonebook.cz e Intelx.io, o herramientas como sublist3r, para buscar información relacionada con los dominios, incluyendo subdominios.

Por otro lado, las herramientas activas para la enumeración de subdominios incluyen herramientas de fuzzing como wfuzz o gobuster. Estas herramientas envían solicitudes a los servidores mediante ataques de fuerza bruta, con el objetivo de encontrar subdominios válidos bajo el dominio principal.

A continuación, os adjuntamos los enlaces a las herramientas vistas en esta clase:

* Phonebook (Herramienta pasiva): [https://phonebook.cz/](https://phonebook.cz/)
* Intelx (Herramienta pasiva): [https://intelx.io/](https://intelx.io/)
* CTFR (Herramienta pasiva): [https://github.com/UnaPibaGeek/ctfr](https://github.com/UnaPibaGeek/ctfr)
* Gobuster (Herramienta activa): [https://github.com/OJ/gobuster](https://github.com/OJ/gobuster)
* Wfuzz (Herramienta activa): [https://github.com/xmendez/wfuzz](https://github.com/xmendez/wfuzz)
* Sublist3r (Herramienta pasiva): [https://github.com/huntergregal/Sublist3r](https://github.com/huntergregal/Sublist3r)

Buscar subdominios
![label text](imgs/01.png)

Buscar email's
![label text](imgs/02.png)

Buscar Urls
![label text](imgs/03.png)

# Herramienta para enumerar Subdomains

## CTRF
Herramienta recolección de subdominio de forma, PASIVA!

Primero clonamos el Repositorios\
Instalamos los paquetes necesarios

![labelt text](imgs/04.png)

Ejecutamos la herramienta para ver que parametros necesitamos\
Toca pasarle el -d mas el dominio y ENTER!

![label text](imgs/05.png)

## Gobuster
Herramienta recolección de subdominios de forma, AGRESIVA o ACTIVA! ya que emplea el uso de BruteForce
![label text](imgs/06.png)

El parametro -u para el dominio\
El parametro -w para la lista a usar\
El parametro -t 20 para hilos\
El grep -v "403" para que nos quite lo que tengan error 403

![label text](imgs/07.png)

## wfuzz
Herramienta de Fuzzing

**FUZZ** es la palabra reservada donde colocara el diccionario

Parametro -c -> coloca color a la saldia\
Parametro --hc=403 oculta los que tengan el 403\
Parametro -t 20 -> lo hace con hilos\
Parametro -w -> seleccionamos la lista a usar\
Parametro -H "Host: FUZZ.tinder.com" donde coloca FUZZ colocara el diccionario\
URL a buscar\

![label text](imgs/08.png)

## Sublist3r

Clonamos el repositorio en la carpeta **/opt/**\
Ingresamos e instalamos

```
python3 setup.py install
```

![label text](imgs/09.png)

Instalamos paquetes que fuera requeridos

```
pip3 install -r requirements.txt
```

![label text](imgs/10.png)

Usamos la herramienta de la siguiente forma

```
python3 sublist3r.py -d tinder.com
```

![label text](imgs/11.png)





























