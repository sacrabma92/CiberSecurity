# Enumeración de gestores de contenido (CMS) – Joomla

AVISO: Han actualizado el proyecto de Github, ahora simplemente lo despliegas con ‘docker-compose up -d‘ y no hace falta realizar el proceso de instalación, ya te viene todo instalado por defecto 😊

En esta clase, estaremos viendo cómo enumerar el gestor de contenido Joomla. Joomla es un sistema de gestión de contenidos (CMS) de código abierto que se utiliza para crear sitios web y aplicaciones en línea. Joomla es muy popular debido a su facilidad de uso y flexibilidad, lo que lo hace una opción popular para sitios web empresariales, gubernamentales y de organizaciones sin fines de lucro.

Joomla es altamente personalizable y cuenta con una gran cantidad de extensiones disponibles, lo que permite a los usuarios añadir funcionalidades adicionales a sus sitios web sin necesidad de conocimientos de programación avanzados. Joomla también cuenta con una comunidad activa de desarrolladores y usuarios que comparten sus conocimientos y recursos para mejorar el CMS.

A continuación, se comparte el enlace del proyecto que estaremos desplegando en Docker para auditar un Joomla:

* CVE-2015-8562: [https://github.com/vulhub/vulhub/tree/master/joomla/CVE-2015-8562](https://github.com/vulhub/vulhub/tree/master/joomla/CVE-2015-8562)
Una de las herramientas que usamos en esta clase es Joomscan. Joomscan es una herramienta de línea de comandos diseñada específicamente para escanear sitios web que utilizan Joomla y buscar posibles vulnerabilidades y debilidades de seguridad.

Joomscan utiliza una variedad de técnicas de enumeración para identificar información sobre el sitio web de Joomla, como la versión de Joomla utilizada, los plugins y módulos instalados y los usuarios registrados en el sitio. También utiliza una base de datos de vulnerabilidades conocidas para buscar posibles vulnerabilidades en la instalación de Joomla.

Para utilizar Joomscan, primero debemos descargar la herramienta desde su sitio web oficial. A continuación se os proporciona el enlace al proyecto:

* Joomscan: [https://github.com/OWASP/joomscan](https://github.com/OWASP/joomscan)
Una vez descargado, podemos utilizar la siguiente sintaxis básica para escanear un sitio web de Joomla:

➜ perl joomscan.pl -u <URL>

Donde <URL> es la URL del sitio web que deseamos escanear. Joomscan escaneará el sitio web y nos proporcionará una lista detallada de posibles vulnerabilidades y debilidades de seguridad.

Es importante tener en cuenta que joomscan no es una herramienta infalible y puede generar falsos positivos o falsos negativos. Por lo tanto, es importante utilizar joomscan junto con otras herramientas y técnicas de seguridad para tener una imagen completa de la seguridad del sitio web de Joomla que estemos auditando.






















































