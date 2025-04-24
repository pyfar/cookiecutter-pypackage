## cookiecutter for pyfar pypackages

[![Documentation Status](https://readthedocs.org/projects/pyfar-cookiecutter-pypackage/badge/?version=latest)](https://pyfar-cookiecutter-pypackage.readthedocs.io/en/latest/?badge=latest)
[![CircleCI](https://circleci.com/gh/pyfar/cookiecutter-pypackage.svg?style=shield)](https://circleci.com/gh/pyfar/cookiecutter-pypackage)

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for pyfar Python packages.

This template is used to keep all pyfar packages consistent and
to provide a good starting point for new packages. It is forked from
`cookiecutter-pypackage <https://github.com/audreyfeldroy/cookiecutter-pypackage>`_.

Free software: BSD license

### Getting Started

The [pyfar workshop](https://mybinder.org/v2/gh/pyfar/gallery/main?labpath=docs/gallery/interactive/pyfar_introduction.ipynb)
gives an overview of the most important pyfar functionality and is a good
starting point. It is part of the [pyfar example gallery](https://pyfar-gallery.readthedocs.io/en/latest/examples_gallery.html)
that also contains more specific and in-depth
examples that can be executed interactively without a local installation by
clicking the mybinder.org button on the respective example. The
[pyfar documentation](https://pyfar.readthedocs.io) gives a detailed and complete overview of pyfar. All
these information are available from [pyfar.org](https://pyfar.org).

### Quickstart

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)

    pip install -U cookiecutter

Generate a Python package project

    cookiecutter https://github.com/pyfar/cookiecutter-pypackage.git

Then:

- Create a repo and put it there.
- Add the repo to your Circleci account.
- Add the repo to your [Read the Docs](https://readthedocs.com/) account + turn on the Read the Docs service hook and activate it for pull requests.
- Release your package using bump-my-version (see [Contributing](https://pyfar-gallery.readthedocs.io/en/latest/contribute/contribution_packages.html#deploying)).
- Activate your project on [pypi.org](https://pypi.org/).

For more details, see the [cookiecutter-pypackage tutorial](https://cookiecutter-pypackage.readthedocs.io/en/latest/tutorial.html).

### Contributing

Check out the [contributing guidelines](https://pyfar.readthedocs.io/en/stable/contributing.html) if you want to become part of pyfar.
