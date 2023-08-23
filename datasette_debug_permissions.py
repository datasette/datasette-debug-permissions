from datasette import hookimpl
import click


# Using tryfirst=True because we want to always fire, even if another plugin answers
# the hook in a way that would prevent other plugins from firing
@hookimpl(tryfirst=True)
def permission_allowed(actor, action, resource):
    click.echo(
        "permission_allowed: action={}, resource={}, actor={}".format(
            action, or_none(resource), or_none(actor)
        ),
        err=True,
    )


def or_none(value):
    return value if value is not None else "<None>"
