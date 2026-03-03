import pathlib
import os

from cosmos import DbtDag, ProjectConfig, ProfileConfig

DBT_PROJECT_PATH = pathlib.Path(
    os.getenv("AIRFLOW_HOME", pathlib.Path(__file__).parent.parent)
) / "dbt_project/micro_project"

micro_project_dag = DbtDag(
    dag_id="micro_project_dag",
    project_config=ProjectConfig(
        dbt_project_path=DBT_PROJECT_PATH,
    ),
    profile_config=ProfileConfig(
        profile_name="micro_project",
        target_name="dev",
        profiles_yml_filepath=DBT_PROJECT_PATH / "profiles.yml",
    )
)