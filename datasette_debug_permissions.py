import datasette
import click
import pathlib
import traceback

datasette_path = pathlib.Path(datasette.__file__)
path_to_remove = str(datasette_path.parent.parent.absolute())


# Using tryfirst=True because we want to always fire, even if another plugin answers
# the hook in a way that would prevent other plugins from firing
@datasette.hookimpl(tryfirst=True)
def permission_allowed(actor, action, resource):
    click.echo(
        "permission_allowed: action={}, resource={}, actor={}\n".format(
            action, or_none(resource), or_none(actor)
        ),
        err=True,
    )
    # Dump out a stack trace
    stack = traceback.format_stack()
    # Find the line that has
    # datasette/app.py ... in permission_allowed\n
    for i, line in enumerate(stack):
        if "datasette/app.py" in line and "permission_allowed" in line:
            break
    # The three lines before i are the most interesting
    click.echo("\n".join(stack[i - 3 : i]).replace(path_to_remove, ""), err=True)


def or_none(value):
    return value if value is not None else "<None>"
