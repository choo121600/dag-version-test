from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.utils.task_group import TaskGroup

teams = ["team_a", "team_b", "team_c"]

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}


@dag(
    dag_id="complex_dynamic_taskflow_dag",
    default_args=default_args,
    description="Complex Dynamic DAG for testing with TaskFlow API",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["dynamic", "taskflow", "complex"]
)
def complex_dynamic_taskflow():

    @task
    def aggregate_results(results: list):
        print("Aggregating all team results...")
        for r in results:
            print(r)
        return "Aggregation complete"

    # 팀별 TaskGroup 생성
    team_results = []

    for team in teams:
        with TaskGroup(group_id=f"{team}_tasks") as tg:

            @task
            def preprocess(team_name: str):
                print(f"[{team_name}] Preprocessing data......!")
                return f"{team_name}_preprocessed"

            @task
            def analyze(preprocessed_data: str):
                print(f"[{preprocessed_data}] Analyzing data...")
                return f"{preprocessed_data}_analyzed"

            @task
            def postprocess(analyzed_data: str):
                print(f"[{analyzed_data}] Postprocessing data...")
                return f"{analyzed_data}_done"

            # TaskFlow 의존성 연결
            result = postprocess(analyze(preprocess(team)))
            team_results.append(result)

    # 모든 팀 결과를 모아서 최종 aggregate
    aggregate_results(team_results)


dag = complex_dynamic_taskflow()
