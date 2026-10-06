# tbp.monty_project_template

This is a template repository to quickly use [tbp.monty](https://github.com/thousandbrainsproject/tbp.monty) for your project, prototype, or paper.

To create a repository from this template, find and click the "Use this template" button:

![Use this template](./delete_me.png)

## Make it yours

After copying the template, you need to address the following TODOs.

### `pyproject.toml`

- Update the project `description`
- Update the project `name`
- Update the `Repository` and `Issues` URLs
- Pin the `tbp.monty` dependency to the desired Monty version for reproduciblity or unpin entirely

### `src` directory

- Rename source path `src/tbp/monty_project_template` to match your `pyproject.toml` project `name`.

### Delete template images

- Delete `delete_me.png`
- Delete `delete_me_too.png`

### `README.md`

- Update for your project

### Recommendations

For a cleaner project commit history, go to your repository settings and in the Pull Requests section, only "Allow squash merging". It also helps to set your default commit message to the "Pull request title" option.

![Pull Request Settings](./delete_me_too.png)

## Installation

The environment for this project is managed with [uv](https://docs.astral.sh/uv/).

To create the environment, run:

```
uv sync --extra dev
```

## Experiments

Define your experiments in the `src/tbp/monty_project_template/conf/experiment` directory
(your path will be different as it will match your project name).
You'll need to pass the `src/tbp/monty_project_template/conf` path as part of your run command
via the Hydra `-cd src/tbp/monty_project_template/conf` option.

After installing the environment, to run an experiment, run:

```bash
uv run python run.py -cd src/tbp/monty_project_template/conf experiment=example
```

To run an experiment where episodes are executed in parallel, run:

```bash
uv run python run_parallel.py -cd src/tbp/monty_project_template/conf experiment=example num_parallel=8
```

## Development

After installing the environment, you can run the following commands to check your code.

### Run formatter

```bash
uv run ruff format
```

### Run style checks

```bash
uv run ruff check
```

### Run dependency checks

```bash
uv run deptry .
```

### Run static type checks

```bash
uv run mypy .
```

### Run tests

```bash
uv run pytest
```
