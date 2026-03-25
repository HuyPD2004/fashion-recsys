import os
import json
from typing import Iterator, Dict, Any, Optional
import pandas as pd 
from infrastructure.config.settings import settings
from infrastructure.config.loggings import setup_logger

logger = setup_logger(__name__)

def _read_jsonl(file_path: str) -> Iterator[Dict[str, Any]]:
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            try:
                yield json.loads(line.strip())
            except json.JSONDecodeError:
                logger.error(f"Error decoding JSON: {line}")
                continue

def load_review_data(limit: Optional[int] = None) -> pd.DataFrame:
    file_path = os.path.join(settings.DATA_DIR, settings.REVIEW_FILE)

    records = []
    try:
        for record in _read_jsonl(file_path):
            try:
                records.append({
                    "user_id": record.get("user_id"),
                    "asin": record.get("asin"),
                    "parent_asin": record.get("parent_asin"),
                    "rating": record.get("rating"),
                    "text": record.get("text"),
                    "timestamp": record.get("sort_timestamp")
                })
            except Exception as e:
                logger.error(f"Error processing record: {record}")
                continue
            if limit is not None and len(records) >= limit:
                break

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")

    return pd.DataFrame(records)

def load_meta_data(limit: Optional[int] = None) -> pd.DataFrame:
    file_path = os.path.join(settings.DATA_DIR, settings.META_FILE)

    records = []

    try:
        for record in _read_jsonl(file_path):
            try:
                images = record.get("images") or []
                image_url = None

                if len(images) > 0:
                    image_url = images[0].get("hi_res")

                details = record.get("details") or {}

                records.append({
                    "title": record.get("title"),
                    "average_rating": record.get("average_rating"),
                    "rating_number": record.get("rating_number"),
                    "price": record.get("price"),
                    "parent_asin": record.get("parent_asin"),
                    "image": image_url,
                    "date_first_available": details.get("Date First Available"),
                    "package_dimensions": details.get("Package Dimensions"),
                    "item_model_number": details.get("Item model number"),
                    "store": record.get("store"),
                    "features": " ".join(record.get("features") or []),
                    "description": " ".join(record.get("description") or [])
                })

            except Exception as e:
                logger.warning(f"Skip bad record: {e}")
                continue

            if limit is not None and len(records) >= limit:
                break

    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

    return pd.DataFrame(records)

def load_full_dataset(limit: Optional[int] = None) -> pd.DataFrame:
    review_df = load_review_data(limit)
    meta_df = load_meta_data(limit)

    df = review_df.merge(meta_df, on="parent_asin", how="left")
    return df

if __name__ == "__main__":
    df = load_full_dataset(limit=1000)
    print(df.head())
    print(df.shape)