"""Constants."""
import jmespath

from nitpick import __version__

PROJECT_NAME = "nitpick"
ERROR_PREFIX = "NIP"
CACHE_DIR_NAME = ".cache"
TOML_EXTENSION = ".toml"
NITPICK_STYLE_TOML = "nitpick-style{}".format(TOML_EXTENSION)
MERGED_STYLE_TOML = "merged-style{}".format(TOML_EXTENSION)
NITPICK_VERSION = "v{}".format(__version__)
DEFAULT_NITPICK_STYLE_URL = "https://raw.githubusercontent.com/andreoliwa/nitpick/{}/{}".format(
    NITPICK_VERSION, NITPICK_STYLE_TOML
)
MANAGE_PY = "manage.py"
ROOT_PYTHON_FILES = ("setup.py", "autoapp.py")
ROOT_FILES = ("requirements*.txt", "Pipfile") + ROOT_PYTHON_FILES

#: Special unique separator for :py:meth:`flatten()` and :py:meth:`unflatten()`,
# to avoid collision with existing key values (e.g. the default dot separator "." can be part of a pyproject.toml key).
UNIQUE_SEPARATOR = "$#@"

# Config sections and keys
TOOL_NITPICK = "tool.nitpick"

# JMESPath expressions
TOOL_NITPICK_JMEX = jmespath.compile(TOOL_NITPICK)
NITPICK_STYLES_INCLUDE_JMEX = jmespath.compile("nitpick.styles.include")
NITPICK_MINIMUM_VERSION_JMEX = jmespath.compile("nitpick.minimum_version")