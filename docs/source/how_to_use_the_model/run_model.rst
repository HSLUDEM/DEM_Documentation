Running a Simulation
====================


Run from command-line tool
-----------

*in progress*


Run from source code
--------------------

The model can be run directly from the Python source code found on `GitHub <https://github.com/HSLUDEM/District_Energy_Model>`_. For this purpose, you must install Python along with the respective packages. You can follow these steps:


**Step 1: Clone repository**

Clone the District_Energy_Model GitHub repository to a local directory:

.. code-block:: shell

    git clone https://github.com/HSLUDEM/District_Energy_Model.git

The :doc:`directory_structure` should be kept as cloned from GitHub.


**Step 2: Conda environment**

You will find a YAML file in the ``config`` directory named ``dem_conda_environment_X.yml`` or similar. Using this file, create a new Conda environment. Instructions on how to create a Conda environment from file can be found `here <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file>`_. If you're not familiar with Conda, take a look at this `user guide <https://docs.conda.io/projects/conda/en/latest/user-guide/index.html>`_.


**Step 3: Data files**

Place all the required data files in the respective directories as described here: :doc:`input_data`.

.. note::

   A full Switzerland-wide data package for DEM simulations is currently in preparation and will be made available soon. This will eliminate the need for users to assemble their own datasets. In the meantime, please reach out to us (:doc:`../contact`) to request access to the data.



**Step 3: Configuation files**

The model doesn't need any configuration files to run a simulation. In this case, standard values will be used. The standard scenario carries out a simulation without optimisation and without any additional scenario. To change parameters in the model, configuration files must be created as described here: :doc:`input_configuration`. These files must be placed in the ``config/input_files`` directory.

**Step 4: Run simulation**

To start a simulation, the Python script ``src/run_dem.py`` must be executed. This can be done via an IDE (e.d., Spyder, Visual Studio, etc...) or from the terminal.

**Step 5: Save results**

The results (various files) will be save automatically to the specified directory. More information about the model output can be found here: :doc:`output`.


