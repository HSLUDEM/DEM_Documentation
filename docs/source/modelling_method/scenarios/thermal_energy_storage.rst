.. thermal-energy-storage-scenario:

Thermal Energy Storage Scenario
=======================================

The thermal energy storage scenario represents
the usage of local thermal energy storage
coupled with heat pumps to store surplus energy
from local renewable production.

The size of the storage is given by the
capacity_kWh parameter in the tes_decentralized 
technology.
The storage is charged whenever the local production
of wind power, solar PV and local hydropower is larger
than the electricity demand. For charging, heat pumps
are used. The storage is modelled as lossless storage.
The storage is discharged as soon as the
local renewable electricity production dips below the
demand.

The thermal energy storage scenario is not compatible
with the battery energy storage scenario.
