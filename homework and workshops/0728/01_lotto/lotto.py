# 여기에 필요한 모듈을 추가합니다.


from calendar import month
from datetime import date
import random
import json
from webbrowser import get

class Lotto:
    # 2-2. 생성자 작성
    def __init__(self):
        self.number_lines = []

    # 2-3. n 줄의 로또 번호를 생성하는 인스턴스 메서드
    def generate_lines(self, n):
        for i in range(n):
            k = random.sample(range(1,46),6)
            k.sort()
            self.number_lines.append(k)
            self.n = n

    # 3-2. 회차, 추첨일, 로또 번호 정보를 출력하는 인스턴스 메서드

    def print_number_lines(self, draw_number):

        year, month, day = self.get_draw_date(draw_number)
       
        print('==================================')
        print(f'     제{draw_number}회 로또     ')
        print('==================================')
        print(f'추첨일 : {year}/{month}/{day} ')
        print('==================================')
        T  = ['A','B','C','D','E']
        for i in range(self.n):
            print(f'{T[i]} : {self.number_lines[i]}')

    # 4-2. 해당 회차의 당첨 번호와 당첨 결과를 출력하는 인스턴스 메서드
    def print_result(self, draw_number):
        
        main_numbers, bonus_number = self.get_lotto_numbers(draw_number)

        print('==========================================')
        print(f'당첨 번호 : {main_numbers} + {bonus_number}')
        print('==========================================')

        for i in range(self.n):
            T  = ['A','B','C','D','E']
            line = self.number_lines[i]
            same_main_counts, is_bonus = self.get_same_info(main_numbers, bonus_number, line)
            ranking = self.get_ranking(same_main_counts, is_bonus)

            if is_bonus == True :
                B = ' + 보너스 '
            else :
                B = ' '

            K = ''
            if ranking == 0 :
                Q = '낙첨'
            else :
                Q = '등 당첨!'
                K = ranking
            print(f'{T[i]} : {same_main_counts}개{B}일치 ({K}{Q})')
        

    # 3-3. 해당 회차 추첨일의 년, 월, 일 정보를 튜플로 반환하는 스태틱 메서드
    @staticmethod
    def get_draw_date(draw_number):
        draw_json = open(f'data\lotto_{draw_number}.json', encoding='utf-8')
        draw_dict = json.load(draw_json)
        t = draw_dict['drwNoDate']
        T = t.split('-')
        year = str(T[0])
        month = str(T[1])
        day = str(T[2])
        
        return year, month, day
        # return year, month, day

    # 4-3. 해당 회차 당첨 번호의 메인 번호와 보너스 번호가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_lotto_numbers(draw_number):
        atari_json = open(f'data\lotto_{draw_number}.json', encoding='utf-8')
        atari_dict = json.load(atari_json)
        main_numbers = []
        for key, value in atari_dict.items():
            if key.startswith('drwt') == True:
                main_numbers.append(value)
        main_numbers.sort()
        bonus_number = atari_dict['bnusNo']
        return main_numbers, bonus_number 
        # return main_numbers, bonus_number

    # 4-4. 한 줄의 로또 번호와 메인 번호가 일치하는 개수와 보너스 번호 일치 여부가 담긴 튜플을 반환하는 스태틱 메서드
    @staticmethod
    def get_same_info(main_numbers, bonus_number, line):
        same_main_counts = 0
        for a in main_numbers:
            if a in line:
                same_main_counts += 1
        
        is_bonus = False
        if bonus_number in line:
            is_bonus = True

        return same_main_counts, is_bonus
        # return same_main_counts, is_bonus

    # 4-5. 당첨 결과를 정수로 반환하는 스태틱 메서드
    @staticmethod
    def get_ranking(same_main_counts, is_bonus):
        if same_main_counts == 6:
            return 1
        if same_main_counts == 5 and is_bonus == True:
            return 2
        if same_main_counts == 5:
            return 3
        if same_main_counts == 4:
            return 4
        if same_main_counts == 3:
            return 5
        if same_main_counts <= 2:
            return 0

        # return ranking
