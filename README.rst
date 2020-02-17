.. image:: https://img.shields.io/travis/com/sizmailov/pybind11-stubgen/master.svg?logo=travis
    :alt: master status
    :target: https://travis-ci.com/sizmailov/pybind11-stubgen

.. image:: https://img.shields.io/pypi/v/pybind11-stubgen.svg?logo=PyPI&logoColor=white
    :alt: pypi package
    :target: https://pypi.org/project/pybind11-stubgen/

.. image:: https://codecov.io/gh/sizmailov/pybind11-stubgen/branch/master/graph/badge.svg
  :alt: coverage
  :target: https://codecov.io/gh/sizmailov/pybind11-stubgen


About
=====

Generates stubs for python modules

There are several tweaks to target specifically modules compiled using `pybind11 <https://github.com/pybind/pybind11>`_

Package targets python3 only. (In fact, it's compatible with python2 but it's not officially supported)

Issues/PR are welcome

Install
=======

**From github:**

.. code-block:: bash

   python setup.py develop
on this repo



Usage
=====


.. code-block:: bash

   python -m pybind11_stubgen -c CONFIG_FILE


Example config file at `pbc.yml`

