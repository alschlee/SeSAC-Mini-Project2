# SeSAC Cloud Camp Mini Project 2

## Project Overview

이 프로젝트는 리액트(React)와 FastAPI를 활용하여 프론트엔드와 백엔드 기능을 통합한 웹 애플리케이션입니다. <br/>
사용자는 백엔드에서 제공하는 JSON 데이터를 프론트엔드를 통해 확인할 수 있습니다.


## Project Duration

- **기간**: 9월 26일 (목) ~ 30일 (월)

## Requirements

- **도커 이미지**: 프론트엔드와 백엔드 기능을 제공하는 도커 이미지를 작성하여 도커 허브에 등록합니다.
- **프론트엔드**: 리액트를 사용하여 본인 이름과 백엔드에서 가져온 데이터를 출력합니다.
- **백엔드**: FastAPI를 사용하여 JSON 형식의 데이터를 반환합니다.
- **데이터 연계**: 프론트엔드와 백엔드를 연계하여 데이터를 가져오고 출력합니다.
- **배포**: 실습에 사용한 가상 머신에 개발한 애플리케이션을 배포합니다.
- **서비스 접근**: 호스트 PC에서 `http://www.test.com`으로 접속하면 서비스가 제공됩니다.

## Result
![result](https://github.com/user-attachments/assets/a843cd8a-bd01-4c41-8cfc-7df253022d0c)

## Project Structure

이 프로젝트는 프론트엔드와 백엔드의 기능을 포함하는 두 개의 주요 디렉토리로 구성되어 있습니다. <br/>
가상 머신 기반 개발 환경 설정 파일 및 관련 스크립트는 별도의 레포지토리 ([alschlee/sesac-cloud-archive](https://github.com/alschlee/sesac-cloud-archive)) 에서 관리됩니다.

```
📁 SeSAC-Mini-Project2
├── 📁 FE
│   └── 📁 jingyeong-app
│       ├── 📁 public              # 정적 파일(HTML, 이미지 등) 보관
│       ├── 📁 src                 # 소스 코드 폴더
│       │   └── App.js             # 메인 애플리케이션 컴포넌트
│       ├── Dockerfile              # 프론트엔드 도커 이미지 빌드 설정
│       └── package.json            # 프론트엔드 프로젝트 의존성 및 스크립트 관리
├── 📁 BE
│   ├── 📁 __pycache__              # 파이썬 컴파일된 파일 저장(자동 생성)
│   ├── Dockerfile                   # 백엔드 도커 이미지 빌드 설정
│   ├── main.py                      # 백엔드 애플리케이션의 메인 코드
│   └── requirements.txt             # 백엔드 프로젝트 의존성 목록
└── leejingyeong.yaml            # Kubernetes 매니페스트 파일
```
