.. _running_a_simulation:

Running a Simulation
====================

The model requires *configuration files* (:doc:`input_configuration`) and *data files* (:doc:`input_data`) to run. In a dedicated project directory (e.g., ``project_dir``), create the following folder structure:

.. code-block:: text

	project_dir/
	├── config/
	│   └── config_files/
	│       └── ...
	└── data/
	    └── ...

Place the *configuration files* in the ``config/config_files`` directory. A set of *configuration files* is provided on |GitHub_configfiles_link|, from where they can be downloaded.

Place the *data files* in the ``data`` directory. *Data files* for Switzerland are provided on |Zenodo_link|. The data package already has the correct directory structure and can be placed in the ``data`` directory (unzipping required). Make sure that the version of the Zenodo data package matches the DEM version you are using. For regions other than Switzerland, data must be created according to the format described in :doc:`input_data`.
 
..
	The model requires configuration files (:doc:`input_configuration`) and data files (:doc:`input_data`) to run. In a dedicated project directory, create a ``config/config_files`` directory where you place the configuration files and a ``data`` directory where you place the data files (see structure below). A set of YAML configuration files is provided on |GitHub_configfiles_link|. Data files for Switzerland are provided on |Zenodo_link|. The data package already has the correct directory structure and can be placed in the ``data`` directory (unzipping required). Make sure that the version of the Zenodo data package matches the DEM version you are using. For regions other than Switzerland, data must be created according to the format described in :doc:`input_data`.

	.. code-block:: text

		project_dir/
		├── config/
		│   └── config_files/
		│       └── ...
		└── data/
			└── ...

DEM can be run three different ways:

- Using the command-line interface: for running simulations without writing any Python code.
- Interactively in a Python environment: by importing the ``district_energy_model`` package in a script or notebook.
- Directly from the source code: by executing the provided Python modules within the project repository.


Run from command-line tool
-----------

**Step 1: Activate the Conda Environment**

Open the command-line tool and activate the DEM Conda environment (exact name depends on installed version):
	
.. code-block:: shell

    conda activate dem_0_1_0_rc0

**Step 2: Configure the Simulation**

If not already done, adapt the configuration files as described in :doc:`input_configuration` and place them in the ``config/config_files`` directory.


**Step 3: Run the Simulation**

Run DEM from the command line with the following command:

.. code-block:: shell

    district_energy_model --project_dir=/path/to/project

Specifying a project directory using ``--project_dir`` is optional. If not provided, DEM uses the current working directory. The ``project_dir`` should contain both ``data/`` and ``config/config_files`` directories.  
Simulation results will be stored inside the selected project directory. DEM will automatically create a directory named ``dem_output`` containing output files.


.. _run_in_Python:

Run programmatically in Python
------------------------------

DEM can also be launched directly from a Python script, which allows the model to be integrated into larger Python workflows or other projects. A minimal example looks as follows:

.. code-block:: python

    import district_energy_model as dem

    my_model = dem.model.launch()

In this example, the ``district_energy_model`` module is first imported. The second line creates and runs a model instance using the default configuration. By default, the ``data`` and ``config`` directories are expected to reside in the same root directory as the Python script. If they are stored elsewhere, the directory can be specified via the ``root_dir=...`` argument in the ``launch()`` method. The model configuration is read from the YAML configuration files unless otherwise specified.

Once launched, results can be retrieved from the model instance (``my_model``):

.. code-block:: python

    res_hourly = my_model.hourly_results()
    res_annual = my_model.annual_results()
    res_cost = my_model.total_cost()

The content of the output is described under :doc:`output`.

- ``hourly_results()`` returns a ``DataFrame`` with hourly time series of energy and resource flows.
- ``annual_results()`` returns a ``dict`` containing annual aggregated values.
- ``total_cost()`` returns a ``dict`` containing cost information (currently only available for optimisation runs), including monetary costs and emissions.

Instead of using YAML configuration files, input can also be supplied directly to the ``launch()`` method via a Python dictionary. This is useful when configuration values depend on preceding computations or when parameter studies are generated programmatically.

The following example shows how to run DEM with configuration input passed directly in Python:

.. code-block:: python
    
    import district_energy_model as dem
    
    # Adjust input configuration:
    config_dict = {
    	'simulation':{
    		'number_of_days':365,
    		'district_number':2762,
    		},
    	'scenarios':{
    		'demand_side':True,
    		'pv_integration':True,
    		},
    	'heat_pump':{
    		'deployment':True,
    		},
    	'district_heating':{
    		'deployment':True,
    		},
    	'solar_pv':{
    		'potential_integration_factor':0.7,
    		},        
    	}
    
    # Create and run model:
    my_model = dem.model.launch(
    	root_dir = './',
    	config_files = False,
    	config_dict = config_dict
    	)
    
    # Retrieve results:
    res_hourly = my_model.hourly_results()
    res_annual = my_model.annual_results()
    res_cost = my_model.total_cost()

Here, configuration input is passed directly to ``launch()`` via ``config_dict``. All values provided in ``config_dict`` override the corresponding default configuration. With the exception of technology parameters, the structure of ``config_dict`` matches the structure of the YAML configuration files (see :doc:`input_configuration`). The name of the respective configuration file serves as the top-level dictionary key. For technologies, the technology names themselves are used as top-level keys.

When configuration is supplied programmatically, the argument ``config_files`` must be set to ``False`` (the default is ``True``). The ``root_dir`` argument specifies the directory containing the ``data`` folder with all required input files (see :doc:`input_data`).

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


.. Links:

.. |Zenodo_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Zenodo</a>

.. |GitHub_configfiles_link| raw:: html

   <a href="https://github.com/HSLUDEM/District_Energy_Model/tree/main/config/config_files" target="_blank">GitHub</a>

