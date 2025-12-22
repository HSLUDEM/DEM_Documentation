.. _tutorial_2:

Tutorial 2: Customised District
===================

.. note::
  *UNDER CONSTRUCTION*
  
This tutorial builds a district energy simulation for a small district of 30 buildings (mostly residential). While in :ref:`Tutorial 1 <tutorial_1>` the model considered the whole municipality of |Allschwil_Wikipedia_link|, this example looks at a few selected buildings of the same municipality (see figure below).

.. image:: images/district.png
   :width: 80%

The same two scenarios as in `Tutorial 1 <tutorial_1>` are considered, the only difference being the size of the thermal energy storage system:

1. **Baseline scenario**: Current energy demand and supply configuration.

2. **Electrification scenario**:

   - Heating electrification: Replacement of 80% of existing fossil-based heating systems (oil and gas boilers) with heat pumps.
   - Solar PV integration: Deployment of 80% of the remaining rooftop solar photovoltaic potential.
   - Thermal energy storage: Implementation of decentralised thermal energy storage systems with a total storage capacity of 30 MWh, charged and discharged by heat pumps.

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

.. code-block:: yaml

    custom_district:
        implemented: true
        EGID_List: [2348043, 245063143, 2348044, 2348045, 391986, 391987, 391988, 391989, 391993, 391990, 391994, 245025839, 245025840, 391992, 245025841, 245025842, 391995, 391996, 391997, 2348046, 3029563, 391998, 245046103, 391999, 245025843, 245045313, 245046052, 392000, 245027525, 3029067]
        custom_district_name: 'tutorial_2_district'

The EDIG numbers for each building are obtained from https://map.geo.admin.ch/.

.. code-block:: yaml

    oil_boiler:
        replacement_factor: 0.8
        
    gas_boiler:
        replacement_factor: 0.8
    
    solar_pv:
        potential_integration_factor: 0.8
        
    tes_decentralised:
        deployment: true
        capacity_kWh: 30000
		
		
		
.. Links:

.. |Allschwil_Wikipedia_link| raw:: html

   <a href="https://en.wikipedia.org/wiki/Allschwil" target="_blank">Allschwil</a>
   
   
.. |Swiss_data_Zenodo_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Zenodo</a>
   
   
.. |bfs_number_link| raw:: html

   <a href="https://www.bfs.admin.ch/bfs/de/home/grundlagen/agvch.html" target="_blank">BFS municipality identifier</a>