Installation
====================

**Requirements**

It is recommended to install DEM in a dedicated ``Conda`` environment to ensure that all dependencies are available in compatible versions (see the steps below).

To run optimisation studies, a solver must be installed before installing DEM. If only simulations are required, no solver installation is necessary. Optimisation in DEM is implemented using the `Calliope <https://calliope.readthedocs.io/en/stable/index.html>`_ framework, and any solver listed on the `Calliope documentation page <https://calliope.readthedocs.io/en/stable/user/installation.html>`_ can be used.

.. note::
  DEM has been tested with `Calliope v0.6.8 <https://calliope.readthedocs.io/en/v0.6.8/index.html>`_ in combination with the `Gurobi <https://www.gurobi.com/>`_ solver.


**Step 1: Create the Conda Environment**

If not already done, download and install `Conda <https://www.anaconda.com/docs/getting-started/miniconda/main>`_ on your operating system. DEM is tested with the ``Conda`` environment provided in a file on `GitHub <https://github.com/HSLUDEM/District_Energy_Model>`_. Locate the file named ``dem_conda_environment_vX_Y_Z.yml`` (or similar) in the ``config`` directory. Make sure to use the correct version (e.g. ``dem_conda_environment_v0_1_0.yml`` for version ``0.1.0``).
Create a new Conda environment from this file:

.. code-block:: shell

    conda env create -f dem_conda_environment_vX_Y_Z.yml
    conda activate dem_X_Y_Z

Refer to the `Conda documentation <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file>`_ for instructions. If you are unfamiliar with Conda, consult the `user guide <https://docs.conda.io/projects/conda/en/latest/user-guide/index.html>`_.


**Step 2: Install the District Energy Model**

After activating the environment, install DEM with ``pip``:

.. code-block:: shell

    pip install district_energy_model


Now you can run the model (see :doc:`run_model`).


