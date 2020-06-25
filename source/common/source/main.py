import sys
from modules import *

def main():
    u_id = input('Enter User ID: ')
    go = Go_recommendation(u_id)
    eat = Eat_recommendation(u_id)
    watch = Watch_recommendation(u_id)

    result = Search_Recommendable_Places(eat, go, u_id)
    if len(result) == 2:
        eat_result = result[0]
        go_result = result[1]
        print()
        print(f'{u_id}님께 추천드릴 맛집은 {eat_result["district"]}에 위치한 \'{eat_result["name"]}\'입니다.')
        print(f'{u_id}님께 추천드릴 데이트 장소는 {go_result["district"]}에 위치한 \'{go_result["p_name"]}\'입니다.')

    elif len(result) == 4:
        eat_result1 = result[0]
        go_result1 = result[1]
        eat_result2 = result[2]
        go_result2 = result[3]
        print()
        print(f'{u_id}님! {eat_result1["district"]}에서의 데이트를 계획하고 계신가요?')
        print(f'{u_id}님께 추천드릴 맛집은 {eat_result1["district"]}에 위치한 \'{eat_result1["name"]}\'입니다.')
        print(f'{u_id}님께 추천드릴 데이트 장소는 {go_result1["district"]}에 위치한 \'{go_result1["p_name"]}\'입니다.\n\n')
        print(f'혹시나! {eat_result2["district"]}에서의 데이트를 계획하고 계신다면?')
        print(f'맛집으로는 {eat_result2["district"]}에 위치한 \'{eat_result2["name"]}\'와 ')
        print(f'데이트 장소로는 {go_result2["district"]}에 위치한 \'{go_result2["p_name"]}\'을(를) 추천드려요.')
        
    print(f'영화가 끌리는 데이트라면 현재 상영중인 영화 \'{watch}\'은(는) 어떠신가요?')

if __name__ == '__main__':
    main()