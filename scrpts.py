def dvizenye(prost, pves):
    vrast = int(input('ввидите растояние'))
    vrema = int(input('ввидите время'))
    sk = vrast // vrema
    print(sk)
    dvizenye = 0.035 * pves + (sk ** 2 / prost) * 0.029 * pves
    dvizenye = dvizenye * vrema
    print(dvizenye)
    return dvizenye
