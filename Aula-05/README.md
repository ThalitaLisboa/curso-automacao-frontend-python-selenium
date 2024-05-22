---

# Aula 5

## Descrição
Nesta aula, você aprenderá a escrever e executar testes automatizados utilizando Selenium e `pytest` para interagir com a página de login e compra do site Saucedemo. Você criará e executará diferentes testes para verificar a funcionalidade do site.

## Arquivo
Esta aula contém o seguinte arquivo:
1. `test_sauce.py`

## Detalhes do Arquivo

### `test_sauce.py`
Este script demonstra o uso de `pytest` com Selenium para testar diferentes cenários no site Saucedemo.
- Define uma fixture `driver` que inicializa o navegador Chrome, navega até a página de login do Saucedemo, maximiza a janela e finaliza o navegador após os testes.
- Inclui três testes:
  - `test_mandatory_scenario`: Executa um fluxo completo de login, adiciona produtos ao carrinho, remove um produto, realiza o checkout e verifica a mensagem de confirmação.
  - `test_sorting`: Testa a funcionalidade de ordenação de produtos por preço, do menor para o maior, e verifica se a ordenação está correta.
  - `test_locked_user`: Testa o login com um usuário bloqueado e verifica a mensagem de erro correspondente.

## Como Rodar
Para rodar o script `test_sauce.py`, siga as instruções abaixo:

### Pré-requisitos
- Certifique-se de ter o Python instalado. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
- Instale as bibliotecas necessárias usando o comando:
  ```sh
  pip install selenium pytest
  ```
- Faça o download do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) que é compatível com a versão do seu Google Chrome. Coloque o executável do ChromeDriver em um diretório que esteja no seu PATH ou forneça o caminho diretamente no script.

### Executando o Script
1. Clone o repositório ou baixe o arquivo da aula.
2. Navegue até o diretório onde o arquivo `test_sauce.py` está localizado.
3. Execute o script com o seguinte comando:
   ```sh
   pytest test_sauce.py
   ```

### Observações
- Certifique-se de que o ChromeDriver está no seu PATH ou ajuste o script para apontar para o local correto do ChromeDriver.
- Este script abrirá o navegador Chrome e executará as ações descritas acima.
- O uso de `sleep()` é para fins de visualização e não é recomendado em scripts de produção. Considere usar esperas explícitas (`WebDriverWait`) para tornar o script mais robusto.

---
