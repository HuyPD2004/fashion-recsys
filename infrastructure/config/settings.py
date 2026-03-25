from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATA_DIR: str = "data/raw"
    PROCESSED_DIR: str = "data/processed"
    MODEL_DIR: str = "models/"

    META_FILE: str = "meta_Amazon_Fashion.jsonl"
    REVIEW_FILE: str = "Amazon_Fashion.jsonl"

    META_URL: str = "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/meta_categories/meta_Amazon_Fashion.jsonl.gz"
    REVIEW_URL: str = "https://mcauleylab.ucsd.edu/public_datasets/data/amazon_2023/raw/review_categories/Amazon_Fashion.jsonl.gz"

    LOG_DIR: str = "logs"
    
    class Config:
        env_file = ".env"


settings = Settings()