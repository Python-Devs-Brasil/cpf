# -*- coding: utf-8 -*-
# A função "validate" recebe nove dígitos, após, gera 2 dígitos verificadores, matematicamente validando o CPF.
# A função "check" calcula e checa a veracidade do CPF fornecido.
# O script não checa com a Receita Federal, a checagem se baseia apenas na parte matemática.

def validate(x):
    x = str(x.replace(".",""))
    if len(x) != 9:
        return False
    else:
        x_ini = x
        z = (((int(x[0])*10)+(int(x[1])*9)+(int(x[2])*8)+(int(x[3])*7)+(int(x[4])*6)+(int(x[5])*5)+(int(x[6])*4)+(int(x[7])*3)+(int(x[8])*2)) % 11)
        if z <= 2:
            dv1 = 0
        else:
            dv1 = (11 - z)
        x = (str(x_ini) + str(dv1))
        z = (((int(x[0])*11)+(int(x[1])*10)+(int(x[2])*9)+(int(x[3])*8)+(int(x[4])*7)+(int(x[5])*6)+(int(x[6])*5)+(int(x[7])*4)+(int(x[8])*3)+(int(x[9])*2)) % 11)
        if z <= 2:
            dv2 = 0
        else:
            dv2 = (11 - z)
        cpf = (x_ini + str(dv1) + str(dv2))
        return("%s.%s.%s-%s" % ((str(cpf))[:3],(str(cpf))[3:6],(str(cpf))[6:9],(str(cpf))[9:]))

def check(x):
    base = (((str(x)).replace(".","")).replace("-",""))
    check = base[:-2]
    if (((str(validate(check))).replace(".","")).replace("-","")) == base:
        return True
    else:
        return False
