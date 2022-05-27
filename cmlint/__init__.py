import click
import re
import sys


@click.command()
@click.argument('path')
def cmlint(path):
    """Simple program that checks a commit message"""
    f = open(path)
    title = f.readline()
    f.close()

    regex = r"^(build|ci|docs|feat|fix|perf|refactor|style|test)(\(.*\))?\!?: (.){0,60}$"

    if re.match(regex, title) is None:
        print("Commit message is not valid! \U0000274C ")
        print("See https://github.com/aleixalcacer/cmlint for more info.")
        sys.exit(-1)
    else:
        print("Commit message is valid! \U0001F973 ")
        sys.exit(0)

