Battery Energy Storage (BES)
=======================================

This technology represent a battery electric energy storage device.
It charges and discharges electric energy.
It has the following properties, to be defined in the input file

+------------------------------+------------------+--------------------------------------------+
| Name                         | Standard Value   | Description                                |
+==============================+==================+============================================+
| deployment                   | True             | Defines whether this technology is deployed|
+------------------------------+------------------+--------------------------------------------+
|| force_asynchronous_prod_con || global variable || If True, charging and discharging         |
||                             ||                 || at the same time is not possible          |
+------------------------------+------------------+--------------------------------------------+
| eta_chg_dchg                 | 0.95             | Efficiency of charging and discharging     |
+------------------------------+------------------+--------------------------------------------+
| bes_gamma                    | 0.001            | Storage losses                             |
+------------------------------+------------------+--------------------------------------------+
|| capacity_kWh                || 'inf'           ||                                           |
||                             ||                 ||                                           |
+------------------------------+------------------+--------------------------------------------+
|| chg_dchg_per_cap_max        || 0.1             || Maximum charge or discharge               |
||                             ||                 || flow per time unit (per hour)             |
+------------------------------+------------------+--------------------------------------------+
| initial_charge               | global variable  | initial charge of the battery at t=0       |
+------------------------------+------------------+--------------------------------------------+
|| optimized_initial_charge    || True            || If True, initial_charge is                |
||                             ||                 || determined within the optimization        |
||                             ||                 || s.t. the initial charge                   |
||                             ||                 || and the final charge are the same         |
+------------------------------+------------------+--------------------------------------------+
| co2_intensity                | 0                | CO_2 intensity                             |
+------------------------------+------------------+--------------------------------------------+
| lifetime                     | 10               | Lifetime of the battery, in years          |
+------------------------------+------------------+--------------------------------------------+
| interest_rate                | global variable  | interest rate for LCC calculation          |
+------------------------------+------------------+--------------------------------------------+
| capex                        | 500              | Capital expenditure per kWh                |
+------------------------------+------------------+--------------------------------------------+
| maintenance_cost             | 2.0              | Yearly maintenance cost per kWh            |
+------------------------------+------------------+--------------------------------------------+

