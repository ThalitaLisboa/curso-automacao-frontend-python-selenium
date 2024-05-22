---

# Aula 3

## Descrição
Nesta aula, você aprenderá a preencher automaticamente um formulário de aplicação de emprego utilizando a biblioteca Selenium em Python. Você criará um script que navega até uma página de formulário, preenche os campos necessários, e verifica a mensagem de sucesso após o envio.

## Arquivos
Esta aula contém o seguinte arquivo:
1. `job_application.py`

## Detalhes do Arquivo

### `job_application.py`
Este script faz o seguinte:
- Abre o navegador Google Chrome.
- Navega até a página de aplicação de emprego.
- Maximiza a janela do navegador.
- Preenche os campos do formulário com informações de teste:
  - Nome completo.
  - Email.
  - Número de telefone.
  - Posição desejada.
  - Localização preferida (remoto).
  - Anos de experiência.
  - Habilidades selecionadas.
- Envia o formulário.
- Verifica se a mensagem de sucesso "Submission successful!" é exibida.
- Fecha o navegador.

## Como Rodar
Para rodar o script `job_application.py`, siga as instruções abaixo:

### Pré-requisitos
- Certifique-se de ter o Python instalado. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
- Instale a biblioteca `selenium` usando o comando:
  ```sh
  pip install selenium
  ```
- Faça o download do [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) que é compatível com a versão do seu Google Chrome. Coloque o executável do ChromeDriver em um diretório que esteja no seu PATH ou forneça o caminho diretamente no script.

### Executando o Script
1. Clone o repositório ou baixe os arquivos da aula.
2. Navegue até o diretório onde o arquivo `job_application.py` está localizado.
3. Execute o script com o seguinte comando:
   ```sh
   python job_application.py
   ```

### Observações
- Certifique-se de que o ChromeDriver está no seu PATH ou ajuste o script para apontar para o local correto do ChromeDriver.
- Este script abrirá o navegador Chrome e executará as ações descritas acima.
- O uso de `sleep()` é para fins de visualização e não é recomendado em scripts de produção. 
---
