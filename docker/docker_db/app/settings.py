
import os 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Replace with your actual database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)




# from starlette.config import Config
# from starlette.datastructures import Secret

# try:
#     config = Config(".env")
# except FileNotFoundError:
#     config = Config()

# DATABASE_URL = config("DATABASE_URL", cast=Secret)