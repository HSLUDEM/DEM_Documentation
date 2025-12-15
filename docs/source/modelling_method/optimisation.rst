Optimisation
=================

The optimisation module allows for an optimisation of the energy 
system using a cost function with can consist of monetary
or carbon cost or a combination of the two quantities.

The optimisation relies on using a LP or MILP
optimizer accessed via the energy system optimization
framework Calliope (Pfenninger & Pickering, 2018). Via Calliope, a solver, such as Gurobi,
is accessed.

The optimisation happens using the methods built into the optimizer.
The more technologies are present in the energy system,
the longer the optimisation takes.
Activating integer variables (i.e. the asynchronous storage)
leads to significantly longer optimisation times.

In addition to the conventional optimisation mode, a 
pareto front mode is also available. In this mode, a 
monetary-co2 pareto front is constructed.

The parameters of the optimisation are

.. include:: ../how_to_use_the_model/input_csv_as_rst/optimisation.rst


References
-----------

Pfenninger, S., & Pickering, B. (2018). *Calliope: a multi-scale energy systems modelling framework.* Journal of Open Source Software, 3(29), 825. |Pfenninger2018_DOI_link|

.. |Pfenninger2018_DOI_link| raw:: html

   <a href="https://doi.org/10.21105/joss.00825" target="_blank">https://doi.org/10.21105/joss.00825</a>