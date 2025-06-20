from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/mercadolibre")
async def mercadolibre(q: str):
    url = f"https://api.mercadolibre.com/sites/MLM/search?q={q}"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        data = r.json()
        return [
            {
                "titulo": item["title"],
                "precio": item["price"],
                "imagen": item["thumbnail"],
                "link": item["permalink"],
                "plataforma": "Mercado Libre"
            }
            for item in data["results"]
        ]