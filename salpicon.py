from operator import itemgetter

def recibir_frutas():
    frutas = []
    cantidad_frutas = int(input("Ingrese la cantidad de frutas para el salpicón: "))
    for i in range(1, cantidad_frutas + 1):
        fruta = {}
        fruta["id"] = i
        fruta["nombre"] = input(f"Ingrese el nombre de la fruta {i}: ")
        fruta["precio_unitario"] = float(input(f"Ingrese el precio unitario de la fruta {i}: "))
        fruta["cantidad"] = int(input(f"Ingrese la cantidad de la fruta {i}: "))
        frutas.append(fruta)
    return frutas

def costo_total(frutas):
    total = sum(fruta["precio_unitario"] * fruta["cantidad"] for fruta in frutas)
    return total

def mostrar_frutas_ordenadas(frutas):
    frutas_ordenadas = sorted(frutas, key=itemgetter("precio_unitario"), reverse=True)
    for fruta in frutas_ordenadas:
        print(f"{fruta['nombre']}: {fruta['precio_unitario']}")

def fruta_mas_barata(frutas):
    fruta_barata = min(frutas, key=itemgetter("precio_unitario"))
    return fruta_barata["nombre"]


frutas = recibir_frutas()
print(f"\nCosto total del salpicón: {costo_total(frutas)}")

print("\nFrutas ordenadas de mayor a menor costo:")
mostrar_frutas_ordenadas(frutas)

print("\nFruta más barata:")
print(fruta_mas_barata(frutas))