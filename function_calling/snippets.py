
# posicional indireto
args = (1, 2)
func(*args)

# posicional direto
func(1, 2)

# nomeado indireto
kwargs = {'foo': 1, 'bar': 2}
func(**kwargs)

# nomeado direto
func(foo=1, bar=2)

