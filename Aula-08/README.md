---

# Aula 8

## Descrição
Nesta aula, você aprenderá a estruturar testes automatizados em Selenium usando um padrão de design de Page Object. Os testes são divididos em diferentes etapas de um formulário de inscrição e incluem esperas explícitas e manipulação de elementos da página.

## Arquivos
Esta aula contém os seguintes arquivos e pastas:

1. `test_mentoria.py`
2. `test_wait.py`
3. `qrcode.png` (usado para upload de arquivos no `test_wait.py`)
4. `pages` (pasta)
    - `base_page.py`
    - `etapa1_page.py`
    - `etapa2_page.py`
    - `etapa3_page.py`
    - `final_page.py`
5. `config` (pasta)
    - `webdriver_singleton.py`

## Detalhes dos Arquivos

### `test_mentoria.py`
Este script testa o fluxo completo de inscrição usando o padrão de Page Object para organizar os métodos de interação com a página.
- Define uma fixture `driver` que inicializa o navegador usando um singleton.
- Inclui dois testes `test_inscricao_completa_1` e `test_inscricao_completa_2`, que preenchem um formulário de inscrição em várias etapas e verificam a mensagem final de sucesso.

#### Testes Incluídos:
- `test_inscricao_completa_1`: Preenche o formulário com os dados de "Lebron".
- `test_inscricao_completa_2`: Preenche o formulário com os dados de "Stephen".

### `test_wait.py`
Este script testa diferentes funcionalidades de espera e interação com elementos dinâmicos da página.
- Define uma fixture `driver` que inicializa o navegador Chrome.
- Inclui seis testes que utilizam diferentes técnicas de espera do Selenium para interagir com uma página web.

#### Testes Incluídos:
- `test_implicity_wait`: Espera que um botão oculto se torne visível e interage com ele.
- `test_file_upload`: Faz o upload de um arquivo e verifica se a mensagem de sucesso é exibida.
- `test_email_sending`: Envia um email e verifica várias condições relacionadas ao envio do email.
- `test_conditional_element`: Interage com um elemento que só se torna visível após uma ação e verifica a mensagem exibida.
- `test_url_change`: Verifica mudanças na URL após uma interação.
- `test_terms_of_service`: Verifica a aceitação dos termos de serviço.

### `pages` (Pasta)
Contém as classes de Page Object que abstraem a interação com diferentes páginas do site.

#### Arquivos Incluídos:
- `base_page.py`: Classe base com métodos comuns para todas as páginas.
- `etapa1_page.py`: Classe para interações na primeira etapa do formulário.
- `etapa2_page.py`: Classe para interações na segunda etapa do formulário.
- `etapa3_page.py`: Classe para interações na terceira etapa do formulário.
- `final_page.py`: Classe para obter a mensagem final de inscrição.

### `config` (Pasta)
Contém o gerenciador de instâncias do WebDriver.

#### Arquivos Incluídos:
- `webdriver_singleton.py`: Classe Singleton para gerenciar a instância única do WebDriver.

## Como Rodar
Para rodar os scripts desta aula, siga as instruções abaixo:

### Pré-requisitos
- Certifique-se de ter o Python instalado. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
- Instale as bibliotecas necessárias usando o comando:
  ```sh
  pip install selenium pytest
  ```
- Faça o download do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) que é compatível com a versão do seu Google Chrome. Coloque o executável do ChromeDriver em um diretório que esteja no seu PATH ou forneça o caminho diretamente no script.
- Certifique-se de que o arquivo `qrcode.png` está no mesmo diretório que os arquivos `test_mentoria.py` e `test_wait.py`.

### Executando os Scripts
1. Clone o repositório ou baixe os arquivos da aula.
2. Navegue até o diretório onde os arquivos estão localizados.

#### Executando `test_mentoria.py`
Execute os testes com o seguinte comando:
   ```sh
   pytest test_mentoria.py
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
