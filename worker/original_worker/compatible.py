from enum import Enum


class CompatibleUtcSimulators(Enum):
    AMICI = ('amici', '0.11.21')
    COPASI = ('copasi', '0.71')
    PYSCES = ('pysces', '1.2.2')
    TELLURIUM = ('tellurium', '0.85')


COMPATIBLE_UTC_SIMULATORS = [CompatibleUtcSimulators[member].value for member in list(dict(CompatibleUtcSimulators.__members__).keys())]
COMPATIBLE_VERIFICATION_SIMULATORS = COMPATIBLE_UTC_SIMULATORS.copy()