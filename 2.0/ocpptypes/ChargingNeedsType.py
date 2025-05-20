from typing import Optional

from datetime import datetime

from ocppenum.EnergyTransferModeEnumType import EnergyTransferModeEnumType
from ocpptypes.ACChargingParametersType import ACChargingParametersType
from ocpptypes.DCChargingParametersType import DCChargingParametersType


class ChargingNeedsType:
    def __init__(self, requestedEnergyTransfer: EnergyTransferModeEnumType, departureTime: Optional[datetime] = None, acChargingParameters: Optional[ACChargingParametersType] = None, dcChargingParameters: Optional[DCChargingParametersType] = None):
        self.requestedEnergyTransfer = requestedEnergyTransfer

        if departureTime:
            self.departureTime = departureTime
        if acChargingParameters:
            self.acChargingParameters = acChargingParameters
        if dcChargingParameters:
            self.dcChargingParameters = dcChargingParameters

    def to_dict(self):
        request = {
            "requestedEnergyTransfer" : self.requestedEnergyTransfer.value,
        }

        if self.departureTime:
            request["departureTime"] = self.departureTime.isoformat().split('.')[0] + 'Z'
        if self.acChargingParameters:
            request["acChargingParameters"] = self.acChargingParameters.to_dict()
        if self.dcChargingParameters:
            request["dcChargingParameters"] = self.dcChargingParameters.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['requestedEnergyTransfer'] = EnergyTransferModeEnumType.sample()

        if option:
            result['departureTime'] = datetime.now().isoformat().split('.')[0] + 'Z'
            result['acChargingParameters'] = ACChargingParametersType.sample(option=option)
            result['dcChargingParameters'] = DCChargingParametersType.sample(option=option)

        return result
    