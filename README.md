# SSD 트레이스 전처리 도구

이 프로젝트는 SSD 트레이스 데이터를 전처리하는 Python 스크립트를 제공합니다.

## 개요

이 도구는 SSD 트레이스 데이터를 CSV 형식으로 변환하여 분석하기 쉽게 만들어줍니다. 원본 트레이스 데이터에서 타임스탬프, 작업 유형, 섹터 번호, I/O 크기 등의 중요한 정보를 추출합니다.

## 기능

- SSD 트레이스 파일을 CSV 형식으로 변환
- 여러 트레이스 파일을 일괄 처리
- 필요한 정보만 추출하여 저장

## 설치 방법

1. 저장소 클론:
```bash
git clone https://github.com/DLST316/-Trace-Name-Details-Actions-YCSB-RocksDB-SSD-Traces-Preprocessing.git
```

2. Python 가상환경 생성 및 활성화:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. 필요한 패키지 설치:
```bash
pip install -r requirements.txt
```

## 사용 방법

1. 트레이스 파일을 프로젝트 디렉토리에 복사합니다.
2. 다음 명령어로 스크립트를 실행합니다:
```bash
python process_trace.py
```

## 출력 형식

생성된 CSV 파일은 다음 열을 포함합니다:
- Timestamp: 작업 시간 (나노초)
- OperationType: 작업 유형 (읽기/쓰기)
- SectorNumber: 섹터 번호
- IOSize: I/O 크기

## 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 기여

기여를 환영합니다! 이슈를 열거나 풀 리퀘스트를 보내주세요. 