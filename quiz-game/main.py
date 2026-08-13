class Quiz:
    def __init__(self, question, choices, answer, hint=""):
        self.question = question  # 문제 내용
        self.choices = choices    # 4개의 선택지 (리스트)
        self.answer = answer      # 정답 번호 (1~4)
        self.hint = hint

    def display(self, index):
        """요구사항 양식에 맞춘 퀴즈 출력 메서드"""
        print("-" * 40)
        print(f"[문제 {index}]")
        print(self.question)
        print()
        for i, choice in enumerate(self.choices, 1):
            print(f"{i}. {choice}")
        print()

    def check_answer(self, user_answer):
        """정답 확인 메서드"""
        return self.answer == user_answer

    def to_dict(self):
        """나중에 state.json에 저장하기 쉽게 딕셔너리로 변환해주는 역할"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint
        }
    
    @classmethod
    def from_dict(cls, data):
        """state.json에서 불러온 데이터를 다시 Quiz 객체로 만들어주는 역할"""
        # 기존 데이터에 힌트가 없을 경우를 대비해 기본값("") 설정
        return cls(data["question"], data["choices"], data["answer"],data.get("hint", ""))

# 프리다이빙 기초 이론 퀴즈 5개 (기본 데이터)
default_quizzes = [
    Quiz(
        "프리다이빙을 할 때 가장 중요하고 기본이 되는 안전 수칙은 무엇인가요?", 
        ["혼자 다이빙하지 않기 (버디 시스템)", "최대한 빨리 하강하기", "숨을 한계까지 참기", "무거운 웨이트 차기"], 
        1,
        "다이빙은 절대 혼자 해서는 안 됩니다. 짝꿍이 필요해요!"
    ),
    Quiz(
        "물속에 들어갈 때 수압에 의해 귀가 아픈 것을 방지하기 위해 압력을 맞추는 기술은?", 
        ["마스크 클리어링", "이퀄라이징(압력평형)", "덕 다이빙", "핀킥"], 
        2,
        "코를 쥐고 '흥!' 하고 불어넣는 기술입니다."
    ),
    Quiz(
        "프리다이버가 입수 전 심박수를 낮추고 몸을 이완시키기 위해 하는 호흡은?", 
        ["초과호흡", "준비호흡(릴랙세이션)", "회복호흡", "무산소호흡"], 
        2,
        "긴장을 풀고(릴랙스) 편안하게 쉬는 호흡입니다."
    ),
    Quiz(
        "프리다이빙 출수 후, 수면 위로 올라오자마자 가장 먼저 해야 하는 필수적인 호흡은?", 
        ["준비호흡", "회복호흡", "초과호흡", "인공호흡"], 
        2,
        "몸 상태를 원래대로 '회복'시키는 호흡입니다."
    ),
    Quiz(
        "상승 중 수면 근처에서 산소 부족으로 의식을 잃는 현상을 무엇이라고 부르나요?", 
        ["잠수병", "질소 마취", "얕은 물 기절 (SWB)", "과호흡 증후군"], 
        3,
        "Shallow Water Blackout의 약자를 생각해 보세요."
    )
]


import sys # 종료 처리를 위해 필요
import json
import random           #  랜덤 기능 추가
from datetime import datetime  #  시간 기록 기능 추가
import os  # 👈 경로를 다루기 위해 추가

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes  # 퀴즈 목록 데이터
        self.best_score = 0     # 최고 점수 초기화
        self.history = []  # 👈 모든 게임 기록을 담을 리스트 추가

    # 💡 현재 파일(main.py)이 있는 폴더 경로를 찾아 state.json과 합칩니다.
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.file_path = os.path.join(base_dir, "state.json")

        self.load_data()        # 객체가 생성될 때 가장 먼저 파일을 읽어옴

    def display_menu(self):
        """메뉴 출력 메서드"""
        print("\n" + "=" * 40)
        print("        🎯 나만의 프리다이빙 퀴즈 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 삭제")    # 👈 기능 추가
        print("4. 퀴즈 목록")
        print("5. 기록 확인")    # 👈 히스토리 확인으로 변경
        print("6. 종료")
        print("=" * 40)

    def show_quiz_list(self):
        """저장된 퀴즈 목록을 보여주는 기능"""
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n")
        print("-" * 40)
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
        else:
            for i, quiz in enumerate(self.quizzes, 1):
                print(f"[{i}] {quiz.question}")
        print("-" * 40)

    def save_data(self):
        """퀴즈 데이터와 최고 점수를 JSON 파일에 저장"""
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
            "history": self.history  # 👈 히스토리도 같이 저장
        }
        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"\n⚠️ 데이터 저장 중 오류가 발생했습니다: {e}")

    def load_data(self):
        """JSON 파일에서 데이터를 불러오기"""
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)
                self.history = data.get("history", []) # 👈 히스토리 불러오기
            print("📂 저장된 데이터를 성공적으로 불러왔습니다.")
            
        except FileNotFoundError:
            print("📂 첫 실행입니다. 기본 퀴즈 데이터로 시작합니다.")
        except Exception as e:
            print(f"\n⚠️ 데이터 파일이 손상되었습니다. ({e})")
            print("기본 퀴즈 데이터로 복구하여 시작합니다.")



    def add_quiz(self):
        """새로운 퀴즈를 입력받아 리스트에 추가하는 기능"""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        
        # 1. 문제 입력 받기 (빈 텍스트 방어)
        while True:
            question = input("문제를 입력하세요: ").strip()
            if not question:
                print("⚠️ 빈 입력입니다. 문제 내용을 입력해 주세요.")
                continue
            break
            
        # 2. 선택지 4개 입력 받기 (빈 텍스트 방어)
        choices = []
        for i in range(1, 5):
            while True:
                choice = input(f"선택지 {i}: ").strip()
                if not choice:
                    print("⚠️ 빈 입력입니다. 선택지 내용을 입력해 주세요.")
                    continue
                choices.append(choice)
                break
                
        # 3. 정답 번호 입력 받기 (숫자, 1~4 범위, 빈 텍스트 방어)
        while True:
            try:
                answer_str = input("정답 번호 (1-4): ").strip()
                if not answer_str:
                    print("⚠️ 빈 입력입니다. 1-4 사이의 숫자를 입력하세요.")
                    continue
                answer = int(answer_str)
                if answer < 1 or answer > 4:
                    print("⚠️ 범위 오류입니다. 1-4 사이의 숫자를 입력하세요.")
                    continue
                break
            except ValueError:
                print("⚠️ 잘못된 입력입니다. 문자가 아닌 숫자를 입력해 주세요.")

        hint = input("힌트를 입력하세요 (없으면 Enter): ").strip()
                
        # 4. 입력받은 정보로 새로운 Quiz 객체를 만들어 목록에 추가
        new_quiz = Quiz(question, choices, answer,hint)
        self.quizzes.append(new_quiz)
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")
        self.save_data()

    def delete_quiz(self):
        """(새로운 기능) 퀴즈 삭제"""
        self.show_quiz_list()
        if not self.quizzes:
            return
            
        try:
            del_idx = int(input("\n삭제할 퀴즈 번호를 입력하세요 (취소: 0): ").strip())
            if del_idx == 0:
                print("취소했습니다.")
                return
            if 1 <= del_idx <= len(self.quizzes):
                deleted = self.quizzes.pop(del_idx - 1)
                print(f"\n🗑️ '{deleted.question}' 문제가 삭제되었습니다.")
                self.save_data()
            else:
                print("⚠️ 잘못된 번호입니다.")
        except ValueError:
            print("⚠️ 숫자를 입력해 주세요.")

    def play_quiz(self):
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        # 1. 문제 수 선택
        while True:
            try:
                num_q = input(f"\n몇 문제를 푸시겠습니까? (최대 {len(self.quizzes)}제): ").strip()
                num_q = int(num_q)
                if 1 <= num_q <= len(self.quizzes):
                    break
                print(f"⚠️ 1부터 {len(self.quizzes)} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("⚠️ 숫자를 입력하세요.")

        # 2. 랜덤 섞기
        selected_quizzes = random.sample(self.quizzes, num_q)
        
        print(f"\n📝 퀴즈를 시작합니다! (총 {num_q}문제)")
        current_score = 0
        
        for i, quiz in enumerate(selected_quizzes, 1):
            quiz.display(i)
            hint_used = False  # 힌트 사용 여부 체크
            
            while True:
                user_input = input("정답 입력 (힌트 보기: h): ").strip().lower()
                
                # 힌트 로직
                if user_input == 'h':
                    if not quiz.hint:
                        print("💡 이 문제는 힌트가 없습니다.")
                    elif hint_used:
                        print(f"💡 이미 힌트를 보셨습니다: {quiz.hint}")
                    else:
                        print(f"💡 힌트: {quiz.hint} (※ 사용 시 점수 차감)")
                        hint_used = True
                    continue
                
                try:
                    user_answer = int(user_input)
                    if 1 <= user_answer <= 4:
                        break
                    print("⚠️ 1-4 사이의 숫자를 입력하세요.")
                except ValueError:
                    print("⚠️ 잘못된 입력입니다. 숫자나 'h'를 입력하세요.")
            
            # 정답 확인 (힌트 사용 시 점수를 절반만 부여)
            if quiz.check_answer(user_answer):
                if hint_used:
                    print("✅ 정답입니다! (힌트 사용으로 부분 점수)\n")
                    current_score += 0.5
                else:
                    print("✅ 정답입니다!\n")
                    current_score += 1
            else:
                print(f"❌ 오답입니다. (정답은 {quiz.answer}번)\n")
        
        # 3. 점수 계산 및 히스토리 저장
        score_percentage = int((current_score / num_q) * 100)
        print("=" * 40)
        print(f"🏆 결과: {num_q}문제 중 {current_score}점! ({score_percentage}점)")
        
        if score_percentage > self.best_score:
            print("🎉 새로운 최고 점수입니다!")
            self.best_score = score_percentage
            
        # 히스토리 기록 (현재 시간, 푼 문제 수, 점수)
        now = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.history.append({"date": now, "count": num_q, "score": score_percentage})
        
        print("=" * 40)
        self.save_data()    


    def show_history(self):
        """(새로운 기능) 최고 점수 및 모든 게임 기록 확인"""
        print(f"\n🏆 최고 점수: {self.best_score}점")
        print("-" * 40)
        print("📜 최근 게임 기록")
        
        if not self.history:
            print("아직 퀴즈를 풀지 않으셨군요! 첫 도전을 시작해 보세요.")
        else:
            # 기록이 여러 개일 경우를 대비해 보기 좋게 출력
            for i, record in enumerate(self.history, 1):
                print(f"{i}. [{record['date']}] {record['count']}문제 진행 ➡️ {record['score']}점")
        print("-" * 40)

    def run(self):
        """게임의 전체 흐름을 제어하는 메인 루프"""
        while True:
            self.display_menu()
            try:
                # 1. 입력 앞뒤 공백 제거
                choice_str = input("선택: ").strip()
                
                # 2. 빈 입력 처리 (안내 문구 1-6으로 수정)
                if not choice_str:
                    print("⚠️ 빈 입력입니다. 1-6 사이의 숫자를 입력하세요.")
                    continue
                
                # 3. 숫자 변환 시도
                choice = int(choice_str)
                
                # 4. 메뉴 분기 및 범위 이탈 검사 (3, 5, 6번 기능 수정됨)
                if choice == 1:
                    self.play_quiz()
                elif choice == 2:
                    self.add_quiz()
                elif choice == 3:
                    self.delete_quiz()     # 👈 [추가됨] 3번: 퀴즈 삭제
                elif choice == 4:
                    self.show_quiz_list()
                elif choice == 5:
                    self.show_history()    # 👈 [수정됨] 5번: 전체 기록 확인
                elif choice == 6:          # 👈 [수정됨] 6번: 종료
                    print("\n게임을 종료합니다. 안녕히 가세요!")
                    self.save_data()
                    break
                else:
                    print("⚠️ 잘못된 입력입니다. 1-6 사이의 숫자를 입력하세요.")
                    
            except ValueError:
                print("⚠️ 잘못된 입력입니다. 문자가 아닌 숫자를 입력해 주세요.")
                
            except (KeyboardInterrupt, EOFError):
                print("\n\n⚠️ 비정상 종료가 감지되었습니다. 데이터를 안전하게 저장하고 종료합니다.")
                self.save_data()
                break

# 프로그램 실행의 진입점
if __name__ == "__main__":
    game = QuizGame(default_quizzes)
    game.run()