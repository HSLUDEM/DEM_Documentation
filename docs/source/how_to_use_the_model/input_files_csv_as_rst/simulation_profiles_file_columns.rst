+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| Number | Column                               | Data type | Description                              | Source for Swiss dataset                 |
+========+======================================+===========+==========================================+==========================================+
| 0      | ``Woody_Biomass_Profile``            | float     | Normalised hourly profile of woody       | Constant hourly profile across the whole |
|        |                                      |           |                                          |                                          |
|        |                                      |           | biomass availability. This accounts for  | year.                                    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | the fact that not the entire resource is |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | available at once due to limitations     |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | such as harvesting, transport, storage,  |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | etc...                                   |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 1      | ``Wet_Biomass_Profile``              | float     | Normalised hourly profile of wet biomass | Constant hourly profile across the whole |
|        |                                      |           |                                          |                                          |
|        |                                      |           | availability. This accounts for the fact | year.                                    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | that not the entire resource is          |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | available at once due to limitations     |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | such as harvesting, transport, storage,  |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | etc...                                   |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 2      | ``Electricity_Profile_MFH``          | float     | Normalised hourly electricity load       | Rinaldi et al. (2022)                    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | profile for multi family houses (MFH).   |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 3      | ``Electricity_Profile_SFH``          | float     | Normalised hourly electricity load       | Rinaldi et al. (2022)                    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | profile for single family houses (SFH).  |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 4      | ``Electricity_Profile_Industry_AG``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Aargau (AG).  | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 5      | ``Electricity_Profile_Industry_FR``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Freiburg      | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (FR).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 6      | ``Electricity_Profile_Industry_GL``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Glarus (GL).  | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 7      | ``Electricity_Profile_Industry_GR``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Graubünden    | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (GR).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 8      | ``Electricity_Profile_Industry_LU``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Luzern (LU).  | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 9      | ``Electricity_Profile_Industry_NE``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Neuenburg     | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (NE).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 10     | ``Electricity_Profile_Industry_SO``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Solothurn     | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (SO).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 11     | ``Electricity_Profile_Industry_SG``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of St. Gallen    | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (SG).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 12     | ``Electricity_Profile_Industry_TI``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Tessin (TI).  | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 13     | ``Electricity_Profile_Industry_TG``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Thurgau (TG). | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 14     | ``Electricity_Profile_Industry_VS``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Wallis (VS).  | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 15     | ``Electricity_Profile_Industry_AI``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Appenzell     | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Innerrhoden (AI).                        |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 16     | ``Electricity_Profile_Industry_AR``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Appenzell     | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Ausserrhoden (AR).                       |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 17     | ``Electricity_Profile_Industry_BL``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Basel-        | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Landschaft (BL).                         |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 18     | ``Electricity_Profile_Industry_BS``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Basel-Stadt   | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (BS).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 19     | ``Electricity_Profile_Industry_BE``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Bern (BE).    | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 20     | ``Electricity_Profile_Industry_JU``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Jura (JU).    | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 21     | ``Electricity_Profile_Industry_SZ``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Schwyz (SZ).  | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 22     | ``Electricity_Profile_Industry_ZG``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Zug (ZG).     | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 23     | ``Electricity_Profile_Industry_OW``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Obwalden      | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (OW).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 24     | ``Electricity_Profile_Industry_NW``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Nidwalden     | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (NW).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 25     | ``Electricity_Profile_Industry_UR``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Uri (UR).     | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 26     | ``Electricity_Profile_Industry_GE``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Genf (GE).    | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 27     | ``Electricity_Profile_Industry_VD``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Waadt (VD).   | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 28     | ``Electricity_Profile_Industry_SH``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Schaffhausen  | :ref:`electricity_demand_industry`.      |
|        |                                      |           |                                          |                                          |
|        |                                      |           | (SH).                                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 29     | ``Electricity_Profile_Industry_ZH``  | float     | Only relevant for region Switzerland.    | Modelled based on grid data (Swissgrid   |
|        |                                      |           |                                          |                                          |
|        |                                      |           | Normalised electricity load profile for  | Ltd, 2025). See                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | industry for the canton of Zürich (ZH).  | :ref:`electricity_demand_industry`.      |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 30     | ``Hydro_Lokal_Laufwasser_Profile``   | float     | Normalised hourly standard profile of    |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | local run-of-river hydro power           |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | generation.                              |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 31     | ``Hydro_Lokal_Speicher_Profile``     | float     | Normalised hourly standard profile of    |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | local storage hydro power generation.    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 32     | ``Hydro_Lokal_Pumpspeicher_Profile`` | float     | Normalised hourly standard profile of    |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | local pumped storage hydro power         |                                          |
|        |                                      |           |                                          |                                          |
|        |                                      |           | generation.                              |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 33     | ``PV_Profile_0``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 0.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 34     | ``PV_Profile_1``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 1.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 35     | ``PV_Profile_2``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 2.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 36     | ``PV_Profile_3``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 3.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 37     | ``PV_Profile_4``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 4.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 38     | ``PV_Profile_5``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 5.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 39     | ``PV_Profile_6``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 6.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 40     | ``PV_Profile_7``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 7.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 41     | ``PV_Profile_8``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 8.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 42     | ``PV_Profile_9``                     | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 9.                     |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 43     | ``PV_Profile_10``                    | float     | Normalised hourly profile of solar PV    | See :ref:`tech_solar_pv`                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | yield at location 10.                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 44     | ``Hydro_National_Profile``           | float     | Normalised hourly profile of hydro power | Modelled based on data from Swiss        |
|        |                                      |           |                                          |                                          |
|        |                                      |           | generation from national electricity     | electricity statistics (Swiss Federal    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | mix, for large hydro power plants not    | Office of Energy, 2022b)                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | considered local.                        |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 45     | ``Nuclear_National_Profile``         | float     | Normalised hourly profile of nuclear     | Modelled based on data from Swiss        |
|        |                                      |           |                                          |                                          |
|        |                                      |           | power generation from national           | electricity statistics (Swiss Federal    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | electricity mix. Nuclear power plants    | Office of Energy, 2022b)                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | are never considered local in DEM.       |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 46     | ``Solar_National_Profile``           | float     | Normalised hourly profile of solar PV    | Modelled based on data from Swiss        |
|        |                                      |           |                                          |                                          |
|        |                                      |           | power generation from national           | electricity statistics (Swiss Federal    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | electricity mix for large solar PV       | Office of Energy, 2022b)                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | plants not considered local.             |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 47     | ``Wind_National_Profile``            | float     | Normalised hourly profile of wind power  | Modelled based on data from Swiss        |
|        |                                      |           |                                          |                                          |
|        |                                      |           | generation from national electricity mix | electricity statistics (Swiss Federal    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | for large wind power plants not          | Office of Energy, 2022b)                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | considered local.                        |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 48     | ``Biomass_National_Profile``         | float     | Normalised hourly profile of power       | Modelled based on data from Swiss        |
|        |                                      |           |                                          |                                          |
|        |                                      |           | generation from biomass from national    | electricity statistics (Swiss Federal    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | electricity mix for large power plants   | Office of Energy, 2022b)                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | not considered local.                    |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 49     | ``Other_National_Profile``           | float     | Normalised hourly profile of power       | Modelled based on data from Swiss        |
|        |                                      |           |                                          |                                          |
|        |                                      |           | generation from other technologies in    | electricity statistics (Swiss Federal    |
|        |                                      |           |                                          |                                          |
|        |                                      |           | the national electricity mix for         | Office of Energy, 2022b)                 |
|        |                                      |           |                                          |                                          |
|        |                                      |           | technologies not considered local.       |                                          |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 50     | ``Import_National_Profile``          | float     | Normalised hourly profile of energy      | Modelled based on data from Swiss        |
|        |                                      |           |                                          |                                          |
|        |                                      |           | imported from other countries.           | electricity statistics (Swiss Federal    |
|        |                                      |           |                                          |                                          |
|        |                                      |           |                                          | Office of Energy, 2022b)                 |
+--------+--------------------------------------+-----------+------------------------------------------+------------------------------------------+
