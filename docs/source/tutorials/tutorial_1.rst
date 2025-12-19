.. _tutorial_1:

Tutorial 1: Swiss Municipality
===================

.. note::
  *UNDER CONSTRUCTION*

This example creates a simulation for the Swiss municipality of |Allschwil_Wikipedia_link|, which is a village in the canton of Basel-Landschaft in Switzerland. We simulate the current demand and energy system (i.e., "as-is"), as well as a scenario consisting of heating electrification, solar PV integration, and thermal energy storage. No optimisation is applied.

First, install DEM as described in the :ref:`installation instructions <installation>`. Create a directory structure as described in :ref:`running_a_simulation`: Your project directory ``project_dir`` (can have any name) must contain the subdirectories ``data`` and ``config/config_files``.

Next you need data files and configuration files. Download the data files package for Switzerland from |Swiss_data_Zenodo_link|. Unzip the archive and place the files in the ``config_files`` directory, keeping the folder structure as downloaded from Zenodo.

Next, we prepare the configuration files. For the first simulation ("as-is") we use all the standard parameters. Therefore, only the ``simulation.yml`` file must be provided to DEM:


.. code-block:: yaml

    number_of_days: 365
    district_number: 2762
    generate_plots: true
    save_results: true

We simulate 365 days for the municipality with ``district_number`` 2762, which refers to the |bfs_number_link| for Allschwil. We want the model to generate plots at the end of the simulation (``generate_plots: true``) and also save the resulting values (``save_results: true``). Place this file (``simulation.yml``) in the ``config_files`` directory.

Open the Anaconda prompt and navigate to the ``project_dir``. Activate the environment you installed for DEM (environment name might vary based on the installed DEM version):

.. code-block:: shell

    conda activate dem_0_1_0_rc0
	
Start the simulation:

.. code-block:: shell

    district_energy_model

Once the simulation is completed, you can find the new directory ``dem_output`` which was created by DEM in ``project_dir`` containing plots and results files.




.. Links:

.. |Allschwil_Wikipedia_link| raw:: html

   <a href="https://en.wikipedia.org/wiki/Allschwil" target="_blank">Allschwil</a>
   
   
.. |Swiss_data_Zenodo_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Zenodo</a>
   
.. |bfs_number_link| raw:: html

   <a href="https://www.bfs.admin.ch/bfs/de/home/grundlagen/agvch.html" target="_blank">BFS number</a>
   
