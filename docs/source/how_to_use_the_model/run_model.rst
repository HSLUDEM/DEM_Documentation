Running a Simulation
====================

The model requires configuration files (:doc:`input_configuration`) and data files (:doc:`input_data`) to run. In a dedicated project directory, create a ``config`` directory where you place the configuration files and a ``data`` directory where you place the data files. A set of configuration files is provided on `GitHub <https://github.com/HSLUDEM/District_Energy_Model/tree/main/config/config_files>`_. Data files for Switzerland are provided on `Zenodo  <https://doi.org/10.5281/zenodo.17603138>`_. The data package already has the correct directory structure and can be placed in the ``data`` directory (unzipping required). Make sure that the version of the Zenodo data package matches the DEM version you are using.


Run from command-line tool
-----------

**Step 1: Activate the Conda Environment**

Open the command-line tool and activate the DEM Conda environment:

.. code-block:: shell

    conda activate dem_X_Y_Z

**Step 2: Run a Simulation**

.. code-block:: shell

    district_energy_model --project_dir=/path/to/project

Specifying a project directory using --project is optional. If not provided, DEM uses the current working directory. The ``project_dir`` should contain both ``data/`` and ``config/`` directories.  
Simulation results will be stored inside the selected project directory. DEM will automatically create a directory named ``dem_output`` containing output files.



.. _run_model_from_source:

Run from source code
--------------------

You can run the District Energy Model directly from the Python source code available on `GitHub <https://github.com/HSLUDEM/District_Energy_Model>`_. Python and the required packages must be installed beforehand.


**Step 1: Clone the Repository**

Clone the GitHub repository to a local directory:

.. code-block:: shell

    git clone https://github.com/HSLUDEM/District_Energy_Model.git

Keep the directory structure exactly as cloned. See :doc:`directory_structure` for details.


**Step 2: Create and Activate the Conda Environment**

(See Step 1 in :doc:`installation`)


**Step 3: Prepare Data Files**

Place the required input data in the directories described above and in :doc:`input_data`.


**Step 3: Configuation Files**

Create configuration files as described in :doc:`input_configuration` and place them in the ``config/config_files`` directory.


**Step 4: Run the Simulation**

Execute the Python script ``src/run_dem_local.py`` either:

- from an IDE (e.g., Spyder, Visual Studio Code), or

- from a terminal window.


**Step 5: Retrieve Results**

Simulation results are saved automatically to the root directory. DEM will automatically create a directory named ``dem_output`` containing output files. See :doc:`output` for details on output files and structure.

