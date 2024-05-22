---

# Aula 7

## Descrição
Nesta aula, você aprenderá a usar diferentes tipos de esperas do Selenium (`implicitly_wait`, `WebDriverWait`) para sincronizar interações com a interface do usuário. Os testes incluirão carregamento de arquivos, envio de emails, interação com elementos condicionais e verificação de mudanças de URL.

## Arquivos
Esta aula contém os seguintes arquivos:
1. `test_wait.py`
2. `qrcode.png` (arquivo de imagem usado para upload)

## Detalhes do Arquivo

### `test_wait.py`
Este script inclui vários testes que utilizam diferentes técnicas de espera do Selenium para interagir com uma página web.
- Define uma fixture `driver` que inicializa o navegador Chrome, maximiza a janela, navega até a página de testes de espera e finaliza o navegador após os testes.
- Inclui cinco testes:
  - `atest_implicity_wait`: Utiliza `sleep` para esperar que um botão oculto se torne visível e então interage com ele.
  - `atest_file_upload`: Realiza o upload de um arquivo de imagem (`qrcode.png`) e verifica se a mensagem de sucesso é exibida.
  - `atest_email_sending`: Clica em um botão para enviar um email e verifica várias condições relacionadas ao envio do email.
  - `atest_conditional_element`: Interage com um elemento que só se torna visível após uma ação e verifica a mensagem exibida.
  - `test_url_change`: Clica em um botão que muda a URL da página e verifica se a URL foi alterada conforme esperado.

## Como Rodar
Para rodar os scripts desta aula, siga as instruções abaixo:

### Pré-requisitos
- Certifique-se de ter o Python instalado. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
- Instale as bibliotecas necessárias usando o comando:
  ```sh
  pip install selenium pytest
  ```
- Faça o download do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) que é compatível com a versão do seu Google Chrome. Coloque o executável do ChromeDriver em um diretório que esteja no seu PATH ou forneça o caminho diretamente no script.
- Certifique-se de que o arquivo `qrcode.png` está no mesmo diretório que o arquivo `test_wait.py`.

### Executando os Scripts
1. Clone o repositório ou baixe os arquivos da aula.
2. Navegue até o diretório onde os arquivos estão localizados.

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
