# Docker SPA

[![Build Status](https://travis-ci.org/carlosmaniero/docker-spa.svg?branch=master)](https://travis-ci.org/carlosmaniero/docker-spa)

Exemplo simples de utilização de docker com SPA (Single Page Application).

## Rodando

Dentro da pasta do projeto execute o build que irá baixar as imagens e as depedências do projeto:

    $ docker-compose build

Para iniciar a aplicação:

    $ docker-compose up

### Escalando a aplicação

Com os containers em execução `docker-compose up`, execute o seguinte comando para escalar dois containers à aplicação `rest_app`:

    $ docker-compose scale rest_app=2

Sim! Sim! Sim! Podemos escalar a aplicação!

**PS:** Caso você não escale duas máquinas para a rest_app, pode haver uma perca no desempenho, já que o ngnix está configurado para rodar com duas máquinas. Caso uma não exista ou esteja offline ele vai redirecionar a requisição para a máquina que estiver funcionando.

## E agora? Como eu faço pra ver isso no navegador?

Só acessar seu [http://localhost/](http://localhost/).

![Magic](http://www.reactiongifs.com/r/mgc.gif)
