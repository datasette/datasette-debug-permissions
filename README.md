# datasette-debug-permissions

[![PyPI](https://img.shields.io/pypi/v/datasette-debug-permissions.svg)](https://pypi.org/project/datasette-debug-permissions/)
[![Changelog](https://img.shields.io/github/v/release/datasette/datasette-debug-permissions?include_prereleases&label=changelog)](https://github.com/datasette/datasette-debug-permissions/releases)
[![Tests](https://github.com/datasette/datasette-debug-permissions/workflows/Test/badge.svg)](https://github.com/datasette/datasette-debug-permissions/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/datasette/datasette-debug-permissions/blob/main/LICENSE)

A Datasette plugin that outputs debug information about permission checks.

## Installation

```bash
datasette install datasette-debug-permissions
```

## Usage

This plugin adds debugging output to standard error as Datasette is running showing any times the `permission_allowed()` plugin hook is called.

See [Authentication and permissions](https://docs.datasette.io/en/stable/authentication.html) in the Datasette documentation for more on why this is useful.

## Example output

```
INFO:     Uvicorn running on http://127.0.0.1:8833 (Press CTRL+C to quit)
permission_allowed: action=view-instance, resource=<None>, actor=<None>
permission_allowed: action=view-database, resource=_internal, actor=<None>
permission_allowed: action=view-database, resource=mydatabase, actor=<None>
permission_allowed: action=view-database, resource=mydatabase, actor=<None>
permission_allowed: action=view-table, resource=('mydatabase', 'mytable'), actor=<None>
permission_allowed: action=view-table, resource=('mydatabase', 'mytable'), actor=<None>
permission_allowed: action=view-instance, resource=<None>, actor=<None>
permission_allowed: action=view-instance, resource=<None>, actor=<None>
permission_allowed: action=debug-menu, resource=<None>, actor=<None>
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:
```bash
cd datasette-debug-permissions
python3 -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```
pip install -e '.[test]'
```
To install the JavaScript build dependencies, run this:
```bash
npm install
```
You can use the [Just](https://github.com/casey/just) command runner to build the TypeScript to minified JavaScript like this:
```bash
just js
```
To run the tests:
```bash
pytest
```
