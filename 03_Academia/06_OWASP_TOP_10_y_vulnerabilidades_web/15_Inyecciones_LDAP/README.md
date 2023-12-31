# Inyecciones LDAP

NOTA (Actualización 24/04/2023): A la hora de clonar el proyecto y hacer un ‘docker build -t ldap-client-container .‘, es probable que tras ejecutar la instrucción ‘apt-get update‘, os salga un error que os impide construir la imagen correctamente.

Para evitar este problema, tan solo es necesario cambiar en el archivo ‘Dockerfile‘ la primera línea de ‘FROM php:7.0-apache‘ a ‘FROM php:8.0-apache‘. De esta forma, ya no tendréis problemas y el laboratorio se podrá desplegar correctamente:

Las inyecciones LDAP (Protocolo de Directorio Ligero) son un tipo de ataque en el que se aprovechan las vulnerabilidades en las aplicaciones web que interactúan con un servidor LDAP. El servidor LDAP es un directorio que se utiliza para almacenar información de usuarios y recursos en una red.

La inyección LDAP funciona mediante la inserción de comandos LDAP maliciosos en los campos de entrada de una aplicación web, que luego son enviados al servidor LDAP para su procesamiento. Si la aplicación web no está diseñada adecuadamente para manejar la entrada del usuario, un atacante puede aprovechar esta debilidad para realizar operaciones no autorizadas en el servidor LDAP.

Al igual que las inyecciones SQL y NoSQL, las inyecciones LDAP pueden ser muy peligrosas. Algunos ejemplos de lo que un atacante podría lograr mediante una inyección LDAP incluyen:

* Acceder a información de usuarios o recursos que no debería tener acceso.
* Realizar cambios no autorizados en la base de datos del servidor LDAP, como agregar o eliminar usuarios o recursos.
* Realizar operaciones maliciosas en la red, como lanzar ataques de phishing o instalar software malicioso en los sistemas de la red.
Para evitar las inyecciones LDAP, las aplicaciones web que interactúan con un servidor LDAP deben validar y limpiar adecuadamente la entrada del usuario antes de enviarla al servidor LDAP. Esto incluye la validación de la sintaxis de los campos de entrada, la eliminación de caracteres especiales y la limitación de los comandos que pueden ser ejecutados en el servidor LDAP.

También es importante que las aplicaciones web se ejecuten con privilegios mínimos en la red y que se monitoreen regularmente las actividades del servidor LDAP para detectar posibles inyecciones.

A continuación, se proporciona el enlace directo al proyecto de Github que nos descargamos para desplegar un laboratorio práctico donde poder ejecutar esta vulnerabilidad:

LDAP-Injection-Vuln-App: [https://github.com/motikan2010/LDAP-Injection-Vuln-App](https://github.com/motikan2010/LDAP-Injection-Vuln-App)
