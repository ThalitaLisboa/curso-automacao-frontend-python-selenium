---

# Aula 10: Testes com CSV, Manipulação de Data e Hora, e Manipulação de Locale

## Sobre

Nesta aula, implementamos testes usando Selenium WebDriver para interagir com elementos de uma página web e realizar as seguintes tarefas:

- Preencher um formulário com dados provenientes de um arquivo CSV.
- Manipular datas e horas, preenchendo campos de formulário com diferentes formatos de data.
- Manipular configurações de locale, alterando a localização padrão e exibindo números formatados de acordo com a configuração.

## Arquivos

- `test_csv.py`: Testa o preenchimento de um formulário com dados lidos de um arquivo CSV (`users.csv`).
- `test_datetime.py`: Testa manipulações de data e hora, preenchendo campos de formulário com diferentes formatos de data e hora.
- `test_locale.py`: Testa manipulações das configurações de locale, alterando a localização padrão e exibindo números formatados de acordo com a configuração.
- `users.csv`: Contém dados de usuários utilizados nos testes do arquivo `test_csv.py`. Os dados estão no formato Nome, Sobrenome, Email.

## Como Rodar

1. Certifique-se de ter o Python e o pip instalados em seu ambiente.
2. Instale as dependências necessárias usando o comando:
    ```
    pip install -r requirements.txt
    ```
3. Certifique-se de ter o Chrome WebDriver instalado e no seu PATH.
4. Para executar os testes, navegue até o diretório da Aula 10 e execute o comando:
    ```
    pytest
    ```
---
