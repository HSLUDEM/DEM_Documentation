+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| Number | Column                                   | Data type | Description                              | Source for Swiss dataset                 |
+========+==========================================+===========+==========================================+==========================================+
| 0      | ``Municipality``                         | object    | Name of the district or municipality     | Grouped value from :ref:`master_file`    |
|        |                                          |           |                                          |                                          |
|        |                                          |           | according to ``GGDENAME`` in             |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`. For municipalities   |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | in Switzerland, it is taken from the     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Official directory fo building addresses |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (Swisstopo, 2024).                       |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 1      | ``GGDENR``                               | int64     | According to ``GGDENR`` in               | Grouped value from :ref:`master_file`    |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`e.                     |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 2      | ``Canton``                               | object    | Same as ``GDEKT`` in :ref:`master_file`. | From :ref:`master_file`.                 |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Canton, in which the district is         |                                          |
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
| 3      | ``Coord_lat_median``                     | float64   | Latitude coordinate of the district.     | Calculated as median from ``Coord_lat``  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Given in decimal format (e.g.,           | values given in :ref:`master_file`.      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | 47.269056).                              |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 4      | ``Coord_long_median``                    | float64   | Longitude coordinate of the district.    | Calculated as median from ``Coord_long`` |
|        |                                          |           |                                          |                                          |
|        |                                          |           | Given in decimal format (e.g., 8.449859) | values given in :ref:`master_file`.      |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 5      | ``altitude_median``                      | float64   | Elevation above sea level of the         | Calculated as median from ``altitude``   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district.                                | values given in :ref:`master_file`.      |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 6      | ``Filename``                             | object    | Name of the file that will be            | Based on values in ``Municipality``      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | automatically generated as a subset from |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`. It must not contain  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | spaces. It is usually based on the       |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | ``Municipality`` name.  For example, if  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the ``Municipality`` name is "Affoltern  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | am Albis", ``Filename`` is               |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | "Affoltern_am_Albis".                    |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 7      | ``LocalHydroPotential``                  | float64   | Local total annual hydro power potential | See :ref:`hydro_power`                   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | in kWh.                                  |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 8      | ``LocalHydroPotential_Laufkraftwerk``    | float64   | Local annual run-of-river hydro power    | See :ref:`hydro_power`                   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | potential in kWh.                        |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 9      | ``LocalHydroPotential_Speicherkraftwerk` | float64   | Local annual storage hydro power         | See :ref:`hydro_power`                   |
|        |                                          |           |                                          |                                          |
|        | `                                        |           | potential in kWh.                        |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 10     | ``LocalHydroPotential_Pumpspeicherkraftw | float64   | Local annual pumped storage hydro power  | See :ref:`hydro_power`                   |
|        |                                          |           |                                          |                                          |
|        | erk``                                    |           | potential in kWh.                        |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 11     | ``v_h_eh``                               | float64   | Required annual heat supply (i.e., heat  | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand) in kWh from electric heaters     | Aggregated value of ``heat_energy_demand |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (eh) in base scenario (i.e., current     | _estimate_kWh_combined`` for all         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | status) for the selected district. Can   | buildings with ``Heating_System`` type   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | be calculated from values contained in   | ``v_h_eh`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`.                      | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 12     | ``v_h_hp``                               | float64   | Required annual heat supply (i.e., heat  | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand) in kWh from heat pumps (hp) in   | Aggregated value of ``heat_energy_demand |
|        |                                          |           |                                          |                                          |
|        |                                          |           | base scenario (i.e., current status) for | _estimate_kWh_combined`` for all         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the selected district. Can be calculated | buildings with ``Heating_System`` type   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | from values contained in                 | ``v_h_hp`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`.                      | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 13     | ``v_h_dh``                               | float64   | Required annual heat supply (i.e., heat  | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand) in kWh from district heating     | Aggregated value of ``heat_energy_demand |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (dh) in base scenario (i.e., current     | _estimate_kWh_combined`` for all         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | status) for the selected district. Can   | buildings with ``Heating_System`` type   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | be calculated from values contained in   | ``v_h_dh`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`.                      | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 14     | ``v_h_gb``                               | float64   | Required annual heat supply (i.e., heat  | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand) in kWh from gas boilers (gb) in  | Aggregated value of ``heat_energy_demand |
|        |                                          |           |                                          |                                          |
|        |                                          |           | base scenario (i.e., current status) for | _estimate_kWh_combined`` for all         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the selected district. Can be calculated | buildings with ``Heating_System`` type   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | from values contained in                 | ``v_h_gb`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`.                      | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 15     | ``v_h_ob``                               | float64   | Required annual heat supply (i.e., heat  | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand) in kWh from oil boilers (ob) in  | Aggregated value of ``heat_energy_demand |
|        |                                          |           |                                          |                                          |
|        |                                          |           | base scenario (i.e., current status) for | _estimate_kWh_combined`` for all         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the selected district. Can be calculated | buildings with ``Heating_System`` type   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | from values contained in                 | ``v_h_ob`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`.                      | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 16     | ``v_h_wb``                               | float64   | Required annual heat supply (i.e., heat  | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand) in kWh from wood boilers (wb) in | Aggregated value of ``heat_energy_demand |
|        |                                          |           |                                          |                                          |
|        |                                          |           | base scenario (i.e., current status) for | _estimate_kWh_combined`` for all         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the selected district. Can be calculated | buildings with ``Heating_System`` type   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | from values contained in                 | ``v_h_wb`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`.                      | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 17     | ``v_h_solar``                            | float64   | Required annual heat supply (i.e., heat  | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand) in kWh from solar thermal in     | Aggregated value of ``heat_energy_demand |
|        |                                          |           |                                          |                                          |
|        |                                          |           | base scenario (i.e., current status) for | _estimate_kWh_combined`` for all         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the selected district. Can be calculated | buildings with ``Heating_System`` type   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | from values contained in                 | ``v_h_solar`` within the selected        |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`.                      | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 18     | ``v_h_other``                            | float64   | Required annual heat supply (i.e., heat  | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | demand) in kWh from other technologies   | Aggregated value of ``heat_energy_demand |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (i.e., unknown) in base scenario (i.e.,  | _estimate_kWh_combined`` for all         |
|        |                                          |           |                                          |                                          |
|        |                                          |           | current status) for the selected         | buildings with ``Heating_System`` type   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. Can be calculated from values  | ``v_h_other`` within the selected        |
|        |                                          |           |                                          |                                          |
|        |                                          |           | contained in :ref:`master_file`.         | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 19     | ``Total_Heating``                        | float64   | Total required annual heat supply (i.e., | Calculated as the sum of the values from |
|        |                                          |           |                                          |                                          |
|        |                                          |           | heat demand) in kWh as the sum from all  | individual technologies (columns 11-18)  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | technologies in base scenario (i.e.,     |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | current status) for the selected         |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district.                                |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 20     | ``v_hw_eh``                              | float64   | Required annual domestic hot water       | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh from   | Aggregated value of                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | electric heaters (eh) in base scenario   | ``dhw_estimation_kWh_combined`` for all  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (i.e., current status) for the selected  | buildings with ``Hot_Water_System`` type |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. Can be calculated from values  | ``v_h_eh`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | contained in :ref:`master_file`.         | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 21     | ``v_hw_hp``                              | float64   | Required annual domestic hot water       | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh from   | Aggregated value of                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | heat pumps (hp) in base scenario (i.e.,  | ``dhw_estimation_kWh_combined`` for all  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | current status) for the selected         | buildings with ``Hot_Water_System`` type |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. Can be calculated from values  | ``v_h_hp`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | contained in :ref:`master_file`.         | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 22     | ``v_hw_dh``                              | float64   | Required annual domestic hot watert      | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh from   | Aggregated value of                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district heating (dh) in base scenario   | `dhw_estimation_kWh_combined`` for all   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (i.e., current status) for the selected  | buildings with ``Hot_Water_System`` type |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. Can be calculated from values  | ``v_h_dh`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | contained in :ref:`master_file`.         | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 23     | ``v_hw_gb``                              | float64   | Required annual domestic hot water       | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh from   | Aggregated value of                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | gas boilers (gb) in base scenario (i.e., | ``dhw_estimation_kWh_combined`` for all  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | current status) for the selected         | buildings with ``Hot_Water_System`` type |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. Can be calculated from values  | ``v_h_gb`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | contained in :ref:`master_file`.         | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 24     | ``v_hw_ob``                              | float64   | Required annual domestic hot water       | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh from   | Aggregated value of                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | oil boilers (ob) in base scenario (i.e., | ``dhw_estimation_kWh_combined`` for all  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | current status) for the selected         | buildings with ``Hot_Water_System`` type |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. Can be calculated from values  | ``v_h_ob`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | contained in :ref:`master_file`.         | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 25     | ``v_hw_wb``                              | float64   | Required annual domestic hot water       | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh from   | Aggregated value of                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | wood boilers (wb) in base scenario       | ``dhw_estimation_kWh_combined`` for all  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (i.e., current status) for the selected  | buildings with ``Hot_Water_System`` type |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. Can be calculated from values  | ``v_h_wb`` within the selected           |
|        |                                          |           |                                          |                                          |
|        |                                          |           | contained in :ref:`master_file`.         | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 26     | ``v_hw_solar``                           | float64   | Required annual domestic hot watert      | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh from   | Aggregated value of                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | solar thermal in base scenario (i.e.,    | ``dhw_estimation_kWh_combined`` for all  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | current status) for the selected         | buildings with ``Hot_Water_System`` type |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district. Can be calculated from values  | ``v_h_solar`` within the selected        |
|        |                                          |           |                                          |                                          |
|        |                                          |           | contained in :ref:`master_file`.         | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 27     | ``v_hw_other``                           | float64   | Required annual domestic hot water       | Calculated from :ref:`master_file`:      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh from   | Aggregated value of                      |
|        |                                          |           |                                          |                                          |
|        |                                          |           | other technologies (i.e., unknown) in    | ``dhw_estimation_kWh_combined`` for all  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | base scenario (i.e., current status) for | buildings with ``Hot_Water_System`` type |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the selected district. Can be calculated | ``v_h_other`` within the selected        |
|        |                                          |           |                                          |                                          |
|        |                                          |           | from values contained in                 | municipality.                            |
|        |                                          |           |                                          |                                          |
|        |                                          |           | :ref:`master_file`.                      |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 28     | ``Total_Hot_Water``                      | float64   | Total required annual domestic hot water | Calculated as the sum of the values from |
|        |                                          |           |                                          |                                          |
|        |                                          |           | supply (i.e., heat demand) in kWh as the | individual technologies (columns 20-27)  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | sum from all technologies in base        |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | scenario (i.e., current status) for the  |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | selected district.                       |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 29     | ``PV_Pot``                               | float64   | Annual rooftop solar photovoltaic        | ``PV_Pot`` values in :ref:`master_file`  |
|        |                                          |           |                                          |                                          |
|        |                                          |           | generation potential of the building (in | aggregated across municipality.          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | kWh).                                    |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 30     | ``TotalEnergy``                          | float64   | Total annual generated energy in kWh     | ``TotalEnergy`` values in                |
|        |                                          |           |                                          |                                          |
|        |                                          |           | from solar PV installation.              | :ref:`master_file` aggregated across     |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 31     | ``kWh_household_sfh``                    | float64   | Total annual electricity demand in kWh   | ``kWh_household_sfh`` values in          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | for single family houses (SFH) in the    | :ref:`master_file` aggregated across     |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district.                                | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 32     | ``kWh_household_mfh``                    | float64   | Total annual electricity demand in kWh   | ``kWh_household_mfh`` values in          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | for multi family houses (MFH) in the     | :ref:`master_file` aggregated across     |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district.                                | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 33     | ``Electricity_Industry``                 | float64   | Annual electricity demand for industry   | ``Electricity_Industry`` values in       |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (if applicable) in kWh for the selected  | :ref:`master_file` aggregated across     |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district.                                | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 34     | ``Electricity_Service``                  | float64   | Annual electricity demand for services   | ``Electricity_Service`` values in        |
|        |                                          |           |                                          |                                          |
|        |                                          |           | (if applicable) in kWh for the selected  | :ref:`master_file` aggregated across     |
|        |                                          |           |                                          |                                          |
|        |                                          |           | district.                                | municipality.                            |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 35     | ``s_wd_bm``                              | float64   | Total woody biomass potential in kWh for | Value of total woody biomass potential   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the selected district.                   | obtained from Data provided by the Swiss |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | Federal Institute for Forest, Snow and   |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | Landscape Research (WSL). Values are     |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | originally provided by municipality. The |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | value for woody biomass with bark and 0% |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | water content is used.                   |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 36     | ``s_wet_bm``                             | float64   | Total wet biomass potential in kWh for   | Data provided by the Swiss Federal       |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the selected district.                   | Institute for Forest, Snow and Landscape |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | Research (WSL) based on Burg et al.      |
|        |                                          |           |                                          |                                          |
|        |                                          |           |                                          | (2018) and Thees et al. (2017).          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 37     | ``PV_Filename``                          | int64     | Identification number of the hourly      | Profile which was simulated closest to   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | solar photovoltaic profile applicable to | the selected municipality is used. See   |
|        |                                          |           |                                          |                                          |
|        |                                          |           | the district based on profiles provided  | also :ref:`tech_solar_pv`.               |
|        |                                          |           |                                          |                                          |
|        |                                          |           | in :ref:`simulation_profiles` columns    |                                          |
|        |                                          |           |                                          |                                          |
|        |                                          |           | 33-43. E.g., "9" for ``PV_Profile_9``.   |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 38     | ``dh_cap_class_1``                       | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 39     | ``dh_cap_class_2``                       | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 40     | ``dh_cap_class_3``                       | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 41     | ``dh_cap_renov_class_1``                 | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 42     | ``dh_cap_renov_class_2``                 | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 43     | ``dh_cap_renov_class_3``                 | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 44     | ``dh_avg_dist_class_1``                  | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 45     | ``dh_avg_dist_class_2``                  | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 46     | ``dh_avg_dist_class_3``                  | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 47     | ``m_per_kWh_class_1_renov``              | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 48     | ``m_per_kWh_class_2_renov``              | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 49     | ``m_per_kWh_class_3_renov``              | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 50     | ``m_per_kWh_class_1``                    | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 51     | ``m_per_kWh_class_2``                    | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
| 52     | ``m_per_kWh_class_3``                    | float64   |                                          |                                          |
+--------+------------------------------------------+-----------+------------------------------------------+------------------------------------------+
