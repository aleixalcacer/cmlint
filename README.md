# cmlint: Commit Message Linter

## Installation

```
pip install git+https://github.com/aleixalcacer/cmlint.git
```

## Commit structure

The first line of the commit message should be structured as follows:
```
<type>[optional scope]: <description>
```

* The types allowed are: `build`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `style` and `test`.
* Scope may be provided to a commit’s type, to provide additional contextual information and is contained within 
  parenthesis, e.g., `feat(linter): add ability to lint commit messages`.

## Usage as a Git hook

To use `cmlint` as a git hook create (or modify) the `.git/hooks/commit-msg` script and add the following line:

```
cmlint "$1"
```

### Example

```
 $ git commit -a -m "feat: Implement a command line tool that lints commit messages"
Commit message is valid! 🥳 
[main b983612] feat: Implement a command line tool that lints commit messages
 5 files changed, 95 insertions(+), 2 deletions(-)
 create mode 100644 cmlint/__init__.py
 create mode 100644 cmlint/command_line.py
 create mode 100644 pyproject.toml
 create mode 100644 setup.py
```
