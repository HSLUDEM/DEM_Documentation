+----------------------------------------+------------------------------------------+--------------------------+------+------------+-----------------+
| Attribute                              | Description                              | Standard value           | Unit | Data type  | Source          |
+========================================+==========================================+==========================+======+============+=================+
| ``nuclear_power_plant_powers``         | Net electric power of the nuclear power  | [1010, 1233, 365, 365]   | —    | List[MW]   | diverse sources |
|                                        |                                          |                          |      |            |                 |
|                                        | plants contributing to the grid supply   |                          |      |            |                 |
|                                        |                                          |                          |      |            |                 |
|                                        | from nuclear. Only the ratio between the |                          |      |            |                 |
|                                        |                                          |                          |      |            |                 |
|                                        | powers matters, as the nuclear share in  |                          |      |            |                 |
|                                        |                                          |                          |      |            |                 |
|                                        | the grid supply is reduced according to  |                          |      |            |                 |
|                                        |                                          |                          |      |            |                 |
|                                        | it using the shutdown years given in the |                          |      |            |                 |
|                                        |                                          |                          |      |            |                 |
|                                        | parameter                                |                          |      |            |                 |
|                                        |                                          |                          |      |            |                 |
|                                        | nuclear_power_plant_shutdown_years.      |                          |      |            |                 |
+----------------------------------------+------------------------------------------+--------------------------+------+------------+-----------------+
| ``nuclear_power_plant_shutdown_years`` | Expected shutdown years of the nuclear   | [2039, 2045, 2033, 2032] | —    | List[year] | diverse sources |
|                                        |                                          |                          |      |            |                 |
|                                        | power plants contributing to the grid    |                          |      |            |                 |
|                                        |                                          |                          |      |            |                 |
|                                        | supply of nuclear power.                 |                          |      |            |                 |
+----------------------------------------+------------------------------------------+--------------------------+------+------------+-----------------+
