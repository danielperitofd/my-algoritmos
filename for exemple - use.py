assistiu = [
    {'nome': 'Jeremi',
     'deu_like': True,
     'comentou': True
     },

     {'nome': 'Thalita',
     'deu_like': True,
     'comentou': True
     },

     {'nome': 'Meyra',
     'deu_like': False,
     'comentou': False
     }
]

for pessoa in assistiu:
    if pessoa['deu_like'] and pessoa['comentou']:
        print('MUITO OBRIGADO')
    else:
        print('FAZ ISSO NÃO POW')
    