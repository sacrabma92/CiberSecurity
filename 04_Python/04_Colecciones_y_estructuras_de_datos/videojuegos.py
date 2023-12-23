#!/usr/bin/python3

juegos = ["Super Mario Bros", "Zelda: Breath of the Wild", "Cyberpunk 2077", "Final Fantasy VII"]

tope = 500

# Género
generos = {
	"Super Mario Bros": "aventura",
	"Zelda: Breath of the Wild": "Aventura",
	"Cyberpunk 2077": "Rol",
	"Final Fantasy VII": "Rol"
}

# Ventas y Stock
ventas_y_stock = {
	"Super Mario Bros": (400,200),
	"Zelda: Breath of the Wild": (600,20),
	"Cyberpunk 2077": (60,120),
	"Final Fantasy VII": (924,3)
}

# Clientes
clientes = {
	"Super Mario Bros": {"Carlos", "DXZ", "Hackvos", "Securiters", "Kibire"},
	"Zelda: Breath of the Wild": {"Carlos", "Hackvos", "Pepe", "Lucia"},
	"Cyberpunk 2077": {"Pepe", "Raquel", "Albert"},
	"Final Fantasy VII": {"Lucia", "Manolo", "Pepe", "Securiters", "Patricia", "Moises"}
}

def sumario(juego):
	# Sumario
	print(f"\n[i] Resumen del juego: {juego}\n")
	print(f"\t[+] Género del juego: {generos[juego]}")
	print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades")
	print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]} unidades")
	print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}")

for juego in juegos:
	if ventas_y_stock[juego][0] > tope:
		sumario(juego)

ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope)

print(f"\n[+] El total de ventas de todos los productos ha sido de {ventas_totales()} productos")

