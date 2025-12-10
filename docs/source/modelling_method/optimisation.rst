Optimisation
=================

The optimisation module allows for an optimisation of the energy 
system using a cost function with can consist of monetary
or carbon cost or a combination of the two quantities.

The optimisation relies on using a LP or MILP
optimizer accessed via the energy system optimization
framework calliope. Via calliope, a solver, such as Gurobi,
is accessed.

In addition to the conventional optimisation mode, a 
pareto front mode is also available. In this mode, a 
monetary-co2 pareto front is constructed.

The parameters of the optimisation are

.. include:: ../how_to_use_the_model/input_csv_as_rst/optimisation.rst
