import os
import requests
from tqdm import tqdm
import gzip
import shutil
from infrastructure.config.settings import settings

def unzip_file(gz_path):
    json_path = gz_path.replace(".gz", "")
    with gzip.open(gz_path, 'rb') as f_in:
        with open(json_path, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    print(f"Unzipped: {json_path}")
    

def download_file(url, output_path):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(output_path, 'wb') as file, tqdm(
        desc=output_path,
        total=total_size,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                file.write(chunk)
                bar.update(len(chunk))


def main():
    os.makedirs(settings.DATA_DIR, exist_ok=True)

    files = {
        settings.META_FILE: settings.META_URL,
        settings.REVIEW_FILE: settings.REVIEW_URL,
    }

    for name, url in files.items():
        output_path = os.path.join(settings.DATA_DIR, name)

        if os.path.exists(output_path):
            print(f"{name} already exists, skipping...")
            continue

        print(f"Downloading {name}...")
        download_file(url, output_path)

    print("Download completed!")

    print("Unzipping files...")
    unzip_file(os.path.join(settings.DATA_DIR, settings.META_FILE))
    unzip_file(os.path.join(settings.DATA_DIR, settings.REVIEW_FILE))
    print("Unzip completed!")

if __name__ == "__main__":
    main()