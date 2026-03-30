

def fitness(kromozom):   #kromozom için uygunluk değerini hesaplar   en iyi degeri maxFitness

    capraz_kesisme = 0

    yatay_kesisme = sum([kromozom.count(k)-1 for k in kromozom])/2
    #  örnek kromozom [4, 3, 4, 3]   için (1+1+1+1)/2=2.0 hesaplanır her biri deger 1 tanesi ile kesisti
    #[1, 2, 3, 4]  ---> 0
    #[1, 1, 3, 4]  ---> 1.0
    #[1, 1, 1, 4]  ---> 3.0
    #[1, 1, 1, 1]  ---> 6.0
    #[1, 1, 2, 2]  ---> 2.0

# çapraz kesisime hesabı-------------------------------------------------
    n = len(kromozom)  # 4 vezir için 4 elemanlı kromozom
    count_sol = 0
    count_sag = 0
    capraz_kesisme = 0
    for tur in range(0, n):  # 0 1 2 3
       # print('-----TUR----------------------------------------------- =', tur)
        for sag in range(1, (n - tur)):  # 1,2,3    1,2    1    0
            # print('    sag: ',sag)
            if (kromozom[tur + sag] == (kromozom[tur] + sag) or kromozom[tur + sag] == (
                    kromozom[tur] - sag)):  # sag taraftakileri   sag-alt  sag-üst

                count_sag += 1
               # print('count_sag:', count_sag)
        for sol in range(1, (tur + 1)):  # 0  0,1   0,1,2   0,1,2,3,
            # print('    sol', sol)
            if (kromozom[tur - sol] == (kromozom[tur] + sol) or kromozom[tur - sol] == (
                    kromozom[tur] - sol)):  # sol tarafindaki capraz kesisimler   sol-alt  sol-üst
                count_sol += 1
               # print('count_sol:', count_sol)
    capraz_kesisme = (count_sag + count_sol)/2       # 2 ye bölünmeli
#------------------------------------------------------------------

    return int(yatay_kesisme + capraz_kesisme)

