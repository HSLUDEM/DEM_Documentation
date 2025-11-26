CHP GT (Combined Heat and Power Gas Turbine)
=======================================

The combined heat-and-power gas turbine represents a gas turbine
that is directly used to co-produce heat and power from gas.
It is connected to the district heating network.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/chp_gt.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_e\_chpgt} = \mathtt{eta\_el} \cdot \mathtt{u\_gas\_chpgt} 

.. math:: \mathtt{v\_h\_chpgt} = \mathtt{htp\_ratio} \cdot \mathtt{eta\_el} \cdot \mathtt{u\_gas\_chpgt} 