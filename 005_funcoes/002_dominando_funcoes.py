def salvar_carro(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

#exemplos de como poderá chamar a função criada
salvar_carro("Fiat","Palio",1999, "ABC-1234")

salvar_carro(marca="Fiat",modelo="Palio", ano= 1999, placa ="ABC-1234")

#esse é o melhor jeito de chamar função
salvar_carro(**{"marca":"Fiat","modelo":"Palio", "ano": 1999, "placa": "ABC-1234"})