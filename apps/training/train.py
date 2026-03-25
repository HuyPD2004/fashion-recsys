from infrastructure.data.loaders import load_data
from infrastructure.data.preprocess import preprocess
from application.pipelines.training_pipeline import run_pipeline

def main():
    data = load_data("data/raw/data.json")
    data = preprocess(data)
    run_pipeline(data)

if __name__ == "__main__":
    main()