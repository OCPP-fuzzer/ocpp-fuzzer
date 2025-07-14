# OCPP Fuzzer

OCPP(Open Charge Point Protocol) 프로토콜을 검증하기 위한 Fuzzer 프로젝트입니다. 현재 프로젝트는 OCPP 1.6 버전을 지원할 예정이며, 다양한 OCPP 메시지에 대한 테스트 데이터를 생성하고 전송할 수 있습니다.

## 목차

- [개요](#개요)
- [주요 기능](#주요-기능)
- [지원 버전](#지원-버전)
- [설치 방법](#설치-방법)
- [사용법](#사용법)
- [프로젝트 구조](#프로젝트-구조)
- [예제](#예제)

## 개요

OCPP Fuzzer는 전기차 충전소 관리 시스템(CSMS)과 충전소(Charge Point) 간의 통신을 위한 OCPP 프로토콜의 안정성과 호환성을 테스트하기 위해 개발되었습니다. 

### 주요 목적
- OCPP 메시지의 유효성 검증
- 프로토콜 구현의 견고성 테스트
- 다양한 엣지 케이스에 대한 테스트 데이터 생성
- OCPP 서버의 응답 처리 검증

### 현재 개발 상태
- **기본 메시지 생성 및 전송**: 완료
- **OCPP 1.6 메시지 타입 지원**: 완료
- **Mutation 기반 Fuzzing**: 개발 중
- **자동화된 테스트 실행**: 개발 중

## 주요 기능

### 1. 메시지 생성 ✅
- **자동 파라미터 생성**: OCPP 스펙에 따른 유효한 테스트 데이터 자동 생성
- **커스텀 파라미터**: 사용자 정의 파라미터로 메시지 구성 가능
- **옵션 파라미터 제어**: 필수 파라미터만 또는 모든 파라미터 포함 선택 가능
- **랜덤 데이터 생성**: 각 실행마다 다른 랜덤 값으로 테스트 데이터 생성

### 2. 메시지 전송 ✅
- **WebSocket 통신**: OCPP 표준 WebSocket 프로토콜 지원
- **실시간 응답**: 서버 응답 실시간 수신 및 표시
- **JSON 형식**: OCPP 표준 JSON 메시지 형식 지원

### 3. 지원 메시지 타입 ✅
- **Request 메시지**: 28가지 OCPP 1.6 Request 메시지 지원
- **Response 메시지**: 28가지 OCPP 1.6 Response 메시지 지원
- **총 메시지 수**: 56개 메시지 타입 지원
- **확장 가능**: 새로운 메시지 타입 추가 용이

### 4. Fuzzing 기능 (개발 중)
- **Mutation 기반 테스트**: 유효한 데이터를 변형하여 엣지 케이스 생성
- **자동화된 테스트 실행**: 다양한 mutation 조합으로 자동 테스트
- **결과 분석**: 서버 응답 분석 및 취약점 탐지

## 지원 버전

### OCPP 1.6 ✅
- **메시지 생성 및 전송**: 완전 구현됨
- **모든 Request/Response 메시지**: 28개 Request, 28개 Response 지원
- **총 메시지 수**: 56개 메시지 타입
- **타입 시스템**: 40+ OCPP 데이터 타입 구현
- **WebSocket 통신**: 안정적인 서버 통신 확인

### OCPP 2.0
- **기본 구조**: 구현됨
- **메시지 타입**: 일부 구현됨
- **완전 지원**: 향후 개발 예정

## 설치 방법

### 1. 저장소 클론
```bash
git clone <repository-url>
cd ocpp-fuzzer
```

### 2. 의존성 설치

#### OCPP 1.6
```bash
cd 1.6
pip install -r requirements.txt
```

#### OCPP 2.0
```bash
cd 2.0
pip install -r requirements.txt
```

### 3. 설치 확인
```bash
python3 run.py --help
```

## 사용법

### 현재 지원 기능
현재 OCPP Fuzzer는 **기본적인 메시지 생성 및 전송 기능**을 제공합니다. 각 실행마다 랜덤한 유효한 테스트 데이터를 생성하여 OCPP 서버에 전송하고 응답을 확인할 수 있습니다.

### 기본 명령어 형식
```bash
python3 run.py --request=[REQUEST_NAME] --url=[SERVER_URL] [OPTIONS]
```

### 매개변수 설명

| 매개변수 | 설명 | 필수 여부 | 예시 |
|---------|------|-----------|------|
| `--request` | OCPP 요청 메시지 이름 | ✅ | `BootNotificationRequest` |
| `--url` | OCPP 서버 WebSocket URL | ✅ | `ws://localhost:8080` |
| `--params` | JSON 형식의 커스텀 파라미터 | ❌ | `{"chargePointModel": "Test"}` |
| `--option` | 옵션 파라미터 포함 여부 | ❌ | `True` 또는 `False` |

### 사용 예제

#### 1. 기본 BootNotification 요청
```bash
python3 run.py --request=BootNotificationRequest --url=ws://localhost:8080
```

#### 2. 모든 파라미터 포함한 요청
```bash
python3 run.py --request=BootNotificationRequest --url=ws://localhost:8080 --option=True
```

#### 3. 커스텀 파라미터로 요청
```bash
python3 run.py --request=BootNotificationRequest --url=ws://localhost:8080 --params='{"chargePointModel": "TestModel", "chargePointVendor": "TestVendor"}'
```

### 향후 개발 예정 기능
- **Mutation 기반 Fuzzing**: 유효한 데이터를 변형하여 엣지 케이스 생성
- **자동화된 테스트 실행**: 다양한 mutation 조합으로 자동 테스트

## 프로젝트 구조

```
ocpp-fuzzer/
├── 1.6/                          # OCPP 1.6 구현
│   ├── message/                  # OCPP 메시지 클래스
│   │   ├── BootNotificationRequest.py
│   │   ├── AuthorizeRequest.py
│   │   └── ... (28개 Request/Response)
│   ├── type/                     # OCPP 데이터 타입
│   │   ├── CiString20Type.py
│   │   ├── AuthorizationStatus.py
│   │   └── ... (40+ 타입)
│   ├── data/                     # 메시지 데이터 정의
│   ├── util/                     # 유틸리티 함수
│   ├── module.py                 # 메시지 모듈 로더
│   ├── sender.py                 # 메시지 전송 로직
│   ├── run.py                    # CLI 진입점
│   └── requirements.txt          # Python 의존성
├── 2.0/                          # OCPP 2.0 구현 (미구현 상태)
│   ├── requests/                 # OCPP 2.0 요청
│   ├── ocpptypes/                # OCPP 2.0 타입
│   ├── ocppenum/                 # OCPP 2.0 열거형
│   └── ...
└── README.md                     # 프로젝트 문서
```

## 예제

### BootNotificationRequest 예제

**실행 명령어:**
```bash
python3 run.py --request=BootNotificationRequest --url=ws://localhost:8080 --option=True
```

**생성되는 요청 메시지 (매번 다른 랜덤 값):**
```json
[
    2,
    "7a9a9e91-faf3-42b0-86d4-7f00afc6e60e",
    "BootNotification",
    {
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

**서버 응답 예시:**
```json
[
    3,
    "7a9a9e91-faf3-42b0-86d4-7f00afc6e60e",
    {
        "status": "Accepted",
        "currentTime": "2024-01-01T00:00:00.000Z",
        "interval": 300
    }
]
```

### 현재 동작 방식
- **랜덤 데이터 생성**: 각 실행마다 `random` 모듈을 사용하여 다른 테스트 데이터 생성
- **유효한 데이터**: OCPP 스펙에 맞는 유효한 형식의 데이터만 생성
- **실시간 통신**: WebSocket을 통해 서버와 실시간 통신
- **응답 확인**: 서버 응답을 즉시 수신하여 표시

## 지원 메시지 목록

### Request 메시지 (28개)
- `AuthorizeRequest`
- `BootNotificationRequest`
- `CancelReservationRequest`
- `ChangeAvailabilityRequest`
- `ChangeConfigurationRequest`
- `ClearCacheRequest`
- `ClearChargingProfileRequest`
- `DataTransferRequest`
- `DiagnosticsStatusNotificationRequest`
- `FirmwareStatusNotificationRequest`
- `GetCompositeScheduleRequest`
- `GetConfigurationRequest`
- `GetDiagnosticsRequest`
- `GetLocalListVersionRequest`
- `HeartbeatRequest`
- `MeterValuesRequest`
- `RemoteStartTransactionRequest`
- `RemoteStopTransactionRequest`
- `ReserveNowRequest`
- `ResetRequest`
- `SendLocalListRequest`
- `SetChargingProfileRequest`
- `StartTransactionRequest`
- `StatusNotificationRequest`
- `StopTransactionRequest`
- `TriggerMessageRequest`
- `UnlockConnectorRequest`
- `UpdateFirmwareRequest`

### Response 메시지 (28개)
- `AuthorizeResponse`
- `BootNotificationResponse`
- `CancelReservationResponse`
- `ChangeAvailabilityResponse`
- `ChangeConfigurationResponse`
- `ClearCacheResponse`
- `ClearChargingProfileResponse`
- `DataTransferResponse`
- `DiagnosticsStatusNotificationResponse`
- `FirmwareStatusNotificationResponse`
- `GetCompositeScheduleResponse`
- `GetConfigurationResponse`
- `GetDiagnosticsResponse`
- `GetLocalListVersionResponse`
- `HeartbeatResponse`
- `MeterValuesResponse`
- `RemoteStartTransactionResponse`
- `RemoteStopTransactionResponse`
- `ReserveNowResponse`
- `ResetResponse`
- `SendLocalListResponse`
- `SetChargingProfileResponse`
- `StartTransactionResponse`
- `StatusNotificationResponse`
- `StopTransactionResponse`
- `TriggerMessageResponse`
- `UnlockConnectorResponse`
- `UpdateFirmwareResponse`


## 개발 로드맵

### Phase 1: 기본 기능 ✅ (완료)
- [x] OCPP 1.6 메시지 타입 구현
- [x] 기본 메시지 생성 및 전송
- [x] WebSocket 통신 구현
- [x] 랜덤 테스트 데이터 생성

### Phase 2: Fuzzing 기능 (진행 중)
- [ ] Mutation 기반 데이터 변형
- [ ] 자동화된 테스트 실행


## 🔗 참고 자료

- [OCPP 1.6 Specification](https://ocpp-spec.org/schemas/v1.6/)
- [OCPP 2.0 Specification](https://ocpp-spec.org/schemas/v2.0/)
- [WebSocket Protocol](https://tools.ietf.org/html/rfc6455)
- [PyJFuzz](https://github.com/mseclab/PyJFuzz)
