#  Pesquisador de CEP em Python

Este é um projeto simples e prático desenvolvido em Python para pesquisar informações de endereço a partir de um número de CEP. A aplicação utiliza a API pública e gratuita **ViaCEP** para buscar os dados em tempo real.

---

##  Tecnologias Utilizadas

* **Python 3:** A linguagem de programação principal.
* **Requests:** Uma biblioteca HTTP para Python que facilita o envio de requisições web.

---

##  Funcionalidades

* **Validação do CEP:** O programa verifica se o CEP tem 8 dígitos e se é composto apenas por números.
* **Busca de dados:** Faz uma requisição à API do ViaCEP para obter informações do endereço.
* **Tratamento de erros:** Lida com CEPs não encontrados e possíveis falhas na conexão com a internet.
* **Interface de linha de comando:** Exibe os resultados de forma clara e formatada no terminal.

---

##  Como Usar

### Pré-requisitos

Certifique-se de ter o **Python 3** instalado em sua máquina.

### 1. Clonar o Repositório

Se você estiver usando Git, pode clonar o projeto com o seguinte comando:

```bash
git clone [https://github.com/seu-usuario/pesquisador-cep-python.git](https://github.com/seu-usuario/pesquisador-cep-python.git)
cd pesquisador-cep-python

2. Instalar a Biblioteca requests
O projeto depende da biblioteca requests. Instale-a usando o pip:

Bash

pip install requests
3. Executar o Programa
Execute o script diretamente do terminal:

Bash

python pesquisador_cep.py
O programa irá pedir que você digite um CEP para iniciar a pesquisa.
