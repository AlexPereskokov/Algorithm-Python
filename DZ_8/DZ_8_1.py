# Сделал два варианта, с хешированием и без
# Тема показалось безумно сложной, поскольку очень много подводных камней и теории
# Буду осваивать уже после диплома, целый день просидел с z-функциями и суффиксным деревом
# Пытался адаптировать код на с++, в итоге то работает то ошибка
# Думаю, в дальнейшем следует делать на этом больший акцент, поскольку тема реально сложная

def simple_var(string):
    _s = string
    _n = len(string)
    _uniq_list = []
    for length in range(_n):
        for index in range(_n - length):
            _pref = _s[index:index+length+1]
            if _uniq_list.count(_pref) == 0 and _pref != _s:
                _uniq_list.append(_pref)
    return len(_uniq_list)


def hash_var(string):
    n = len(string)
    p = 31
    p_pow = [1]
    pref_hash_lst = []
    hash_lst = []
    for pw in range(n-1):
        p += 1
        p_pow_el = (p_pow[pw-1] * p)
        p_pow.append(p_pow_el)
    for hs in range(n):
        pref_hash_el = hash((s[hs]) * p_pow[hs])
        pref_hash_lst.append(pref_hash_el)
        if hs > 0:
            pref_hash_lst[hs] += pref_hash_lst[hs-1]
    for i in range(n+1):
        i += 1
        for j in range(n-i+1):
            cur_h = pref_hash_lst[j + i - 1]
            if j > 0:
                cur_h -= pref_hash_lst[j-1]
            cur_h *= p_pow[n-j-1]
            hash_lst.append(cur_h)
    return len(set(hash_lst))


s = input(' Введите свою строку: ')
print(simple_var(s))
print(hash_var(s))
