from os import waitstatus_to_exitcode
from prefect import Flow
from prefect.tasks.dbt import DbtShellTask

with Flow(name="dbt_flow") as f:
    task = DbtShellTask(
        profile_name="insider",
        environment="dev",
        profiles_dir="../dbt/profiles",
        log_stderr=True,
        return_all=True,
    )(command="dbt run --project-dir ../dbt/insider")

out = f.run()
