+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| Number | Column                                        | Data type | Description                                    | Source for Swiss dataset                                                 |
+========+===============================================+===========+================================================+==========================================================================+
| 0      | ``Municipality``                              | string    | Name of the district or municipality           | Grouped value from :ref:`master_file`                                    |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | according to ``GGDENAME`` in                   |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`. For municipalities         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | in Switzerland, it is taken from the           |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | Official directory fo building addresses       |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (Swisstopo, 2024).                             |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 1      | ``GGDENR``                                    | int       | According to ``GGDENR`` in                     | Grouped value from :ref:`master_file`                                    |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`e.                           |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 2      | ``Canton``                                    | string    | Same as ``GDEKT`` in                           | From :ref:`master_file`.                                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`. Canton, in which the       |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district is located. For regions outside       |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | of Switzerland, this is not relevant or        |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | can be assigned according to similar           |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | regional entities such as e.g.                 |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | provinces. For Switzerland, the short          |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | form is used (e.g., ZH, FR, … ).               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 3      | ``Coord_lat_median``                          | float     | Latitude coordinate of the district.           | Calculated as median from ``Coord_lat``                                  |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | Given in decimal format (e.g.,                 | values given in :ref:`master_file`.                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | 47.269056).                                    |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 4      | ``Coord_long_median``                         | float     | Longitude coordinate of the district.          | Calculated as median from ``Coord_long``                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | Given in decimal format (e.g., 8.449859)       | values given in :ref:`master_file`.                                      |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 5      | ``altitude_median``                           | float     | Elevation above sea level of the               | Calculated as median from ``altitude``                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district.                                      | values given in :ref:`master_file`.                                      |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 6      | ``Filename``                                  | string    | Name of the file that will be                  | Based on values in ``Municipality``                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | automatically generated as a subset from       |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`. It must not contain        |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | spaces. It is usually based on the             |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | ``Municipality`` name.  For example, if the    |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | ``Municipality`` name is "Affoltern am Albis", |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | ``Filename`` is "Affoltern_am_Albis".          |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 7      | ``LocalHydroPotential``                       | float     | Local total annual hydro power potential       | See :ref:`hydro_power`                                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | in kWh.                                        |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 8      | ``LocalHydroPotential_Laufkraftwerk``         | float     | Local annual run-of-river hydro power          | See :ref:`hydro_power`                                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | potential in kWh.                              |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 9      | ``LocalHydroPotential_Speicherkraftwerk``     | float     | Local annual storage hydro power               | See :ref:`hydro_power`                                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | potential in kWh.                              |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 10     | ``LocalHydroPotential_Pumpspeicherkraftwerk`` | float     | Local annual pumped storage hydro power        | See :ref:`hydro_power`                                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | potential in kWh.                              |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 11     | ``v_h_eh``                                    | float     | Required annual heat supply (i.e., heat        | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | demand) in kWh from electric heaters           | Aggregated value of ``heat_energy_demand_estimate_kWh_combined`` for all |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (eh) in base scenario (i.e., current           | buildings with ``Heating_System`` type                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | status) for the selected district. Can         | ``v_h_eh`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | be calculated from values contained in         | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`.                            |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 12     | ``v_h_hp``                                    | float     | Required annual heat supply (i.e., heat        | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | demand) in kWh from heat pumps (hp) in         | Aggregated value of ``heat_energy_demand_estimate_kWh_combined`` for all |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | base scenario (i.e., current status) for       | buildings with ``Heating_System`` type                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the selected district. Can be calculated       | ``v_h_hp`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | from values contained in                       | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`.                            |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 13     | ``v_h_dh``                                    | float     | Required annual heat supply (i.e., heat        | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | demand) in kWh from district heating           | Aggregated value of ``heat_energy_demand_estimate_kWh_combined`` for all |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (dh) in base scenario (i.e., current           | buildings with ``Heating_System`` type                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | status) for the selected district. Can         | ``v_h_dh`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | be calculated from values contained in         | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`.                            |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 14     | ``v_h_gb``                                    | float     | Required annual heat supply (i.e., heat        | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | demand) in kWh from gas boilers (gb) in        | Aggregated value of ``heat_energy_demand_estimate_kWh_combined`` for all |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | base scenario (i.e., current status) for       | buildings with ``Heating_System`` type                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the selected district. Can be calculated       | ``v_h_gb`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | from values contained in                       | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`.                            |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 15     | ``v_h_ob``                                    | float     | Required annual heat supply (i.e., heat        | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | demand) in kWh from oil boilers (ob) in        | Aggregated value of ``heat_energy_demand_estimate_kWh_combined`` for all |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | base scenario (i.e., current status) for       | buildings with ``Heating_System`` type                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the selected district. Can be calculated       | ``v_h_ob`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | from values contained in                       | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`.                            |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 16     | ``v_h_wb``                                    | float     | Required annual heat supply (i.e., heat        | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | demand) in kWh from wood boilers (wb) in       | Aggregated value of ``heat_energy_demand_estimate_kWh_combined`` for all |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | base scenario (i.e., current status) for       | buildings with ``Heating_System`` type                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the selected district. Can be calculated       | ``v_h_wb`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | from values contained in                       | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`.                            |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 17     | ``v_h_solar``                                 | float     | Required annual heat supply (i.e., heat        | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | demand) in kWh from solar thermal in           | Aggregated value of ``heat_energy_demand_estimate_kWh_combined`` for all |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | base scenario (i.e., current status) for       | buildings with ``Heating_System`` type                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the selected district. Can be calculated       | ``v_h_solar`` within the selected                                        |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | from values contained in                       | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`.                            |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 18     | ``v_h_other``                                 | float     | Required annual heat supply (i.e., heat        | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | demand) in kWh from other technologies         | Aggregated value of ``heat_energy_demand_estimate_kWh_combined`` for all |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (i.e., unknown) in base scenario (i.e.,        | buildings with ``Heating_System`` type                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | current status) for the selected               | ``v_h_other`` within the selected                                        |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district. Can be calculated from values        | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | contained in :ref:`master_file`.               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 19     | ``Total_Heating``                             | float     | Total required annual heat supply (i.e.,       | Calculated as the sum of the values from                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | heat demand) in kWh as the sum from all        | individual technologies (columns 11-18)                                  |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | technologies in base scenario (i.e.,           |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | current status) for the selected               |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district.                                      |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 20     | ``v_hw_eh``                                   | float     | Required annual domestic hot water             | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh from         | Aggregated value of ``dhw_estimation_kWh_combined`` for all              |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | electric heaters (eh) in base scenario         | buildings with ``Hot_Water_System`` type                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (i.e., current status) for the selected        | ``v_h_eh`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district. Can be calculated from values        | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | contained in :ref:`master_file`.               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 21     | ``v_hw_hp``                                   | float     | Required annual domestic hot water             | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh from         | Aggregated value of ``dhw_estimation_kWh_combined`` for all              |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | heat pumps (hp) in base scenario (i.e.,        | buildings with ``Hot_Water_System`` type                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | current status) for the selected               | ``v_h_hp`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district. Can be calculated from values        | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | contained in :ref:`master_file`.               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 22     | ``v_hw_dh``                                   | float     | Required annual domestic hot watert            | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh from         | Aggregated value of `dhw_estimation_kWh_                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district heating (dh) in base scenario         | combined`` for all buildings with ``Hot_Water_System@@EXPR               |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (i.e., current status) for the selected        | _1@@v_h_dh`` within the selected                                         |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district. Can be calculated from values        | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | contained in :ref:`master_file`.               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 23     | ``v_hw_gb``                                   | float     | Required annual domestic hot water             | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh from         | Aggregated value of ``dhw_estimation_kWh_combined`` for all              |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | gas boilers (gb) in base scenario (i.e.,       | buildings with ``Hot_Water_System`` type                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | current status) for the selected               | ``v_h_gb`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district. Can be calculated from values        | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | contained in :ref:`master_file`.               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 24     | ``v_hw_ob``                                   | float     | Required annual domestic hot water             | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh from         | Aggregated value of ``dhw_estimation_kWh_combined`` for all              |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | oil boilers (ob) in base scenario (i.e.,       | buildings with ``Hot_Water_System`` type                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | current status) for the selected               | ``v_h_ob`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district. Can be calculated from values        | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | contained in :ref:`master_file`.               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 25     | ``v_hw_wb``                                   | float     | Required annual domestic hot water             | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh from         | Aggregated value of ``dhw_estimation_kWh_combined`` for all              |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | wood boilers (wb) in base scenario             | buildings with ``Hot_Water_System`` type                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (i.e., current status) for the selected        | ``v_h_wb`` within the selected                                           |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district. Can be calculated from values        | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | contained in :ref:`master_file`.               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 26     | ``v_hw_solar``                                | float     | Required annual domestic hot watert            | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh from         | Aggregated value of ``dhw_estimation_kWh_combined`` for all              |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | solar thermal in base scenario (i.e.,          | buildings with ``Hot_Water_System`` type                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | current status) for the selected               | ``v_h_solar`` within the selected                                        |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district. Can be calculated from values        | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | contained in :ref:`master_file`.               |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 27     | ``v_hw_other``                                | float     | Required annual domestic hot water             | Calculated from :ref:`master_file`:                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh from         | Aggregated value of ``dhw_estimation_kWh_combined`` for all              |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | other technologies (i.e., unknown) in          | buildings with ``Hot_Water_System`` type                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | base scenario (i.e., current status) for       | ``v_h_other`` within the selected                                        |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the selected district. Can be calculated       | municipality.                                                            |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | from values contained in                       |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | :ref:`master_file`.                            |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 28     | ``Total_Hot_Water``                           | float     | Total required annual domestic hot water       | Calculated as the sum of the values from                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | supply (i.e., heat demand) in kWh as the       | individual technologies (columns 20-27)                                  |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | sum from all technologies in base              |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | scenario (i.e., current status) for the        |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | selected district.                             |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 29     | ``PV_Pot``                                    | float     | Annual rooftop solar photovoltaic              | ``PV_Pot`` values in :ref:`master_file`                                  |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | generation potential of the building (in       | aggregated across municipality.                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | kWh).                                          |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 30     | ``TotalEnergy``                               | float     | Total annual generated energy in kWh           | ``TotalEnergy`` values in :ref:`master_file`                             |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | from solar PV installation.                    | aggregated across municipality.                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 31     | ``kWh_household_sfh``                         | float     | Total annual electricity demand in kWh         | ``kWh_household_sfh`` values in :ref:`master_file`                       |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | for single family houses (SFH) in the          | aggregated across municipality.                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district.                                      |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 32     | ``kWh_household_mfh``                         | float     | Total annual electricity demand in kWh         | ``kWh_household_mfh`` values in :ref:`master_file`                       |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | for multi family houses (MFH) in the           | aggregated across municipality.                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district.                                      |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 33     | ``Electricity_Industry``                      | float     | Annual electricity demand for industry         | ``Electricity_Industry`` values in :ref:`master_file`                    |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (if applicable) in kWh for the selected        | aggregated across municipality.                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district.                                      |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 34     | ``Electricity_Service``                       | float     | Annual electricity demand for services         | ``Electricity_Service`` values in :ref:`master_file`                     |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | (if applicable) in kWh for the selected        | aggregated across municipality.                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district.                                      |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 35     | ``s_wd_bm``                                   | float     | Total woody biomass potential in kWh for       | Value of total woody biomass potential                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the selected district.                         | obtained from Data provided by the Swiss                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           |                                                | Federal Institute for Forest, Snow and                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           |                                                | Landscape Research (WSL). Values are                                     |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           |                                                | originally provided by municipality. The                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           |                                                | value for woody biomass with bark and 0%                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           |                                                | water content is used.                                                   |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 36     | ``s_wet_bm``                                  | float     | Total wet biomass potential in kWh for         | Data provided by the Swiss Federal                                       |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the selected district.                         | Institute for Forest, Snow and Landscape                                 |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           |                                                | Research (WSL) based on Burg et al.                                      |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           |                                                | (2018) and Thees et al. (2017).                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 37     | ``PV_Filename``                               | int       | Identification number of the hourly            | Profile which was simulated closest to                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | solar photovoltaic profile applicable to       | the selected municipality is used. See                                   |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | the district based on profiles provided        | also :ref:`tech_solar_pv`.                                               |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | in :ref:`simulation_profiles` columns          |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | 33-43. E.g., "9" for ``PV_Profile_9``.         |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 38     | ``dh_cap_class_1``                            | float     | Thermal power need of the buildings in         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district energy expansion class 1, pre         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | renovation                                     |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 39     | ``dh_cap_class_2``                            | float     | Thermal power need of the buildings in         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district energy expansion class 2, pre         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | renovation                                     |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 40     | ``dh_cap_class_3``                            | float     | Thermal power need of the buildings in         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district energy expansion class 3, pre         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | renovation                                     |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 41     | ``dh_cap_renov_class_1``                      | float     | Thermal power need of the buildings in         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district energy expansion class 1, post        |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | renovation                                     |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 42     | ``dh_cap_renov_class_2``                      | float     | Thermal power need of the buildings in         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district energy expansion class 2, post        |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | renovation                                     |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 43     | ``dh_cap_renov_class_3``                      | float     | Thermal power need of the buildings in         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | district energy expansion class 3, post        |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | renovation                                     |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 44     | ``dh_avg_dist_class_1``                       | float     | Average distance to neighbouring egids         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | of buildings in district energy                |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | expansion class 1                              |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 45     | ``dh_avg_dist_class_2``                       | float     | Average distance to neighbouring egids         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | of buildings in district energy                |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | expansion class 2                              |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 46     | ``dh_avg_dist_class_3``                       | float     | Average distance to neighbouring egids         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | of buildings in district energy                |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | expansion class 3                              |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 47     | ``m_per_kWh_class_1_renov``                   | float     | Meters of distance to neighbouring             |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings per kWh heat demand for              |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings in district energy expansion         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | class 1, post renovation                       |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 48     | ``m_per_kWh_class_2_renov``                   | float     | Meters of distance to neighbouring             |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings per kWh heat demand for              |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings in district energy expansion         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | class 2, post renovation                       |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 49     | ``m_per_kWh_class_3_renov``                   | float     | Meters of distance to neighbouring             |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings per kWh heat demand for              |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings in district energy expansion         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | class 3, post renovation                       |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 50     | ``m_per_kWh_class_1``                         | float     | Meters of distance to neighbouring             |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings per kWh heat demand for              |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings in district energy expansion         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | class 1, pre renovation                        |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 51     | ``m_per_kWh_class_2``                         | float     | Meters of distance to neighbouring             |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings per kWh heat demand for              |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings in district energy expansion         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | class 2, pre renovation                        |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
| 52     | ``m_per_kWh_class_3``                         | float     | Meters of distance to neighbouring             |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings per kWh heat demand for              |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | buildings in district energy expansion         |                                                                          |
|        |                                               |           |                                                |                                                                          |
|        |                                               |           | class 3, pre renovation                        |                                                                          |
+--------+-----------------------------------------------+-----------+------------------------------------------------+--------------------------------------------------------------------------+
