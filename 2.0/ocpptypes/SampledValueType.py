from typing import Optional

from ocppenum.ReadingContextEnumType import ReadingContextEnumType
from ocppenum.MeasurandEnumType import MeasurandEnumType
from ocppenum.PhaseEnumType import PhaseEnumType
from ocppenum.LocationEnumType import LocationEnumType
from ocpptypes.SignedMeterValueType import SignedMeterValueType
from ocpptypes.UnitOfMeasureType import UnitOfMeasureType


class SampledValueType:
    def __init__(self, value: float, context: Optional[ReadingContextEnumType] = None, measurand: Optional[MeasurandEnumType] = None, phase: Optional[PhaseEnumType] = None, location: Optional[LocationEnumType] = None, signedMeterValue: Optional[SignedMeterValueType] = None, unitOfMeasure: Optional[UnitOfMeasureType] = None):
        self.value = value

        if context:
            self.context = context
        if measurand:
            self.measurand = measurand
        if phase:
            self.phase = phase
        if location:
            self.location = location
        if signedMeterValue:
            self.signedMeterValue = signedMeterValue
        if unitOfMeasure:
            self.unitOfMeasure = unitOfMeasure

    def to_dict(self):
        request = {
            "value" : self.value,
        }

        if self.context:
            request["context"] = self.context.value
        if self.measurand:
            request["measurand"] = self.measurand.value
        if self.phase:
            request["phase"] = self.phase.value
        if self.location:
            request["location"] = self.location.value
        if self.signedMeterValue:
            request["signedMeterValue"] = self.signedMeterValue.to_dict()
        if self.unitOfMeasure:
            request["unitOfMeasure"] = self.unitOfMeasure.to_dict()

        return request
    
    @classmethod
    def sample(cls, option=False):
        result = {}

        result['value'] = 1.0

        if option:
            result['context'] = ReadingContextEnumType.sample()
            result['measurand'] = MeasurandEnumType.sample()
            result['phase'] = PhaseEnumType.sample()
            result['location'] = LocationEnumType.sample()
            result['signedMeterValue'] = SignedMeterValueType.sample(option=option)
            result['unitOfMeasure'] = UnitOfMeasureType.sample(option=option)

        return result
    