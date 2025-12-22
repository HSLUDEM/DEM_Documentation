.. _tutorial_1:

Tutorial 1: Swiss Municipality
===================

This tutorial builds a district energy simulation for the Swiss municipality of |Allschwil_Wikipedia_link|, located in the canton of Basel-Landschaft. Two scenarios are defined and simulated:

1. **Baseline scenario**: Current energy demand and supply configuration.

2. **Electrification scenario**:

   - Heating electrification: Replacement of 80% of existing fossil-based heating systems (oil and gas boilers) with heat pumps.
   - Solar PV integration: Deployment of 80% of the remaining rooftop solar photovoltaic potential.
   - Thermal energy storage: Implementation of decentralised thermal energy storage systems with a total storage capacity of 20 GWh, charged and discharged by heat pumps.

No optimisation is performed.

Prerequisites
---------

*(skip if already completed previously)*

Install DEM following the :ref:`installation instructions <installation>`.
Create a project directory (arbitrary name, referred to as ``project_dir``) with the structure described in :ref:`running_a_simulation`, containing the following sub-directories:

- ``project_dir/data``

- ``project_dir/config/config_files``

Data setup
---------

*(skip if already completed previously)*

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

Selected outputs for the *baseline scenario* are shown below as interactive plots:

.. raw:: html
    :file: tutorial_1_baseline_plots/electricity_balance_daily.html

.. raw:: html
    :file: tutorial_1_baseline_plots/heat_balance_daily.html
	
.. raw:: html
    :file: tutorial_1_baseline_plots/sankey.html
	
	
Configuration: electrification scenario
---------

For the electrification scenario, several default parameters are modified. The file ``simulation.yml`` remains identical to the baseline configuration:

.. code-block:: yaml

    number_of_days: 365
    district_number: 2762
    generate_plots: true
    save_results: true

In order to activate the three measures *heating electrification*, *solar PV integration*, and *thermal energy storage*, create the :ref:`scenario configuration file <scenarios>` ``scenarios.yml`` with the following content and place it in ``project_dir/config/config_files``:

.. code-block:: yaml

    fossil_heater_retrofit: true
    pv_integration: true
    thermal_energy_storage: true
	
Activating these measures requires corresponding adjustments to technology parameters:

- *Heating electrification* replaces 80% of installed oil and gas boilers with heat pumps.

- *Solar PV integration* activates the use of 80% of the remaining available rooftop PV potential.

- *Thermal energy storage* (TES) introduces decentralised storage systems operated in conjunction with individual heat pumps.

Only technology parameters that deviate from default values must be specified. Create the :ref:`technologies configuration file <technologies_config_file>` with the following content and place it in ``project_dir/config/config_files``:

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

The :ref:`heat pump technology <tech_heat_pump>` is already deployed by default in the baseline scenario. Therefore, no changes are required and it does not need to be included in the technologies configuration file.

The following technologies are modified:

- ``oil_boiler``: The :ref:`oil boiler technology <tech_oil_boiler>` is deployed by default, so the ``deployment`` parameter is omitted. The default ``replacement_factor`` of 1.0 is reduced to 0.8.

- ``gas_boiler``: The :ref:`gas boiler technology <tech_gas_boiler>` is deployed by default. As with oil boilers, the ``replacement_factor`` is reduced from 1.0 to 0.8.

- ``solar_pv``: The :ref:`solar PV technology <tech_solar_pv>` is deployed by default. The ``potential_integration_factor`` is increased from the default value of 0.3 to 0.8.

- ``tes_decentralised``: The :ref:`decentralised thermal energy storage technology <tech_tes_decentralised>` is disabled by default. It is activated by setting ``deployment`` to ``true``. The total storage capacity is defined using ``capacity_kWh`` and is set to 20 GWh (20'000'000 kWh).

Running the simulation: electrification scenario
---------

The simulation procedure is identical to the baseline scenario.

Open an Anaconda prompt and navigate to ``project_dir``.
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

Selected outputs for the *electrification scenario* are shown below as interactive plots:

.. raw:: html
    :file: tutorial_1_electrification_plots/electricity_balance_daily.html

.. raw:: html
    :file: tutorial_1_electrification_plots/heat_balance_daily.html
	
.. raw:: html
    :file: tutorial_1_electrification_plots/tesdc_sos_hourly.html
	
.. raw:: html
    :file: tutorial_1_electrification_plots/sankey.html


.. Links:

.. |Allschwil_Wikipedia_link| raw:: html

   <a href="https://en.wikipedia.org/wiki/Allschwil" target="_blank">Allschwil</a>
   
   
.. |Swiss_data_Zenodo_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Zenodo</a>
   
   
.. |bfs_number_link| raw:: html

   <a href="https://www.bfs.admin.ch/bfs/de/home/grundlagen/agvch.html" target="_blank">BFS municipality identifier</a>
   
   