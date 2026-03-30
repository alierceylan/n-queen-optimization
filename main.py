from tkinter import ttk
from tkinter import *

from DGA import *


from NvezirFitnessfunction import fitness



root=Tk()

root.title("N VEZIR")



style=ttk.Style()
style.theme_use('classic')

f2=ttk.Frame(root)


f2.pack()
f2.config(width=300,height=100,relief=RIDGE)
#[7, 3, 6, 8, 5, 1, 4, 2]




kromozom_sayisi=100  # populasyondaki kromozom sayısı
generasyon=0


def run(vezir_sayisi):   # verilen vezir_sayisi na uygun kromozom u döndürüyor.

    initialfitness=[]
    i=0
    a=100
    b=100
    #maxFitness =(vezir_sayisi*(vezir_sayisi-1))/2  # bir kromozom için uygunluk değerinin olabilecek en yüksek degeri (hepsi farklı satırda 1 2 3 4 gibi n*(n+1)/2)
    populasyon = [kromozom_uret(vezir_sayisi) for _ in range(kromozom_sayisi)]   #kromozomlardan olusan populasyon yapıyoruz 4 e kromozomsayisi array
    for k in populasyon:
        if fitness(k) < a : a=fitness(k)
#
    generasyon = 0
    eniyi=0

    while not 0 in [fitness(kromozom) for kromozom in populasyon]:  # hiç girmedigi 1-3 arası girdiğide oldu
       # print('generasyonlar deneniyor')
        populasyon =ODA_algoritma(populasyon,fitness)
        generasyon += 1
        print('iterasyon:',generasyon)
        if generasyon==1000 :
          for k in populasyon:
              if fitness(k) < b: b = fitness(k)
          print('initial en küçük fitness:', a)
          print('1000.iterasyon en kücük fitness',b)
          break




    for kromozom in populasyon:     # populasyondaki tüm kromozomların fitness değeri hesablanıyor,0 olanı bulup onu run metoduna cevap olarak döndürüyoruz

        if fitness(kromozom) == 0:
            print('initial en küçük fitness:',a)
            print('iterasyon:', generasyon)
            return kromozom




def run2(nq):
    chrom = [0]*nq
    board = [ [0] * nq for _ in range(nq)]
    BTQueen(board, 0, chrom)
    return chrom




def NxNtahta(dizi):
    counter = 0
    for i in dizi:
        for n in range(len(dizi)):
            if counter%2 == 0:
                if n%2 == 0:
                    if n == i-1:
                        ttk.Label (f1, background='#995', text='♕',font=("?", 30),anchor="center").grid (row=n, column=counter, sticky='snew', ipadx=80/len(dizi), ipady=80/len(dizi))
                    else:
                        ttk.Label (f1, background='#995', text='        ').grid (row=n, column=counter, sticky='snew', ipadx=80/len(dizi), ipady=80/len(dizi))
                else:
                    if n == i-1:
                        ttk.Label (f1, background='#ff9', text='♕',font=("?", 30),anchor="center").grid (row=n, column=counter, sticky='snew', ipadx=80/len(dizi), ipady=80/len(dizi))
                    else:
                        ttk.Label (f1, background='#ff9', text='        ').grid (row=n, column=counter, sticky='snew', ipadx=80/len(dizi), ipady=80/len(dizi))
            else:
                if n%2 == 0:
                    if n == i-1:
                        ttk.Label (f1, background='#ff9', text='♕',font=("?", 30),anchor="center").grid (row=n, column=counter, sticky='snew', ipadx=80/len(dizi), ipady=80/len(dizi))
                    else:
                        ttk.Label (f1, background='#ff9', text='       ').grid (row=n, column=counter, sticky='snew', ipadx=80/len(dizi), ipady=80/len(dizi))
                else:
                    if n == i-1:
                        ttk.Label (f1, background='#995', text='♕',font=("?", 30),anchor="center").grid (row=n, column=counter, sticky='snew', ipadx=80/len(dizi), ipady=80/len(dizi))
                    else:
                        ttk.Label (f1, background='#995', text='        ').grid (row=n, column=counter, sticky='snew', ipadx=80/len(dizi), ipady=80/len(dizi))
        counter+=1


#-------------------------------
style=ttk.Style()
style.theme_use('classic')

f1=ttk.Frame(root)
f1.config(width=300,height=100,relief=RIDGE)



#-----f1.pack()----------------------------------

# =============1===================================================================================
but1 = ttk.Button(f2, text='kolay', width=20)
but1.grid(row=0, column=0, sticky='nsew')
but1.config(command=lambda: [restart_program(), Click()])



def Click():
    Click.a = 1

    if Click.a == 1:
        kromozom = run(4)
        NxNtahta(kromozom)


       # ttk.Label (f2, background='#199', text= 0,font=("?", 15),anchor="center").grid (row=1, column=0, sticky='snew', ipadx=1, ipady=1)
        f1.pack()

# =============2===================================================================================
but2 = ttk.Button(f2, text='orta', width=20)
but2.grid(row=0, column=1, sticky='nsew')
but2.config(command=lambda: [restart_program(), Click2()])


def Click2():
    Click2.s = 2
    if Click2.s == 2:
        kromozom = run(6)
        NxNtahta(kromozom)
        f1.pack()


# =============3===================================================================================

but3 = ttk.Button(f2, text='zor', width=20)
but3.grid(row=0, column=2, sticky='nsew')
but3.config(command=lambda: [restart_program(), Click3()])


def Click3():
    Click3.t = 3

    if Click3.t == 3:
        kromozom = run(8)
        NxNtahta(kromozom)
        f1.pack()


# =============restart program===================================================================================
def restart_program():
    for label in f1.grid_slaves():
        label.grid_forget()


root.mainloop()
