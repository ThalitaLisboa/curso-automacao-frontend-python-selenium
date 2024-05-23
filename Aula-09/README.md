
---

# Aula 9: Testes Automatizados com Selenium e PageFactory

## Sobre

Nesta aula, você aprenderá a implementar testes automatizados utilizando o Selenium WebDriver e o padrão PageFactory. Os testes interagem com uma página web, preenchendo formulários de inscrição em múltiplas etapas e validando mensagens de sucesso.

## Conteúdo

### Arquivos de Teste

- **`test_mentoria.py`**: Contém testes que preenchem um formulário de inscrição em múltiplas etapas e validam a mensagem final de sucesso.

### Configuração do WebDriver

- **`webdriver_singleton.py`**: Implementa o padrão Singleton para a instância do WebDriver, garantindo que apenas uma instância do WebDriver seja criada e reutilizada durante os testes.

### Páginas

- **`base_page.py`**: 
  - **Descrição**: Define a classe base para todas as páginas, incluindo métodos comuns como navegar para a URL base e esperar por elementos.
  - **Funções**: Navegar para a URL principal do site e fornecer métodos para esperar que elementos específicos estejam visíveis na página.

- **`etapa1_page.py`**:
  - **Descrição**: Define a página da primeira etapa do formulário.
  - **Funções**: Preencher os campos "nome", "email", "idade", "whatsapp", "cidade" e clicar no botão "Prosseguir".

- **`etapa2_page.py`**:
  - **Descrição**: Define a página da segunda etapa do formulário.
  - **Funções**: Preencher os campos "trabalha na área", "experiência", "empresa" e clicar no botão "Prosseguir".

- **`etapa3_page.py`**:
  - **Descrição**: Define a página da terceira etapa do formulário.
  - **Funções**: Preencher os campos "interesse na mentoria" e "descrição" e clicar no botão "Enviar Inscrição".

- **`final_page.py`**:
  - **Descrição**: Define a página final após o envio do formulário.
  - **Funções**: Obter a mensagem de confirmação de inscrição.

## Estrutura do Projeto

```
.
├── config/
│   └── webdriver_singleton.py
├── pages/
│   ├── base_page.py
│   ├── etapa1_page.py
│   ├── etapa2_page.py
│   ├── etapa3_page.py
│   └── final_page.py
├── tests/
│   └── test_mentoria.py
├── requirements.txt
└── README.md
```

## Pré-Requisitos

- **Python**: Certifique-se de ter o Python instalado no seu sistema. [Download Python](https://www.python.org/downloads/)
- **Chrome WebDriver**: Certifique-se de ter o Chrome WebDriver instalado e configurado no seu PATH. [Download ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads)

### Instalação das Dependências

Para instalar as dependências necessárias, execute:
```sh
pip install -r requirements.txt
```

## Guia de Configuração

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

Para executar um teste específico, utilize:
```sh
pytest tests/test_mentoria.py
```

## Recursos Adicionais

- **Documentação do Selenium WebDriver**: [Selenium Documentation](https://www.selenium.dev/documentation/en/)
- **Documentação do Python**: [Python Documentation](https://docs.python.org/3/)



---
