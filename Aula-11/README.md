
---

# Aula 11: Testes Automatizados com Selenium e Configurações Avançadas

## Sobre

Nesta aula, você aprenderá a implementar testes automatizados utilizando o Selenium WebDriver com diferentes abordagens para configuração e execução de testes. Exploraremos o uso de argparse para configurações via linha de comando, ConfigParser para arquivos de configuração, e técnicas de manipulação aleatória de elementos na página.

## Conteúdo

### Arquivos de Teste

- **`argparse.py`**: Utiliza argparse para permitir a configuração de testes via linha de comando, permitindo especificar o URL e o navegador.
- **`test_configparser.py`**: Utiliza ConfigParser para ler as configurações de um arquivo INI, permitindo a configuração do navegador e URL para os testes.
- **`test_random.py`**: Implementa diferentes métodos para clicar em botões de forma aleatória em uma página, utilizando várias funções do módulo random.
- **`test_re.py`**: Realiza interações baseadas em expressões regulares para extrair e utilizar dados de um texto estruturado.

## Estrutura do Projeto

```
.
├── config.ini
├── argparse.py
├── test_configparser.py
├── test_random.py
├── test_re.py
└── README.md
```

## Pré-Requisitos

- **Python**: Certifique-se de ter o Python instalado no seu sistema. [Download Python](https://www.python.org/downloads/)
- **Chrome WebDriver**: Certifique-se de ter o Chrome WebDriver instalado e configurado no seu PATH. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- **Firefox WebDriver**: Certifique-se de ter o Firefox WebDriver (geckodriver) instalado e configurado no seu PATH. [Download geckodriver](https://github.com/mozilla/geckodriver/releases)

### Instalação das Dependências

Para instalar as dependências necessárias, execute:
```sh
pip install selenium
```

## Guia de Configuração

### Configuração do Ambiente

1. **Clone o Repositório**:
   ```sh
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um Ambiente Virtual**:
   ```sh
   python -m venv venv
   source venv/bin/activate # No Windows: venv\Scripts\activate
   ```

3. **Instale as Dependências**:
   ```sh
   pip install selenium
   ```

### Executando os Testes

#### `argparse.py`

Para executar o script `argparse.py` utilizando a linha de comando para especificar o URL e o navegador, utilize:
```sh
python argparse.py --url "https://www.example.com" --browser "chrome"
```

#### `test_configparser.py`

Para executar o teste que utiliza o arquivo de configuração `config.ini`, utilize:
```sh
pytest test_configparser.py
```

#### `test_random.py`

Para executar os testes que realizam cliques aleatórios em botões, utilize:
```sh
pytest test_random.py
```

#### `test_re.py`

Para executar o teste que utiliza expressões regulares para interagir com elementos da página, utilize:
```sh
pytest test_re.py
```

## Descrição das Páginas

- **`argparse.py`**:
  - **Descrição**: Este script utiliza o argparse para permitir a configuração de testes via linha de comando. O usuário pode especificar o URL e o navegador a ser utilizado.
  - **Funções**: Navegar para o URL especificado e imprimir o título da página.

- **`test_configparser.py`**:
  - **Descrição**: Este teste utiliza o ConfigParser para ler configurações de um arquivo INI, permitindo a configuração do navegador e URL para os testes.
  - **Funções**: Navegar para o URL especificado no arquivo INI e imprimir o título da página.

- **`test_random.py`**:
  - **Descrição**: Este teste implementa diferentes métodos para clicar em botões de forma aleatória em uma página. Utiliza várias funções do módulo random.
  - **Funções**: Clicar em botões aleatórios utilizando métodos como random.choice(), random.randint(), random.shuffle(), entre outros.

- **`test_re.py`**:
  - **Descrição**: Este teste realiza interações baseadas em expressões regulares para extrair e utilizar dados de um texto estruturado.
  - **Funções**: Extrair códigos de transação e números de telefone de um texto e utilizá-los para interagir com a página.

## Recursos Adicionais

- **Documentação do Selenium WebDriver**: [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- **Documentação do Python**: [Python Documentation](https://docs.python.org/3/)
- **Documentação do argparse**: [argparse Documentation](https://docs.python.org/3/library/argparse.html)
- **Documentação do ConfigParser**: [ConfigParser Documentation](https://docs.python.org/3/library/configparser.html)
- **Documentação do módulo random**: [random Documentation](https://docs.python.org/3/library/random.html)
- **Documentação do módulo re**: [re Documentation](https://docs.python.org/3/library/re.html)


---
