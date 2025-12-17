+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| Attribute                           | Description                              | Standard value | Unit         | Data type | Source |
+=====================================+==========================================+================+==============+===========+========+
| ``deployment``                      | If set to 'true', the technology will be | True           | —            | bool      |        |
|                                     |                                          |                |              |           |        |
|                                     | considered in the energy system model    |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | (this does not necessarily mean it will  |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | be used). Only relevant for              |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | optimisation.                            |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``kWp_max``                         | Kilowatt Peak: Maximum power output of   | 1e+32          | kW           | float     |        |
|                                     |                                          |                |              |           |        |
|                                     | wind power system.                       |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``kWp_max_systemwide``              |                                          | 'inf'          |              | float     |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``co2_intensity``                   | Carbon-dioxide intensity of technology   | 0              | kg CO2/kWh   | float     |        |
|                                     |                                          |                |              |           |        |
|                                     | output (annual average value).           |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``lifetime``                        | Expected lifetime of technology before   | 25             | years        | int       |        |
|                                     |                                          |                |              |           |        |
|                                     | replacement is required.                 |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``maintenance_cost``                |                                          | 11.3           | CHF/kWp/year | float     |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``capex_CHFpkWp``                   | CAPEX cost of technology per unit of     | 2075           | CHF/kWp      | float     |        |
|                                     |                                          |                |              |           |        |
|                                     | capacity.                                |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``interest_rate``                   | Interest rate for computing levelised    | 0.025          | —            | float     |        |
|                                     |                                          |                |              |           |        |
|                                     | costs (if required).                     |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``potential_integration_factor``    | Used for scenario                        | 0              | —            | float     |        |
|                                     |                                          |                |              |           |        |
|                                     | 'wind_power_integration'. This factor    |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | specifies the fraction of additional     |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | wind power potential to be implemented.  |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | The additional wind power potential is   |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | based on a a simulation done by Wind-    |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | Topo.                                    |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``virtual_export_tariff``           | virtual export tarriff to prefer         | 0              | CHF/kWh      | float     |        |
|                                     |                                          |                |              |           |        |
|                                     | internal usage of the electricity        |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``export_subsidy``                  | subsidy to make export more likely (and  | 0              | CHF/kWh      | float     |        |
|                                     |                                          |                |              |           |        |
|                                     | prevent cycling of storages to curtail   |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | energy)                                  |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``wind_power_installed_allocation`` | Decision on whether the installed wind   |                | —            | str       |        |
|                                     |                                          |                |              |           |        |
|                                     | power will be counted towards the local  |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | electricity generation or towards the    |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | national electricity mix. Options:       |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | 'national', 'local'                      |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
| ``v_e_wp_national_recalc``          | If set to 'true, recalculation of hourly |                | —            | bool      |        |
|                                     |                                          |                |              |           |        |
|                                     | national wind power profile of installed |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | capacity will be carried out; default    |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | should be 'false', as this is only       |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | required when new wind power plants have |                |              |           |        |
|                                     |                                          |                |              |           |        |
|                                     | been installed.                          |                |              |           |        |
+-------------------------------------+------------------------------------------+----------------+--------------+-----------+--------+
