# cmlint: Commit Message Linter

## Usage

1. Before you can run hooks, you need to have the pre-commit package manager installed:
```
pip install pre-commit
```

2. Add a pre-commit configuration creating a file named `.pre-commit-config.yaml` containing:
```
repos:
-   repo: https://github.com/aleixalcacer/cmlint
    rev: v0.2.0
    hooks:
    -   id: cmlint
```

3. Install the git hook script:
```
pre-commit install --hook-type commit-msg
```


#### Example

```
$ git commit -a -m "docs: Add instructions to use cmlint inside the pre-commit tool"
  Check Yaml...........................................(no files to check)Skipped
  Fix End of Files.........................................................Passed
  Trim Trailing Whitespace.................................................Passed
  black................................................(no files to check)Skipped
  cmlint...................................................................Passed
  [main 408e8d8] docs: Add instructions to use cmlint inside the pre-commit tool
   1 file changed, 25 insertions(+), 17 deletions(-)
```

## Commit structure

The first line of the commit message should be structured as follows:
```
<type>[optional scope]: <description>
```

* The types allowed are: `build`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `style` and `test`.
* Scope may be provided to a commit’s type, to provide additional contextual information and is contained within
  parenthesis, e.g., `feat(linter): add ability to lint commit messages`.
