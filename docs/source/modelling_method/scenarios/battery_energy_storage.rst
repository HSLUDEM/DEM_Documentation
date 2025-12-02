.. _battery-energy-storage-scenario:

Battery Energy Storage Scenario
=======================================

The battery energy storage scenario is a manual
scenario that describes the deployment of 
battery electric energy storage (BES) to 
store local renewable energy.

The BES is charged when the local renewable electric energy
production is higher than the demand. The local renewable
electricity production consists of solar PV, wind turbines
and local hydropower. 

The BES is discharged as soon as the local renewable
electricity production dips below the demand, until it 
is fully discharged. The capacity of the BES that is
deployed is given by the parameter capacity_kWh of the
bes technology. The BES is modelled to have both charging
and discharging losses and a constant loss rate each hour.

The BES scenario is not compatible with the TES scenario.



