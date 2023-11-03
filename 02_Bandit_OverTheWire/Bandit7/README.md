# Bandit 7

El password para el siguiente nivel esta almacenado en un archivo **data.txt** junto con la palabra **millionth**
![label text](imgs/01.png)

Grepeamos la palabra millionth en el archivo data.txt\
Una de las formas de hacerlos es por medio de
```
grep "millionth" data.txt
```
Otra forma de hacer la busqueda en el fichero es
```
cat data.txt | grep "millionth"
```
Otra forma buscar seria:
```
awk '/millionth/' data.txt
```
Obtenemos un resultados con dos valores distitnos 1 a la izquierda y el otro a la derecha. Para quedarnos solamente con el que nos interesa el de la derecha hacemos un:
```
awk 'NF{print $NF}'
```
