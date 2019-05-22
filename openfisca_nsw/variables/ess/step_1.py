# Import from openfisca-core the common Python objects used to code the legislation in OpenFisca
from openfisca_core.model_api import *
# Import the Entities specifically defined for this tax and benefit system
from openfisca_nsw.entities import *


class measured_electricity_consumption(Variable):
    value_type = int
    entity = Building
    definition_period = DAY
    label = "Measured Electricity Consumption (MWh)"
