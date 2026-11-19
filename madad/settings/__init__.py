from os import environ

from split_settings.tools import include, optional

ENV = environ.get("DJANGO_ENV") or "development"

include(
    "components/base.py",
    # "components/debug.py",  # add later when useful
    # optionally load environment-specific configuration
    optional("environments/{0}.py".format(ENV)),
    # for now, we require local settings
    "local_settings.py",
)
