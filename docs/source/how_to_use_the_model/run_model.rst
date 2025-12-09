Running a Simulation
====================

The model requires configuration files (:doc:`input_configuration`) and data files (:doc:`input_data`) to run. In a dedicated project directory, create a ``config/config_files`` directory where you place the configuration files and a ``data`` directory where you place the data files (see structure below). A set of YAML configuration files is provided on `GitHub <https://github.com/HSLUDEM/District_Energy_Model/tree/main/config/config_files>`_. Data files for Switzerland are provided on `Zenodo  <https://doi.org/10.5281/zenodo.17603138>`_. The data package already has the correct directory structure and can be placed in the ``data`` directory (unzipping required). Make sure that the version of the Zenodo data package matches the DEM version you are using. For regions other than Switzerland, data must be created according to the format described in :doc:`input_data`.

.. code-block:: text

	project_dir/
	├── config/
	│   └── config_files/
	│       └── ...
	└── data/
	    └── ...

..
	.. code-block:: text

		project_dir/
		├── config/
		│   ├── config_files/
		│   │   ├── demand_side.yaml
		│   │   ├── meta_data.yaml
		│   │   ├── optimisation.yaml
		│   │   ├── scenarios.yaml
		│   │   ├── simulation.yaml
		│   │   ├── supply.yaml
		│   │   └── technologies.yaml
		│   └── dem_conda_environment.yml
		└── data/
			├── community_data/
			│   └── ...
			├── electricity_demand/
			│   └── ...
			├── electricity_mix_national/
			│   └── electricity_mix.feather
			├── heat_demand/
			│   └── DHW_Profile.feather
			├── master_data/
			│   ├── HDD_and_HDH_profiles/
			│   │   ├── HDD_Municipality_2023.feather
			│   │   ├── HDD_Municipality_2030.feather
			│   │   ├── HDD_Municipality_2040.feather
			│   │   ├── HDD_Municipality_2050.feather
			│   │   └── ...
			│   └── simulation_data/
			│       ├── df_master_sim.feather
			│       ├── meta_file_2.feather
			│       ├── simulation_profiles_file.feather
			│       └── ...
			├── tech_wind_power/
			│   ├── profiles/
			│   │   └── ...
			│   └── p_installed_kW_wind_power.feather
			└── weather_data/
				└── com_files/
					└── ...

DEM can be run three different ways:
- Using the command-line interface: for running simulations without writing any Python code.
- Interactively in a Python environment: by importing the district_energy_model package in a script or notebook.
- Directly from the source code: by executing the provided Python modules within the project repository.


Run from command-line tool
-----------

**Step 1: Activate the Conda Environment**

Open the command-line tool and activate the DEM Conda environment:

.. code-block:: shell

    conda activate dem_X_Y_Z

**Step 2: Configure the Simulation**

Adapt the configuration files as described in :doc:`input_configuration` and place them in the ``config/config_files`` directory.


**Step 3: Run the Simulation**

Run the DEM from the command line with the following command:

.. code-block:: shell

    district_energy_model --project_dir=/path/to/project

Specifying a project directory using ``--project_dir`` is optional. If not provided, DEM uses the current working directory. The ``project_dir`` should contain both ``data/`` and ``config/config_files`` directories.  
Simulation results will be stored inside the selected project directory. DEM will automatically create a directory named ``dem_output`` containing output files.


.. _run_in_Python:

Run programmatically in Python
------------------------------

DEM can be launched from within a Python script, which allows the model to be integrated into other Python projects. A minimally required code to launch DEM in a Python environment looks as follows:

.. code-block:: python

    import district_energy_model as dem

    my_model = dem.model.launch()

In above code, the ``district_energy_model`` module is imported first. The second line creates and runs a model instance. The ``data`` and ``config`` directories are assumed to be in the same root directory as the Python script from which DEM is launched. Alternatively, another directory can be specified with the ``root_dir=...`` argument in the ``launch()`` method. In above example, the model configuration is read from the configuration files. Results can be retrieved from the created model instance (``my_model``):

.. code-block:: python

    res_hourly = my_model.hourly_results()
    res_annual = my_model.annual_results()
    res_cost = my_model.total_cost()

The content of the output is described under :doc:`output`. ``hourly_results()`` returns a dataframe containing hourly timeseries of the resulting energy and resource flows. ``annual_results()`` returns a ``dict`` containing annual values of the same data. ``total_cost()`` contains resulting cost data, including monetary cost and emissions (currently only available for optimisations).

Instead of using YAML configuration files, input can also be passed directly to the ``launch()`` method within Python. This can for example be useful when technology or simulation parameters are taken from a preceding Python routine. Here is an example of how to run DEM when passing configuration info to the model directly in Python:

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

In above code, the configuration input is directly passed to the ``launch()`` method via the ``config_dict`` argument. Values contained in the ``config_dict`` dictionary replace the standard input values. Except for technology configurations, all data in ``config_dict`` is specified the same way as it would be specified in the YAML configuration files (see :doc:`input_configuration`) with the name of the respective file being used as a top-level key in the dictionary. For technologies, the name of the technologies are used directly as top-level keys.

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

