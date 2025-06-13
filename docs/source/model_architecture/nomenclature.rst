Nomenclature and Abbreviations
==============================

+------------------------+------------+----------+----------+
| Header row, column 1   | Header 2   | Header 3 | Header 4 |
| (header rows optional) |            |          |          |
+========================+============+==========+==========+
| body row 1, column 1   | column 2   | column 3 | column 4 |
+------------------------+------------+----------+----------+
| body row 2             | ...        | ...      |          |
+------------------------+------------+----------+----------+

+--------------------------+---------------------------------------------------+
|                          |                                                   |
| **General:**             |                                                   |
| _com                    | community                                         |
| _pot                    | potential                                         |
| _base                   | values for current situation                      |
|                          |                                                  |
| **Data type:**          |                                                   |
| df                      | dataframe                                         |
| ds                      | dataseries                                        |
| list                    | list                                              |
|                          |                                                  |
| **Energy flows:**       |                                                   |
| d                       | demand                                            |
| m                       | import                                            |
| u                       | technology input                                  |
| v                       | technology output                                 |
| l                       | losses                                            |
| s                       | supply                                            |
| src                     | source                                            |
|                          |                                                  |
| **Technologies:**       |                                                   |
| _pv                     | solar photovoltaic                                |
| _solar                  | solar thermal                                     |
| _wp                     | wind power                                        |
| _grid                   | grid supply (electricity)                         |
| _hp                     | heat pump                                         |
| _eh                     | electric heater                                   |
| _ob                     | oil boiler                                        |
| _wb                     | wood boiler                                       |
| _gb                     | gas boiler                                        |
| _dh                     | district heating                                  |
| _tes                    | thermal energy storage                            |
| _bes                    | battery energy storage                            |
| _hydro                  | hydro power                                       |
| _bm                     | biomass (collective)                              |
| _hg                     | hydrothermal gasification                         |
| _agu                    | anaerobic digestion upgrade                       |
| _aguh                   | anaerobic digestion upgrade hydrogen              |
| _aguc                   | anaerobic digestion CHP                           |
| _wgu                    | wood gasification upgrade                         |
| _wguh                   | wood gasification upgrade hydrogen                |
| _wguc                   | wood gasification CHP                             |
| _hydp                   | hydrogen production                               |
| _chpgt                  | CHP gas turbine                                   |
| _gtcp                   | gas turbine (central plant)                       |
| _st                     | steam turbine                                     |
| _wbcp                   | wood boiler (central plant)                       |
| _wte                    | waste-to-energy plant                             |
| _hpcp                   | heat pump (central plant)                         |
|                          |                                                  |
| **Technology parameters:** |                                                |
| _p                      | system size (kW or kWp)                           |
| sos                     | state of storage (-)                              |
| _q                      | energy level, e.g. in storage (kWh)               |
|                          |                                                  |
| **Energy carriers:**    |                                                   |
| _h                      | heat                                              |
| _e                      | electricity                                       |
| _gas                    | gas                                               |
| _oil                    | oil                                               |
| _wd                     | wood                                              |
| _msw                    | municipal solid waste                             |
| _bm                     | biomass                                           |
| _steam                  | steam                                             |
|                          |                                                  |
| **Emission carriers:**  |                                                   |
| _co2                    | CO2 (kg)                                          |
|                          |                                                  |
| **Time resolution:**    |                                                   |
| _hr                     | hourly (mostly omitted)                           |
| _yr                     | annual                                            |
|                          |                                                  |
| **Aggregation resolution:** |                                               |
| _bdg                    | building level                                    |
|                          |                                                  |
| **Iteration indeces:**  |                                                   |
| _t                      | time                                              |
|                          |                                                  |
| **Examples:**           |                                                   |
| u_e_hp                  | electricity input to heat pump (kWh)              |
| v_h_hp                  | heat output from heat pump (kWh)                  |
| d_e_yr                  | annual electricity demand (kWh)                   |
+--------------------------+---------------------------------------------------+



