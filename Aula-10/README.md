---

# Aula 10: Testes com CSV, Manipulação de Data e Hora, e Manipulação de Locale

## Sobre

Nesta aula, implementamos testes usando Selenium WebDriver para interagir com elementos de uma página web e realizar as seguintes tarefas:

- Preencher um formulário com dados provenientes de um arquivo CSV.
- Manipular datas e horas, preenchendo campos de formulário com diferentes formatos de data.
- Manipular configurações de locale, alterando a localização padrão e exibindo números formatados de acordo com a configuração.

## Conteúdo

### Arquivos de Teste

- **`test_csv.py`**: Teste para preenchimento de um formulário com dados lidos de um arquivo CSV (`users.csv`).
- **`test_datetime.py`**: Teste para manipulações de data e hora, preenchendo campos de formulário com diferentes formatos de data e hora.
- **`test_locale.py`**: Teste para manipulações das configurações de locale, alterando a localização padrão e exibindo números formatados de acordo com a configuração.
- **`users.csv`**: Contém dados de usuários utilizados nos testes do arquivo `test_csv.py`. Os dados estão no formato Nome, Sobrenome, Email.

## Pré-Requisitos

- **Python**: Certifique-se de ter o Python instalado no seu sistema. Você pode baixar a versão mais recente [aqui](https://www.python.org/downloads/).
- **Chrome WebDriver**: Certifique-se de ter o Chrome WebDriver instalado e configurado no seu PATH. Você pode baixá-lo [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads).

### Instalação das Dependências

Instale as dependências necessárias executando o seguinte comando:
```sh
pip install -r requirements.txt
```

---

## Guia Rápido

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
   pip install -r requirements.txt
   ```

### Executando os Testes

Para executar todos os testes, utilize o comando:
```sh
pytest
```

Para executar um teste específico, use:
```sh
pytest caminho/para/o/arquivo_de_teste.py
```

---

## Estrutura do Projeto

- **tests/**: Diretório contendo todos os arquivos de teste.
- **requirements.txt**: Arquivo com as dependências necessárias para executar os testes.
- **users.csv**: Arquivo CSV com dados de usuários para o teste `test_csv.py`.

---

## Recursos Adicionais

- **Documentação do Selenium WebDriver**: [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- **Python**: [Documentação Oficial](https://docs.python.org/3/)

---

