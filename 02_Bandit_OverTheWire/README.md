# Comandos o notas extras

## Contar las lineas que tiene un fichero
Con el comando wc -l contamos la cantidad de lineas que tiene\
![label text](imgs/02.png)

## Mostrar el ultimo argumento con AWK 
```
awk 'NF{print $NF}'
```
Con el comando nos trae el ultimo argumento \
![label text](imgs/03.png)

# Independizar un proceso
Independizar un programa de la Shell, en caso que no funcione con -a quitarla 
```
disown -a
```

## 1 Averiguar en que linea se encuentra una palabra GREP
## 2 Buscar en un archivo la linea X que contiene AWK
![label text](imgs/04.png)

## Comando que busca un archivo por variables
```
find . -type f -printf "%f\t%p\t%u\t%g\t%m\n | column -t
```
**%f** -> Archivos \
**%p** -> Ruta absoluta '
**%u** -> El usuario propietario del archivo \
**%g** -> El grupo asignado \
**%m** -> Permisos asignados a nivel numerico \
**\\t** -> Tabulador \
**\\n** -> Salto de linea \
**column -t** -> Organiza todo en columnas separado por tabulador \
![label text](imgs/01.png) \

# Comando Xargs
Se utiliza para aplicar un comando de forma paralela al siguiente comando \




