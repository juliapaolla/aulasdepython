#01 a
idade = 18
convidado = True
comprou_ingresso = True

print((idade >= 18 and comprou_ingresso) or (idade >= 18 and convidado))

#b)
idade = 18
vip = True
feminino = True
comprou_ingresso = True

print((idade >= 18 and vip and feminino) or (idade >= 18 and comprou_ingresso))


#03
cliente = 5
garantia = True
deposito_inicial = True 
conta_especial = True

print((cliente >= 5 and garantia and deposito_inicial) or (conta_especial and deposito_inicial))


#04
prova = 70
frequencia = 75
pagomatricula = True
inscricaoprazo = True

print((prova >= 70 and frequencia >= 75) or (pagomatricula and inscricaoprazo))


