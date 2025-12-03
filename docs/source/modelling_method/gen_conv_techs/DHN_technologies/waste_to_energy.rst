Waste To Energy
=======================================

The Waste To Energy technology represents a waste
incineration plant. It co-generates electricity and
useful heat that can be used directly in the 
district heating network.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/waste_to_energy.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_e\_wte} = \mathtt{eta\_el} \cdot \mathtt{u\_msw\_wte} 

.. math:: \mathtt{v\_h\_wte} = \mathtt{htp\_ratio} \cdot \mathtt{eta\_el} \cdot \mathtt{u\_msw\_wte} 

The symbols and names of the flows are

.. include:: ../../../how_to_use_the_model/flows_tables/wte.rst
