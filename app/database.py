kimport os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Render yoki local muhitdan DATABASE_URL olinadi
DATABASE_URL = os.getenv("DATABASE_URL")

# Agar DATABASE_URL muhitda belgilanmagan bo'lsa, to'g'ri Render Postgres URL ishlatiladi
if not DATABASE_URL:
    DATABASE_URL = "postgresql://my_postgres_db_zryg_user:i3JYKQDKFyncdLiYmK5Eqe9ydqZU3H98@dpg-da4rb2gn74is73ef56s0-a.ohio-postgres.render.com/my_postgres_db_zryg"

# Render bergan postgres:// manzilini SQLAlchemy talab qiladigan postgresql:// ga o'tkazish
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
