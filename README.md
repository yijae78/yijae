# 대한예수교장로회 통합측 조직신학 안내 앱

이 저장소는 대한예수교장로회 통합측 조직신학을 소개하는 간단한 Python 표준 라이브러리 웹 애플리케이션을 제공합니다. 추가 패키지 없이 실행할 수 있도록 HTTP 서버를 직접 구현했습니다.

## 구성

- `app.py` – HTTP 서버와 조직신학 주제를 JSON 구조로 정의합니다.
- `templates/index.html` – 웹 인터페이스 템플릿입니다.
- `requirements.txt` – 외부 의존성 없이 실행한다는 정보를 기록합니다.

## 실행 방법

1. (선택) 가상 환경을 생성하고 활성화합니다.

   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   Windows 사용자는 PowerShell에서 다음 명령을 사용합니다.

   ```powershell
   python -m venv venv
   venv\Scripts\Activate.ps1
   ```

2. 서버를 실행합니다.

   ```bash
   python app.py
   ```

3. 브라우저에서 <http://127.0.0.1:5000> 주소로 접속하거나, JSON API는 <http://127.0.0.1:5000/api/sections> 경로에서 확인합니다.

## API

- `/` – 조직신학 설명 페이지를 HTML로 제공합니다.
- `/api/sections` – 동일한 내용을 JSON 형식으로 제공합니다.

## 참고

제공된 내용은 대한예수교장로회 통합측의 역사와 신학적 특징을 교육 목적으로 요약한 것입니다.
