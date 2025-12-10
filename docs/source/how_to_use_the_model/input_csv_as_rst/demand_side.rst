+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| Attribute                                | Description                              | Standard value                           | Unit | Data type        | Source |
+==========================================+==========================================+==========================================+======+==================+========+
| year                                     | Year to be simulated. Takes into account | 2023                                     | —    | int              |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | future weather scenario and retrofitting |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | of buildings. Options: '2023', '2030',   |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | '2040', '2050'.                          |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| rcp_scenario                             | Representative Concentration Pathways    | 'RCP26'                                  | —    | str              |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | (RCP) for future climate. Options:       |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | 'RCP26'.                                 |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| ts_type                                  | Type of temperature data line to use.    | 'tas_median'                             | —    | str              |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| ev_integration                           | If set to 'true', electrification of     | True                                     | —    | bool             |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | mobility sector will be considered and   |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | electricity demand profiles will be      |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | adjusted accordingly.                    |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| ev_integration_factor                    | Relative strength of the electrification | 100                                      | —    | float            |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | of mobility. At 100, all the remaining   |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | fossil road transport is electrified, at |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | a value smaller than 100, only that      |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | percentage.                              |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| ev_flexibility                           | If set to 'true', the available          | True                                     | —    | bool             |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | flexibility in demand shifting stemming  |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | from the EV demand will be considered in |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | the optimisation.                        |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| total_renovation                         | If set to 'True', the total renovation   | True                                     | —    | bool             |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | of buildings is taken into account. This |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | means that buildings are assumed to be   |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | renovated if they're sufficiently old,   |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | with a certain probability. Totally      |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | renovated buildings are assumed to have  |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | a modern building envelope with          |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | correspondingly low demand for space     |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | heating. Furthermore, their heat         |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | generators are replaced.                 |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| use_constant_total_renovation_rate       | If set to 'True', a constant percentage  | False                                    | —    | bool             |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | of all sufficiently old buildings is     |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | totally renovated in each time step.     |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | Else, renovation happens based on a      |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | model derived from Streicher et al.      |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| renovation_scenario                      | Renovation scenario to use. Options are  | renovation_low'                          | —    | str              |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | 'renovation_low', 'renovation_base' and  |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | 'renovation_high'. It is recommended to  |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | use 'renovation_low'                     |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| constant_total_renovation_rate           | If a constant total renovation rate is   | 0.018                                    | —    | float            |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | used, value of that rate.                |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| total_renovation_heat_generator_reassign | In manual scenarios (no optimization),   | {                                        | —    | Dict[str, float] |        |
|                                          |                                          |                                          |      |                  |        |
| ment_rates_space_heating_for_manual_scen | what heat generators are installed after |             'v_h_eh' : 0.0, 'v_h_hp' :   |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
| arios                                    | total renovation for space heating.      | 0.8, 'v_h_dh' : 0.05, 'v_h_gb' : 0.05,   |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          |                                          | 'v_h_ob' : 0.05,                         |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          |                                          |             'v_h_wb' : 0.05, 'v_h_solar' |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          |                                          | : 0.0, 'v_h_other' : 0.0 }               |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| total_renovation_heat_generator_reassign | In manual scenarios (no optimization),   | {                                        | —    | Dict[str, float] |        |
|                                          |                                          |                                          |      |                  |        |
| ment_rates_dhw_for_manual_scenarios      | what heat generators are installed after |             'v_hw_eh' : 0.05, 'v_hw_hp'  |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | total renovation for domestic hot water  | : 0.0, 'v_hw_dh' : 0.95,                 |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | heating.                                 |             'v_hw_gb' : 0.0, 'v_hw_ob' : |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          |                                          | 0.0, 'v_hw_wb' : 0.0,                    |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          |                                          |             'v_hw_solar' : 0.0,          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          |                                          | 'v_hw_other' : 0.0 }                     |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| heat_generator_renovation                | If 'true', heat generators are replaced  | True                                     | —    | bool             |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | as they reach the end of their life.     |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
| act_on_fossil_heater_retrofit            | Interaction between                      | False                                    | —    | bool             |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | fossile_heater_retrofit and heat         |                                          |      |                  |        |
|                                          |                                          |                                          |      |                  |        |
|                                          | generator renovation                     |                                          |      |                  |        |
+------------------------------------------+------------------------------------------+------------------------------------------+------+------------------+--------+
