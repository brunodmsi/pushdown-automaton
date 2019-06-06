class Grammars:
	def __init__(self):
		self.automata = ["SZ"]

	def printAutomata(self):
		print(self.automata)
	def normalizeAutomata(self):
		self.automata = ["SZ"]
	def automataLength(self):
		return len(self.automata)

	def G1(self, entry):
		self.printAutomata()

		for i in entry:
			for j in range(self.automataLength()):

				if self.automata[j][0] == "S" and i == "a":
					self.automata.append(self.automata[j].replace("S", "AB", 1))
					self.automata.append(self.automata[j].replace("S", "SBB", 1))
					self.automata[j] = " "

				elif self.automata[j][0] == "A" and i == "a":
					self.automata.append(self.automata[j].replace("A", "", 1))
					self.automata[j] = " "

				elif self.automata[j][0] == "B" and i == "b":
					self.automata.append(self.automata[j].replace("B", "", 1))
					self.automata[j] == " "

				else:
					print "NEGADO -> {0}".format(self.automata[j])
					self.automata[j] = " "

			indexs = []
			for j in range(self.automataLength()):
				if self.automata[j] == " ":
					indexs.append(j)

			for j in range(len(indexs)):
				del self.automata[indexs[len(indexs) - j - 1]]

			if self.automata:
				self.printAutomata()

		for j in self.automata:
			if j == "Z":
				print "DEFERIDA"
			else:
				print "INDEFERIDA"

		if not self.automata:
			print "INDEFERIDA"

		self.normalizeAutomata()

	def G2(self, entry):
		self.printAutomata()

		for i in entry:
			for j in range(self.automataLength()):

				if self.automata[j][0] == "S" and i == "a":
					self.automata.append(self.automata[j].replace("S", "ABB", 1))
					self.automata.append(self.automata[j].replace("S", "AA", 1))
					self.automata[j] = " "

				elif self.automata[j][0] == "A" and i == "a":
					self.automata.append(self.automata[j].replace("A", "", 1))
					self.automata.append(self.automata[j].replace("A", "BB", 1))
					self.automata[j] = " "

				elif self.automata[j][0] == "B" and i == "a":
					self.automata.append(self.automata[j].replace("B", "", 1))
					self.automata.append(self.automata[j].replace("B", "BB", 1))
					self.automata[j] = " "

				elif self.automata[j][0] == "B" and i == "b":
					self.automata.append(self.automata[j].replace("B", "BB", 1))
					self.automata[j] = " "

				else:
					print "NEGADO -> {0}".format(self.automata[j])
					self.automata[j] = " "
			
			indexs = []
			for j in range(self.automataLength()):
				if self.automata[j] == " ":
					indexs.append(j)

			for j in range(len(indexs)):
				del self.automata[indexs[len(indexs) - j - 1]]

			if self.automata:
				self.printAutomata()
			
		if "Z" in self.automata:
			print "DEFERIDA"
		else:
			print "INDEFERIDA"

		if not self.automata:
			print "INDEFERIDA"

		self.normalizeAutomata()

	def G3(self, entry):
		self.printAutomata()

		for i in entry:
			for j in range(self.automataLength()):

				if self.automata[j][0] == "S" and i == "a":
					self.automata.append(self.automata[j].replace("S", "", 1))
					self.automata[j] = " "

				elif self.automata[j][0] == "S" and i == "b":
					self.automata.append(self.automata[j].replace("S", "XA", 1))
					self.automata.append(self.automata[j].replace("S", "A", 1))
					self.automata[j] = " "

				elif self.automata[j][0] == "A" and i == "b":
					self.automata.append(self.automata[j].replace("A", "X", 1))
					self.automata.append(self.automata[j].replace("A", "", 1))
					self.automata[j] = " "				
				
				elif self.automata[j][0] == "X" and i == "b":
					self.automata.append(self.automata[j].replace("X", "XAX", 1))
					self.automata.append(self.automata[j].replace("X", "AX", 1))
					self.automata.append(self.automata[j].replace("X", "XA", 1))
					self.automata.append(self.automata[j].replace("X", "A", 1))
					self.automata[j] = " "

				elif self.automata[j][0] == "X" and i == "a":
					self.automata.append(self.automata[j].replace("X", "", 1))
					self.automata.append(self.automata[j].replace("X", "X", 1))
					self.automata[j] = " "

				else:
					print "NEGADO -> {0}".format(self.automata[j])
					self.automata[j] = " "		

			indexs = []
			for j in range(self.automataLength()):
				if self.automata[j] == " ":
					indexs.append(j)
			
			for j in range(len(indexs)):
				del self.automata[indexs[len(indexs) - j - 1]]

			if self.automata:
				self.printAutomata()

		if "Z" in self.automata:
			print "DEFERIDA"
		else:
			print "INDEFERIDA"

		if not self.automata:
			print "INDEFERIDA"

		self.normalizeAutomata()

	def G4(self, entry):
		self.printAutomata()

		for i in entry:
			for j in range(self.automataLength()):

				if i == "a" and self.automata[j][0] == "S":
						self.automata.append(self.automata[j].replace("S","BX", 1))
						self.automata.append(self.automata[j].replace("S", "XAX", 1))
						self.automata[j] = " "

				elif i == "b" and self.automata[j][0] == "S":
						self.automata.append(self.automata[j].replace("S", "", 1))
						self.automata[j] = " "

				elif i == "a" and self.automata[j][0] == "A":
						self.automata.append(self.automata[j].replace("A", "", 1))
						self.automata[j] = " "

				elif i == "b" and self.automata[j][0] == "B":
						self.automata.append(self.automata[j].replace("B", "", 1))
						self.automata[j] = " "

				elif i == "a" and self.automata[j][0] == "X":
						self.automata.append(self.automata[j].replace("X", "BX", 1))
						self.automata[j] = " "

				elif i == "b" and self.automata[j][0] == "X":
						self.automata.append(self.automata[j].replace("X", "", 1))
						self.automata[j] = " "

				else:
						print "INDEFERIDO -> ".format(self.automata[j])
						self.automata[j] = " "
					
			indexs = []
			for j in range(self.automataLength()):
				if self.automata[j] == " ":
					indexs.append(j)
			
			for j in range(len(indexs)):
				del self.automata[indexs[len(indexs) - j - 1]]

			if self.automata:
				self.printAutomata()

		if "Z" in self.automata:
			print "DEFERIDA"
		else:
			print "INDEFERIDA"

		if not self.automata:
			print "INDEFERIDA"

		self.normalizeAutomata()

				