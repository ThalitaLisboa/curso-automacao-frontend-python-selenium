---

# Aula 4

## Descrição
Nesta aula, você aprenderá como escrever e executar testes automatizados usando as bibliotecas `pytest` e `unittest` em Python, além de integrar testes com Selenium para automação de navegador. Você criará e executará diferentes tipos de testes para garantir a funcionalidade do código.

## Arquivos
Esta aula contém os seguintes arquivos:
1. `sample_pytest.py`
2. `sample_unittest.py`
3. `test_fs.py`
4. `test_ja.py`

## Detalhes dos Arquivos

### `sample_pytest.py`
Este script demonstra o uso básico da biblioteca `pytest` com fixtures.
- Define fixtures para execução antes e depois de todos os testes (`before_all`) e antes e depois de cada teste (`before_each`).
- Inclui dois testes simples:
  - `test_sum`: Verifica se 1+1 é igual a 2.
  - `test_sub`: Verifica se 2-1 é igual a 1.

### `sample_unittest.py`
Este script demonstra o uso da biblioteca `unittest` para criar testes unitários.
- Define uma classe de teste `TestCalculator` que inclui:
  - `setUpClass`: Método executado uma vez antes de todos os testes.
  - `test_sum`: Verifica se 1+1 é igual a 2.
  - `test_sub`: Verifica se 2-1 é igual a 1.
  - `tearDownClass`: Método executado uma vez após todos os testes.

### `test_fs.py`
Este script demonstra o uso de `pytest` com Selenium para testar uma página web.
- Define uma fixture `driver` que inicializa o navegador Chrome, navega até a página do UOL, maximiza a janela e finaliza o navegador após o teste.
- Inclui um teste:
  - `test_get_title`: Verifica se o título da página é "UOL - Seu universo online".

### `test_ja.py`
Este script demonstra o uso de `pytest` com Selenium para testar um formulário de aplicação de emprego.
- Define uma fixture `driver` que inicializa o navegador Chrome, navega até a página do formulário, maximiza a janela e finaliza o navegador após o teste.
- Inclui três testes:
  - `test_happy_path`: Preenche todos os campos do formulário corretamente e verifica a mensagem de sucesso.
  - `test_only_name`: Preenche apenas o campo do nome e verifica a mensagem de sucesso.
  - `test_without_filling`: Submete o formulário sem preencher nenhum campo e verifica a mensagem de sucesso.

## Como Rodar
Para rodar os scripts desta aula, siga as instruções abaixo:

### Pré-requisitos
- Certifique-se de ter o Python instalado. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
- Instale as bibliotecas necessárias usando o comando:
  ```sh
  pip install selenium pytest
  ```
- Faça o download do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) que é compatível com a versão do seu Google Chrome. Coloque o executável do ChromeDriver em um diretório que esteja no seu PATH ou forneça o caminho diretamente no script.

### Executando os Scripts
1. Clone o repositório ou baixe os arquivos da aula.
2. Navegue até o diretório onde os arquivos estão localizados.

#### Executando `sample_pytest.py`
Execute os testes com o seguinte comando:
   ```sh
   pytest sample_pytest.py
   ```

#### Executando `sample_unittest.py`
Execute os testes com o seguinte comando:
   ```sh
   python -m unittest sample_unittest.py
   ```

#### Executando `test_fs.py`
Execute os testes com o seguinte comando:
   ```sh
   pytest test_fs.py
   ```

#### Executando `test_ja.py`
Execute os testes com o seguinte comando:
   ```sh
   pytest test_ja.py
   ```

### Observações
- Certifique-se de que o ChromeDriver está no seu PATH ou ajuste os scripts para apontar para o local correto do ChromeDriver.
- Estes scripts abrirão o navegador Chrome e executarão as ações descritas acima.
- O uso de `sleep()` é para fins de visualização e não é recomendado em scripts de produção. 

---
