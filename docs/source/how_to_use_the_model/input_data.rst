Model Input - Data Files
========================

Time series data, as well as information about buildings and districts, are provided to the District Energy Model (DEM) through data files. Most of these files are stored in Feather format (Apache Software Foundation, 2025).  

This section describes the required files, their contents, and the expected data formats. Although all files must be present for the simulation to run, their entries can be set to zero if a dataset is not relevant to a specific case (for example, the wind power file if wind generation is excluded from the scenario).

All input files must be located within the ``data`` directory following the predefined directory structure (see below).

.. note::
  For Switzerland, a complete dataset package is available on |Zenodo_link|. After downloading and unzipping the archive, place its contents in the ``data`` directory of your project. The required directory structure is already provided.

.. |Zenodo_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Zenodo</a>


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

.. _master_file:

Master file
-----------

This file contains information about each individual building, with one row per building. District-level information is derived from this file through aggregation. The file may include data for multiple districts; during a simulation, only the buildings belonging to the specified district are selected.  

Each building is identified by a unique identification number (column 0: ``EGID``) and assigned to a municipality represented by a numerical code (column 4: ``GGDENR``). Custom districts can also be analyzed by specifying the buildings included in the district via their ``EGID`` values.  

For Switzerland, data in columns 0 to 15 (except for columns 1 and 5) is sourced from the *Federal Register of Buildings and Dwellings (RBD)* (Federal Statistical Office, 2025), and the corresponding column naming conventions have been adopted accordingly (see |rbd_attributes_link|).

.. |rbd_attributes_link| raw:: html

   <a href="https://www.regbl.admin.ch/catalog" target="_blank">RBD Catalogue of Attributes</a>


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/master_file_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/master_file_columns.rst


Meta file
-----------
This file contains information about each district, with one row per district. Some of the data can be derived as an aggregate from the *Master File*.  

The district identification number (column 1: ``GGDENR``) must match the corresponding municipality code of the buildings listed in the *Master File*.

.. include:: ../how_to_use_the_model/input_files_csv_as_rst/meta_file_2_info_notitleline.rst


.. include:: ../how_to_use_the_model/input_files_csv_as_rst/meta_file_2_columns.rst


.. _simulation_profiles:

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

Apache Software Foundation. (2025). *Feather file format (Apache Arrow)*. |Apache_link|

.. |Apache_link| raw:: html

   <a href="https://arrow.apache.org/docs/python/feather.html" target="_blank">https://arrow.apache.org/docs/python/feather.html</a>
   
Burg, V., Bowman, G., Erni, M., Lemm, R., & Thees, O. (2018). *Analyzing the potential of domestic biomass resources for the energy transition in Switzerland*. Biomass and bioenergy, 111, 60-69. |Burg2018_link|

.. |Burg2018_link| raw:: html

   <a href="https://doi.org/10.1016/j.biombioe.2018.02.007" target="_blank">https://doi.org/10.1016/j.biombioe.2018.02.007</a>

Dujardin, J., Lehning, M. (2022a). *Wind-Topo_model*. EnviDat. |Dujardin2022a_link|

.. |Dujardin2022a_link| raw:: html

   <a href="https://www.doi.org/10.16904/envidat.301" target="_blank">https://www.doi.org/10.16904/envidat.301</a>

Dujardin, J., & Lehning, M. (2022b). *Wind‐Topo: Downscaling near‐surface wind fields to high‐resolution topography in highly complex terrain with deep learning*. Quarterly Journal of the Royal Meteorological Society, 148(744), 1368-1388. |Dujardin2022b_link|

.. |Dujardin2022b_link| raw:: html

   <a href="https://doi.org/10.1002/qj.4265" target="_blank">https://doi.org/10.1002/qj.4265</a>

Parajeles Herrera, M., & Hug, G. (2025a). *Charging Demand and Flexibility Bounds for Large-Scale BEV Fleets - The Case Study of Switzerland* [Data set]. Zenodo. |Herrera2025a_link|

.. |Herrera2025a_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.16597426" target="_blank">https://doi.org/10.5281/zenodo.16597426</a>

Parajeles Herrera, M & Hug, G. (2025b). *Modeling Charging Demand and Quantifying Flexibility Bounds for Large-Scale BEV Fleets*. 2025 IEEE Kiel PowerTech, Kiel, Germany, 2025, pp. 1-6. DOI: |Herrera2025b_link|

