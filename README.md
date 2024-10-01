# spectacular-fsize-bug

## Usage

[Install `rye`](https://rye.astral.sh/guide/installation/), then

```shell
rye sync
rye run python src/manage.py migrate
rye run python src/manage.py runserver 8000
```

Upload a file:

```shell
curl -F fname=@LICENSE http://localhost:8000/foo/
```

List uploaded files:

```shell
curl http://localhost:8000/foo/
```

Get OpenAPI schema:

```shell
curl http://localhost:8000/schema/
```

