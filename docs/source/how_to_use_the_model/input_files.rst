Model Input Files
================

Timeseries data, as well as information about buildings and districts is provided to DEM via input files. Most of the files are in feather format (Apache Software Foudnation, 2025). This section describes the required files, it's content, and required formats. Even though the files are required for the simulation to run, its entries can be set to 0 if the information is not relevant to a specific case (e.g. wind power file if no wind power is considered in the simulation).
All the input files must be placed in the ``data`` directory using the provided directory structure (see below).

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
    │   │       ├── meat_file_2.feather
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




Master file
-----------

File containing information about each individual building (one row per building). Information about the whole district is extractred from this file by means of aggregation. The file can contain information about multiple district. In a simulation, only the information about buildings for the specified district will be extracted. Each building has a unique identification number (column 0: EGID) and belongs to a municipality identified by a number (column 4: GGDENR). Custom district can also be analysed by specifying (via EGID) which buildings belong to the districts. For Switzerland, data in columns 0 to 15 is extracted from the Federal Register of Buildings and Dwellings (RBD) (Federal Statistical Office, 2025). The naming convention of these columns has been adopted accordingly.

.. csv-table::
	      :file: input_files_csv/master_file_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/master_file_columns.csv
	      :widths: auto
	      :header-rows: 1

Meta file
-----------
File containing information about districts (one row per district). Some of the data can be taken as an aggregate from the Master File or vice verca. The number of the district (column 1: GGDENR) must match with the respective buildings in the Master File.

.. csv-table::
	      :file: input_files_csv/meta_file_2_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/meta_file_2_columns.csv
	      :widths: auto
	      :header-rows: 1

Simulation profiles
-------------------
File containing hourly profiles across one year (i.e., 8760 hours) for various generation and demand metrics on national and regional level.

.. csv-table::
	      :file: input_files_csv/simulation_profiles_file_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/simulation_profiles_file_columns.csv
	      :widths: auto
	      :header-rows: 1

Temperatures
------------
File containing hourly temperature data across one year (i.e., 8760 hours) for different years. One file must be provided per district, where the temperatures are spatial averages across the district. Past years contain historic data from monitoring stations, whereas future years contain projected values based on climate scenarios (see also :ref:`climate-adjustment`).

.. csv-table::
	      :file: input_files_csv/temperature_file_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/temperature_file_columns.csv
	      :widths: auto
	      :header-rows: 1

DWH profile
-----------

.. csv-table::
	      :file: input_files_csv/dhw_profile_file_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/dhw_profile_file_columns.csv
	      :widths: auto
	      :header-rows: 1

Wind power capacity
-------------------

.. csv-table::
	      :file: input_files_csv/wind_power_cap_file_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/wind_power_cap_file_columns.csv
	      :widths: auto
	      :header-rows: 1

Wind power profiles
-------------------

*in progress*

National electricity mix
------------------------

.. csv-table::
	      :file: input_files_csv/electricity_mix_file_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/electricity_mix_file_columns.csv
	      :widths: auto
	      :header-rows: 1

HDD profiles
------------

.. csv-table::
	      :file: input_files_csv/hdd_file_info.csv
	      :widths: auto
	      :header-rows: 0
		  
.. csv-table::
	      :file: input_files_csv/hdd_file_columns.csv
	      :widths: auto
	      :header-rows: 1

EV demand profiles
------------------
*in progress*

References
----------

Apache Software Foundation. (2025). *Feather file format (Apache Arrow)*. https://arrow.apache.org/docs/python/feather.html

Federal Statistical Office (FSO). (2025). *Federal register of buildings and dwellings (RBD)*. https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html