.. |Herrera2025b_link| raw:: html

   <a href="https://doi.org/10.1109/PowerTech59965.2025.11180551" target="_blank">https://doi.org/10.1109/PowerTech59965.2025.11180551</a>

Federal Statistical Office (FSO). (2025). *Federal register of buildings and dwellings (RBD)*. |FSO2025_link|

.. |FSO2025_link| raw:: html

   <a href="https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html" target="_blank">https://www.bfs.admin.ch/bfs/en/home/registers/federal-register-buildings-dwellings.html</a>

Federal Office of Topography Swisstopo. (2024). *Official directory of building addresses*. |swisstopo2024_link|

.. |swisstopo2024_link| raw:: html

   <a href="https://www.swisstopo.admin.ch/en/official-directory-of-building-addresses" target="_blank">https://www.swisstopo.admin.ch/en/official-directory-of-building-addresses</a>

Rinaldi, A., Ramirez, H., Schroeteler, B., & Meier, M. (2022). *The role of energy storage technologies in the context of the Swiss energy transition (SwissStore)* [Data set]. Zenodo. |Rinaldi2022_link|

.. |Rinaldi2022_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.6782179" target="_blank">https://doi.org/10.5281/zenodo.6782179</a>

Swiss Federal Office of Energy (SFOE). (2023). *Dokumentation Geodatenmodell Solarenergie: Solarenergie – Eignung Dächer (Sonnendach.ch) und Solarenergie – Eignung Fassaden (Sonnenfassade.ch)* (Version 1.5). Eidgenössisches Departement für Umwelt, Verkehr, Energie und Kommunikation (UVEK). |sonnendach2023_link|

.. |sonnendach2023_link| raw:: html

   <a href="https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/solar-energy/suitability-of-roofs-for-use-of-solar-energy.html" target="_blank">https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/solar-energy/suitability-of-roofs-for-use-of-solar-energy.html</a>

Swiss Federal Office of Energy (SFOE). (2022). *Dokumentation «minimales Geodatenmodell»: Elektrizitätsproduktionsanlagen* (Version 1.0rev, Geobasisdatensatz Nr. 221.1). Eidgenössisches Departement für Umwelt, Verkehr, Energie und Kommunikation. |e_prod_plants_link|

.. |e_prod_plants_link| raw:: html

   <a href="https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/production-plants/electricity-production-plants.html" target="_blank">https://www.bfe.admin.ch/bfe/en/home/supply/digitalization-and-geoinformation/geoinformation/geodata/production-plants/electricity-production-plants.html</a>

Streicher, K. N., Berger, M., Panos, E., Narula, K., Soini, M. C., & Patel, M. K. (2021). *Optimal building retrofit pathways considering stock dynamics and climate change impacts.* Energy Policy, 152, 112220. |Streicher2021_DOI_link|

.. |Streicher2021_DOI_link| raw:: html

   <a href="https://doi.org/10.1016/j.enpol.2021.112220" target="_blank">https://doi.org/10.1016/j.enpol.2021.112220</a>
   
Schneeberger, S., Meister, C., & Schuetz, P. (2025). Estimating the heating energy demand of residential buildings in Switzerland using only public data. Energy and Buildings, 116371. |Schneeberger2025_DOI_link|

.. |Schneeberger2025_DOI_link| raw:: html

   <a href="https://doi.org/10.1016/j.enbuild.2025.116371" target="_blank">https://doi.org/10.1016/j.enbuild.2025.116371</a>
   
Thees, O., Burg, V., Erni, M., Bowman, G., & Lemm, R. (2017). *Biomassenpotenziale der Schweiz für die energetische Nutzung*. Eidg. Forschungsanstalt für Wald, Schnee und Landschaft WSL. |Thees2017_link|

.. |Thees2017_link| raw:: html

   <a href="https://www.wsl.ch/de/publikationen/biomassepotenziale-der-schweiz-fuer-die-energetische-nutzung-ergebnisse-des-schweizerischen-energiekompetenzzentrums-sccer-biosweet/" target="_blank">https://www.wsl.ch/de/publikationen/biomassepotenziale-der-schweiz-fuer-die-energetische-nutzung-ergebnisse-des-schweizerischen-energiekompetenzzentrums-sccer-biosweet/</a>






.. other Links:

.. |Swiss_data_Zenodo_link|

   <a href="https://doi.org/10.5281/zenodo.17603138" target="_blank">Swiss dataset</a>










