# -*- coding: utf-8 -*-
"""
Rotinas de manipulação e validação de números de CPF.

"""

class CPFError(Exception):
	pass

class CPF:
	"""
	Validação matemática do número do Cadastro de Pessoas Físicas (CPF).

	"""
	def __init__(self, cpf=''):
		if not '-' in cpf:
			cpf += '-'

		cpf = cpf.replace('.', '').split('-')
		self.__nums__ = map(int, cpf[0])
		self.__validation__ = map(int, cpf[1])

		if not len(self.__nums__) in (0, 9):
			raise CPFError,	"O CPF tem %d dígitos em vez de 9" % len(
					self.__nums__)

		if not len(self.__validation__) in (0, 2):
			raise CPFError, ("O dígito de verificação tem %d" +
				" dígitos em vez de 2") % len(
					self.__validation__)

	def __str__(self, usedots=True):
		"""
		Retorna o CPF como string.

		@param usedots: Usa notação com pontos a cada três números.

		Ex.:
		>>> c = CPF('123456789-00')
		>>> str(c)
		'123.456.789-00'
		>>> c = CPF('123.456.789')
		>>> str(c)
		'123.456.789-00'
		>>> c.__str__(False)
		'123456789-00'
		"""
		return ('%d%d%d.%d%d%d.%d%d%d-%d%d' if usedots else
				'%d%d%d%d%d%d%d%d%d-%d%d') % tuple(self.__nums__+self.__validation__)

	def __repr__(self):
		return '<CPF %s at 0x%x>' % (str(self), id(self))

	def validate(self):
		"""
		Calcula os dígitos de verificação para o CPF.

		@return: Uma lista com os dígitos de verificação.
		"""

		z = 0
		vd = [0,0]

		for i in range(len(self.__nums__)):
			z += self.__nums__[i] * (10 - i)
		z = z % 11

		vd[0] = 0 if z <= 2 else (11 - z)

		tmp = self.__nums__ + [vd[0]]
		z = 0
		for i in range(len(tmp)):
			z += tmp[i] * (11 - i)
		z = z % 11

		vd[1] = 0 if z <= 2 else (11 - z)

		self.__validation__ = vd

		return vd

	def check(self):
		"""
		Verifica se o dígito de verificação dado corresponde ao
		resto do número de CPF.

		@return: True se válido, False caso contrário.
		"""
		v = self.__validation__
		return v == self.validate()

def generate():
	"""
	Gera um número de CPF aleatório válido.

	@return: Um objeto do tipo CPF correspondente.
	"""
	from random import randint

	cpf = ''.join(map(str, [randint(0, 9) for i in range(0, 9)]))
	cpf = CPF(cpf)
	cpf.validate()

	return cpf

def main():
	"""
	Inicia módulo como script.
	"""
	import sys
	import getopt

	opts, args = getopt.getopt(sys.argv[1:], 'gv:')
		
	for opt,arg in opts:
		if opt == '-g':
			print generate()
			return
		elif opt == '-v':
			c = CPF(arg)
			if c.check():
				print 'CPF válido.'
				sys.exit(0)
			else:
				print 'CPF inválido.'
				sys.exit(1)


if __name__ == '__main__':
	main()
