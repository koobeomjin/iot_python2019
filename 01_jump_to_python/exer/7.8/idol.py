def show_candidates(candidate_list):
    for candidate in candidate_list:
        print(candidate, end='')
    print('')

def make_idol(candidate_list):
    for candidate in candidate_list:
        print('\n신예 아이돌', candidate,'인기급상승', end='')
    print('')

def make_world_star(candidate_list):
    for candidate in candidate_list:
        print('아이돌',candidate,'월드스타 등극')
    print('')

with open('연습생.txt', 'r',encoding='UTF-8') as f:
    candidate_list = []
    temp_list = f.readlines()
    for temp in temp_list:
        candidate_list.append(temp.rstrip())

    show_candidates(temp_list)
    make_idol(candidate_list)
    print('')
    make_world_star(candidate_list)