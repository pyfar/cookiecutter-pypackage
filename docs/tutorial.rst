.. _tutorial:

Tutorial
========

.. note:: This tutorial is adapted for pyfar from the `Forked repo`_!

.. _`Forked repo`: https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/docs/tutorial.rst

To start with, you will need a `GitHub account`_ and an account on `PyPI`_. Create these before you get started on this tutorial. If you are new to Git and GitHub, you should probably spend a few minutes on some of the tutorials at the top of the page at `GitHub Help`_.

.. _`GitHub account`: https://github.com/
.. _`PyPI`: https://pypi.python.org/pypi
.. _`GitHub Help`: https://help.github.com/


Step 1: Install Cookiecutter
----------------------------

Install your cookiecutter into a virtualenv. Assuming you have Anaconda or Miniconda installed, this is how you set up and activate your virtual environment:

.. code-block:: bash

    conda create --name mypackage python
    conda activate mypackage

Here, ``mypackage`` is the name of the package that you'll create.


Install cookiecutter:

.. code-block:: bash

    pip install cookiecutter


Step 2: Generate Your Package
-----------------------------

Now it's time to generate your Python package.

Use cookiecutter, pointing it at the cookiecutter-pypackage repo:

.. code-block:: bash

    cookiecutter https://github.com/pyfar/cookiecutter-pypackage.git

You'll be asked to enter a bunch of values to set the package up.
If you don't know what to enter, have a look to :ref:`prompts` or stick with
the defaults.


Step 3: Create a GitHub Repo
----------------------------

Go to your GitHub account and create a new repo named ``mypackage``, where ``mypackage`` matches the ``[project_slug]`` from your answers to running cookiecutter. 

You will find one folder named after the ``[project_slug]``. Move into this folder, and then setup git to use your GitHub repo and upload the code:

.. code-block:: bash

    cd mypackage
    git init .
    git add .
    git commit -m "Initial skeleton."
    git remote add origin git@github.com:myusername/mypackage.git
    git push -u origin main

Where ``myusername`` and ``mypackage`` are adjusted for your username and package name.

You'll need a ssh key to push the repo. You can `Generate`_ a key or `Add`_ an existing one.

.. _`Generate`: https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/
.. _`Add`: https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/


Step 4: Install Dev Requirements
--------------------------------

You should still be in the folder containing the ``pyproject.toml`` file.

Your virtualenv should still be activated. If it isn't, activate it now. Install the new project's local development requirements:

.. code-block:: bash

    pip install -e ".[dev]"


Step 5: Set Up Circle Ci
------------------------

`CircleCI`_ is a continuous integration tool used to prevent integration problems. Every commit to a branch will trigger automated testing for the package.

Login using your Github credentials. It may take a few minutes for CircleCi to load up a list of all your GitHub repos. They in the Projects environment.

Add the public repo to your CircleCI account by clicking ``Set Up Project`` next to the ``mypackage`` repo. Choose the ``.circleci/config.yml`` file and click ``Set Up Project``. No need to do further settings.

You can now push to your GitHub repo and CircleCI will automatically run the tests. You can see the status of your tests in the CircleCI dashboard and on Github.

.. _`CircleCI`: https://circleci.com/


Step 6: Set Up Read the Docs
----------------------------

`Read the Docs`_ hosts documentation for the open source community. Think of it as Continuous Documentation.

Log into your account at `Read the Docs`_ . If you don't have one, create one and log into it. Connect your GitHub account to your Read the Docs account.
Click on the ``Add project`` button. You should find your project ``mypackage`` repo listed. Use the ``Continue`` button to import the project via using the automatic configuration. It is already setup in your Github repository with the ``.readthedocs.yaml`` file.

.. _`Read the Docs`: https://readthedocs.org/

Step 7: Add repo to the Gallery
-------------------------------

No the `pyfar gallery`_ header need to be updated, create a pull request which adds the new package into the `header.rst`_ file.
After this is merged all other documentations of the packages have to rebuild. In this way the new package will be listed in the gallery and all packages headers.

.. _`pyfar gallery`: https://github.com/pyfar/gallery
.. _`header.rst`: https://github.com/pyfar/gallery/blob/main/docs/_static/header.rst

Step 8: Release on PyPI
-----------------------

The Python Package Index or `PyPI`_ is the official third-party software repository for the Python programming language. Python developers intend it to be a comprehensive catalog of all open source Python packages.

First we need to setup the automatic deployment of the package to PyPI cia CircleCI. It is already configured in the ``.circleci/config.yml`` file.

All we need to do is adding the token to the CircleCI project. 
See `PyPI Help`_ for more information about it.

When you are ready, release your package as described in the `pyfar deploying guidelines`_.


.. _`PyPI`: https://pypi.python.org/pypi
.. _`PyPI Help`: https://pypi.org/help/#apitoken
.. _`pyfar deploying guidelines`: https://pyfar-gallery.readthedocs.io/en/latest/contribute/contribution_packages.html#deploying


Having problems?
----------------

Go to our `Issues`_ page and create a new Issue. Be sure to give as much information as possible.

.. _`Issues`: https://github.com/pyfar/cookiecutter-pypackage/issues
