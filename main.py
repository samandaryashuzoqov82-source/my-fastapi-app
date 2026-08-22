import asyncio
import os
import httpx
import redis
from fastapi import FastAPI

app = FastAPI()

# --- SIZNING BOR KODINGIZ (REDIS) ---
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

try:
    redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
    redis_client.ping()
    print("Redis'ga muvaffaqiyatli ulandi!")
except Exception as e:
    print(f"Redis ulanishida xatolik: {e}")
    redis_client = None


# --- SERVERNI UYGO'TIB TURUVCHI YANGI KOD ---
async def keep_alive():
    while True:
        await asyncio.sleep(600)  # Har 10 daqiqada (600 soniya)
        try:
            async with httpx.AsyncClient() as client:
                await client.get(
                    "https://my-fastapi-app-s9tv.onrender.com/docs"
                )
                print("Server uyg'otildi!")
        except Exception as e:
            print("Xatolik:", e)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(keep_alive())


@app.get("/")
def read_root():
    return {"status": "ok"}
