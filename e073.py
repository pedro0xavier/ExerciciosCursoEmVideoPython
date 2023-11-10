'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:a) Os 5 primeiros times.b) Os últimos 4 colocados.c) Times em ordem alfabética.d) Em que posição está o time do Vasco.'''

timesbr = 'Botafogo', 'Palmeiras','Bragantino', 'Grêmio', 'Atlético MG','Flamengo', 'Athletico PR', 'Fluminense', 'Fortaleza', 'São Paulo', 'Internacional', 'Cuiabá', 'Corinthans', 'Santos', 'Bahia', 'Vasco da Gama', 'Cruzeiro', 'Goiás', 'Coritiba','América MG'
print (f'Os primeiros cinco times da tabela do brasileirão são {timesbr[0:4]}')
print (f'Os quatro últimos colocados são {timesbr[-4:]}')
print(f'Os times em ordem alfabética: {sorted (timesbr)}')