import random


def kromozom_uret(vezir_sayisi):

    return [ random.randint(1, vezir_sayisi) for _ in range(vezir_sayisi) ]  # rasgele bir kromozom dizisi üretiyoruz 1 ile vezirs arasında vezir sa kadar  eleman üret

def mutasyon(kromozom):

    n = len(kromozom)
    c = random.randint(0, n - 1)

    m = random.randint(1, n)
    kromozom[c] = m
    return kromozom
def alimutasyon(kromozom):

    n = len(kromozom)

    c1 = random.randint(0, n - 1)
    m1 = random.randint(1, n)
    c2 = random.randint(0, n - 1)
    m2 = random.randint(1, n)
    c3 = random.randint(0, n - 1)
    m3 = random.randint(1, n)
    c4 = random.randint(0, n - 1)
    m4 = random.randint(1, n)
    c5 = random.randint(0, n - 1)
    m5 = random.randint(1, n)
    c6 = random.randint(0, n - 1)
    m6 = random.randint(1, n)
    c7 = random.randint(0, n - 1)
    m7 = random.randint(1, n)
    c8 = random.randint(0, n - 1)
    m8 = random.randint(1, n)
    kromozom[c1] = m1
    kromozom[c2] = m2
    kromozom[c3] = m3
    kromozom[c4] = m4
    kromozom[c5] = m5
    kromozom[c6] = m6
    kromozom[c7] = m7
    kromozom[c8] = m8
    return kromozom

def caprazlama(kromozomX, kromozomY):   # iki kromozomdan yeni bir  kromozom üretiyoruz.
    n = len(kromozomX)
    c = random.randint(1, n - 1)   # en az bir tane gen sabit kalsın
    return kromozomX[0:c] + kromozomY[c:n]

def olasilik(kromozom, fitness):   # her kromozom için fitness degeri ile orantili  olasılık degeri döndürüyor.
       return 1/(fitness(kromozom)+1)

def rasgele_kromozom(populasyon, populasyondaki_olasiliklar):

    total = sum(w for w in populasyondaki_olasiliklar)
    r = random.uniform(0, total)
    upto = 0
    for c, w in zip(populasyon, populasyondaki_olasiliklar):
        if upto + w >= r:
            return c
        upto += w
    assert False, "No Chromosome Selected"

def DGA_algoritma(populasyon,fitness):


    yeni_populasyon = []
    populasyondaki_olasiliklar = [olasilik(kromozom, fitness) for kromozom in populasyon]  # populasyondaki her kromozomun olasiliklarını hesaplıyoruz
    for i in range(len(populasyon)):

        x = rasgele_kromozom(populasyon, populasyondaki_olasiliklar)
        y = rasgele_kromozom(populasyon, populasyondaki_olasiliklar)

        child = mutasyon(x)
        child = caprazlama(child, y)
        if fitness(child) > (fitness(x)):
            child = x

        yeni_populasyon.append(child)
        if fitness(child) == 0:
            print('child fitness :',fitness(child))
            break
        #print('child fitness :',fitness(child))
    return yeni_populasyon
def ODA_algoritma(populasyon,fitness):
    mutation_probability = 0.19
    DO=0.08
    T = 100  # populasyon size
    sac=100  # populasyon size
    count=0
    count2=sac
    A=2  # çözüme ne kadar yaklaşma aralıgı
    aliii=0



    yeni_populasyon = []
    populasyondaki_olasiliklar = [olasilik(k, fitness) for k in populasyon]
    for i in range(len(populasyon)):
        x = rasgele_kromozom(populasyon, populasyondaki_olasiliklar)
        y = rasgele_kromozom(populasyon, populasyondaki_olasiliklar)
        child = caprazlama(x, y)
        if random.random() < mutation_probability:
            child = mutasyon(child)

        if fitness(child) > fitness(x):
            child =x
        if fitness(child) > fitness(y):
            child = y
        if fitness(child) == 0:
            print('child fitness :', fitness(child))
            yeni_populasyon.append(child)
            break


          #------------ali--------------
        if (fitness(child)<A):  # belirtilen sayıya A kadar yaklastı ve sayıyoruz
          count+=1
        if(A<=fitness(child)):
          if count!=0:
           count-=100
       # print('count',count)
        if count==T:      # çözümüm  Y yakınında  T üretimdir bulamadık
          if random.random() < DO:
              for i in range(0,99):
                #yeni_populasyon.append(alimutasyon(k))
                yeni_populasyon[i]=alimutasyon(populasyon[i])

              print('------------------------------------------dagıtıldı')
          count=0


           #-------------------------------------

        yeni_populasyon.append(child)

    return yeni_populasyon
def GA_algoritma(populasyon,fitness):
    mutation_probability = 0.19
    yeni_populasyon = []
    populasyondaki_olasiliklar = [olasilik(k, fitness) for k in populasyon]
    for i in range(len(populasyon)):
        x = rasgele_kromozom(populasyon, populasyondaki_olasiliklar) #best chromosome 1
       # print('X-----------',x)
        y = rasgele_kromozom(populasyon, populasyondaki_olasiliklar) #best chromosome 2
       # print('y-----------',y)
        child = caprazlama(x, y) #creating two new chromosomes from the best 2 chromosomes
       # print('capraz-----',child)
        if random.random() < mutation_probability:
            child = mutasyon(child)
           # print('mutas-----',child)
        if fitness(child) > fitness(x):
            child =x
        if fitness(child) > fitness(y):
            child = y
       # print('yenichild =:', child)
        yeni_populasyon.append(child)
        if fitness(child) == 0:
            print('child fitness :', fitness(child))
            break
    return yeni_populasyon


