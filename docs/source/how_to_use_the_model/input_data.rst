Model Input - Data Files
========================

Time series data, as well as information about buildings and districts, are provided to the District Energy Model (DEM) through data files. Most of these files are stored in Feather format (Apache Software Foundation, 2025).  

This section describes the required files, their contents, and the expected data formats. Although all files must be present for the simulation to run, their entries can be set to zero if a dataset is not relevant to a specific case (for example, the wind power file if wind generation is excluded from the scenario).

..
  .. note::

     A full Switzerland-wide data package for DEM simulations is currently in preparation and will be made available soon. This will eliminate the need for users to assemble their own datasets. In the meantime, please reach out to us (:doc:`../contact`) to request access to the data.

All input files must be located within the ``data`` directory following the predefined directory structure (see below).

.. note::
  For Switzerland, a complete dataset package is available on `Zenodo  <https://doi.org/10.5281/zenodo.17603138>`_. After downloading and unzipping the archive, place its contents in the ``data`` directory of your project. The required directory structure is already included.


.. code-block:: text

    District_Energy_Model/
    ├── config/
    │   ├── ...
    │   └── ...
    ├── data/
    │   ├── community_data/
    │   │   └── ...
    │   ├── electricity_demand/
    │   │   └── ...
    │   ├── electricity_mix_national/
    │   │   └── electricity_mix.feather
    │   ├── heat_demand/
    │   │   └── DHW_Profile.feather
    │   ├── master_data/
    │   │   ├── HDD_and_HDH_profiles/
    │   │   │   ├── HDD_Municipality_2023.feather
    │   │   │   ├── HDD_Municipality_2030.feather
    │   │   │   ├── HDD_Municipality_2040.feather
    │   │   │   ├── HDD_Municipality_2050.feather
    │   │   │   └── ...
    │   │   └── simulation_data/
    │   │       ├── df_master_sim.feather
    │   │       ├── meta_file_2.feather
    │   │       ├── simulation_profiles_file.feather
    │   │       └── ...
    │   ├── tech_wind_power/
    │   │   ├── profiles/
    │   │   │   └── ...
    │   │   └── p_installed_kW_wind_power.feather
    │   └── weather_data/
    │       └── com_files/
    │           └── ...
    ├── doc/
    │   ├── ...
    │   └── ...
    ├── src/
    │   ├── ...
    │   └── ...
    ├── LICENSE.txt
    └── README.md


Master File
-----------

This file contains information about each individual building, with one row per building. District-level information is derived from this file through aggregation. The file may include data for multiple districts; during a simulation, only the buildings belonging to the specified district are selected.  

Each building is identified by a unique identification number (column 0: ``EGID``) and assigned to a municipality represented by a numerical code (column 4: ``GGDENR``). Custom districts can also be analyzed by specifying the buildings included in the district via their ``EGID`` values.  

For Switzerland, data in columns 0 to 15 is sourced from the *Federal Register of Buildings and Dwellings (RBD)* (Federal Statistical Office, 2025), and the corresponding column naming conventions have been adopted accordingly.

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/master_file_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/master_file_columns.rst


Meta file
-----------
This file contains information about each district, with one row per district. Some of the data can be derived as an aggregate from the *Master File*.  

The district identification number (column 1: ``GGDENR``) must match the corresponding municipality code of the buildings listed in the *Master File*.

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/meta_file_2_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/meta_file_2_columns.rst


Simulation profiles
-------------------
This file contains hourly profiles for an entire year (i.e., 8760 hours) representing various generation and demand metrics at national and regional levels.  

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/simulation_profiles_file_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/simulation_profiles_file_columns.rst


Temperatures
------------
These files contains hourly temperature data for an entire year (i.e., 8760 hours) across multiple years (i.e., one column per year). One file must be provided per district, where the temperature values represent spatial averages over the district area.

Past years include historical measurements from monitoring stations, while future years contain projected values based on climate scenarios (see also :ref:`climate-adjustment`).

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/temperature_file_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/temperature_file_columns.rst


DHW profile
-----------
This file contains an hourly domestic hot water (DHW) demand profile for an entire year (i.e., 8760 hours). The profile is normalised to 1 and can be scaled according to the annual DHW demand of the district or building.

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/dhw_profile_file_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/dhw_profile_file_columns.rst


Wind power capacity
-------------------
This file contains the currently installed wind power capacity (in kW) for each municipality.

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/wind_power_cap_file_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/wind_power_cap_file_columns.rst


Wind power profiles
-------------------
These files contain normalised hourly wind power generation profiles aggregated at the municipal level. For each municipality, two files are provided: one representing profiles optimised for maximum annual generation, and another optimised for maximum winter generation.

For Switzerland, the Wind-Topo dataset is used (Dujardin and Lehning, 2022a and 2022b).

*in progress*

National electricity mix
------------------------
This file contains hourly profiles of the national electricity mix. The data include the hourly contribution of each generation technology and are used to create normalised profiles of national electricity generation technologies.

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/electricity_mix_file_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/electricity_mix_file_columns.rst


HDD Profiles
------------
These files contain the number of heating degree days (HDD) per year for each municipality, calculated for base temperatures of 12 °C and 15 °C. Each file corresponds to one simulation year, and each row represents a single municipality.

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/hdd_file_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/hdd_file_columns.rst


EV demand profiles
------------------
For Switzerland, the dataset by Herrera and Hug (2025a; 2025b) is used to model hourly EV charging demand and daily flexibility.

*in progress*


References
-----------

Apache Software Foundation. (2025). *Feather file format (Apache Arrow)*. https://arrow.apache.org/docs/python/feather.html

Dujardin, J., Lehning, M. (2022a). *Wind-Topo_model*. EnviDat. https://www.doi.org/10.16904/envidat.301.

Dujardin, J., & Lehning, M. (2022b). *Wind‐Topo: Downscaling near‐surface wind fields to high‐resolution topography in highly complex terrain with deep learning*. Quarterly Journal of the Royal Meteorological Society, 148(744), 1368-1388. https://doi.org/10.1002/qj.4265

Parajeles Herrera, M., & Hug, G. (2025a). *Charging Demand and Flexibility Bounds for Large-Scale BEV Fleets - The Case Study of Switzerland* [Data set]. Zenodo. https://doi.org/10.5281/zenodo.16597426

Herrera, M. P., & Hug, G. (2025b). *Modeling Charging Demand and Quantifying Flexibility Bounds for Large-Scale BEV Fleets*. arXiv preprint arXiv:2504.03633. https://doi.org/10.48550/arXiv.2504.03633

Federal Statistical Office (FSO). (2025). *Federal register of buildings and dwellings (RBD)*. https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html
