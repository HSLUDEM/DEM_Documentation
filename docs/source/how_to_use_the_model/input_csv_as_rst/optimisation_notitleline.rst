+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| Attribute                        | Description                              | Standard value | Unit    | Data type | Source |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``enabled``                      | MILP optimisation is enabled if set to   | False          | —       | bool      |        |
|                                  |                                          |                |         |           |        |
|                                  | "True".                                  |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``clustering``                   | *Deprecated: This option is not          | False          | —       | bool      |        |
|                                  |                                          |                |         |           |        |
|                                  | available.*                              |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``pareto_monetary_co2``          | Set to True to calculate a pareto front  | False          | —       | bool      |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``N_pareto``                     | Number of pareto points                  | 6              | —       | int       |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``objective_monetary``           | Weight of monetary objective for         | 1              | —       | float     |        |
|                                  |                                          |                |         |           |        |
|                                  | objective function in optimisation.      |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``objective_co2``                | Weight of emissions objective for        | 0              | —       | float     |        |
|                                  |                                          |                |         |           |        |
|                                  | objective function in optimisation.      |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``objective_ess``                | Not yet implemented.                     | 0              | —       | float     |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``objective_tss``                | Not yet implemented.                     | 0              | —       | float     |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``bigM_value``                   | Default: 1e9; cost of unmet demand;      | 100000         | CHF/kWh | float     |        |
|                                  |                                          |                |         |           |        |
|                                  | large value makes model convergence      |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | slow; https://calliope.readthedocs.io/en |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | /stable/user/building.html#allowing-for- |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | unmet-demand                             |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``solver``                       | Solver for optimisation, e.g. 'cbc',     | 'gurobi'       | —       | string    |        |
|                                  |                                          |                |         |           |        |
|                                  | 'gurobi', etc. Must be compatible with   |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | Calliope.                                |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``solver_option_NumericFocus``   | Default: 0; https://docs.gurobi.com/proj | 1              | —       | int       |        |
|                                  |                                          |                |         |           |        |
|                                  | ects/optimizer/en/current/reference/para |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | meters.html#parameternumericfocus        |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``solver_option_TimeLimit``      | Default: 'Infinity'; https://docs.gurobi | 36000          | s       | int       |        |
|                                  |                                          |                |         |           |        |
|                                  | .com/projects/optimizer/en/current/refer |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | ence/parameters.html#timelimit           |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``solver_option_Presolve``       | Default: -1; https://docs.gurobi.com/pro | -1             | —       | int       |        |
|                                  |                                          |                |         |           |        |
|                                  | jects/optimizer/en/current/reference/par |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | ameters.html#presolve                    |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``solver_option_Aggregate``      | Default: 1; https://docs.gurobi.com/proj | 1              | —       | int       |        |
|                                  |                                          |                |         |           |        |
|                                  | ects/optimizer/en/current/reference/para |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | meters.html#aggregate                    |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``solver_option_FeasibilityTol`` | Default: 1e-6; https://docs.gurobi.com/p | 0.01           | var     | float     |        |
|                                  |                                          |                |         |           |        |
|                                  | rojects/optimizer/en/current/reference/p |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | arameters.html#feasibilitytol            |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``solver_option_MIPGap``         | Default: 1e-4; https://docs.gurobi.com/p | 0.0001         | —       | float     |        |
|                                  |                                          |                |         |           |        |
|                                  | rojects/optimizer/en/current/reference/p |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | arameters.html#mipgap                    |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``MIPGap_increase``              | If set to True, MIPGap will be increased | False          | —       | bool      |        |
|                                  |                                          |                |         |           |        |
|                                  | to 0.01 if a storage technology is       |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | activated in order to avoid numerical    |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | problems.                                |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``save_math_model``              | If set to 'true', the math. model        | False          | —       | bool      |        |
|                                  |                                          |                |         |           |        |
|                                  | formulations are written to an .lp file; |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | can take long to produce and result in   |                |         |           |        |
|                                  |                                          |                |         |           |        |
|                                  | large file;                              |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
| ``save_calliope_files``          | If set to 'True', the calliope files     | False          | —       | bool      |        |
|                                  |                                          |                |         |           |        |
|                                  | (input and results) will be saved.       |                |         |           |        |
+----------------------------------+------------------------------------------+----------------+---------+-----------+--------+
