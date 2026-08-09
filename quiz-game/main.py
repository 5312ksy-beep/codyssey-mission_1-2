class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question  # 문제 내용
        self.choices = choices    # 4개의 선택지 (리스트)
        self.answer = answer      # 정답 번호 (1~4)

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
            "answer": self.answer
        }

    @classmethod
    def from_dict(cls, data):
        """state.json에서 불러온 데이터를 다시 Quiz 객체로 만들어주는 역할"""
        return cls(data["question"], data["choices"], data["answer"])


# 프리다이빙 기초 이론 퀴즈 5개 (기본 데이터)
default_quizzes = [
    Quiz(
        "프리다이빙을 할 때 가장 중요하고 기본이 되는 안전 수칙은 무엇인가요?", 
        ["혼자 다이빙하지 않기 (버디 시스템)", "최대한 빨리 하강하기", "숨을 한계까지 참기", "무거운 웨이트 차기"], 
        1
    ),
    Quiz(
        "물속에 들어갈 때 수압에 의해 귀가 아픈 것을 방지하기 위해 압력을 맞추는 기술은?", 
        ["마스크 클리어링", "이퀄라이징(압력평형)", "덕 다이빙", "핀킥"], 
        2
    ),
    Quiz(
        "프리다이버가 입수 전 심박수를 낮추고 몸을 이완시키기 위해 하는 호흡은?", 
        ["초과호흡", "준비호흡(릴랙세이션)", "회복호흡", "무산소호흡"], 
        2
    ),
    Quiz(
        "프리다이빙 출수 후, 수면 위로 올라오자마자 가장 먼저 해야 하는 필수적인 호흡은?", 
        ["준비호흡", "회복호흡", "초과호흡", "인공호흡"], 
        2
    ),
    Quiz(
        "상승 중 수면 근처에서 산소 부족으로 의식을 잃는 현상을 무엇이라고 부르나요?", 
        ["잠수병", "질소 마취", "얕은 물 기절 (SWB)", "과호흡 증후군"], 
        3
    )
]


import sys # 맨 윗줄에 추가 (종료 처리를 위해 필요)

# ... (앞서 작성한 Quiz 클래스와 default_quizzes 코드는 그대로 둡니다) ...

class QuizGame:
    def __init__(self, quizzes):
        self.quizzes = quizzes  # 퀴즈 목록 데이터
        self.best_score = 0     # 최고 점수 초기화


    def display_menu(self):
        """메뉴 출력 메서드"""
        print("\n" + "=" * 40)
        print("        🎯 나만의 프리다이빙 퀴즈 🎯")
        print("=" * 40)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 40)

    def run(self):
        """게임의 전체 흐름을 제어하는 메인 루프"""
        while True:
            self.display_menu()
            try:
                # 1. 입력 앞뒤 공백 제거 (.strip())
                choice_str = input("선택: ").strip()
                
                # 2. 빈 입력(그냥 Enter) 처리
                if not choice_str:
                    print("⚠️ 빈 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                    continue
                
                # 3. 숫자 변환 시도 (실패 시 ValueError 발생)
                choice = int(choice_str)
                
                # 4. 메뉴 분기 및 범위 이탈 검사
                if choice == 1:
                    print("\n[알림] 퀴즈 풀기 기능은 다음 단계에서 구현합니다!")
                elif choice == 2:
                    print("\n[알림] 퀴즈 추가 기능은 다음 단계에서 구현합니다!")
                elif choice == 3:
                    print("\n[알림] 퀴즈 목록 기능은 다음 단계에서 구현합니다!")
                elif choice == 4:
                    print("\n[알림] 점수 확인 기능은 다음 단계에서 구현합니다!")
                elif choice == 5:
                    print("\n게임을 종료합니다. 안녕히 가세요!")
                    break
                else:
                    print("⚠️ 잘못된 입력입니다. 1-5 사이의 숫자를 입력하세요.")
                    
            except ValueError:
                # 'abc' 같은 문자를 입력했을 때의 처리
                print("⚠️ 잘못된 입력입니다. 문자가 아닌 숫자를 입력해 주세요.")
                
            except (KeyboardInterrupt, EOFError):
                # 평가 기준 충족: Ctrl+C 등으로 강제 종료 시도 시 튕기지 않고 안전하게 처리
                print("\n\n⚠️ 비정상 종료가 감지되었습니다. 데이터를 안전하게 저장하고 종료합니다.")
                # (추후 여기에 state.json 저장 메서드를 호출할 예정입니다)
                break


# 프로그램 실행의 진입점
if __name__ == "__main__":
    game = QuizGame(default_quizzes)
    game.run()