Steam Turbine
=======================================

The steam turbine is a large-scale technology connected
to the district heating and electric grid. It converts
hot steam into electricity and useful heat.
Its heat output can be used directly for district heating.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/steam_turbine.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_e\_st} = \mathtt{eta\_el} \cdot \mathtt{u\_steam\_st} 

.. math:: \mathtt{v\_h\_st} = \mathtt{htp\_ratio} \cdot \mathtt{eta\_el} \cdot \mathtt{u\_steam\_st} 