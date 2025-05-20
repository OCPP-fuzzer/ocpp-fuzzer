from typing import Optional

from type.UnitOfMeasure import UnitOfMeasure
from type.Phase import Phase
from type.Location import Location
from type.Measurand import Measurand
from type.ValueFormat import ValueFormat
from type.ReadingContext import ReadingContext

class SampledValue:

    def __init__(self,
        value: str,
        context: Optional[ReadingContext]= None,
        format: Optional[ValueFormat]= None,
        measurand: Optional[Measurand]= None,
        phase: Optional[Phase]= None,
        location: Optional[Location]= None,
        unit: Optional[UnitOfMeasure]= None
    ):
        self.value = value
        if context:
            self.context = context
        if format:
            self.format = format
        if measurand:
            self.measurand = measurand
        if phase:
            self.phase = phase
        if location:
            self.location = location
        if unit:
            self.unit = unit

    def get_value(self):
        result = {
            "value" : self.value,
        }
        if self.context:
            result['context'] = self.context.get_value()
        if self.format:
            result['format'] = self.format.get_value()
        if self.measurand:
            result['measurand'] = self.measurand.get_value()
        if self.phase:
            result['phase'] = self.phase.get_value()
        if self.location:
            result['location'] = self.location.get_value()
        if self.unit:
            result['unit'] = self.unit.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['value'] = "string"
        if option:
            result['context'] = ReadingContext.get_sample(option=option)
        if option:
            result['format'] = ValueFormat.get_sample(option=option)
        if option:
            result['measurand'] = Measurand.get_sample(option=option)
        if option:
            result['phase'] = Phase.get_sample(option=option)
        if option:
            result['location'] = Location.get_sample(option=option)
        if option:
            result['unit'] = UnitOfMeasure.get_sample(option=option)
        return result