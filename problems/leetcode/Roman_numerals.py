'''
https://leetcode.com/problems/integer-to-roman/
'''

def give_roman(num):
    if num < 1 and num > 3999:
        raise ValueError('num overflow!!')

    mapping = {
        1: 'I',
        4: 'IV',
        5: 'V',
        9: 'IX',
        10: 'X',
        40: 'XL',
        50: 'L',
        90: 'XC',
        100: 'C',
        400: 'CD',
        500: 'D',
        900: 'CM',
        1000: 'M',
        4000: 'EOP'
    }
    res = []
    cut = list(mapping.keys())[::-1]
    while num > 0:
        for idx, val in enumerate(cut):
            if num >= val:
                res.append(mapping[cut[idx]])
                num = num - cut[idx]
                break

    return ''.join(res)

print(give_roman(123))