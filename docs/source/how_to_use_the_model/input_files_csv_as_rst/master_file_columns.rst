+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| Number | Column                                   | Data type | Description                              | Source for Swiss dataset                 |
+========+==========================================+===========+==========================================+==========================================+
| 0      | ``EGID``                                 | int       | Unique identifier assigned to each       | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | building. For Switzerland, these are     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | allready assigned to each building (see  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | www.regbl.admin.ch/catalog). For         |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | buildings in other regions or not        |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | existing, a new EGID identifier can be   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | assigned, but should be different from   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | those already existing.                  |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 1      | ``GDEKT``                                | string    | Canton, in which the building is         | Swisstopo, 2024                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | located. For regions outside of          |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Switzerland, this is not relevant or can |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | be assigned according to similar         |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | regional entities such as e.g.           |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | provinces. For Switzerland, the short    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | form is used (e.g., ZH, FR, … ).         |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 2      | ``GKAT``                                 | float     | Building category, adopted according to  | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Federal Statistical Office (2025). The   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | categroy code is a numeric integer       |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | consisting of 4 digits. The codes for    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | each category can be found on            |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | www.regbl.admin.ch/catalog. For example, |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | category "1020" refers to "Building for  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | residential use only". Among others,     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | this categorisation is used to           |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | distinguis between different types of    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | energy demand.                           |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 3      | ``GKLAS``                                | float     | Building class, adopted according to     | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Federal Statistical Office (2025). The   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | class code is a numeric integer          |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | consisting of 4 digits. The codes for    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | each class can be found on               |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | www.regbl.admin.ch/catalog. For example, |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | building class "1211" refers to          |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | "Hotels", while class "1220" refers to   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Office buildings. Among others, this     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | classification is used to distinguis     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | between different types of energy        |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand.                                  |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 4      | ``GGDENR``                               | int       | Unique identifier assigned to each       | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. For Switzerland, it is the     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | number of the commune according to the   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Official Register of Swiss Communes in   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Switzerland. For other regions or        |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | districts with customised boundaries     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | other than the official Swiss communes,  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | new numbers can be assigned (>7000).     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | They must be unique and not coincide     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | with existing numbers.                   |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 5      | ``GGDENAME``                             | string    | Name of the district. For municipalities | Swisstopo, 2024                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | in Switzerland, it is taken from the     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Official directory fo building addresses |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (Swisstopo, 2024).                       |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 6      | ``GKODE``                                | float     | E coordinate of the building (for        | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Switzerland in LV95 standard). Not       |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | relevant for regions other than          |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Switzerland.                             |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 7      | ``GKODN``                                | float     | N coordinate of the building (for        | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Switzerland in LV95 standard). Not       |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | relevant for regions other than          |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Switzerland.                             |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 8      | ``GBAUJ``                                | float     | Year of construction of the building     | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | according to Federal Statistical Office, |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | 2025. See www.regbl.admin.ch/catalog.    |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 9      | ``GBAUP``                                | float     | Period of construction according to      | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Federal Statistical Office, 2025. See    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | www.regbl.admin.ch/catalog.              |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 10     | ``GAREA``                                | float     | Surface area of building (floor area) in | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | square meters according to Federal       |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Statistical Office, 2025. See            |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | www.regbl.admin.ch/catalog.              |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 11     | ``GASTW``                                | float     | Number of floors and basements,          | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | including ground floor. According to     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Federal Statistical Office, 2025. See    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | www.regbl.admin.ch/catalog.              |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 12     | ``GENH1``                                | float     | Energy source / heat source 1 described  | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | as numeric code of 4 digits according to |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Federal Statistical Office, 2025. See    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | www.regbl.admin.ch/catalog. For example, |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | code "7520" refers to "Gas".             |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 13     | ``GENH2``                                | float     | Energy source / heat source 2 (if        | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | applicable). Described as numeric code   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | of 4 digits in the same way as           |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | ``GENH1``.                               |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 14     | ``GENW1``                                | float     | Energy / heat source for hot water 1     | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | described as numeric code of 4 digits    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | accordint to Federal Statistical Office, |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | 2025. See www.regbl.admin.ch/catalog.    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | For example, code "7520" refers to       |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | "Gas".                                   |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 15     | ``GENW2``                                | float     | Energy / heat source for hot water 2 (if | Federal Statistical Office, 2025         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | applicable). Described as numeric code   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | of 4 digits in the same way as           |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | ``GENW1``.                               |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 16     | ``Coord_lat``                            | float     | Latitude coordinate of the building in   | Converted from ``GKODN``.                |
|        |                                          |           |                                          |                                          |
|        |                                          |           | decimal format (e.g., 47.269056)         |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 17     | ``Coord_long``                           | float     | Longitude coordinate the building in     | Converted from ``GKODE``.                |
|        |                                          |           |                                          |                                          |
|        |                                          |           | decimal format (e.g., 8.449859)          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 18     | ``PV_Pot``                               | float     | Annual rooftop solar photovoltaic        | Swiss Federal Office of Energy, 2023     |
|        |                                          |           |                                          |                                          |
|        |                                          |           | generation potential of the building (in |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | kWh).                                    |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 19     | ``PV_Pot_reco``                          | float     | Recommended annual rooftop solar         | Subset calculated from ``PV_tot``.       |
|        |                                          |           |                                          |                                          |
|        |                                          |           | photovoltaic generation potential based  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | on roof suitability. Subset of           |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | ``PV_Pot``.                              |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 20     | ``FPV_Pot``                              | float     | Annual fassade solar photovoltaic        | Swiss Federal Office of Energy, 2023     |
|        |                                          |           |                                          |                                          |
|        |                                          |           | generation potential of the building (in |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | kWh).                                    |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 21     | ``FPV_Pot_reco``                         | float     | Recommended annual fassade solar         | Subset calculated from ``FPV_tot``.      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | photovoltaic generation potential based  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | on fassade suitability. Subset of        |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | ``FPV_Pot``.                             |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 22     | ``BeginningOfOperation``                 | string    | Commissioning date of the installed      | Swiss Federal Office of Energy, 2022a    |
|        |                                          |           |                                          |                                          |
|        |                                          |           | solar photovoltaic system.               |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 23     | ``InitialPower``                         | float     | Initial commissioning capacity of the    | Swiss Federal Office of Energy, 2022a    |
|        |                                          |           |                                          |                                          |
|        |                                          |           | installed solar photovoltaic system in   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | kW. For solar PV systems without         |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | expansion, the initial commissioning     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | capacity corresponds to the total        |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | capacity.                                |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 24     | ``TotalPower``                           | float     | Total installed solar PV capacity        | Swiss Federal Office of Energy, 2022a    |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (including any possible expansions) in   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | kW.                                      |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 25     | ``PlantCategory``                        | string    | OPTIONAL. Solar PV plant type according  | Swiss Federal Office of Energy, 2022a    |
|        |                                          |           |                                          |                                          |
|        |                                          |           | to Swiss Federal Office of Energy        |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (2022). (Options: "plantcat_8" =         |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | attached; "plantcat_9" = integrated).    |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 26     | ``TotalEnergy``                          | float     | Total annual generated energy in kWh     | Calculated based on ``TotalPower`` using |
|        |                                          |           |                                          |                                          |
|        |                                          |           | from solar PV installation.              | an assumed value of full load hours      |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | (e.g., 1000 kWh/kWp).                    |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 27     | ``altitude``                             | int       | Elevation above sea level of the         | Obtained through Open-Elevation API      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | building.                                | (www.open-elevation.com)                 |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 28     | ``Temperature_mean``                     | float     | Mean annual ambient temperature at       | Calculated as mean from hourly           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | building location.                       | temperature profile.                     |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 29     | ``renovation_base``                      | float     | Only required for ``demand_side``        | Calculated using renovation rates        |
|        |                                          |           |                                          |                                          |
|        |                                          |           | scenario with renovation. Year of        | scenario based on Streicher at al.       |
|        |                                          |           |                                          |                                          |
|        |                                          |           | renovation for this building (in the     | (2021). See :ref:`renovation-scenario`   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | future) for renovation scenario "base"   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (e.g., 2045).                            |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 30     | ``renovation_low``                       | float     | Only required for ``demand_side``        | Calculated using renovation rates        |
|        |                                          |           |                                          |                                          |
|        |                                          |           | scenario with renovation. Year of        | scenario based on Streicher at al.       |
|        |                                          |           |                                          |                                          |
|        |                                          |           | renovation for this building (in the     | (2021). See :ref:`renovation-scenario`   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | future) for renovation scenario "low"    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (e.g., 2045).                            |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 31     | ``renovation_high``                      | float     | Only required for ``demand_side``        | Calculated using renovation rates        |
|        |                                          |           |                                          |                                          |
|        |                                          |           | scenario with renovation. Year of        | scenario based on Streicher at al.       |
|        |                                          |           |                                          |                                          |
|        |                                          |           | renovation for this building (in the     | (2021). See :ref:`renovation-scenario`   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | future) for renovation scenario "high"   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (e.g., 2045).                            |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 32     | ``heat_energy_demand_estimate_kWh_combin | float     | Annual space heating demand in kWh.      | Computed according to Schneeberger et    |
|        |                                          |           |                                          |                                          |
|        | ed``                                     |           |                                          | al. (2025). See also                     |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | :ref:`space_heating_demand_modelling`    |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 33     | ``dhw_estimation_kWh_combined``          | float     | Annual domestic hot water (DHW) demand   | See :ref:`dhw_demand_modelling`          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | in kWh.                                  |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 34     | ``cluster_number``                       | int       | *currently not used*                     | *n/a*                                    |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 35     | ``kWh_household_sfh``                    | float     | If the building is a single family house | See                                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (SFH): annual electricity demand in kWh. | :ref:`electricity_demand_residential`    |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Otherwise 0.                             |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 36     | ``kWh_household_mfh``                    | float     | If the building is a multi family house  | See                                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (MFH): annual electricity demand in kWh. | :ref:`electricity_demand_residential`    |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Otherwise 0.                             |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 37     | ``Heating_System``                       | string    | Heat flow in DEM nomenclature            | See: :ref:`nomenclature`                 |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (:ref:`nomenclature`) for specified      |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | heating system. E.g., ``v_h_hp`` for     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | heat pump (hp) heat flow.                |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 38     | ``Hot_Water_System``                     | string    | Heat flow in DEM nomenclature            | See: :ref:`nomenclature`                 |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (:ref:`nomenclature`) for specified hot  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | water system. E.g., ``v_hw_hp`` for heat |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | pump (hp) hot water flow.                |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 39     | ``Electricity_Industry``                 | float     | Annual electricity demand for industry   | See :ref:`electricity_demand_industry`   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (if applicable) in kWh.                  |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 40     | ``Electricity_Service``                  | float     | Annual electricity demand for services   | See :ref:`electricity_demand_industry`   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (if applicable) in kWh.                  |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 41     | ``s_wd_bm``                              | float     | Share of total woody biomass potential   | Value of total woody biomass potential   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | in kWh allocated to individual building. | obtained from Data provided by the Swiss |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | Federal Institute for Forest, Snow and   |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | Landscape Research (WSL). Values are     |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | originally provided by municipality.     |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | Here, the share per building is          |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | calculated based on share of building    |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | surface area (``GAREA``) in relation to  |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | the whole municipality. The value for    |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | woody biomass with bark and 0% water     |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | content is used.                         |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 42     | ``s_wet_bm``                             | float     | Share of total wet biomass potential in  | Data provided by the Swiss Federal       |
|        |                                          |           |                                          |                                          |
|        |                                          |           | kWh allocated to individual building.    | Institute for Forest, Snow and Landscape |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | Research (WSL) based on Burg et al.      |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | (2018) and Thees et al. (2017). Here,    |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | the share per building is calculated     |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | based on share of building surface area  |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | (``GAREA``) in relation to the whole     |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 43     | ``LocalHydroPotential_Laufkraftwerk``    | float     | Share of local annual run-of-river hydro | See :ref:`hydro_power`                   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | power potential in kWh allocated to      |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | individual building.                     |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 44     | ``LocalHydroPotential_Speicherkraftwerk` | float     | Share of local annual storage hydro      | See :ref:`hydro_power`                   |
|        |                                          |           |                                          |                                          |
|        | `                                        |           | power potential in kWh allocated to      |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | individual building.                     |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 45     | ``LocalHydroPotential_Pumpspeicherkraftw | float     | Share of local annual pumped storage     | See :ref:`hydro_power`                   |
|        |                                          |           |                                          |                                          |
|        | erk``                                    |           | hydro power potential in kWh allocated   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | to individual building.                  |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 46     | ``avg_dh_connection_distance``           | float     | Average distance to nearby buildings on  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | a near-optimal triangulation of the      |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | building points on the plane.            |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 47     | ``dh_distance_cat``                      | int       | Distance category obtained by combining  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | ``avg_dh_connection_distance`` with the  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | thermal demand of the buildings.         |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 48     | ``heat_energy_demand_renov_estimate_kWh` | float     | Post-total renovation heat energy demand |                                          |
|        |                                          |           |                                          |                                          |
|        | `                                        |           | estimation                               |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
