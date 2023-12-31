# Enumeración y explotación de WebDAV

WebDAV (Web Distributed Authoring and Versioning) es una extensión del protocolo HTTP que permite a los usuarios acceder y manipular archivos en un servidor web a través de una conexión segura.

Cuando hablamos de enumerar un servidor WebDAV, a lo que nos referimos es al proceso de recopilar información sobre los recursos disponibles en el servidor WebDAV. Los atacantes pueden utilizar herramientas de enumeración de WebDAV para buscar recursos protegidos en el servidor, como archivos de configuración, contraseñas y otros datos confidenciales. Los atacantes pueden utilizar la información recopilada durante la enumeración para planificar ataques más sofisticados contra el servidor.

Asimismo, esta fase inicial de reconocimiento implica el intentar identificar las extensiones de archivo permitidas en el servidor. Una vez detectadas las extensiones de archivo permitidas, los atacantes pueden aprovecharse de esto para cargar y ejecutar archivos que contengan código malicioso. Si los archivos maliciosos se cargan y ejecutan con éxito en el servidor web, los atacantes pueden obtener acceso no autorizado al servidor y comprometer la seguridad del sistema.

Una de las herramientas que vemos en esta clase es Davtest. La herramienta Davtest es una herramienta de línea de comandos que se utiliza para realizar pruebas de penetración en servidores WebDAV. Davtest puede utilizarse para enumerar recursos protegidos en un servidor WebDAV, así como para probar la configuración de seguridad del servidor. Davtest también puede utilizarse para probar la autenticación y la autorización del servidor, y para detectar vulnerabilidades conocidas.

Otra de las herramientas que vemos en esta clase es Cadaver. Cadaver es otra herramienta de línea de comandos que se utiliza para interactuar con servidores WebDAV. Cadaver permite a los usuarios navegar por los recursos del servidor, cargar y descargar archivos, y ejecutar comandos en el servidor. Cadaver también puede utilizarse para realizar pruebas de penetración en servidores WebDAV, como la enumeración de recursos protegidos y la explotación de vulnerabilidades conocidas.

Para prevenir la enumeración y explotación de WebDAV, es importante que los administradores de sistemas implementen medidas de seguridad adecuadas en el servidor. Esto puede incluir la limitación de los recursos disponibles en el servidor y la utilización de autenticación y autorización fuertes. Además, es importante que los usuarios protejan sus contraseñas y eviten el uso de contraseñas débiles o fáciles de adivinar.

A continuación, se proporciona el enlace al proyecto de Github el cual estaremos usando en esta clase para desplegar un entorno vulnerable con el que poder practicar:

WebDav: [https://hub.docker.com/r/bytemark/webdav](https://hub.docker.com/r/bytemark/webdav)
