greeting = "hELLO WORLD AND OTHERS"
print(greeting)
print(greeting.split())
print(greeting.split(sep=" "))
print(greeting.split(sep=":"))

greeting = "hELLO:WORLD:AND:OTHERS"
print(greeting.split(sep=":"))
print(greeting.split(sep=":", maxsplit=2))


