# Django 셋팅

## 파이썬 버전
python.org에서 3.11 이상의 버전을 다운받아서 설치

## powershell
터미널을 vscode에 열어줌(Ctrl + `).

## 파이썬 버전확인
터미널 -> 다음 명령어 입력
python --version

# 가상환경속으로 들어가기
.\venv\Scripts\activate # window
.\venv\Script\activate.bat # window
source ./venv/bin/activate # mac, linux

mkdir mysite
# mysite라는 폴더 생성 => 마우스 클릭하셔서 생성하는 것과 차이 없습니다. 보통 mysite라는 이름 대신 프로젝트 이름을 넣습니다.
cd mysite
# 폴더 이동
python -m venv venv
# 가상 환경 설정(이어 설명합니다.) 하는 명령어 입니다.

# 가상환경 설정
#     * 가상환경은 선택이 아니라 필수 입니다.
#     * 가상환경을 왜 잡을까요? 관리, 이관, 업데이트 등에 중요한 거점이 됩니다.
#     * pip list를 쳐보세요. 많은 python 라이브러리가 보이죠? 여기서 소숫점 3번째 짜리까지 안맞으면 작동 안되는 경우도 허다합니다. => 가상 환경은 통째로 다 이동합니다.
#     * `python -m venv venv`뒤가 가상환경 이름입니다.

# window에서 오류가 뜰 경우
+ CategoryInfo          : 보안 오류: (:) [], PSSecurityException
+ FullyQualifiedErrorId : UnauthorizedAccess
# 이걸 입력해주세요.
Set-ExecutionPolicy Unrestricted