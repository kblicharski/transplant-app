from random import *

def DonorABO(age):
    r = random()
    if age < 1:
        r -= 0.4484046693
        if r <= 0:
            return 'O'
        r -= 0.3698054475
        if r <= 0:
            return 'A'
        r -= 0.1364980545
        if r <= 0:
            return 'B'
        r -= 0.04529182879
        if r <= 0:
            return 'AB'
    elif age >= 1 and age <= 5:
        r -= 0.4540906997
        if r <= 0:
            return 'O'
        r -= 0.3691831765
        if r <= 0:
            return 'A'
        r -= 0.13190285
        if r <= 0:
            return 'B'
        r -= 0.04482327388
        if r <= 0:
            return 'AB'
    elif age >=6 and age <=10:
        r -= 0.4543125534
        if r <= 0:
            return 'O'
        r -= 0.3658101079
        if r <= 0:
            return 'A'
        r -= 0.130269389
        if r <= 0:
            return 'B'
        r -= 0.04960794969
        if r <= 0:
            return 'AB'
    elif age >= 11 and age <= 17:
        r -= 0.4312198607
        if r <= 0:
            return 'O'
        r -= 0.3896052867
        if r <= 0:
            return 'A'
        r -= 0.1252902304
        if r <= 0:
            return 'B'
        r -= 0.05388462225
        if r <= 0:
            return 'AB'
    elif age >= 18 and age <= 34:
        r -= 0.4399975274
        if r <= 0:
            return 'O'
        r -= 0.3813692299
        if r <= 0:
            return 'A'
        r -= 0.1281881811
        if r <= 0:
            return 'B'
        r -= 0.05044506153
        if r <= 0:
            return 'AB'
    elif age >= 35 and age <= 49:
        r -= 0.4390806497
        if r <= 0:
            return 'O'
        r -= 0.3839946115
        if r <= 0:
            return 'A'
        r -= 0.1280024401
        if r <= 0:
            return 'B'
        r -= 0.04892229876
        if r <= 0:
            return 'AB'
    elif age >= 50 and age <= 64:
        r -= 0.4464450381
        if r <= 0:
            return 'O'
        r -= 0.3822190111
        if r <= 0:
            return 'A'
        r -= 0.1254289816
        if r <= 0:
            return 'B'
        r -= 0.04590696923
        if r <= 0:
            return 'AB'
    elif age >= 65:
        r -= 0.4718261331
        if r <= 0:
            return 'O'
        r -= 0.375245163
        if r <= 0:
            return 'A'
        r -= 0.1177842566
        if r <= 0:
            return 'B'
        r -= 0.03514444739
        if r <= 0:
            return 'AB'

