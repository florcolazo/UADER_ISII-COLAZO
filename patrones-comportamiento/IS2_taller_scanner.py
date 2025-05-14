import os

"""State class: Base State class"""
class State:

	def scan(self):
		# Avanza a la siguiente estación
		self.pos += 1
		if self.pos == len(self.stations):
			self.pos = 0
		print("Sintonizando... Estación {} {}".format(self.stations[self.pos], self.name))

#*------- Implementa como barrer las estaciones de AM
class AmState(State):

	def __init__(self, radio):
		self.radio = radio
		self.stations = ["1250", "1380", "1510"]
		self.pos = 0
		self.name = "AM"

	def toggle_amfm(self):
		print("Cambiando a FM")
		self.radio.state = self.radio.fmstate

#*------- Implementa como barrer las estaciones de FM
class FmState(State):

	def __init__(self, radio):
		self.radio = radio
		self.stations = ["81.3", "89.1", "103.9"]
		self.pos = 0
		self.name = "FM"

	def toggle_amfm(self):
		print("Cambiando a AM")
		self.radio.state = self.radio.amstate

#*--------- Construye la radio con todas sus formas de sintonía
class Radio:

	def __init__(self):
		self.fmstate = FmState(self)
		self.amstate = AmState(self)
		self.state = self.fmstate  # Inicialmente en FM

		# Diccionario de memorias M1 a M4 (pueden ser AM o FM)
		self.memorias = {
			'M1': ("AM", "1380"),
			'M2': ("FM", "103.9"),
			'M3': ("AM", "1510"),
			'M4': ("FM", "89.1")
		}
		self.memoria_keys = list(self.memorias.keys())
		self.memoria_index = 0

	def toggle_amfm(self):
		self.state.toggle_amfm()

	def scan(self):
		# Escanea estación actual
		self.state.scan()

		# También escanea una memoria
		memoria_actual = self.memoria_keys[self.memoria_index]
		tipo, frecuencia = self.memorias[memoria_actual]
		print(f"Memoria {memoria_actual}: {tipo} {frecuencia}")

		# Avanza al siguiente índice de memoria
		self.memoria_index += 1
		if self.memoria_index == len(self.memoria_keys):
			self.memoria_index = 0

#*---------------------
if __name__ == "__main__":
	os.system("clear")
	print("\nCrea un objeto radio y almacena las siguientes acciones")
	radio = Radio()
	actions = [radio.scan] * 3 + [radio.toggle_amfm] + [radio.scan] * 3
	actions *= 2

	print("\nRecorre las acciones ejecutando la acción, el objeto cambia la interfaz según el estado\n")
	for action in actions:
		action()
