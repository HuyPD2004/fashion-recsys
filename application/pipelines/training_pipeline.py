from application.training.train_cf import train_cf
from application.training.train_content import train_content

def run_pipeline(data):
    cf_model = train_cf(data)
    cb_model = train_content(data)

    print("Training pipeline completed")