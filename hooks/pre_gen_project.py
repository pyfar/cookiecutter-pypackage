import re
import sys


MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'
module_name = '{{ cookiecutter.project_slug}}'
if not re.match(MODULE_REGEX, module_name):
    print(f'ERROR: The project slug ({module_name}) is not a valid Python module name. Please do not use a - and use _ instead')

    #Exit to cancel project
    sys.exit(1)


MODULE_REGEX = '3.[0-9]+'
default_python_version = '{{ cookiecutter.default_python_version }}'
if not re.match(MODULE_REGEX, default_python_version):
    print(f'ERROR: The project slug ({default_python_version}) is not a valid Python version number. Please use python 3.x')

    #Exit to cancel project
    sys.exit(1)


MODULE_REGEX = '3.[0-9]+'
minimum_python_version = '{{ cookiecutter.minimum_python_version }}'
if not re.match(MODULE_REGEX, minimum_python_version):
    print(f'ERROR: The project slug ({minimum_python_version}) is not a valid Python version number. Please use python 3.x')

    #Exit to cancel project
    sys.exit(1)

