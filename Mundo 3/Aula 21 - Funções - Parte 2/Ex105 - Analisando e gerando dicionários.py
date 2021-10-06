def notas(*nota, sit=False):
    """
        -> Analizando Notas
        :param nota: Recebe varios valores para a expressão
        :param sit: Mostra a situação do aluno, de acordo com a média
        :return: Retorna uma dicionário com os valores: Total de Notas, Maior Nota, Menor Nota, Situação (opcional)
    """
    r = {'Total': len(nota), 'Maior': max(nota), 'Menor': min(nota), 'Média': sum(nota) / len(nota)}
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'APROVADO'
        if r['Média'] >= 5:
            r['Situação'] = 'RECUPERAÇÃO'
        else:
            r['Situação'] = 'REPROVADO'
    return r


resp = notas(2, 5, 9, 7, sit=True)
print(resp)
help(notas)