def RecipABO(age):
    r = random()
    if age < 1:
        r -= 0.4437965261
        if r <= 0:
            return 'O'
        r -= 0.3822580645
        if r <= 0:
            return 'A'
        r -= 0.1274193548
        if r <= 0:
            return 'B'
        r -= 0.04652605459
        if r <= 0:
            return 'AB'
    elif age >= 1 and age <= 5:
        r -= 0.4848097672
        if r <= 0:
            return 'O'
        r -= 0.3473168654
        if r <= 0:
            return 'A'
        r -= 0.1308915389
        if r <= 0:
            return 'B'
        r -= 0.03698182851
        if r <= 0:
            return 'AB'
    elif age >= 6 and age <= 10:
        r -= 0.4759050587
        if r <= 0:
            return 'O'
        r -= 0.3583073603
        if r <= 0:
            return 'A'
        r -= 0.1283864781
        if r <= 0:
            return 'B'
        r -= 0.03740110285
        if r <= 0:
            return 'AB'
    elif age >= 11 and age <= 17:
        r -= 0.4773664525
        if r <= 0:
            return 'O'
        r -= 0.3631917138
        if r <= 0:
            return 'A'
        r -= 0.1205044596
        if r <= 0:
            return 'B'
        r -= 0.03893737412
        if r <= 0:
            return 'AB'
    elif age >= 18 and age <= 34:
        r -= 0.4576955138
        if r <= 0:
            return 'O'
        r -= 0.3751705062
        if r <= 0:
            return 'A'
        r -= 0.1228402546
        if r <= 0:
            return 'B'
        r -= 0.04429372537
        if r <= 0:
            return 'AB'
    elif age >= 35 and age <= 49:
        r -= 0.4461098037
        if r <= 0:
            return 'O'
        r -= 0.3789854193
        if r <= 0:
            return 'A'
        r -= 0.1277469128
        if r <= 0:
            return 'B'
        r -= 0.04715786409
        if r <= 0:
            return 'AB'
    elif age >= 50 and age <= 64:
        r -= 0.4323714268
        if r <= 0:
            return 'O'
        r -= 0.389312786
        if r <= 0:
            return 'A'
        r -= 0.1295944539
        if r <= 0:
            return 'B'
        r -= 0.04872133329
        if r <= 0:
            return 'AB'
    elif age >= 65:
        r -= 0.4290151385
        if r <= 0:
            return 'O'
        r -= 0.3938834405
        if r <= 0:
            return 'A'
        r -= 0.1264031891
        if r <= 0:
            return 'B'
        r -= 0.0506982318
        if r <= 0:
            return 'AB'

