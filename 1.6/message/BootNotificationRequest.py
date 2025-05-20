from typing import Optional

from type.CiString20Type import CiString20Type
from type.CiString50Type import CiString50Type
from type.CiString25Type import CiString25Type

class BootNotificationRequest:

    def __init__(self,
        chargePointModel: CiString20Type,
        chargePointVendor: CiString20Type,
        chargeBoxSerialNumber: Optional[CiString25Type]= None,
        chargePointSerialNumber: Optional[CiString25Type]= None,
        firmwareVersion: Optional[CiString50Type]= None,
        iccid: Optional[CiString20Type]= None,
        imsi: Optional[CiString20Type]= None,
        meterSerialNumber: Optional[CiString25Type]= None,
        meterType: Optional[CiString25Type]= None
    ):
        self.chargePointModel = chargePointModel
        self.chargePointVendor = chargePointVendor
        if chargeBoxSerialNumber:
            self.chargeBoxSerialNumber = chargeBoxSerialNumber
        if chargePointSerialNumber:
            self.chargePointSerialNumber = chargePointSerialNumber
        if firmwareVersion:
            self.firmwareVersion = firmwareVersion
        if iccid:
            self.iccid = iccid
        if imsi:
            self.imsi = imsi
        if meterSerialNumber:
            self.meterSerialNumber = meterSerialNumber
        if meterType:
            self.meterType = meterType

    def get_value(self):
        result = {
            "chargePointModel" : self.chargePointModel.get_value(),
            "chargePointVendor" : self.chargePointVendor.get_value(),
        }
        if self.chargeBoxSerialNumber:
            result['chargeBoxSerialNumber'] = self.chargeBoxSerialNumber.get_value()
        if self.chargePointSerialNumber:
            result['chargePointSerialNumber'] = self.chargePointSerialNumber.get_value()
        if self.firmwareVersion:
            result['firmwareVersion'] = self.firmwareVersion.get_value()
        if self.iccid:
            result['iccid'] = self.iccid.get_value()
        if self.imsi:
            result['imsi'] = self.imsi.get_value()
        if self.meterSerialNumber:
            result['meterSerialNumber'] = self.meterSerialNumber.get_value()
        if self.meterType:
            result['meterType'] = self.meterType.get_value()
        return result

    @classmethod
    def get_sample(cls, option=False):
        result = {}
        result['chargePointModel'] = CiString20Type.get_sample(option=option)
        result['chargePointVendor'] = CiString20Type.get_sample(option=option)
        if option:
            result['chargeBoxSerialNumber'] = CiString25Type.get_sample(option=option)
        if option:
            result['chargePointSerialNumber'] = CiString25Type.get_sample(option=option)
        if option:
            result['firmwareVersion'] = CiString50Type.get_sample(option=option)
        if option:
            result['iccid'] = CiString20Type.get_sample(option=option)
        if option:
            result['imsi'] = CiString20Type.get_sample(option=option)
        if option:
            result['meterSerialNumber'] = CiString25Type.get_sample(option=option)
        if option:
            result['meterType'] = CiString25Type.get_sample(option=option)
        return result