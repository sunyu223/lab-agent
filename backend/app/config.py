from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent # 后端项目的根目录

class Settings(BaseSettings):
    DATABASE_URL: str
    JWT_SECRET_KEY: str 
    JWT_EXPIRE_HOURS: int = 24
    JWT_ALGORITHM: str = "HS256"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env", 
        env_file_encoding="utf-8")

settings = Settings()

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
MAX_FILE_SIZE = 1024 * 1024 * 100 #100M

ALLOWED_EXTENSIONS = {
    ".jpg",
    ".png",
    ".jpeg",
    ".gif",
    ".zip",
    ".webp",
    ".pdf",
    ".doc",
    ".docx",
    ".xls",
    ".xlsx",
}