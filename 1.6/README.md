# OCPP 1.6 Sender
## 개요
* 현재 sender 기능 및 요청에 따른 파라미터 생성 기능까지 구현됨

## 사용법
### 모듈 설치
* websocket 설치
```
pip install -r requirement.txt
```

### 명령줄
```sh
python3 run.py --request=[REQUEST NAME] --param=[JSON PARAM] --url=[SERVER URL] --option=[True or False]
```

```sh
python3 run.py --request=BootNotificationRequest --url=http://test.com --option=True
```

```sh
BootNotificationRequest
Request:
[
    2,
    "7a9a9e91-faf3-42b0-86d4-7f00afc6e60e",
    "BootNotification",
    {s
        "chargePointModel": "ahPEcratDRnQTuUC3Xa",
        "chargePointVendor": "k8IFVU",
        "chargeBoxSerialNumber": "r4ar",
        "chargePointSerialNumber": "vQSPP5YOUhVvfgXj",
        "firmwareVersion": "rpXuPzHWxFiodFuIbaIuhkgQQqbU4k",
        "iccid": "lGP",
        "imsi": "gV23Zdrol68rH",
        "meterSerialNumber": "d4yy0obwJmVzA8mSt0",
        "meterType": "aP8hvcmNeMksc7rMFt3DBq3"
    }
]
```

### 인자 설명
* `--request`
    * 어떤 요청을 보낼 것인지 명시합니다.
    * [요청 종류](#요청종류) 참조

* `--url`
    * OCPP 서버의 주소를 명시합니다.

* `--param`
    * 요청에 대한 json 파라미터 입니다.
    * 해당 인자가 없을 경우, sender 자체적으로 인자를 구성하여 요청을 전송합니다.

* `--option`
    * `--param` 인자를 명시하지 않았을 경우 사용됩니다.
    * 요청에 대한 파라미터를 필수 항목으로만 구성할 것인지, 옵션 항목을 포함할 것인지 명시합니다.
    * `--option=True` : 요청에 대한 모든(필수, 옵션) 파라미터를 구성합니다.
    * `--option=False` : 요청에 대한 필수 파라미터만 구성합니다.


## 요청종류
```
StartTransactionRequest
DiagnosticsStatusNotificationRequest
ResetRequest
GetCompositeScheduleRequest
AuthorizeRequest
ReserveNowRequest
UpdateFirmwareRequest
RemoteStopTransactionRequest
UnlockConnectorRequest
ChangeAvailabilityRequest
BootNotificationRequest
ClearChargingProfileRequest
MeterValuesRequest
HeartbeatRequest
RemoteStartTransactionRequest
CancelReservationRequest
GetConfigurationRequest
TriggerMessageRequest
ClearCacheRequest
StatusNotificationRequest
SetChargingProfileRequest
GetLocalListVersionRequest
ChangeConfigurationRequest
DataTransferRequest
SendLocalListRequest
StopTransactionRequest
FirmwareStatusNotificationRequest
GetDiagnosticsRequest
```

## 응답종류
```
ClearCacheResponse
BootNotificationResponse
GetConfigurationResponse
SendLocalListResponse
GetLocalListVersionResponse
RemoteStartTransactionResponse
SetChargingProfileResponse
UpdateFirmwareResponse
DiagnosticsStatusNotificationResponse
UnlockConnectorResponse
ChangeConfigurationResponse
AuthorizeResponse
StopTransactionResponse
MeterValuesResponse
ResetResponse
TriggerMessageResponse
ChangeAvailabilityResponse
DataTransferResponse
ClearChargingProfileResponse
StatusNotificationResponse
HeartbeatResponse
ReserveNowResponse
CancelReservationResponse
GetDiagnosticsResponse
FirmwareStatusNotificationResponse
StartTransactionResponse
RemoteStopTransactionResponse
GetCompositeScheduleResponse
```

## Reference
* [OCPP-Spec](https://ocpp-spec.org/schemas/v1.6/)