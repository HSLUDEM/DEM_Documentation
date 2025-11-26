Battery Energy Storage (BES)
=======================================

The BES technology represents a battery electric storage system
connected to the electric grid. 
It can be either a small scale battery, a swarm of small scale
batteries or grid scale batteries. The definition of the technology
is not defining this, but only maintenance and capital cost.

It can be charged by all 
the technologies that are defined via the connections parameters in
the input file. The battery has a given maximum capacity that can be set
by the optimizer if optimization is activated. When charging and
discharging, a fixed loss rate is applied. Furthermore, the storage
loses energy at a constant rate. The electric energy stored in batteries
can be discharged to any consumers in the local district.

Using the parameter force_asynchronous_prod_con, the optimizer can be 
forced to never charge and discharge the storage at the same time.
This can be useful to prevent the energy system from disposing of 
electric energy using the charging and discharging losses of the 
storage.

The initial charge of the storage is usually set to be optimized. Then,
the constraint is that the initial and final storage level have to be 
equal. Alternatively, a fixed initial state of charge can be defined.

.. include:: ../../how_to_use_the_model/input_csv_as_rst/bes.rst

The variables of the 

+--------------------+-----------+
| Quantity           | Symbol    |
+====================+===========
| Contained energy   | q_e_bes   |
+--------------------+-----------+
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

.. math:: \mathtt{q\_e\_bes}(t+1) = \mathtt{q\_e\_bes}(t) - \gamma \mathtt{q\_e\_bes}(t) + \eta \mathtt{u\_e\_bes}(t+1) - (1/\eta) \mathtt{v\_e\_bes}(t+1)

where we refer to bes_gamma as :math:`\gamma` and to eta_chg_dchg as :math:`\eta`. 
Importantly, the charging and discharging powers are measured at the system connection, 
not directly at the storage. Therefore, the amount of energy charged into the storage
is smaller than the charging power u_e_bes and the amount energy discharged from the
storage is larger than v_e_bes, both by  a factor eta_chg_dchg.

Importantly, the value given in q_e_bes is the stored energy at the end of a given time period.






