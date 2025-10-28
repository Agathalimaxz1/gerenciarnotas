def calcular_media(lst):
    return sum(lst) / len(lst)
def verificar_situacao(media):
    if media >= 7:
        return "Aprovado"
    elif 5 <= media <= 6.9:
        return "Recuperação"
    elif media <5:
        return "Reprovado"

