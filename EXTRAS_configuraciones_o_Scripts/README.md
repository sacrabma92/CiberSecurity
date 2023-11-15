# Configuraciones extras y Scripts

## Configuración para borrado seguro
Este scrip guarda en el .zshrc
```ruby
function rmk(){
    scrub -p dod $1
    shred -zun 20 -v $1
}
```

Este Script para resetear el target de la polybar

```python
function cleartarget(){
	echo '' > /home/dxz/.config/bin/target
}
```

# Atajos de Teclado de Linux para Shell

```
Ctrl + A	-> Voy al inicio de la linea de comandos
Ctrl + E	-> Voy al final de la linea de comandos
Alt + B		-> Ir al comienzo de la palabra anterior
Alt + F		-> Avanzar de palabra a palabra
Ctrl + U	-> Borrar desde el cursor al Inicio
Ctrl + K	-> Borrar desde el cursor al final
Ctrl + W	-> Borrar la palabra anterior "hasta que encuentre un espacio"
Alt + D		-> Borrar la palabra siguiente

```






















