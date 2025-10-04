def minha_funcao_decoradora(funcao_decoradora):
    def funcao_wrapper():
        print("essa aqui vai ser um decorador")
        funcao_decoradora()
    return funcao_wrapper

@minha_funcao_decoradora
def minha_funcao():
    print("um print")

minha_funcao()        