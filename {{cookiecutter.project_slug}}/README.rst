{% set is_open_source = cookiecutter.open_source_license != 'Not open source' -%}
{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}
{% if is_open_source %}
.. image:: https://badge.fury.io/py/{{ cookiecutter.project_slug }}.svg
    :target: https://badge.fury.io/py/{{ cookiecutter.project_slug }}
.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
    :target: https://{{ cookiecutter.project_slug }}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. image:: https://circleci.com/gh/{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug | replace("_", "-") }}.svg?style=shield
    :target: https://circleci.com/gh/{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug | replace("_", "-") }}
{%- endif %}

{% if cookiecutter.add_pyup_badge == 'y' %}
.. image:: https://pyup.io/repos/github/{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}/shield.svg
     :target: https://pyup.io/repos/github/{{ cookiecutter.git_username }}/{{ cookiecutter.project_slug }}/
     :alt: Updates
{% endif %}
.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/pyfar/gallery/main?labpath=docs/gallery/interactive/pyfar_introduction.ipynb

{{ cookiecutter.project_short_description }}

Getting Started
===============

The `pyfar workshop`_ gives an overview of the most important pyfar
functionality and is a good starting point. It is part of the
`pyfar example gallery`_ that also contains more specific and in-depth
examples that can be executed interactively without a local installation by
clicking the mybinder.org button on the respective example. The
`pyfar documentation`_ gives a detailed and complete overview of pyfar. All
these information are available from `pyfar.org`_.

Installation
============

Use pip to install {{ cookiecutter.project_slug }}

.. code-block:: console

    $ pip install {{ cookiecutter.project_slug }}

(Requires Python {{ cookiecutter.minimum_python_version }} or higher)

If the installation fails, please check out the `help section`_.

Contributing
============

Check out the `contributing guidelines`_ if you want to become part of pyfar.

.. _pyfar workshop: https://mybinder.org/v2/gh/pyfar/gallery/main?labpath=docs/gallery/interactive/pyfar_introduction.ipynb
.. _pyfar example gallery: https://pyfar-gallery.readthedocs.io/en/latest/examples_gallery.html
.. _pyfar documentation: https://pyfar.readthedocs.io
.. _pyfar.org: https://pyfar.org
.. _help section: https://pyfar-gallery.readthedocs.io/en/latest/help
.. _contributing guidelines: https://pyfar.readthedocs.io/en/stable/contributing.html
