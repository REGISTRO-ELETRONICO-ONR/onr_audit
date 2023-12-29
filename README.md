# ONR AUDIT
_Aplicativo Backend contruído em Flask para gerar dados necessários para auditoria dos cartórios_

## 📋 Pré-requisitos
- Python 3.11
- pip (gerenciador de pacotes Python)

## 🛠️ Passo a Passo

### 1️⃣ Configuração do Ambiente Virtual
É recomendável usar um ambiente virtual para isolar as dependências do projeto. No terminal, navegue até o diretório do projeto e execute:

`python3 -m venv venv`

`source venv/bin/activate  # No Windows use 'venv\Scripts\activate'`

### 2️⃣ Instalação das Dependências
Instale as dependências necessárias usando o arquivo `requirements.txt`:

`pip install -r requirements.txt`

### 3️⃣ Configuração Inicial
A configuração inicial do Flask é feita através do arquivo `create_app.py`, que inicializa o aplicativo com a configuração apropriada.

### 4️⃣ Execução da Aplicação
Execute o arquivo principal para iniciar o servidor Flask:

`python main.py`


Isso iniciará o servidor Flask na porta 5000 e estará acessível em `http://0.0.0.0:5000`.

### 5️⃣ Configuração do Namespace `/credential`
Antes de usar as rotas em `/request-details`, é necessário configurar a aplicação no namespace `/credential`:

`curl -X POST http://0.0.0.0:5000/credential/register -d '{"credential": "sua_credencial"}'`


Aguarde a resposta com o status 200, indicando sucesso.

### 6️⃣ Usando as Rotas Principais
Após a configuração bem-sucedida no `/credential/register`, você pode começar a usar as rotas principais em `/request-details`.

## 📖 Documentação Swagger Completa
A documentação Swagger da aplicação está completa e disponível. Ela é uma ótima ferramenta para entender e testar as rotas da API.

A documentação se encontra na URL raíz do projeto, no caso em: `http://0.0.0.0:5000`

## 📝 Notas Adicionais
- Verifique se o Python 3.11 está corretamente instalado e configurado no seu PATH.
- O uso do `venv` é opcional, mas altamente recomendado.
- O arquivo `requirements.txt` deve conter todas as bibliotecas necessárias para a aplicação.

---

