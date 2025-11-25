+---------------------------------+--------------+-----------+------------------------------------------+
| Attribute                       | Unit         | Data type | Description                              |
+=================================+==============+===========+==========================================+
| deployment                      | —            | bool      | If set to 'true', the technology will be |
|                                 |              |           | considered in the energy system model    |
|                                 |              |           | (this does not necessarily mean it will  |
|                                 |              |           | be used). Only relevant for              |
|                                 |              |           | optimisation.                            |
+---------------------------------+--------------+-----------+------------------------------------------+
| kWp_max                         | kW           | float     | Kilowatt Peak: Maximum power output of   |
|                                 |              |           | wind power system.                       |
+---------------------------------+--------------+-----------+------------------------------------------+
| kWp_max_systemwide              |              | float     |                                          |
+---------------------------------+--------------+-----------+------------------------------------------+
| co2_intensity                   | kg CO2/kWh   | float     | Carbon-dioxide intensity of technology   |
|                                 |              |           | output (annual average value).           |
+---------------------------------+--------------+-----------+------------------------------------------+
| lifetime                        | years        | int       | Expected lifetime of technology before   |
|                                 |              |           | replacement is required.                 |
+---------------------------------+--------------+-----------+------------------------------------------+
| maintenance_cost                | CHF/kWp/year | float     |                                          |
+---------------------------------+--------------+-----------+------------------------------------------+
| capex_CHFpkWp                   | CHF/kWp      | float     | CAPEX cost of technology per unit of     |
|                                 |              |           | capacity.                                |
+---------------------------------+--------------+-----------+------------------------------------------+
| interest_rate                   | —            | float     | Interest rate for computing levelised    |
|                                 |              |           | costs (if required).                     |
+---------------------------------+--------------+-----------+------------------------------------------+
| potential_integration_factor    | —            | float     | Used for scenario                        |
|                                 |              |           | 'wind_power_integration'. This factor    |
|                                 |              |           | specifies the fraction of additional     |
|                                 |              |           | wind power potential to be implemented.  |
|                                 |              |           | The additional wind power potential is   |
|                                 |              |           | based on a a simulation done by Wind-    |
|                                 |              |           | Topo.                                    |
+---------------------------------+--------------+-----------+------------------------------------------+
| virtual_export_tariff           | CHF/kWh      | float     | virtual export tarriff to prefer         |
|                                 |              |           | internal usage of the electricity        |
+---------------------------------+--------------+-----------+------------------------------------------+
| export_subsidy                  | CHF/kWh      | float     | subsidy to make export more likely (and  |
|                                 |              |           | prevent cycling of storages to curtail   |
|                                 |              |           | energy)                                  |
+---------------------------------+--------------+-----------+------------------------------------------+
| wind_power_installed_allocation | —            | str       | Decision on whether the installed wind   |
|                                 |              |           | power will be counted towards the local  |
|                                 |              |           | electricity generation or towards the    |
|                                 |              |           | national electricity mix. Options:       |
|                                 |              |           | 'national', 'local'                      |
+---------------------------------+--------------+-----------+------------------------------------------+
| v_e_wp_national_recalc          | —            | bool      | If set to 'true, recalculation of hourly |
|                                 |              |           | national wind power profile of installed |
|                                 |              |           | capacity will be carried out; default    |
|                                 |              |           | should be 'false', as this is only       |
|                                 |              |           | required when new wind power plants have |
|                                 |              |           | been installed.                          |
+---------------------------------+--------------+-----------+------------------------------------------+
