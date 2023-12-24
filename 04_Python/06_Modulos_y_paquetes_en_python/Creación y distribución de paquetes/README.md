## Cursos disponibles:

- Introducción a Linux [15 horas]
- Personalización de Linux [3 horas]
- Introducción al Hacking [53 horas]

## Instalación

Instala el paquete usando 'pip3'

'''python3
pip3 install hack4u
'''

## Uso básico

### Listar tods los cursos

'''python
from hack4u import list_courses

for coruse in list_coruses():
  print(coruse)
'''

### Obtener un curso por nombre

'''python
from hack4u import get_curse_by_name

course = get_course_by_name("Introduccion a Linux")
print(course)
'''

### Calcular duración total de los cursos

'''python3
from hack4u.utils import total_duration

print(f"Duracción total: {total_duration()} horas")
'''