def RecipAGE(age):
    r = random()
    if age < 1:
        r -= 0.5308949416
        if r <= 0:
            return int(random(0, 1))
        r -= 0.2686381323
        if r <= 0:
            return int(random(1, 5))
        r -= 0.008404669261
        if r <= 0:
            return int(random(6, 10))
        r -= 0.00326848249
        if r <= 0:
            return int(random(11, 17))
        r -= 0.04233463035
        if r <= 0:
            return int(random(18, 34))
        r -= 0.06054474708
        if r <= 0:
            return int(random(35, 49))
        r -= 0.06552529183
        if r <= 0:
            return int(random(50, 64))
        r -= 0.02038910506
        if r <= 0:
            return int(random(65, 100))
    elif age >= 1 and age <= 5:
        r -= 0.1443427894
        if r <= 0:
            return int(random(0, 1))
        r -= 0.3081682354
        if r <= 0:
            return int(random(1, 5))
        r -= 0.07799644573
        if r <= 0:
            return int(random(6, 10))
        r -= 0.03422628842
        if r <= 0:
            return int(random(11, 17))
        r -= 0.1060356743
        if r <= 0:
            return int(random(18, 34))
        r -= 0.1514513263
        if r <= 0:
            return int(random(35, 49))
        r -= 0.1433554927
        if r <= 0:
            return int(random(50, 64))
        r -= 0.03442374778
        if r <= 0:
            return int(random(65, 100))
    elif age >= 6 and age <= 10:
        r -= 0.02678363481
        if r <= 0:
            return int(random(0, 1))
        r -= 0.08671686981
        if r <= 0:
            return int(random(1, 5))
        r -= 0.1129570686
        if r <= 0:
            return int(random(6, 10))
        r -= 0.1155189814
        if r <= 0:
            return int(random(11, 17))
        r -= 0.1584504309
        if r <= 0:
            return int(random(18, 34))
        r -= 0.2287865849
        if r <= 0:
            return int(random(35, 49))
        r -= 0.2173744275
        if r <= 0:
            return int(random(50, 64))
        r -= 0.05341200217
        if r <= 0:
            return int(random(65, 100))
    elif age >= 11 and age <= 17:
        r -= 0.006876350712
        if r <= 0:
            return int(random(0, 1))
        r -= 0.01950383111
        if r <= 0:
            return int(random(1, 5))
        r -= 0.02245083856
        if r <= 0:
            return int(random(6, 10))
        r -= 0.07390737466
        if r <= 0:
            return int(random(11, 17))
        r -= 0.170926432
        if r <= 0:
            return int(random(18, 34))
        r -= 0.3119362732
        if r <= 0:
            return int(random(35, 49))
        r -= 0.3288145886
        if r <= 0:
            return int(random(50, 64))
        r -= 0.0655843112
        if r <= 0:
            return int(random(65, 100))
    elif age >= 18 and age <= 34:
        r -= 0.002724406978
        if r <= 0:
            return int(random(0, 1))
        r -= 0.010883364
        if r <= 0:
            return int(random(1, 5))
        r -= 0.009252523524
        if r <= 0:
            return int(random(6, 10))
        r -= 0.03158980796
        if r <= 0:
            return int(random(11, 17))
        r -= 0.1674630684
        if r <= 0:
            return int(random(18, 34))
        r -= 0.3037309636
        if r <= 0:
            return int(random(35, 49))
        r -= 0.3844837177
        if r <= 0:
            return int(random(50, 64))
        r -= 0.08987214781
        if r <= 0:
            return int(random(65, 100))
    elif age >= 35 and age <= 49:
        r -= 0.00102936224
        if r <= 0:
            return int(random(0, 1))
        r -= 0.003558289225
        if r <= 0:
            return int(random(1, 5))
        r -= 0.005013375355
        if r <= 0:
            return int(random(6, 10))
        r -= 0.01972308885
        if r <= 0:
            return int(random(11, 17))
        r -= 0.1329783516
        if r <= 0:
            return int(random(18, 34))
        r -= 0.3116870739
        if r <= 0:
            return int(random(35, 49))
        r -= 0.4127297797
        if r <= 0:
            return int(random(50, 64))
        r -= 0.1132806791
        if r <= 0:
            return int(random(65, 100))
    elif age >= 50 and age <= 64:
        r -= 0.0002566759514
        if r <= 0:
            return int(random(0, 1))
        r -= 0.001112262456
        if r <= 0:
            return int(random(1, 5))
        r -= 0.001131275489
        if r <= 0:
            return int(random(6, 10))
        r -= 0.005903546881
        if r <= 0:
            return int(random(11, 17))
        r -= 0.08984608949
        if r <= 0:
            return int(random(18, 34))
        r -= 0.2352482627
        if r <= 0:
            return int(random(35, 49))
        r -= 0.4854502762
        if r <= 0:
            return int(random(50, 64))
        r -= 0.1810516109
        if r <= 0:
            return int(random(65, 100))
    elif age >= 65:
        r -= 0.0001060164325
        if r <= 0:
            return int(random(0, 1))
        r -= 0.0003710575139
        if r <= 0:
            return int(random(1, 5))
        r -= 0.0006360985953
        if r <= 0:
            return int(random(6, 10))
        r -= 0.002173336867
        if r <= 0:
            return int(random(11, 17))
        r -= 0.03975616221
        if r <= 0:
            return int(random(18, 34))
        r -= 0.1690432017
        if r <= 0:
            return int(random(35, 49))
        r -= 0.4956268222
        if r <= 0:
            return int(random(50, 64))
        r -= 0.2922873045
        if r <= 0:
            return int(random(65, 100))

