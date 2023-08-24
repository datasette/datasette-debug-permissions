from click.testing import CliRunner
from datasette.cli import cli
import json


def test_datasette_debug_permissions():
    # datasette --get '/-/databases.json'
    result = CliRunner(mix_stderr=False).invoke(cli, ["--get", "/-/plugins.json"])
    assert json.loads(result.output) == [
        {
            "name": "datasette-debug-permissions",
            "static": False,
            "templates": False,
            "version": "0.1",
            "hooks": ["permission_allowed"],
        }
    ]
    # Should have logged to stderr:
    assert result.stderr.startswith(
        "permission_allowed: action=view-instance, resource=<None>, actor=<None>\n\n"
    )
    # Should have three stack frames:
    assert result.stderr.count(" File ") == 3
