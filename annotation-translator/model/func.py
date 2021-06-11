import sys

def getValue(value):
    list_, cnt = [], 1
    for v in value.split('\n'):
        if '#' in v:    # #이 있는지 확인하는 문단
            if remark_chk(v):   # 주석이 맞는지 확인
                idx = v.rfind('#')
                value = v[idx:]
                dic = {
                    'label': f'line : {cnt} => {value}',
                    'detail' : f'{value}의 번역문'
                }
                list_.append(dic)
        cnt += 1
    print(list_)


def remark_chk(text):
    chk = True
    for i in list(text):
        if i in ['"', "'"]:
            chk = not chk
        if i == '#' and chk:
            return True
    
    return False

if __name__ == '__main__':
    getValue(sys.argv[1])