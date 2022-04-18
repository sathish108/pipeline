"""
This module is used for  build the pybuilder(pybuilder is configured with this module)
"""
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "pybuild-flow"
default_task = "publish"


@init
def set_properties(project):
    """
    This method does not have importance
 """
    pass
