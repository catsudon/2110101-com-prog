
# Task: BNK48.py

``` py
inp = ""
aidoru_list = set()
score = {}
oshi_ni_natta = {}
oshi_list_of = {}
SIMP_count = {}
has_voted_for = {}
while (not inp.isdigit()):
    inp = input()
    if (inp.isdigit()):
        break
    otaku, idol, vote = inp.split()
    vote = int(vote)
    aidoru_list.add(idol)

    if idol in score:
        score[idol] += vote
    else:
        score[idol] = vote

    if ((otaku, idol) in oshi_ni_natta):
        pass
    else:
        oshi_ni_natta[(otaku, idol)] = True
        if idol in SIMP_count:
            SIMP_count[idol] += 1
        else:
            SIMP_count[idol] = 1

    if otaku in oshi_list_of:
        oshi_list_of[otaku].add(idol)
    else:
        oshi_list_of[otaku] = set([idol])

    if (otaku, idol) in has_voted_for:
        has_voted_for[(otaku, idol)] += vote
    else:
        has_voted_for[(otaku, idol)] = vote

if inp == '1':
    a = []
    for idol, vote in score.items():
        a += [(-vote, idol)]
    a = sorted(a)
    # print(a)
    b = []
    for i in range(min(3, len(a))):
        b += [a[i][1]]

    print(", ".join(b))

if inp == '2':
    a = []
    for idol, simp in SIMP_count.items():
        a += [(-simp, idol)]
    a = sorted(a)

    b = []
    for i in range(min(3, len(a))):
        b += [a[i][1]]

    print(", ".join(b))

if inp == '3':
    voted = {}
    for (otaku, aidoru), score in has_voted_for.items():
        if otaku in voted:
            voted[otaku] += [(-score, aidoru)]
        else:
            voted[otaku] = [(-score, aidoru)]

    kami_aidoru_lv = {}
    for otaku, list_of_oshi in voted.items():
        list_of_oshi = sorted(list_of_oshi)
        kamioshi = list_of_oshi[0][1]
        if kamioshi in kami_aidoru_lv:
            kami_aidoru_lv[kamioshi] += 1
        else:
            kami_aidoru_lv[kamioshi] = 1

    for i in aidoru_list:
        if(not i in kami_aidoru_lv):
            kami_aidoru_lv[i] = 0

    a = []
    for aidoru, score in kami_aidoru_lv.items():
        a += [(-score, aidoru)]
    a = sorted(a)
    b = []
    for i in range(min(3, len(a))):
        b += [a[i][1]]

    print(", ".join(b))
```
    