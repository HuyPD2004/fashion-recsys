#!/bin/bash

BASE=recsys-hybrid

mkdir -p $BASE/{apps/api/{routes,schemas,dependencies},apps/training,apps/batch}
mkdir -p $BASE/domain/{models,entities,services}
mkdir -p $BASE/application/{training,inference,pipelines}
mkdir -p $BASE/infrastructure/{data,db,ml,retrieval,config}
mkdir -p $BASE/mlops/{airflow/dags,mlflow,docker,ci_cd}
mkdir -p $BASE/{notebooks,data/{raw,processed,features},models/{cf,content,hybrid}}
mkdir -p $BASE/tests/{unit,integration}
mkdir -p $BASE/{scripts,web}

touch $BASE/apps/api/main.py
touch $BASE/apps/api/routes/recommend.py
touch $BASE/apps/training/train.py
touch $BASE/apps/batch/batch_infer.py

touch $BASE/domain/models/{cf_model.py,content_model.py,hybrid_model.py}
touch $BASE/domain/entities/{user.py,item.py}
touch $BASE/domain/services/recommender.py

touch $BASE/application/training/{train_cf.py,train_content.py,train_hybrid.py}
touch $BASE/application/inference/recommend.py
touch $BASE/application/pipelines/training_pipeline.py

touch $BASE/infrastructure/data/{loaders.py,preprocess.py,feature_store.py}
touch $BASE/infrastructure/db/{postgres.py,redis_cache.py}
touch $BASE/infrastructure/ml/{model_registry.py,tracking.py}
touch $BASE/infrastructure/retrieval/faiss_index.py
touch $BASE/infrastructure/config/settings.py

touch $BASE/mlops/docker/{Dockerfile.api,Dockerfile.train,docker-compose.yml}
touch $BASE/mlops/ci_cd/github_actions.yml

touch $BASE/scripts/{download_data.py,run_pipeline.sh}
touch $BASE/web/{index.html,app.js,styles.css}

touch $BASE/{requirements.txt,pyproject.toml,README.md}

echo "Project structure created!"
