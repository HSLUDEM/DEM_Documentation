+----------------------------------+-------------+-----------+------------------------------------------+
| Attribute                        | Unit        | Data type | Description                              |
+==================================+=============+===========+==========================================+
| deployment                       | —           | bool      | If set to 'true', the technology will be |
|                                  |             |           |                                          |
|                                  |             |           | considered in the energy system model    |
|                                  |             |           |                                          |
|                                  |             |           | (this does not necessarily mean it will  |
|                                  |             |           |                                          |
|                                  |             |           | be used). Only relevant for              |
|                                  |             |           |                                          |
|                                  |             |           | optimisation.                            |
+----------------------------------+-------------+-----------+------------------------------------------+
| demand_share_type                |             | str       |                                          |
+----------------------------------+-------------+-----------+------------------------------------------+
| demand_share_val                 |             | float     |                                          |
+----------------------------------+-------------+-----------+------------------------------------------+
| import_kW_th_max                 | kW          | float     | Maximum thermal capacity of heat import  |
|                                  |             |           |                                          |
|                                  |             |           | (from outside the municipality).         |
+----------------------------------+-------------+-----------+------------------------------------------+
| grid_kW_th_max                   | kW          | float     | Maximum thermal capacity of the grid.    |
+----------------------------------+-------------+-----------+------------------------------------------+
| investment_dh_grid_per_m         | CHF/m       | int       |                                          |
+----------------------------------+-------------+-----------+------------------------------------------+
| maintenance_cost_dh_grid_per_m   | CHF/m/year  | int       |                                          |
+----------------------------------+-------------+-----------+------------------------------------------+
| closeness_based_dh_expansio_cost |             | bool      |                                          |
+----------------------------------+-------------+-----------+------------------------------------------+
| capex                            | CHF/kW      | float     |                                          |
+----------------------------------+-------------+-----------+------------------------------------------+
| maintenance_cost                 | CHF/kW/year | float     |                                          |
+----------------------------------+-------------+-----------+------------------------------------------+
| tariff_CHFpkWh                   | CHF/kWh     | float     | Tariff for imported heat.                |
+----------------------------------+-------------+-----------+------------------------------------------+
| co2_intensity                    | kg CO2/kWh  | float     | Carbon-dioxide intensity of technology   |
|                                  |             |           |                                          |
|                                  |             |           | output (annual average value).           |
+----------------------------------+-------------+-----------+------------------------------------------+
| lifetime                         | years       | int       | Expected lifetime of technology before   |
|                                  |             |           |                                          |
|                                  |             |           | replacement is required.                 |
+----------------------------------+-------------+-----------+------------------------------------------+
| interest_rate                    | —           | float     | Interest rate for computing levelised    |
|                                  |             |           |                                          |
|                                  |             |           | costs (if required).                     |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources                     | —           | dict      | Connected heat sources                   |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: import             | —           | bool      | If set to 'true', heat import is allowed |
|                                  |             |           |                                          |
|                                  |             |           | (based on 'import_kW_th_max')            |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: chp_gt             | —           | bool      | If set to 'true', CHP gas turbine plant  |
|                                  |             |           |                                          |
|                                  |             |           | is connected to district heating network |
|                                  |             |           |                                          |
|                                  |             |           | (DHN). Technology must be deployed       |
|                                  |             |           |                                          |
|                                  |             |           | accordingly.                             |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: steam_turbine      | —           | bool      | If set to 'true', steam turbine is       |
|                                  |             |           |                                          |
|                                  |             |           | connected to the DHN. Technology must be |
|                                  |             |           |                                          |
|                                  |             |           | deployed accordingly.                    |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: waste_to_energy    | —           | bool      | If set to 'true', the waste-to-energy    |
|                                  |             |           |                                          |
|                                  |             |           | plant is connected to the DHN.           |
|                                  |             |           |                                          |
|                                  |             |           | Technology must be deployed accordingly. |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: heat_pump_cp       | —           | bool      | If set to 'true', a central heat pump is |
|                                  |             |           |                                          |
|                                  |             |           | connected to the DHN. Technology must be |
|                                  |             |           |                                          |
|                                  |             |           | deployed accordingly.                    |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: heat_pump_cp_lt    | —           | bool      | If set to 'true', a central heat pump    |
|                                  |             |           |                                          |
|                                  |             |           | converting low-temperature waste heat    |
|                                  |             |           |                                          |
|                                  |             |           | into useful heat is connected to the     |
|                                  |             |           |                                          |
|                                  |             |           | DHN. Technology must be deployed         |
|                                  |             |           |                                          |
|                                  |             |           | accordingly.                             |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: oil_boiler_cp      | —           | bool      | If set to 'true', a central oil boiler   |
|                                  |             |           |                                          |
|                                  |             |           | is connected to the DHN. Technology must |
|                                  |             |           |                                          |
|                                  |             |           | be deployed accordingly.                 |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: electric_heat_cp   | —           | bool      | If set to 'true', a central electric     |
|                                  |             |           |                                          |
|                                  |             |           | resistance heater is connected to the    |
|                                  |             |           |                                          |
|                                  |             |           | DHN. Technology must be deployed         |
|                                  |             |           |                                          |
|                                  |             |           | accordingly.                             |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: wood_boiler_cp     | —           | bool      | If set to 'true', a central wood boiler  |
|                                  |             |           |                                          |
|                                  |             |           | is connected to the DHN. Technology must |
|                                  |             |           |                                          |
|                                  |             |           | be deployed accordingly.                 |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: gas_boiler_cp      | —           | bool      | If set to 'true', a central gas boiler   |
|                                  |             |           |                                          |
|                                  |             |           | is connected to the DHN. Technology must |
|                                  |             |           |                                          |
|                                  |             |           | be deployed accordingly.                 |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: waste_heat         | —           | bool      | If set to 'true', a hot waste heat       |
|                                  |             |           |                                          |
|                                  |             |           | source is connected to the DHN.          |
|                                  |             |           |                                          |
|                                  |             |           | Technology must be deployed accordingly. |
+----------------------------------+-------------+-----------+------------------------------------------+
| heat_sources: biomass            | —           | bool      | If set to 'true', biomass technologies   |
|                                  |             |           |                                          |
|                                  |             |           | are connected to the DHN. Technology     |
|                                  |             |           |                                          |
|                                  |             |           | must be deployed accordingly.            |
+----------------------------------+-------------+-----------+------------------------------------------+
