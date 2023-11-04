# Configuraciones extras y Scripts

## Configuración para borrado seguro
Este scrip guarda en el .zshrc
```
function rmk(){
    scrub -p dod $1
    shred -zun 20 -v $1
}
```
