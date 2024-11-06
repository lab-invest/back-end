InvestLab API

InvestLab é uma API desenvolvida com FastAPI para fornecer cotações de ações e dados históricos, consultando a API do Yahoo Finance. Este serviço é ideal para obter dados de mercado em tempo real e históricos para análises financeiras e estudos de investimentos.
Índice

    Instalação
    Configuração
    Uso
    Endpoints
    Exemplo de Requisição
    Licença

Instalação

    Clone este repositório:

git clone https://github.com/usuario/investlab-api.git

Navegue até o diretório do projeto:

cd investlab-api

Instale as dependências:

    pip install -r requirements.txt

Configuração

    Configure a variável de ambiente PORT, se necessário, para definir a porta em que a API será executada. A porta padrão é 8000.
    CORS: A API permite origens locais padrão, como localhost:8000. Para ajustar essas configurações, edite a lista origins no código da API.

Uso

Execute a API usando o seguinte comando:

python -m uvicorn main:app --reload

A API estará acessível em: http://localhost:8000.
Rotas de Exemplo

Abaixo estão os endpoints principais oferecidos pela InvestLab API:

    GET /stock?ticker={ticker}: Retorna a cotação atual do ativo.
    GET /wallet/rentability/: Retorna a rentabilidade de uma carteira

Substitua {ticker} pelo símbolo do ativo (ex.: VALE3.SA, TAEE3.SA).
Endpoints
GET /stock?ticker={ticker}

Retorna a cotação atual do ativo.

    Parâmetro: ticker - símbolo do ativo (ex.: PETR4.SA para Petrobrás).
    Resposta: Retorna a cotação atual

Exemplo de Resposta

{
 62.119998931884766
}


Exemplo de Requisição

Para consultar a cotação de uma ação, faça uma requisição GET para:

curl -X 'GET' 'http://127.0.0.1:8000/stock/?ticker=VALE3.SA

SWAGGER

Para visualizar o swagger coloque um /docs no final da url da api

Ex: http://127.0.0.1:8000/docs