.. _prompts:

Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
    Your full name.

email
    Your email address.

git_service
    Your git service username, Github (default), or gitlab from RWTH Aachen University.

github_username
    Your git service username.

project_name
    The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here.

project_slug
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of project_name. Note: your PyPi project and Travis links will use project_slug, so change those in the README afterwards.

project_short_description
    A 1-sentence description of what your Python package does.

project_long_description
    A more detailed description of what your Python package does. This is used in the documentation.

pypi_username
    Your Python Package Index account username.

version
    The starting version number of the package.

Options
-------

The following package configuration options set up different features for your project.

use_circle_ci
    Whether to use `CircleCI <https://circleci.com/>`_.

use_pytest
    Whether to use `pytest <https://docs.pytest.org/en/latest/>`_ in your package.

use_numpy
    Whether to use `NumPy <http://www.numpy.org/>`_ in your package.

use_matplotlib
    Whether to use `Matplotlib <https://matplotlib.org/>`_ in your package.

use_scipy
    Whether to use `SciPy <https://www.scipy.org/>`_ in your package.

use_pyfar
    Whether to use `Pyfar <https://www.pyfar.org/>`_ in your package.

use_black
    Whether to use `Black <https://black.readthedocs.io/en/stable/>`_ in your package.

install_libsndfile1
    Whether we need to install libsndfile1 on ci before running the continues integrations.

new_project
    Whether we are creating a new project or we overwrite an existing one. If it is overwriting,
    we don't overwrite existing implementations e.g. ``__init__.py`` files.

use_pypi_deployment_with_ci
    Whether to use PyPI deployment with `CircleCI <https://circleci.com/>`_.

add_pyup_badge
    Whether to include a `pyup <https://github.com/pyupio/pyup>`_ badge

minimum_python_version
    The minimum Python version required to run the package.

default_python_version
    The default Python version to use in the package. Mainly used for CircleCI or readthedocs configuration.

keywords
    A comma-separated list of keywords with Quotation Marks for your package. These are pasted in the ``pyproject.toml``.

command_line_interface
    Whether to create a console script using Click. Console script entry point will match the project_slug. Options: ['Click', 'Argparse', 'No command-line interface']

open_source_license
    Choose a `license <https://choosealicense.com/>`_. Options: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License 2.0, 5. GNU General Public License v3, 6. Not open source]
