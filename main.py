import os
import redis

# Render'dagi REDIS_URL ni oladi, bo'lmasa local yaratadi
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")

try:
    redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
    # Ulanishni tekshirish
    redis_client.ping()
    print("Redis'ga muvaffaqiyatli ulandi!")
except Exception as e:
    print(f"Redis ulanishida xatolik (e'tiborsiz qoldirildi): {e}")
    redis_client = None
