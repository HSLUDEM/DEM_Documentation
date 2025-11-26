Gas Turbine Central Plant
=======================================

The gas turbine central plant burns gas
to co-generate steam and electricity.
The steam can then be used in a steam turbine
to co-generate electricity and heat.

.. include:: ../../../how_to_use_the_model/input_csv_as_rst/gas_turbine_cp.rst

The relationship between the in- and outflows is given by

.. math:: \mathtt{v\_e\_gtcp} = \mathtt{eta\_el} \cdot \mathtt{u\_gas\_gtcp}

.. math:: \mathtt{v\_steam\_gtcp} = \mathtt{htp\_ratio} \cdot \mathtt{eta\_el} \cdot \mathtt{u\_gas\_gtcp}
