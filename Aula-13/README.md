

---

# Aula 13: Testes Automatizados com Selenium - Diversos Cenários e Configurações

## Sobre

Nesta aula, exploramos diversas abordagens e técnicas para a criação de testes automatizados com o Selenium WebDriver, incluindo testes em diferentes navegadores, manipulação de dados de teste a partir de arquivos JSON, escopos de fixtures, manipulação de janelas do navegador e testes parametrizados com URLs diferentes.

## Conteúdo

### Arquivos de Teste

- **`teste_browsers.py`**: Realiza testes em múltiplos navegadores (Chrome, Firefox).
- **`test_data.py`**: Carrega dados de teste a partir de um arquivo JSON e preenche um formulário na web.
- **`test_scope.py`**: Demonstra o uso de diferentes escopos de fixtures (sessão, módulo, classe, função).
- **`test_urls.py`**: Executa testes em múltiplos URLs fornecidos como parâmetros.
- **`test_window.py`**: Manipula janelas e abas do navegador, realiza operações de captura de tela e ajustes de tamanho/posição da janela.

### Arquivos de Dados

- **`users.json`**: Contém dados de usuários utilizados nos testes do arquivo `test_data.py`.

## Estrutura do Projeto

```
.
├── teste_browsers.py
├── test_data.py
├── test_scope.py
├── test_urls.py
├── test_window.py
├── users.json
└── README.md
```

## Pré-Requisitos

- **Python**: Certifique-se de ter o Python instalado no seu sistema. [Download Python](https://www.python.org/downloads/)
- **Chrome WebDriver**: Certifique-se de ter o Chrome WebDriver instalado e configurado no seu PATH. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- **Firefox WebDriver**: Certifique-se de ter o Firefox WebDriver (geckodriver) instalado e configurado no seu PATH. [Download geckodriver](https://github.com/mozilla/geckodriver/releases)

### Instalação das Dependências

Para instalar as dependências necessárias, execute:
```sh
pip install selenium pytest
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
   pip install selenium pytest
   ```

### Executando os Testes

#### `teste_browsers.py`

Para executar os testes em múltiplos navegadores, utilize:
```sh
pytest teste_browsers.py
```

#### `test_data.py`

Para executar os testes que carregam dados de um arquivo JSON e preenchem um formulário, utilize:
```sh
pytest test_data.py
```

#### `test_scope.py`

Para executar os testes que demonstram o uso de diferentes escopos de fixtures, utilize:
```sh
pytest test_scope.py
```

#### `test_urls.py`

Para executar os testes que navegam para múltiplos URLs, utilize:
```sh
pytest test_urls.py
```

#### `test_window.py`

Para executar os testes que manipulam janelas e abas do navegador, capturam telas e ajustam tamanho/posição da janela, utilize:
```sh
pytest test_window.py
```

## Descrição dos Arquivos

- **`teste_browsers.py`**:
  - **Descrição**: Realiza testes de abertura de páginas em múltiplos navegadores (Chrome, Firefox).
  - **Funções**: Abre o Google e UOL, verifica o título da página.

- **`test_data.py`**:
  - **Descrição**: Carrega dados de teste de um arquivo JSON e preenche um formulário web.
  - **Funções**: Carrega dados de `users.json`, preenche um formulário com esses dados e verifica a submissão bem-sucedida.

- **`test_scope.py`**:
  - **Descrição**: Demonstra o uso de diferentes escopos de fixtures para configuração do ambiente de teste.
  - **Funções**: Define fixtures com escopos de sessão, módulo, classe e função, e executa testes utilizando essas fixtures.

- **`test_urls.py`**:
  - **Descrição**: Executa testes em múltiplos URLs fornecidos como parâmetros.
  - **Funções**: Abre URLs fornecidos como parâmetros e verifica o título da página.

- **`test_window.py`**:
  - **Descrição**: Manipula janelas e abas do navegador, realiza operações de captura de tela e ajustes de tamanho/posição da janela.
  - **Funções**: Abre e fecha novas abas, ajusta o tamanho e posição da janela, captura telas e verifica a existência dos arquivos de screenshot.

---