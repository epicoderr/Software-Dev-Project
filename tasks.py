from invoke import task
import sys

is_windows = sys.platform.startswith('win')

@task
def start(ctx):
    ctx.run("poetry run python src/main.py", pty=not is_windows)

@task
def test(ctx):
    ctx.run("poetry run pytest src", pty=not is_windows)


@task
def coverage(ctx):
    ctx.run(" poetry run coverage run --branch -m pytest src", pty=not is_windows)


@task(coverage)
def coverage_report(ctx):
    ctx.run(" poetry run coverage html", pty=not is_windows)