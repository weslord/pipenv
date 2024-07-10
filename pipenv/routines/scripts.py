import sys

from pipenv.utils import console, err

def do_scripts(state):
    if not state.project.pipfile_exists:
        err.print("No Pipfile present at project home.")
        sys.exit(1)
    scripts = state.project.parsed_pipfile.get("scripts", {})
    first_column_width = max(len(word) for word in ["Command"] + list(scripts))
    second_column_width = max(len(word) for word in ["Script"] + list(scripts.values()))
    lines = [f"{command:<{first_column_width}}  Script" for command in ["Command"]]
    lines.append(f"{'-' * first_column_width}  {'-' * second_column_width}")
    lines.extend(
        f"{name:<{first_column_width}}  {script}" for name, script in scripts.items()
    )
    console.print("\n".join(line for line in lines))
