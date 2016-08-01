# Docker SPA

[![Build Status](https://travis-ci.org/carlosmaniero/docker-spa.svg?branch=master)](https://travis-ci.org/carlosmaniero/docker-spa)
[![Coverage Status](https://coveralls.io/repos/github/carlosmaniero/docker-spa/badge.svg?branch=master)](https://coveralls.io/github/carlosmaniero/docker-spa?branch=master)


Exemplo simples de utilização de docker com SPA (Single Page Application).

## Rodando

Dentro da pasta do projeto execute o build que irá baixar as imagens e as depedências do projeto:

    $ docker-compose build

Para popular o banco de dados execute:

    $ docker-compose run rest_app python3 manage.py loaddata initial_data

**PS**: Me desculpe, mas eu não manjo nada de carro.

Para iniciar a aplicação:

    $ docker-compose up


### Escalando a aplicação

Com os containers em execução `docker-compose up`, execute o seguinte comando para escalar dois containers à aplicação `rest_app`:

    $ docker-compose scale rest_app=2

Sim! Sim! Sim! Podemos escalar a aplicação! O HAPROXY detecta automaticamente a
quantidade de máquinas de aplicação e coloca no balanceador <3

## E agora? Como eu faço pra ver isso no navegador?

Só acessar seu [http://localhost/](http://localhost/).

![Magic](http://www.reactiongifs.com/r/mgc.gif)


# Testes

É bem simples clique no ícone do coveralls acima! Se quiser rodar na unha, segue os passos:

Para executar os testes utilize o seguinte comando:

    docker-compose run rest_app coverage run --source='.' manage.py test

Relatório:

    docker-compose run rest_app coverage report     # Terminal
    docker-compose run rest_app coverage html       # Em HTML

O relatório em html é gerado em `rest_app/htmlcov`.


# API Rest

## Montadora

### Criando
```sh
curl -XPOST -H "Content-type: application/json" -d '{"name": "Volkswagen"}' 'http://localhost/api/manufacturers/'
```

Retorno: 201

```json
{"id":3,"name":"Volkswagen"}
```

### Editando
```sh
curl -XPUT -H "Content-type: application/json" -d '{"name": "VW"}' 'http://localhost/api/manufacturers/3/'
```

Retorno: 200

```json
{"id":3,"name":"VW"}
```


### Obter
```sh
curl http://localhost/api/manufacturers/3/
```

Retorno: 200

```json
{"id":3,"name":"VW"}
```

### Listando
```sh
curl http://localhost/api/manufacturers/
```

Retorno: 201

```json
[
    {"id":1,"name":"GM"},
    {"id":2,"name":"Fiat"},
    {"id":3,"name":"VW"}
]
```

### Removendo
```sh
curl -XDELETE 'http://localhost/api/manufacturer/3/'
```

Retorno: 204


## Veículos

### Campos:
Campo           | Descrição
--------------- | -------------
manufacturer    | id da montadora
model_name      | Modelo do veículo
color           | Cor do veículo (azul, preto, prata, vermelho, verde, outro)
category        | Categoria do veículo (carro, moto)
engine          | Motor do veículo
kms             | Kilometragem

### Criando
```sh
curl -XPOST -H "Content-type: application/json" -d '{"manufacturer":4,"model_name":"Fusca","color":"azul","category":"carro","kms":0,"engine":"1000"}' 'http://localhost/api/vehicles/'
```

Retorno: 201

```json
{
  "id":4,
  "manufacturer":4,
  "model_name":"Fusca",
  "color":"azul",
  "category":"carro",
  "kms":0,
  "engine":"1000"
}
```

### Atualizando
```sh
curl -XPUT -H "Content-type: application/json" -d '{"manufacturer":4,"model_name":"Brasilia","color":"azul","category":"carro","kms":0,"engine":"1000"}' 'http://localhost/api/vehicles/4/'
```

Retorno: 200

```json
{
  "id":4,
  "manufacturer":4,
  "model_name":"Brasilia",
  "color":"azul",
  "category":"carro",
  "kms":0,
  "engine":"1000"
}
```

### Obter
```sh
curl http://localhost/api/vehicles/4/
```

Retorno: 200

```json
{
  "id":4,
  "manufacturer":4,
  "model_name":"Brasilia",
  "color":"azul",
  "category":"carro",
  "kms":0,
  "engine":"1000"
}
```

### Listando
```sh
curl http://localhost/api/vehicles/
```

Retorno: 200

```json
[
    {
      "id":3,
      "manufacturer":2,
      "model_name":"Palio",
      "color":"azul",
      "category":"carro",
      "kms":0,
      "engine":"1000"
    },
    {
      "id":2,
      "manufacturer":2,
      "model_name":"Uno",
      "color":"prata",
      "category":"carro",
      "kms":0,
      "engine":"1.0"
    },
    {
      "id":1,
      "manufacturer":1,
      "model_name":"Vectra",
      "color":"prata",
      "category":"carro",
      "kms":0,
      "engine":"V8"
    },
    {
      "id":4,
      "manufacturer":4,
      "model_name":"Brasilia",
      "color":"azul",
      "category":"carro",
      "kms":0,
      "engine":"1000"
    }
]
```

### Filtros
Recebe os possíveis filtros de veículos indexados na aplicação.

```sh
curl http://localhost/api/index/filters/
```

Retorno: 200

```json
{
    "color":[
      {
         "key":"azul",
         "doc_count":2
      },
      {
         "key":"prata",
         "doc_count":2
      }
    ],
    "manufacturer":[
      {
         "key":"fiat",
         "doc_count":2
      },
      {
         "key":"gm",
         "doc_count":1
      },
      {
         "key":"volkswagen",
         "doc_count":1
      }
    ],
    "category":[
      {
         "key":"carro",
         "doc_count":4
      }
    ],
    "motor":[
      {
         "key":"fiat",
         "doc_count":2
      },
      {
         "key":"gm",
         "doc_count":1
      },
      {
         "key":"volkswagen",
         "doc_count":1
      }
    ]
}
```
