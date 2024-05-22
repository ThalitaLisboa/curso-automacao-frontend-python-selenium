```markdown
# Aula 12 - Testes de Interação Avançada com Elementos Web

## Descrição
Nesta aula, você aprenderá a escrever testes automatizados utilizando o Selenium WebDriver para interagir com elementos web avançados, como sliders, switches, dropdowns dinâmicos, modais e iframes.

## Arquivos

- `test_slider_interaction.py`: Contém um teste para interagir com um controle deslizante (slider) e verificar se o valor foi ajustado corretamente.
- `test_switch_interaction.py`: Implementa um teste para alternar um switch e verificar se o estado mudou adequadamente.
- `test_dynamic_dropdown_interaction.py`: Este arquivo contém um teste para selecionar opções em um dropdown dinâmico e verificar se as seleções foram aplicadas corretamente.
- `test_modal_interaction.py`: Contém um teste para interagir com um modal, preenchendo campos e verificando mensagens de sucesso.
- `test_iframe_interaction.py`: Implementa um teste para interagir com elementos dentro de um iframe, realizando ações e verificando mensagens.

## Pré-Requisitos
- Python instalado no sistema. Você pode baixar o Python [aqui](https://www.python.org/downloads/).
- Instalação das dependências necessárias usando o comando:
  ```sh
  pip install -r requirements.txt
  ```
- Certifique-se de que o Chrome WebDriver está instalado e configurado corretamente. Você pode baixar o Chrome WebDriver [aqui](https://sites.google.com/a/chromium.org/chromedriver/downloads). Certifique-se de adicionar o executável do Chrome WebDriver ao seu PATH.

## Como Rodar

1. Clone ou baixe os arquivos desta aula.
2. Navegue até o diretório da Aula 12 no terminal.
3. Execute os testes utilizando o comando:
   ```sh
   pytest
   ```

Certifique-se de ter os requisitos necessários instalados e o WebDriver configurado corretamente antes de executar os testes.

### Observações

- Verifique se o Chrome WebDriver está no seu PATH ou ajuste o caminho diretamente nos arquivos de teste, se necessário.
- Os scripts abrirão o navegador Chrome e executarão as ações descritas em cada teste.
- O uso de `sleep()` é para fins de visualização e não é recomendado em scripts de produção. Considere usar esperas explícitas (`WebDriverWait`) para tornar os scripts mais robustos.
```

