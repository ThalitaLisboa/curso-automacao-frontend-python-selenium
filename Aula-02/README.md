---

# Aula 2

## Descrição
Nesta aula, você aprenderá como utilizar a biblioteca Selenium em Python para automatizar a navegação em um navegador web. Você criará scripts que abrem páginas da web, localizam elementos usando diferentes estratégias, e interagem com esses elementos.

## Arquivos
Esta aula contém os seguintes arquivos:
1. `first_script.py`
2. `locators.py`

## Detalhes dos Arquivos

### `first_script.py`
Este script faz o seguinte:
- Abre o navegador Google Chrome.
- Navega até o site "https://www.uol.com.br".
- Maximiza a janela do navegador.
- Espera 5 segundos.
- Captura e imprime o título da página.
- Fecha o navegador.

### `locators.py`
Este script demonstra como localizar elementos em páginas da web usando diferentes métodos de localização. Ele faz o seguinte:
- Abre o navegador Google Chrome.
- Navega até a página de login do site de e-commerce da LambdaTest.
- Maximiza a janela do navegador.
- Localiza elementos na página de login usando ID e nome.
- Navega até a página de formulário AJAX no site da LambdaTest.
- Maximiza a janela do navegador.
- Localiza um botão na página de formulário AJAX usando o nome da classe.
- Navega até a página principal do playground do Selenium da LambdaTest.
- Maximiza a janela do navegador.
- Localiza um link usando o texto do link, texto parcial do link e a tag do elemento.
- Imprime o título da página no console.
- Fecha o navegador.

## Como Rodar
Para rodar os scripts `first_script.py` e `locators.py`, siga as instruções abaixo:

### Pré-requisitos
- Certifique-se de ter o Python instalado. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
- Instale a biblioteca `selenium` usando o comando:
  ```sh
  pip install selenium
  ```
- Faça o download do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) que é compatível com a versão do seu Google Chrome. Coloque o executável do ChromeDriver em um diretório que esteja no seu PATH ou forneça o caminho diretamente no script.


#### Executando `first_script.py`
Execute o script com o seguinte comando:
   ```sh
   python first_script.py
   ```

#### Executando `locators.py`
Execute o script com o seguinte comando:
   ```sh
   python locators.py
   ```

### Observações
- Certifique-se de que o ChromeDriver está no seu PATH ou ajuste os scripts para apontar para o local correto do ChromeDriver.
- Estes scripts abrirão o navegador Chrome e executarão as ações descritas acima.
- O uso de `sleep()` é para fins de visualização e não é recomendado em scripts de produção.

---

