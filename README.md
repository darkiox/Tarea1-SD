
# Tarea 1 - Sistemas Distribuidos
Desarrollado por [Darkiox](https://github.com/darkiox) y [JavierGv1](https://github.com/)

Sistema que implementa Redis para caché y gRPC para conexión entre microservicios.

Base de datos utiliza postgresql (user = postgres, pass = postgrespw, nombre db = tarea)

La búsqueda se realiza con el campo "keywords", buscando si contiene el string ingresado en la query.

Front-end no era necesario, pero fue montado como POC en el puerto 5050.

Para montar el sistema se debe ejecutar el siguiente comando en el directorio del archivo "docker-compose.yml"

```bash
  docker compose build && docker compose run
```


## Video

[![Video](https://img.youtube.com/vi/3Mng6gakTtA/maxresdefault.jpg)](https://www.youtube.com/watch?v=3Mng6gakTtA)
## Agradecimientos/Fuentes

 - [Problema Psycopg2 con libpq por uso de chip ARM](https://github.com/psycopg/psycopg2/issues/1360)
 - [Redis](https://redis.io/docs/getting-started/)
 - [gRPC](https://grpc.io/docs/platforms/web/basics/)

