from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.utils.task_group import TaskGroup
import random

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
    dag_id="enhanced_dynamic_taskflow_dag",
    default_args=default_args,
    description="Enhanced Dynamic DAG with validation and branching",
    schedule=None,
    start_date=datetime(2025, 1, 1),
    catchup=False,
    tags=["dynamic", "taskflow", "complex"]
)
def enhanced_dynamic_taskflow():

    @task
    def aggregate_results(results: list):
        print("Aggregating all team results...")
        for r in results:
            print(r)
        return "Aggregation complete"

    @task
    def compute_statistics(results: list):
        print("Computing statistics from team results...")
        stats = {
            "total_teams": len(results),
            "success_count": sum([1 for r in results if "done" in r])
        }
        print(stats)
        return stats

    # 팀별 TaskGroup 생성
    team_results = []

    for team in teams:
        with TaskGroup(group_id=f"{team}_tasks") as tg:

            @task
            def preprocess(team_name: str):
                print(f"[{team_name}] Preprocessing data......!")
                return f"{team_name}_preprocessed"

            @task
            def validate(preprocessed_data: str):
                print(f"[{preprocessed_data}] Validating data...")
                # 랜덤으로 데이터 검증 성공/실패 시뮬레이션
                if random.choice([True, True, False]):
                    print("Validation passed")
                    return preprocessed_data
                else:
                    raise ValueError(f"{preprocessed_data} validation failed!")

            @task
            def analyze(validated_data: str):
                print(f"[{validated_data}] Analyzing data...")
                # 랜덤 점수 생성
                score = random.randint(0, 100)
                print(f"Analysis score: {score}")
                return {"team": validated_data, "score": score}

            @task
            def postprocess_by_score(result: dict):
                if result["score"] >= 50:
                    print(
                        f"[{result['team']}] High score postprocessing for {result['score']}")
                    return f"{result['team']}_high_done"
                else:
                    print(
                        f"[{result['team']}] Low score postprocessing for {result['score']}")
                    return f"{result['team']}_low_done"

            # TaskFlow 의존성 연결
            validated = validate(preprocess(team))
            analyzed = analyze(validated)
            post_result = postprocess_by_score(analyzed)
            team_results.append(post_result)

    # 중간 통계 계산
    stats = compute_statistics(team_results)

    # 최종 결과 집계
    aggregate_results(team_results)


dag = enhanced_dynamic_taskflow()
