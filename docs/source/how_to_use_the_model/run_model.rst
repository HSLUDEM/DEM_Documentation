Running a Simulation
====================


Run from command-line tool
-----------

*Work in progress*


Run from source code
--------------------

You can run the District Energy Model directly from the Python source code available on `GitHub <https://github.com/HSLUDEM/District_Energy_Model>`_. Python and the required packages must be installed beforehand.


**Step 1: Clone the Repository**

Clone the GitHub repository to a local directory:

.. code-block:: shell

    git clone https://github.com/HSLUDEM/District_Energy_Model.git

Keep the directory structure exactly as cloned. See :doc:`directory_structure` for details.


**Step 2: Create the Conda Environment**

In the config directory, locate the file named ``dem_conda_environment.yml`` (or similar).
Create a new Conda environment from this file. Refer to the `Conda documentation <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-from-an-environment-yml-file>`_ Conda for instructions.
If you are unfamiliar with Conda, consult the `user guide <https://docs.conda.io/projects/conda/en/latest/user-guide/index.html>`_.


**Step 3: Prepare Data Files**

Place the required input data in the directories described in :doc:`input_data`.

.. note::

   A complete Switzerland-wide data package for DEM simulations is currently in preparation and will be made available soon. This will eliminate the need for users to assemble their own datasets. In the meantime, please reach out to us (:doc:`../contact`) to request access to the data.



**Step 3: Configuation Files**

The model can run without configuration files, in which case default settings and parameter values are applied. The default scenario performs a basic simulation without optimisation or additional scenarios.
To modify model parameters, create configuration files as described in :doc:`input_configuration` and place them in the ``config/input_files`` directory.


**Step 4: Run the Simulation**

Execute the Python script ``src/run_dem.py`` either:

- from an IDE (e.g., Spyder, Visual Studio Code), or

- from a terminal window.


**Step 5: Retrieve Results**

Simulation results are saved automatically to the specified output directory. See :doc:`output` for details on output files and structure.

