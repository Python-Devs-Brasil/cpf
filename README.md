## Descrição
Um script com funcionalidades relacionados a CPF.

- Geração aleatória válida
- Validação de cpf digitados

> Obs: O script apenas verifica a fórmula matemática de um **cpf**, não é checado o valor na Receita Federal.


#### Funções

**generate**
>Função que retorna um cpf válido

#### Métodos

instancia.**check**
>Função que retorna ```True``` caso cpf digitado seja válido e ```False``` caso contrário.


instancia.**validate**
>Função que retorna um ```list``` com os 2 dígitos verificadores do cpf

## Modo de Uso

Coloque o arquivo **cpf.py** no diretório do seu projeto

#### Para gerar um **cpf** válido:

```python
from cpf import *

cpf = generate()
print cpf

```

####Verificar um **cpf** digitado:

```python
from cpf import *

cpf_user = CPF(raw_input('CPF: '))

if cpf_user.check():
    print 'CPF válido'
else:
	print 'CPF inválido'
```

#### Verificar os 2 dígitos verificadores.

```python
from cpf import *

cpf = generate()
print 'CPF gerado: {}'.format(cpf)

digitos = cpf.validate()
print 'Dígitos verificadores : {}'.format(digitos)
```