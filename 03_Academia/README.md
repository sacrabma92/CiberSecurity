# Listado de Academia
En esta ocación estoy sacando apuntes sobre la Academia de S4vitar para tener los conceptos más claros e investigar al respecto.

# Instalación de SecList

Repositorio para ataque de fuerza bruta.
Clonamos el repo en la ruta: **/usr/share/**

[SecList](https://github.com/danielmiessler/SecLists)

![label text](imgs/01.png)

# Comandos Eliminacion Docker

Borrar todas las imagenes

```
docker rmi $(docker images -q) --force
```

Borrar todos los contenedores

```
docker rm $(docker ps -a -q) --force
```

Borrar volumenes

```
docker volume rm $(docker volume ls -q)
```

[01 Conceptos Básicos](https://github.com/sacrabma92/CiberSecurity/tree/main/03_Academia/01%20Conceptos%20Basicos)
[02 Reconocimiento](https://github.com/sacrabma92/CiberSecurity/tree/main/03_Academia/02_Reconocimiento)
