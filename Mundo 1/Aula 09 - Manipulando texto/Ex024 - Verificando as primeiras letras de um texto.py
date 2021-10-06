cid = input('Qual cidade você mora? ')
cid2 = cid.upper()
cid3 = cid2.split()
cid4 = 'SANTO' in cid3[0]
print('Sua cidade {} começa com a palavra santo?'.format(cid))
print(cid4)