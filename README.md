# portal-noticias-api
A solução foi desenvolvida com Python e com os pacotes **Flask, SQLAlchemy e Marshmallow**.
Todas requisições e respostas são representadas em documentos **JSON**.

## Configuração
### Instalando Dependências
Use o gerenciado de pacote [pip](https://pip.pypa.io/en/stable/) para instalar as dependências.

```bash
pip install -r requirements.txt
```

### Configurando o Banco de Dados
O banco de dados utilizado é o **SQLite (relacional)** e o mesmo pode ser criado e configurado com os seguintes comandos:

```bash
flask db init
flask db migrate
flask db upgrade
```

## Inicializando
Para executar o projeto basta executar o seguinte comando:

```bash
flask run
```
ou
```bash
python app.py
```

## End Points
Essa seção apresenta todos endpoints disponíveis.

### ./authors/
Endpoint `{base_url}/authors/` para manipulação de autores.

- `[POST] ./authors/`:  Persiste novo autor.
- `[GET] ./authors/`: Lista todos autores cadastrados.
- `[GET] ./authors/<int:author_id>/`: Retorna autor específico.
- `[PUT] ./authors/<int:author_id>/`: Atualiza autor específico.
- `[DELETE] ./authors/<int:author_id>/`: Deleta autor específico.

O objeto **Author** é representado da seguinte forma para manipulação.

```json
{
    "id": 1,
    "name": "Foo",
    "description": "Bar"
}
```

### ./news/
Endpoint `{base_url}/news/` para manipulação de notícias.

- `[POST] ./news/`:  Persiste nova notícia.
- `[GET] ./news/`: Lista todas notícias cadastradas.
- `[GET] ./news/?filter={valor}`: Lista todas notícias cadastradas que contenham correspondência do parâmetro `filter`. É filtrado título, conteúdo e nome do autor.
- `[GET] ./news/<int:news_id>/`: Retorna notícia específica.
- `[GET] ./news/<int:news_id>/preview`: Renderiza a noticia em um template HTML.
- `[PUT] ./news/<int:news_id>/`: Atualiza notícia específica.
- `[DELETE] ./news/<int:news_id>/`: Deleta notícia específica.

O objeto **News** é representado da seguinte forma para manipulação.

```json
{
	"id": 1,
	"title": "Lorem Ipsum",
	"content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In quam leo, lacinia non sodales ut, porttitor sed sapien. Maecenas sit amet ex imperdiet eros pulvinar hendrerit. Nunc at urna rutrum, sodales eros at, sagittis risus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Ut sed laoreet libero. Vestibulum vitae ultricies turpis, ut malesuada lorem. Fusce mattis vel mauris sed elementum. Nulla porttitor posuere tortor, a euismod felis varius non. Cras a dignissim erat. Mauris dignissim neque ut imperdiet maximus. Maecenas mollis tortor nec ipsum consectetur scelerisque. Maecenas sed felis vitae lectus mattis blandit. In ac hendrerit enim, non sagittis augue. Donec id efficitur sem. Quisque tincidunt tortor eu massa lobortis eleifend.",
    	"author": {
        	"id": 1,
		"name": "Luciana Potter",
		"description": "foo bar"
	}
}
```
