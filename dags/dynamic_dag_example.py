import os
import yaml
from datetime import datetime
from airflow.sdk import dag, task

# 1. 환경 변수 사용
deployment = os.environ.get("DEPLOYMENT", "DEV")  # DEV 또는 PROD

# 2. 외부 설정 파일 로드
config_path = os.path.join(os.path.dirname(
    __file__), "config/dag_configs.yaml")
with open(config_path) as f:
    config_data = yaml.safe_load(f)

configs = config_data["configs"]

# 3. Dynamic DAG 생성
for config_name, config in configs.items():
    dag_id = f"dynamic_dag_{config_name}"

    @dag(dag_id=dag_id, start_date=datetime(2025, 1, 1), schedule=None, catchup=False)
    def dynamic_generated_dag():
        @task
        def print_message(message: str):
            print(f"[{deployment}] {message}")  # 환경 변수 반영

        # Dynamic Task 생성 예제
        from utils.common import ALL_TASKS
        for task_name in ALL_TASKS:
            print_message(f"{task_name} says: {config['message']}")

    # DAG 등록
    dynamic_generated_dag()
