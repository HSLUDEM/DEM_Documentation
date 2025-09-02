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

The variables of the 

+--------------------+-----------+
| Contained energy   | q_e_bes   |
+====================+===========+
| Charging power     | u_e_bes   |
+--------------------+-----------+
| Discharging power  | v_e_bes   |
+--------------------+-----------+
| Storage losses     | l_q_e_bes |
+--------------------+-----------+
| Charging losses    | l_u_e_bes |
+--------------------+-----------+
| Discharging losses | l_v_e_bes |
+--------------------+-----------+

The relationship between q_e_bes(t) and q_e_bes(t+1) is given by

.. math:: \mathtt{q\_e\_bes}(t+1) = \mathtt{q\_e\_bes}(t) - \gamma \mathtt{q\_e\_bes}(t) + \eta \mathtt{u\_e\_bes} - (1/\eta) \mathtt{v\_e\_bes}

where we refer to bes_gamma as :math:`\gamma` and to eta_chg_dchg as :math:`\eta`. 
Importantly, the charging and discharging powers are measured at the system connection, 
not directly at the storage. Therefore, the amount of energy charged into the storage
is smaller than the charging power u_e_bes and the amount energy discharged from the
storage is larger than v_e_bes, both by  a factor eta_chg_dchg.

