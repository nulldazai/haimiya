# `haimiya`

an overengineered wrapper over safebooru to fetch random community artwork of
[Haimiya Mio](https://en.wikipedia.org/wiki/Haimiya_Is_Scary_Cute)

## Usage

Requirements: `uv`, `docker`, `caddy`

### Development

```
$ uv sync --frozen
$ uv run haimiya
```

Code quality commands:

```
$ uv format
$ uv check
$ uv tool run ruff check
```

### Deployment

```
$ docker compose up -d --build
$ caddy run
```
