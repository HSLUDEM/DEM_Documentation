.. _tutorial_1:

Tutorial 1: Swiss Municipality
===================

.. note::
*UNDER CONSTRUCTION*

This tutorial builds a district energy simulation for the Swiss municipality of |Allschwil_Wikipedia_link|, located in the canton of Basel-Landschaft. Two scenarios are defined:

1. **Baseline (“as-is”)**: current energy demand and supply configuration.

2. **Electrification scenario**: heating electrification, solar PV deployment, and thermal energy storage.

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

For the baseline simulation, all default model parameters are used. Only the file ``simulation.yml`` is required.

Create ``simulation.yml`` with the following content:

.. code-block:: yaml

    number_of_days: 365
    district_number: 2762
    generate_plots: true
    save_results: true
	
Parameter definitions:

- ``number_of_days``: full-year simulation horizon.

- ``district_number``: |bfs_number_link| (2762 corresponds to Allschwil).

- ``generate_plots``: activates automatic plot generation.

- ``save_results``: writes numrical outputs to file.

Place ``simulation.yml`` in ``config/config_files``.

Running the simulation
---------

Open an Anaconda prompt and navigate to ``project_dir``.
Activate the DEM environment (name depends on the installed version):

.. code-block:: shell

    conda activate dem_0_1_0_rc0

Start the simulation:

.. code-block:: shell

    district_energy_model

Outputs
---------

After completion, DEM creates a dem_output directory inside project_dir.
This directory contains result files and generated plots.

Embedded examples:

.. raw:: html
    :file: tutorial_1_plots/electricity_balance_daily.html

.. raw:: html
    :file: tutorial_1_plots/heat_balance_daily.html




.. Links:

.. |Allschwil_Wikipedia_link| raw:: html

   <a href="https://en.wikipedia.org/wiki/Allschwil" target="_blank">Allschwil</a>
   
   
.. |Swiss_data_Zenodo_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Zenodo</a>
   
.. |bfs_number_link| raw:: html

   <a href="https://www.bfs.admin.ch/bfs/de/home/grundlagen/agvch.html" target="_blank">BFS municipality identifier</a>
   
   
.. code-block:: bash

     district_energy_model bash
	 
.. code-block:: sh

     district_energy_model sh
	 
.. code-block:: console

     district_energy_model console
	 
.. code-block:: powershell

     district_energy_model powershell
	 
.. code-block:: cmd

     district_energy_model cmd
	 
.. code-block:: zsh

     district_energy_model zsh
	 
.. code-block:: fish

     district_energy_model fish
	 
.. code-block:: shell

     district_energy_model shell