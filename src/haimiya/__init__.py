from urllib.parse import urlencode

import aiohttp
from quart import Quart, Response


class App(Quart):
    client: aiohttp.ClientSession


app = App(__name__)


@app.while_serving
async def lifespan():
    app.client = aiohttp.ClientSession()
    yield
    await app.client.close()


@app.route("/")
async def index():
    async with app.client.get(
        "https://safebooru.org/index.php",
        params=urlencode(
            {
                "page": "dapi",
                "s": "post",
                "q": "index",
                "limit": 1,
                "json": 1,
                "tags": "sort:random+haimiya_mio_(kamiyama_sumu)",
            },
            safe="+:()",
        ),
    ) as res:
        json = await res.json()

        file = json[0]["file_url"]

    async with app.client.get(file) as res:
        return Response(
            await res.content.read(), content_type=res.content_type, status=res.status
        )


def main():
    app.run()
