# from scipy.special import comb
# import math

def comb(n, k):
    if (k > n):
        return 0
    elif (k == 0):
        return 1
    else:
        return comb(n - 1, k - 1) + comb(n - 1, k);
# 3 boyutlu dusunulebilir matematiksel ispat icin
# K 13 olana kadar normal calisiyor sonrasinda bug var. Muhtemelen e li sayilarla ilgili
def calculate_a(K):
    '''
    P'yi degistirmek girilmesi gereken datanin hangi sayidan baslayacagini seciyor. Arttirmak piramtite saga kaydiriyor. Default: K + 1
    P'yi arttirmak ayni zamanda Worpitzky ucgeninde surumu arttiriyor ///assagi carpraza/// sola goturuyor.///
    L'yi azaltmak Worpitzky ucgeninin surumunu arttiriyor ve assagi goturuyor. Piramitte uste cikiyor. Default: K
    J'yi arttirmak Worpitzky ucgeninde alta inmeni sagliyor. Default: K

    J den buyuk P le L nin esitlenmesi 0 liyor grafikle cozulebilir gibi kesistikleri nokta buluyor sanirim
    L nin negatif sayi olmasi 0 liyor muhtamelen gercek cozum kumesi yok diyor
    P yi K kucukken degistirmek farkli sayilar verdirtiyor
    '''
    A = 5
    P = A
    L = A - 1
    J = 6
    # L yi belli bir seviyenin uzerine cikarmak garip sayilar veriyor.
    # piramidin yonunu degistirmek icin belki - i ler + yapilabilir

    r1 = 0

    # burasi n degerlerine 0 atiyor
    # coefficents = {}
    # for i in range(K + 1):
    #     coefficents["n{}".format(i + 1)] = 0


    for i in range(K + 1): #buradaki K yi degistirmek bir sey yapmiyor cunku combinasyonda (a,b) de b a den buyukse 0 veriyor
        coefficient = (-1) ** i * comb(L, i)
        term = coefficient * (P - i) ** J
        r1 += term

    return r1
'''
    for i in range(K + 1): #buradaki K yi degistirmek bir sey yapmiyor cunku combinasyonda (a,b) de b a den buyukse 0 veriyor
        coefficient = (-1) ** (P - i) * comb(L, i)
        term = coefficient * i ** J
        r1 += term
'''

'''
    Burasi sondaki sifirlari da hesaplayan kisim
    for f in range(K):
        J = K - f
        for i in range(K + 1):
            coefficient = (-1) ** i * comb(K, i)
            term = coefficient * (P - i) ** J
            r1 += term
            '''


K = 6
a = calculate_a(K)
print(a)


# print(math.factorial(K))