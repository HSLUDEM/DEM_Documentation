+---------------------------------------+--------------+-----------+------------------------------------------+
| Attribute                             | Unit         | Data type | Description                              |
+=======================================+==============+===========+==========================================+
| deployment                            | —            | bool      | If set to 'true', the technology will be |
|                                       |              |           |                                          |
|                                       |              |           | considered in the energy system model    |
|                                       |              |           |                                          |
|                                       |              |           | (this does not necessarily mean it will  |
|                                       |              |           |                                          |
|                                       |              |           | be used). Only relevant for              |
|                                       |              |           |                                          |
|                                       |              |           | optimisation.                            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| force_asynchronous_prod_con           | —            | bool      | If set to 'true', the tes cannot be      |
|                                       |              |           |                                          |
|                                       |              |           | charged and discharged simultaneously    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| eta_chg_dchg                          | —            | float     | Charging and discharging efficiency      |
|                                       |              |           |                                          |
|                                       |              |           | (fixed). Roundtrip-efficiency is         |
|                                       |              |           |                                          |
|                                       |              |           | calculated as eta_chg_dchg*eta_chg_dchg. |
+---------------------------------------+--------------+-----------+------------------------------------------+
| tes_gamma                             | 1/timestep   | float     | Loss rate: fraction of heat lost to the  |
|                                       |              |           |                                          |
|                                       |              |           | environment during one timestep (e.g. 1  |
|                                       |              |           |                                          |
|                                       |              |           | hour)                                    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| capacity_kWh                          | kWh          | float     | Storage capacity.                        |
+---------------------------------------+--------------+-----------+------------------------------------------+
| force_cap_max                         |              | bool      |                                          |
+---------------------------------------+--------------+-----------+------------------------------------------+
| chg_dchg_per_cap_max                  | 1/timestep   | float     | Max. charge/discharge (kW) per storage   |
|                                       |              |           |                                          |
|                                       |              |           | cap (kWh) per timestep.                  |
+---------------------------------------+--------------+-----------+------------------------------------------+
| initial_charge                        | —            | float     | Initial charge of battery (fraction of   |
|                                       |              |           |                                          |
|                                       |              |           | total storage capacity)                  |
+---------------------------------------+--------------+-----------+------------------------------------------+
| optimized_initial_charge              |              | bool      |                                          |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections                           | —            | dict      | Technologies connected to TES can be     |
|                                       |              |           |                                          |
|                                       |              |           | switched on (True) of off (False).       |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: district_heating_network | —            | bool      | If set to 'true', the district heating   |
|                                       |              |           |                                          |
|                                       |              |           | network is connected to TES. Technology  |
|                                       |              |           |                                          |
|                                       |              |           | must be deployed accordingly.            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: district_heat_import     | —            | bool      | If set to 'true', district_heat_import   |
|                                       |              |           |                                          |
|                                       |              |           | is connected to TES. Technology must be  |
|                                       |              |           |                                          |
|                                       |              |           | deployed accordingly.                    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: chp_gt                   | —            | bool      | If set to 'true', the CHP gas turbine is |
|                                       |              |           |                                          |
|                                       |              |           | connected to TES. Technology must be     |
|                                       |              |           |                                          |
|                                       |              |           | deployed accordingly.                    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: steam_turbine            | —            | bool      | If set to 'true', the steam turbine is   |
|                                       |              |           |                                          |
|                                       |              |           | connected to TES. Technology must be     |
|                                       |              |           |                                          |
|                                       |              |           | deployed accordingly.                    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: waste_to_energy          | —            | bool      | If set to 'true', the waset-to-energy    |
|                                       |              |           |                                          |
|                                       |              |           | plant is connected to TES. Technology    |
|                                       |              |           |                                          |
|                                       |              |           | must be deployed accordingly.            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: oil_boiler_cp            | —            | bool      | If set to 'true', a centralised oil      |
|                                       |              |           |                                          |
|                                       |              |           | boiler is connected to TES. Technology   |
|                                       |              |           |                                          |
|                                       |              |           | must be deployed accordingly.            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: electric_heater_cp       | —            | bool      | If set to 'true', a centralised electric |
|                                       |              |           |                                          |
|                                       |              |           | heater is connected to TES. Technology   |
|                                       |              |           |                                          |
|                                       |              |           | must be deployed accordingly.            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: wood_boiler_cp           | —            | bool      | If set to 'true', a centralised wood     |
|                                       |              |           |                                          |
|                                       |              |           | boiler is connected to TES. Technology   |
|                                       |              |           |                                          |
|                                       |              |           | must be deployed accordingly.            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: gas_boiler_cp            | —            | bool      | If set to 'true', a centralised gas      |
|                                       |              |           |                                          |
|                                       |              |           | boiler is connected to TES. Technology   |
|                                       |              |           |                                          |
|                                       |              |           | must be deployed accordingly.            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: heat_pump_cp             | —            | bool      | If set to 'true', a centralised heat     |
|                                       |              |           |                                          |
|                                       |              |           | pump is connected to TES. Technology     |
|                                       |              |           |                                          |
|                                       |              |           | must be deployed accordingly.            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: heat_pump_cp_lt          | —            | bool      | If set to 'true', a centralised heat     |
|                                       |              |           |                                          |
|                                       |              |           | pump converting low-temperature waste    |
|                                       |              |           |                                          |
|                                       |              |           | heat to high-temperature useful heat is  |
|                                       |              |           |                                          |
|                                       |              |           | connected to TES. Technology must be     |
|                                       |              |           |                                          |
|                                       |              |           | deployed accordingly.                    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: waste_heat               | —            | bool      | If set to 'true', a waste heat source is |
|                                       |              |           |                                          |
|                                       |              |           | connected to TES. Technology must be     |
|                                       |              |           |                                          |
|                                       |              |           | deployed accordingly.                    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| connections: biomass                  | —            | bool      | If set to 'true', a biomass technologies |
|                                       |              |           |                                          |
|                                       |              |           | are connected to TES. Technology must be |
|                                       |              |           |                                          |
|                                       |              |           | deployed accordingly.                    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| co2_intensity                         | kg CO2/kWh   | float     | Carbon-dioxide intensity of technology   |
|                                       |              |           |                                          |
|                                       |              |           | output (annual average value).           |
+---------------------------------------+--------------+-----------+------------------------------------------+
| lifetime                              | years        | int       | Expected lifetime of technology before   |
|                                       |              |           |                                          |
|                                       |              |           | replacement is required.                 |
+---------------------------------------+--------------+-----------+------------------------------------------+
| capex                                 | CHF/kWh      | float     | CAPEX of TES per kWh capacity            |
+---------------------------------------+--------------+-----------+------------------------------------------+
| maintenance_cost                      | CHF/kWh/year | float     | OPEX of TES per kWh capacity and year    |
+---------------------------------------+--------------+-----------+------------------------------------------+
| interest_rate                         | —            | float     | Interest rate for computing levelised    |
|                                       |              |           |                                          |
|                                       |              |           | costs (if required).                     |
+---------------------------------------+--------------+-----------+------------------------------------------+
