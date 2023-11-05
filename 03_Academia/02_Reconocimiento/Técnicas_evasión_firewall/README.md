# Técnicas evasión de Firewall (MTU, Data Length, Source Port, Decoy, etc...)

Cuando se realizan pruebas de penetración, uno de los mayores desafíos es evadir la detección de los Firewalls, que son diseñados para proteger las redes y sistemas de posibles amenazas. Para superar este obstáculo, Nmap ofrece una variedad de técnicas de evasión que permiten a los profesionales de seguridad realizar escaneos sigilosos y evitar así la detección de los mismos.

Algunos de los parámetros vistos en esta clase son los siguientes:

MTU (–mtu): La técnica de evasión de MTU o “Maximum Transmission Unit” implica ajustar el tamaño de los paquetes que se envían para evitar la detección por parte del Firewall. Nmap permite configurar manualmente el tamaño máximo de los paquetes para garantizar que sean lo suficientemente pequeños para pasar por el Firewall sin ser detectados.
Data Length (–data-length): Esta técnica se basa en ajustar la longitud de los datos enviados para que sean lo suficientemente cortos como para pasar por el Firewall sin ser detectados. Nmap permite a los usuarios configurar manualmente la longitud de los datos enviados para que sean lo suficientemente pequeños para evadir la detección del Firewall.
Source Port (–source-port): Esta técnica consiste en configurar manualmente el número de puerto de origen de los paquetes enviados para evitar la detección por parte del Firewall. Nmap permite a los usuarios especificar manualmente un puerto de origen aleatorio o un puerto específico para evadir la detección del Firewall.
Decoy (-D): Esta técnica de evasión en Nmap permite al usuario enviar paquetes falsos a la red para confundir a los sistemas de detección de intrusos y evitar la detección del Firewall. El comando -D permite al usuario enviar paquetes falsos junto con los paquetes reales de escaneo para ocultar su actividad.

Fragmented (-f): Esta técnica se basa en fragmentar los paquetes enviados para que el Firewall no pueda reconocer el tráfico como un escaneo. La opción -f en Nmap permite fragmentar los paquetes y enviarlos por separado para evitar la detección del Firewall.
Spoof-Mac (–spoof-mac): Esta técnica de evasión se basa en cambiar la dirección MAC del paquete para evitar la detección del Firewall. Nmap permite al usuario configurar manualmente la dirección MAC para evitar ser detectado por el Firewall.
Stealth Scan (-sS): Esta técnica es una de las más utilizadas para realizar escaneos sigilosos y evitar la detección del Firewall. El comando -sS permite a los usuarios realizar un escaneo de tipo SYN sin establecer una conexión completa, lo que permite evitar la detección del Firewall.
min-rate (–min-rate): Esta técnica permite al usuario controlar la velocidad de los paquetes enviados para evitar la detección del Firewall. El comando –min-rate permite al usuario reducir la velocidad de los paquetes enviados para evitar ser detectado por el Firewall.
Es importante destacar que, además de las técnicas de evasión mencionadas anteriormente, existen muchas otras opciones en Nmap que pueden ser utilizadas para realizar pruebas de penetración efectivas y evadir la detección del Firewall. Sin embargo, las técnicas que hemos mencionado son algunas de las más populares y ampliamente utilizadas por los profesionales de seguridad para superar los obstáculos que presentan los Firewalls en la realización de pruebas de penetración.

## Fragmentar paquete
```
nmap -f -p- 192.168.1.1
```

El parametro --mtu (Maximum tranmision unit) debe ser multiplo de 8 el minimo es 8. 8,16,24 etc...
```

nmao -f -p- --mtu 8 192.168.1.1
```

## Decoy
El parametro -D lo que hace es tramimar peticiones desde otras IP que se le pasen. Puede ser que desde otra IP pueda tener respuesta --OPEN el puerto que estamos tramitando. En este caso los 500 mas buscados. Se puede colocar mas IP's separado por ,
```
nmap -p --top-ports 500 -v -n 192.168.1.1 -D 192.168.1.2,192.168.1.3,192.168.1.4
```

## Cambiar el tamaño del paquete
Hay Firewall que reconocen el tamaño de paquetes que se envian entonces pueden bloquear la petición, por este motivo podriamos cambiar el tamaño.
Lo que estamos haciendo decirle a nmap que el paquete le sume 21 al peso del paquete.
```
nmap -p22 192.168.1.1 --data-length 21
```

## Selft Scan -sS
A nivel de paquetes lo hace es NO enviar un RST. En algunos casos los firewall pueden estar configurados para que no guarden log de este tipo de scan.
```
nmap -p- --open -sS --min-rate 5000 -v -n -Pn 192.168.1.1
```
