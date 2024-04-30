vitorias = int(input('Total de vitorias: '))
derrotas = int(input('Total de derrotas: '))
saldo = vitorias - derrotas

def ranqueada():
    
    if saldo >= 10:
        rank = "Ferro"
    elif saldo > 10 and saldo <= 20:
        rank = "Bronze"
    elif saldo > 20 and saldo <= 40:
        rank = "Prata"
    elif saldo > 40 and saldo <= 60:
        rank = "Ouro"
    elif saldo > 60 and saldo <= 80:
        rank = "Diamante"
    elif saldo > 80 and saldo <= 100:
        rank = "Lendário"
    elif saldo > 100:
        rank = "Imortal"

    return rank

rank = ranqueada()

print("O Herói tem de saldo de "+ str(saldo) +" vitórias está no nível de " + rank )
