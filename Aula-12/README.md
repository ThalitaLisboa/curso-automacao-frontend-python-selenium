---
# Aula 12 - Testes de Interação Avançada com Elementos Web

## Descrição
Nesta aula, você aprenderá a escrever testes automatizados utilizando o Selenium WebDriver para interagir com elementos web avançados, como sliders, switches, dropdowns dinâmicos, modais e iframes.

## Conteúdo

### Arquivos de Teste

- **`test_slider_interaction.py`**: Teste para interagir com um controle deslizante (slider) e verificar se o valor foi ajustado corretamente.
- **`test_switch_interaction.py`**: Teste para alternar um switch e verificar se o estado mudou adequadamente.
- **`test_dynamic_dropdown_interaction.py`**: Teste para selecionar opções em um dropdown dinâmico e verificar se as seleções foram aplicadas corretamente.
- **`test_modal_interaction.py`**: Teste para interagir com um modal, preenchendo campos e verificando mensagens de sucesso.
- **`test_iframe_interaction.py`**: Teste para interagir com elementos dentro de um iframe, realizando ações e verificando mensagens.

## Pré-Requisitos

- **Python**: Certifique-se de ter o Python instalado no seu sistema. Você pode baixar a versão mais recente [aqui](https://www.python.org/downloads/).
- **Dependências**: Instale as dependências necessárias executando o seguinte comando:
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

---

## Recursos Adicionais

- **Documentação do Selenium WebDriver**: [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- **Python**: [Documentação Oficial](https://docs.python.org/3/)

---
