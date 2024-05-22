---

# Aula 6

## Descrição
Nesta aula, você aprenderá a escrever e executar testes automatizados utilizando Selenium e `pytest` para diferentes cenários de validação, preenchimento de formulários e espera em páginas web. Você criará e executará diferentes testes para verificar a funcionalidade de diversos elementos em uma página web.

## Arquivos
Esta aula contém os seguintes arquivos:
1. `test_ja.py`
2. `test_validation.py`
3. `test_wait.py`

## Detalhes dos Arquivos

### `test_ja.py`
Este script testa o preenchimento de um formulário de aplicação de emprego.
- Define uma fixture `driver` que inicializa o navegador Chrome, navega até a página do formulário, maximiza a janela e finaliza o navegador após os testes.
- Inclui quatro testes:
  - `test_happy_path`: Preenche todos os campos do formulário corretamente e verifica a mensagem de sucesso.
  - `test_only_name`: Preenche apenas o campo do nome e verifica a mensagem de sucesso.
  - `test_without_filling`: Submete o formulário sem preencher nenhum campo e verifica a mensagem de sucesso.
  - `test_years_using_keys`: Usa as teclas de seta para incrementar e decrementar o número de anos de experiência.

### `test_validation.py`
Este script testa diferentes funcionalidades de validação na página.
- Define uma fixture `driver` que inicializa o navegador Chrome, navega até a página de validação, maximiza a janela e finaliza o navegador após os testes.
- Inclui nove testes:
  - `test_get_attribute`: Verifica o atributo `data-test` do elemento com ID `title`.
  - `test_is_displayed`: Verifica se a mensagem oculta é exibida após clicar no botão de toggle.
  - `test_is_enabled`: Verifica se o campo de entrada está habilitado.
  - `test_get_property`: Verifica o estado da propriedade `checked` de um checkbox antes e depois de clicar.
  - `test_is_selected`: Verifica se o checkbox está selecionado antes e depois de clicar.
  - `test_value_of_css_property`: Verifica o valor da propriedade CSS `color` de um botão.
  - `test_get_size`: Verifica o tamanho de um botão.
  - `test_get_location`: Verifica a localização de um botão na página.
  - `test_tag_name`: Verifica o nome da tag de um botão.

### `test_wait.py`
Este script testa o uso de esperas implícitas no Selenium.
- Define uma fixture `driver` que inicializa o navegador Chrome, define uma espera implícita de 10 segundos, navega até a página de espera, maximiza a janela e finaliza o navegador após os testes.
- Inclui um teste:
  - `test_implicity_wait`: Clica em um botão para revelar um botão oculto e então clica no botão oculto.

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

#### Executando `test_ja.py`
Execute os testes com o seguinte comando:
   ```sh
   pytest test_ja.py
   ```

#### Executando `test_validation.py`
Execute os testes com o seguinte comando:
   ```sh
   pytest test_validation.py
   ```

#### Executando `test_wait.py`
Execute os testes com o seguinte comando:
   ```sh
   pytest test_wait.py
   ```

### Observações
- Certifique-se de que o ChromeDriver está no seu PATH ou ajuste os scripts para apontar para o local correto do ChromeDriver.
- Estes scripts abrirão o navegador Chrome e executarão as ações descritas acima.
- O uso de `sleep()` é para fins de visualização e não é recomendado em scripts de produção. Considere usar esperas explícitas (`WebDriverWait`) para tornar os scripts mais robustos.

---
