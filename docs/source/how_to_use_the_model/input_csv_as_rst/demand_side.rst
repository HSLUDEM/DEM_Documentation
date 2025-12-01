+----------------+------------------------------------------+----------------+------+-----------+--------+
| Attribute      | Description                              | Standard value | Unit | Data type | Source |
+================+==========================================+================+======+===========+========+
| year           | Year to be simulated. Takes into account |                | —    | int       |        |
|                |                                          |                |      |           |        |
|                | future weather scenario and retrofitting |                |      |           |        |
|                |                                          |                |      |           |        |
|                | of buildings. Options: '2023', '2030',   |                |      |           |        |
|                |                                          |                |      |           |        |
|                | '2040', '2050'.                          |                |      |           |        |
+----------------+------------------------------------------+----------------+------+-----------+--------+
| rcp_scenario   | Representative Concentration Pathways    |                | —    | str       |        |
|                |                                          |                |      |           |        |
|                | (RCP) for future climate. Options:       |                |      |           |        |
|                |                                          |                |      |           |        |
|                | 'RCP26'.                                 |                |      |           |        |
+----------------+------------------------------------------+----------------+------+-----------+--------+
| ev_integration | If set to 'true', electrification of     |                | —    | bool      |        |
|                |                                          |                |      |           |        |
|                | mobility sector will be considered and   |                |      |           |        |
|                |                                          |                |      |           |        |
|                | electricity demand profiles will be      |                |      |           |        |
|                |                                          |                |      |           |        |
|                | adjusted accordingly.                    |                |      |           |        |
+----------------+------------------------------------------+----------------+------+-----------+--------+
| ev_flexibility | If set to 'true', the available          |                | —    | bool      |        |
|                |                                          |                |      |           |        |
|                | flexibility in demand shifting stemming  |                |      |           |        |
|                |                                          |                |      |           |        |
|                | from the EV demand will be considered in |                |      |           |        |
|                |                                          |                |      |           |        |
|                | the optimisation.                        |                |      |           |        |
+----------------+------------------------------------------+----------------+------+-----------+--------+
