# Importa a biblioteca 'requests'
import requests


def pesquisar_cep():
    # função q vai pesquisar o cep
    print('----PESQUISAR CEP----')

    # solicita ao usuario p digitar o cep e remove espaços em branco
    # o loop 'while True' garante q o programa so vai prosseguir com um cep válido
    while True:
        cep = input('digite o cep (somente numeros):').strip() # usado pra remover espaços em brancos

        # verifica se o cep tem 8 digitos, que é o formato padrão no brasil
        if len(cep) == 8 and cep.isdigit(): # isdigit é uma função q verifica se sao digitos de 0 a 9
            break
        else:
            print('cep inválido. tente denovo!')

    # url da api viacep usando o cep fornecido pelo usuario
    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        # faz a req get para a url da api
        # a resposta da requisição é armazenda na variavel 'response'
        response = requests.get(url)

        # o metodo 'raise_for_status()' verifica a req se foi bem sucedida
        # se ocorrer um erro por exemplo 404
        response.raise_for_status()

        # o metodo '.json()' converter a respostas JSON em um dicionario py dados = response.json()
        dados = response.json()

        # verifica se a chave 'erro' existe no dicionario
        # se existir significa q o cep nao foi achado
        if 'erro' in dados:
            print('\nCep nao encontrado.')
        else:
            # se nao der erro exibe os dados do endereço de forma formatada
            print('\n---Endereço encontrado---')
            print(f"cep: {dados.get('cep')}")
            print(f"logradouro: {dados.get('logradouro')}")
            print(f"bairro: {dados.get('bairro')}")
            print(f"cidade: {dados.get('localidade')}")  # CORRIGIDO: Chave 'localidade'
            print(f"ddd: {dados.get('ddd')}")
    except requests.exceptions.RequestException as e:
        # trata possíveis erros de conexão, como falta de internet.
        print(f"\nErro de conexão: {e}")
    except Exception as e:
        # captura de erros mais geral para qualquer outra exceção.
        print(f"\nOcorreu um erro inesperado: {e}")

# função para iniciar o programa.
if __name__ == "__main__":
    pesquisar_cep()