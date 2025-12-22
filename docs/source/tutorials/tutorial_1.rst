.. _tutorial_1:

Tutorial 1: Swiss Municipality
===================

This tutorial builds a district energy simulation for the Swiss municipality of |Allschwil_Wikipedia_link|, located in the canton of Basel-Landschaft. Two scenarios are defined and simulated:

1. **Baseline scenario**: Current energy demand and supply configuration.

2. **Electrification scenario**:

   - Heating electrification: Replacing 80% of current fossil heaters (oil and gas boilers) with heat pumps.
   - Solar PV integration: Deploying 80% of the remaining rooftop solar photovoltaic potential.
   - Thermal energy storage: Implementing thermal energy storage systems with a total storage capacity of 20Gwh supplied by decentralised heat pumps.

No optimisation is performed.

Prerequisites
---------

Install DEM following the :ref:`installation instructions <installation>`.
Create a project directory (arbitrary name, referred to as ``project_dir``) with the structure described in :ref:`running_a_simulation`, containing the following sub-directories:

- ``project_dir/data``

- ``project_dir/config/config_files``

Data setup
---------

Download the Swiss input data package from |Swiss_data_Zenodo_link|.
Extract the archive and copy its contents into the ``data`` directory, preserving the original folder hierarchy as downloaded from Zenodo.


Configuration: baseline scenario
---------

For the baseline simulation, all default model parameters are used. Therefore, only the file ``simulation.yml`` is required.

Create ``simulation.yml`` with the following content:

.. code-block:: yaml

    number_of_days: 365
    district_number: 2762
    generate_plots: true
    save_results: true
	
Parameter definitions:

- ``number_of_days``: full-year simulation horizon (i.e., 365 days).

- ``district_number``: |bfs_number_link| (2762 corresponds to Allschwil).

- ``generate_plots``: activates automatic plot generation.

- ``save_results``: writes numerical outputs to file.

Place ``simulation.yml`` in ``config/config_files``.

Running the simulation: baseline scenario
---------

Open an Anaconda prompt and navigate to ``project_dir``.
Activate the DEM environment (name depends on the installed version):

.. code-block:: shell

    conda activate dem_0_1_0_rc0

Start the simulation:

.. code-block:: shell

    district_energy_model

Outputs: baseline scenario
---------

After completion, DEM creates a ``dem_output`` directory inside ``project_dir``.
This directory contains result files and generated plots.

Below you find some of the outputs provided as interactive plots:

.. raw:: html
    :file: tutorial_1_baseline_plots/electricity_balance_daily.html

.. raw:: html
    :file: tutorial_1_baseline_plots/heat_balance_daily.html
	
.. raw:: html
    :file: tutorial_1_baseline_plots/sankey.html
	
	
Configuration: electrification scenario
---------

For the electrification simulation, some of the default parameters must be customised. The content of the file ``simulation.yml`` remains the same as in the baseline scenario:

.. code-block:: yaml

    number_of_days: 365
    district_number: 2762
    generate_plots: true
    save_results: true

In order to activate the three measures *heating electrification*, *solar PV integration*, and *thermal energy storage*, create the :ref:`scenario configuration file <scenarios>` ``scenarios.yml`` as follows:

.. code-block:: yaml

    fossil_heater_retrofit: true
    pv_integration: true
    thermal_energy_storage: true

For these measures to be implemented, the respective technologies must be adapted as well. Only the values deviating from the default values must be provided. *Heating electrification* means the replacement of 80% of currently installed oil boilers and gas boilers with heat pumps. *Solar PV integration* means the use of 80% of the remaining rooftop solar photovoltaic potential. *Thermal energy storage* (TES) refers to the implementation of decentralised TES systems that are charged and discharged via the individual heat pumps.

Only technology parameter values deviating from the default values must be provided. Create the :ref:`technologies configuration file <technologies_config_file>` as follows:

.. code-block:: yaml

    oil_boiler:
        replacement_factor: 0.8
    
    gas_boiler:
        replacement_factor: 0.8

    solar_pv:
        potential_integration_factor: 0.8
    
    tes_decentralised:
        deployment: true
        capacity_kWh: 20000000

The :ref:`heat pump technology <tech_heat_pump>` is already deployed in the baseline scenario by default. Therefore, no changes are required and it doesn't have to appear in the technologies configuration file. The following technologies are adapted:

- ``oil_boiler``: The :ref:`oil boiler technology <tech_oil_boiler>` is deployed by default, so the ``deployment`` parameter is not required. However, by default the ``replacement_factor`` is set to 1. Here it is changed to 0.8.

- ``gas_boiler``: The :ref:`gas boiler technology <tech_gas_boiler>` is also deployed by default, so the ``deployment`` parameter is not required. However, by default the ``replacement_factor`` is set to 1. Here it is changed to 0.8.

- ``solar_pv: The :ref:`solar PV technology <tech_solar_pv>` is also deployed by default, so the ``deployment`` parameter is not required. However, by default the ``potential_integration_factor`` is set to 0.3. Here it is changed to 0.8.

- ``tes_decentralised``: The :ref:`decentralised thermal energy storage (tes) technology <tech_tes_decentralised>` is deactivated by defaults. Therefore, the ``deployment`` parameter is set to ``true``. The storage capacity value is defined with the ``capacity_kWh`` parameter. Here it is set to 20 GWh (i.e., 20'000'000 kWh).

Running the simulation: electrification scenario
---------

The simulation is run the same way as in the baseline scenario. Open an Anaconda prompt and navigate to ``project_dir``.
Activate the DEM environment (name depends on the installed version):

.. code-block:: shell

    conda activate dem_0_1_0_rc0

Start the simulation:

.. code-block:: shell

    district_energy_model

Outputs: electrification scenario
---------

After completion, DEM creates a ``dem_output`` directory inside ``project_dir``.
This directory contains result files and generated plots.

Below you find some of the outputs provided as interactive plots:

.. raw:: html
    :file: tutorial_1_electrification_plots/electricity_balance_daily.html

.. raw:: html
    :file: tutorial_1_electrification_plots/heat_balance_daily.html
	
.. raw:: html
    :file: tutorial_1_electrification_plots/sankey.html




.. Links:

.. |Allschwil_Wikipedia_link| raw:: html

   <a href="https://en.wikipedia.org/wiki/Allschwil" target="_blank">Allschwil</a>
   
   
.. |Swiss_data_Zenodo_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Zenodo</a>
   
.. |bfs_number_link| raw:: html

   <a href="https://www.bfs.admin.ch/bfs/de/home/grundlagen/agvch.html" target="_blank">BFS municipality identifier</a>
   
   