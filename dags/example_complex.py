from __future__ import annotations

import pendulum

from airflow.providers.standard.operators.bash import BashOperator
from airflow.sdk import DAG, chain

with DAG(
    dag_id="example_complex",
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example", "example2", "example3", "version-test"],
    description="Complex DAG with short sleep delays for version change testing - VERSION 1",
) as dag:
    create_entry_group = BashOperator(
        task_id="create_entry_group",
        bash_command="echo '🚀 [V1] create_entry_group 시작' && sleep 5 && echo '✅ create_entry_group 완료'"
    )

    create_entry_group_result = BashOperator(
        task_id="create_entry_group_result",
        bash_command="echo '📊 [V1] create_entry_group_result' && sleep 3 && echo '✅ 완료'"
    )

    create_entry_group_result2 = BashOperator(
        task_id="create_entry_group_result2",
        bash_command="echo '📊 [V1] create_entry_group_result2' && sleep 3 && echo '✅ 완료'"
    )

    create_entry_gcs = BashOperator(
        task_id="create_entry_gcs",
        bash_command="echo '☁️ [V1] create_entry_gcs 시작' && sleep 10 && echo '✅ create_entry_gcs 완료 - 여기서 DAG를 수정하세요!'"
    )

    create_entry_gcs_result = BashOperator(
        task_id="create_entry_gcs_result",
        bash_command="echo '📊 [V1] create_entry_gcs_result' && sleep 4 && echo '✅ 완료'"
    )

    create_entry_gcs_result2 = BashOperator(
        task_id="create_entry_gcs_result2",
        bash_command="echo '📊 [V1] create_entry_gcs_result2' && sleep 4 && echo '✅ 완료'"
    )

    create_tag = BashOperator(
        task_id="create_tag",
        bash_command="echo '🏷️ [V1] create_tag 시작' && sleep 7 && echo '✅ create_tag 완료'"
    )

    create_tag_result = BashOperator(
        task_id="create_tag_result",
        bash_command="echo '📊 [V1] create_tag_result' && sleep 3 && echo '✅ 완료'"
    )

    create_tag_result2 = BashOperator(
        task_id="create_tag_result2",
        bash_command="echo '📊 [V1] create_tag_result2' && sleep 3 && echo '✅ 완료'"
    )

    create_tag_template = BashOperator(
        task_id="create_tag_template",
        bash_command="echo '📋 [V1] create_tag_template 시작' && sleep 6 && echo '✅ create_tag_template 완료'"
    )

    create_tag_template_result = BashOperator(
        task_id="create_tag_template_result",
        bash_command="echo '📊 [V1] create_tag_template_result' && sleep 4 && echo '✅ 완료'"
    )

    create_tag_template_result2 = BashOperator(
        task_id="create_tag_template_result2",
        bash_command="echo '📊 [V1] create_tag_template_result2' && sleep 4 && echo '✅ 완료'"
    )

    create_tag_template_field = BashOperator(
        task_id="create_tag_template_field",
        bash_command="echo '🔧 [V1] create_tag_template_field 시작' && sleep 5 && echo '✅ create_tag_template_field 완료'"
    )

    create_tag_template_field_result = BashOperator(
        task_id="create_tag_template_field_result",
        bash_command="echo '📊 [V1] create_tag_template_field_result' && sleep 3 && echo '✅ 완료'"
    )

    create_tag_template_field_result2 = BashOperator(
        task_id="create_tag_template_field_result2",
        bash_command="echo '📊 [V1] create_tag_template_field_result2' && sleep 3 && echo '✅ 완료'"
    )

    delete_entry = BashOperator(
        task_id="delete_entry",
        bash_command="echo '🗑️ [V1] delete_entry 시작' && sleep 10 && echo '✅ delete_entry 완료 - DAG 수정 완료 시점'"
    )

    delete_entry_group = BashOperator(
        task_id="delete_entry_group",
        bash_command="echo '🗑️ [V1] delete_entry_group' && sleep 4 && echo '✅ 완료'"
    )

    delete_tag = BashOperator(
        task_id="delete_tag",
        bash_command="echo '🗑️ [V1] delete_tag' && sleep 4 && echo '✅ 완료'"
    )

    delete_tag_template_field = BashOperator(
        task_id="delete_tag_template_field",
        bash_command="echo '🗑️ [V1] delete_tag_template_field' && sleep 4 && echo '✅ 완료'"
    )

    delete_tag_template = BashOperator(
        task_id="delete_tag_template",
        bash_command="echo '🗑️ [V1] delete_tag_template' && sleep 4 && echo '✅ 완료'"
    )

    get_entry_group = BashOperator(
        task_id="get_entry_group",
        bash_command="echo '📥 [V1] get_entry_group' && sleep 3 && echo '✅ 완료'"
    )

    get_entry_group_result = BashOperator(
        task_id="get_entry_group_result",
        bash_command="echo '📊 [V1] get_entry_group_result' && sleep 2 && echo '✅ 완료'"
    )

    get_entry = BashOperator(
        task_id="get_entry",
        bash_command="echo '📥 [V1] get_entry' && sleep 3 && echo '✅ 완료'"
    )

    get_entry_result = BashOperator(
        task_id="get_entry_result",
        bash_command="echo '📊 [V1] get_entry_result' && sleep 2 && echo '✅ 완료'"
    )

    get_tag_template = BashOperator(
        task_id="get_tag_template",
        bash_command="echo '📥 [V1] get_tag_template' && sleep 3 && echo '✅ 완료'"
    )

    get_tag_template_result = BashOperator(
        task_id="get_tag_template_result",
        bash_command="echo '📊 [V1] get_tag_template_result' && sleep 2 && echo '✅ 완료'"
    )

    list_tags = BashOperator(
        task_id="list_tags",
        bash_command="echo '📝 [V1] list_tags' && sleep 4 && echo '✅ 완료'"
    )

    list_tags_result = BashOperator(
        task_id="list_tags_result",
        bash_command="echo '📊 [V1] list_tags_result' && sleep 2 && echo '✅ 완료'"
    )

    lookup_entry = BashOperator(
        task_id="lookup_entry",
        bash_command="echo '🔍 [V1] lookup_entry' && sleep 4 && echo '✅ 완료'"
    )

    lookup_entry_result = BashOperator(
        task_id="lookup_entry_result",
        bash_command="echo '📊 [V1] lookup_entry_result' && sleep 2 && echo '✅ 완료'"
    )

    rename_tag_template_field = BashOperator(
        task_id="rename_tag_template_field",
        bash_command="echo '✏️ [V1] rename_tag_template_field' && sleep 5 && echo '✅ 완료'"
    )

    search_catalog = BashOperator(
        task_id="search_catalog",
        bash_command="echo '🔎 [V1] search_catalog' && sleep 6 && echo '✅ 완료'"
    )

    search_catalog_result = BashOperator(
        task_id="search_catalog_result",
        bash_command="echo '📊 [V1] search_catalog_result' && sleep 2 && echo '✅ 완료'"
    )

    update_entry = BashOperator(
        task_id="update_entry",
        bash_command="echo '🔄 [V1] update_entry' && sleep 5 && echo '✅ 완료'"
    )

    update_tag = BashOperator(
        task_id="update_tag",
        bash_command="echo '🔄 [V1] update_tag' && sleep 5 && echo '✅ 완료'"
    )

    update_tag_template = BashOperator(
        task_id="update_tag_template",
        bash_command="echo '🔄 [V1] update_tag_template' && sleep 5 && echo '✅ 완료'"
    )

    update_tag_template_field = BashOperator(
        task_id="update_tag_template_field",
        bash_command="echo '🔄 [V1] update_tag_template_field' && sleep 5 && echo '✅ 완료'"
    )

    create_tasks = [
        create_entry_group,
        create_entry_gcs,
        create_tag_template,
        create_tag_template_field,
        create_tag,
    ]
    chain(*create_tasks)

    create_entry_group >> delete_entry_group
    create_entry_group >> create_entry_group_result
    create_entry_group >> create_entry_group_result2

    create_entry_gcs >> delete_entry
    create_entry_gcs >> create_entry_gcs_result
    create_entry_gcs >> create_entry_gcs_result2

    create_tag_template >> delete_tag_template_field
    create_tag_template >> create_tag_template_result
    create_tag_template >> create_tag_template_result2

    # create_tag_template_field >> delete_tag_template_field
    # create_tag_template_field >> create_tag_template_field_result
    # create_tag_template_field >> create_tag_template_field_result2

    create_tag >> delete_tag
    create_tag >> create_tag_result
    create_tag >> create_tag_result2

    create_tag_template >> get_tag_template >> delete_tag_template
    get_tag_template >> get_tag_template_result

    create_entry_gcs >> get_entry >> delete_entry
    get_entry >> get_entry_result

    create_entry_group >> get_entry_group >> delete_entry_group
    get_entry_group >> get_entry_group_result

    create_tag >> list_tags >> delete_tag
    list_tags >> list_tags_result

    create_entry_gcs >> lookup_entry >> delete_entry
    lookup_entry >> lookup_entry_result

    create_tag_template_field >> rename_tag_template_field >> delete_tag_template_field

    chain(create_tasks, search_catalog)
    search_catalog >> search_catalog_result

    create_entry_gcs >> update_entry >> delete_entry
    create_tag >> update_tag >> delete_tag
    create_tag_template_field >> update_tag_template_field
