# codyssey-mission_1-2

# 🎯 나만의 프리다이빙 퀴즈 게임

터미널에서 실행되는 파이썬 기반의 객체 지향 퀴즈 프로그램입니다.
프리다이빙의 기초 이론을 퀴즈를 통해 학습할 수 있습니다.

---

## 📌 주요 기능
1. **퀴즈 풀기**: 저장된 퀴즈를 풀고 점수를 계산합니다.
2. **퀴즈 추가**: 프로그램 내에서 새로운 퀴즈를 등록할 수 있습니다.
3. **퀴즈 목록**: 등록된 모든 퀴즈의 목록을 확인합니다.
4. **점수 확인**: 게임에서 획득한 최고 점수를 기록하고 보여줍니다.
5. **데이터 영구 저장**: `state.json` 파일을 통해 프로그램이 종료되어도 데이터가 유지됩니다.

---

## 🛠️ 개발 환경
- Python 3.9 (문법 호환성 확보 및 예외 처리 완료)
- 내장 라이브러리 `json`, `sys` 사용

---

## 💻 Git 실습 내용 (Clone & Pull)
본 프로젝트를 진행하며 원격 저장소(Remote Repository)와 로컬 환경을 동기화하는 실습을 진행했습니다.

### 1. Git Clone 실습
GitHub에 생성된 원격 저장소를 로컬의 새로운 폴더로 복제(Clone)하여 초기 작업 환경을 세팅했습니다.

```bash
# 원격 저장소 복제 명령어
git clone https://github.com/5312ksy-beep/codyssey-mission_1-2/tree/main

sey-mission_1-2.git
'codyssey-mission_1-2'에 복제합니다...
remote: Enumerating objects: 31, done.
remote: Counting objects: 100% (31/31), done.
remote: Compressing objects: 100% (19/19), done.
remote: Total 31 (delta 9), reused 28 (delta 9), pack-reused 0 (from 0)
오브젝트를 받는 중: 100% (31/31), 8.90 KiB | 8.90 MiB/s, 완료.
델타를 알아내는 중: 100% (9/9), 완료.

```
### 2. Git Pull 실습
원격 저장소(GitHub)에 업데이트된 최신 커밋 내역을 내 컴퓨터(로컬) 환경으로 안전하게 가져와 동기화하고 병합(Merge)하는 실습을 진행했습니다.

```bash
# 원격 저장소의 최신 변경 사항을 로컬 브랜치로 가져오기
git pull origin main

https://github.com/5312ksy-beep/codyssey-mission_1-2 URL에서
 * branch            main       -> FETCH_HEAD
이미 업데이트 상태입니다.