def LiveOrDead(age, reciepABO):
    # False is dead
    r = random()
    if age < 1:
        if reciepABO == 'O':
            r -= 1
            if r <= 0:
                return False
        if reciepABO == 'A':
            r -= 1
            if r <= 0:
                return False
        if reciepABO == 'B':
            r -= 1
            if r <= 0:
                return False
        if reciepABO == 'AB':
            r -= 1
            if r <= 0:
                return False
    elif age >= 1 and age <= 5:
        if reciepABO == 'O':
            r -= 0.9998550515
            if r <= 0:
                return False
            r -= 0.0001449485433
            if r <= 0:
                return True
        if reciepABO == 'A':
            r -= 1
            if r <= 0:
                return False
        if reciepABO == 'B':
            r -= 1
            if r <= 0:
                return False
        if reciepABO == 'AB':
            r -= 1
            if r <= 0:
                return False
    elif age >= 6 and age <= 10:
        if reciepABO == 'O':
            r -= 0.9998291183
            if r <= 0:
                return False
            r -= 0.0001708817498
            if r <= 0:
                return True
        if reciepABO == 'A':
            r -= 1
            if r <= 0:
                return False
        if reciepABO == 'B':
            r -= 1
            if r <= 0:
                return False
        if reciepABO == 'AB':
            r -= 1
            if r <= 0:
                return False
    elif age >= 11 and age <= 17:
        if reciepABO == 'O':
            r -= 0.9992544732
            if r <= 0:
                return False
            r -= 0.000745526839
            if r <= 0:
                return True
        if reciepABO == 'A':
            r -= 0.9992665261
            if r <= 0:
                return False
            r -= 0.0007334739158
            if r <= 0:
                return True
        if reciepABO == 'B':
            r -= 0.999572345
            if r <= 0:
                return False
            r -= 0.0004276550249
            if r <= 0:
                return True
        if reciepABO == 'AB':
            r -= 0.9996685449
            if r <= 0:
                return False
            r -= 0.0003314550878
            if r <= 0:
                return True
    elif age >= 18 and age <= 34:
        if reciepABO == 'O':
            r -= 0.9280164262
            if r <= 0:
                return False
            r -= 0.07198357378
            if r <= 0:
                return True
        if reciepABO == 'A':
            r -= 0.9331587806
            if r <= 0:
                return False
            r -= 0.06684121938
            if r <= 0:
                return True
        if reciepABO == 'B':
            r -= 0.9330835713
            if r <= 0:
                return False
            r -= 0.06691642865
            if r <= 0:
                return True
        if reciepABO == 'AB':
            r -= 0.95390706
            if r <= 0:
                return False
            r -= 0.04609293996
            if r <= 0:
                return True
    elif age >= 35 and age <= 49:
        if reciepABO == 'O':
            r -= 0.898348746
            if r <= 0:
                return False
            r -= 0.101651254
            if r <= 0:
                return True
        if reciepABO == 'A':
            r -= 0.8971702797
            if r <= 0:
                return False
            r -= 0.1028297203
            if r <= 0:
                return True
        if reciepABO == 'B':
            r -= 0.9038919778
            if r <= 0:
                return False
            r -= 0.09610802224
            if r <= 0:
                return True
        if reciepABO == 'AB':
            r -= 0.923366671
            if r <= 0:
                return False
            r -= 0.076633329
            if r <= 0:
                return True
    elif age >= 50 and age <= 64:
        if reciepABO == 'O':
            r -= 0.9481921554
            if r <= 0:
                return False
            r -= 0.05180784464
            if r <= 0:
                return True
        if reciepABO == 'A':
            r -= 0.9434164055
            if r <= 0:
                return False
            r -= 0.05658359449
            if r <= 0:
                return True
        if reciepABO == 'B':
            r -= 0.9505835986
            if r <= 0:
                return False
            r -= 0.04941640139
            if r <= 0:
                return True
        if reciepABO == 'AB':
            r -= 0.9585835577
            if r <= 0:
                return False
            r -= 0.04141644233
            if r <= 0:
                return True
    elif age >= 65:
        if reciepABO == 'O':
            r -= 0.9801145939
            if r <= 0:
                return False
            r -= 0.01988540613
            if r <= 0:
                return True
        if reciepABO == 'A':
            r -= 0.9786693036
            if r <= 0:
                return False
            r -= 0.02133069643
            if r <= 0:
                return True
        if reciepABO == 'B':
            r -= 0.9797479748
            if r <= 0:
                return False
            r -= 0.0202520252
            if r <= 0:
                return True
        if reciepABO == 'AB':
            r -= 0.9773755656
            if r <= 0:
                return False
            r -= 0.02262443439
            if r <= 0:
                return True