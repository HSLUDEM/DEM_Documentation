+-----------------------+------------------------------------------+----------------+--------------+-----------+
| Attribute             | Description                              | Standard value | Unit         | Data type |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``deployment``        | If set to 'true', the technology will be | False          | —            | bool      |
|                       |                                          |                |              |           |
|                       | considered in the energy system model    |                |              |           |
|                       |                                          |                |              |           |
|                       | (this does not necessarily mean it will  |                |              |           |
|                       |                                          |                |              |           |
|                       | be used). Only relevant for              |                |              |           |
|                       |                                          |                |              |           |
|                       | optimisation.                            |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``kW_el_max``         | Maximum electrical power output.         | inf            | kW_el        | str/float |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``force_cap_max``     | Force implementation of maximum capacity | False          | kW           | bool      |
|                       |                                          |                |              |           |
|                       | specified in kW_el_max. Only relevant    |                |              |           |
|                       |                                          |                |              |           |
|                       | for optimisation.                        |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``cap_min_use``       |                                          | 0              | kW           | float     |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``annual_msw_supply`` |                                          | inf            | kg/year      | str       |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``hv_msw_MJpkg``      | Lower heating value of municipal solid   | 12             | MJ/kg        | float     |
|                       |                                          |                |              |           |
|                       | waste (MSW).                             |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``eta_el``            | Electrical conversion efficiency.        | 0.35           | —            | float     |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``htp_ratio``         | Heat-to-power (htp) ratio (kW_th/kW_el)  | 1.5            | kW_th/kW_el  | float     |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``msw_price_CHFpkg``  | Price of municipal solid waste. Will     | -0.3           | CHF/kg       | float     |
|                       |                                          |                |              |           |
|                       | usually be negative (i.e. revenue).      |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``co2_intensity``     | Carbon-dioxide intensity of technology   | 0.645          | kg CO2/kWh   | float     |
|                       |                                          |                |              |           |
|                       | output (annual average value).           |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``lifetime``          | Expected lifetime of technology before   | 25             | years        | int       |
|                       |                                          |                |              |           |
|                       | replacement is required.                 |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``capital_cost``      | CAPEX cost of technology per unit of     | 2000           | CHF/kWp      | float     |
|                       |                                          |                |              |           |
|                       | capacity.                                |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``maintenance_cost``  | OPEX cost of technology per unit of      | 119            | CHF/kWp/year | float     |
|                       |                                          |                |              |           |
|                       | capacity.                                |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
| ``interest_rate``     | Interest rate for computing levelised    | 0.025          | —            | float     |
|                       |                                          |                |              |           |
|                       | costs (if required).                     |                |              |           |
+-----------------------+------------------------------------------+----------------+--------------+-----------+
