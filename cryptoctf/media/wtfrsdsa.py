#!/usr/bin/python -u
import os
import math

def really(really, secure, data, storage, algorithm, securesecure, datadata):
    reallydata = pow(secure, algorithm - 2, algorithm)
    reallysecure = (datadata * reallydata) % algorithm
    securedata = (really * reallydata) % algorithm
    securealgorithm = pow(data, reallysecure, storage)
    algorithmsecure = pow(securesecure, securedata, storage)
    algorithmdata = securealgorithm * algorithmsecure % storage % algorithm
    return algorithmdata == really

def secure(really, secure, data, storage, algorithm, reallyreally):
    reallydata = pow(data, storage, secure)
    reallysecure = reallydata % really
    storagedata = pow(storage, really-2, really) * (reallyreally + algorithm * reallysecure)
    securereally = storagedata % really
    return reallysecure, securereally

def data(really):
    secure = 0
    while not secure:
        data = os.urandom(int(math.ceil(math.log(really, 256))))
        if data:
            algorithm =  int(data.encode('hex'),16)
            if algorithm > 1 and algorithm < really:
                secure = algorithm
    return secure

def storage(really):
    algorithmdata = False
    reallydata = 0
    while not algorithmdata:
        reallydata = data(2**really)
        algorithmdata = algorithm(reallydata)
    return reallydata

def algorithm(really):
    if really == 2:
        return True
    if really % 2 == 0:
        return False
    reallysecure, securereally = 0, really - 1
    while securereally % 2 == 0:
        reallysecure += 1
        securereally //= 2
    for securedata in xrange(64):
        algorithmdata = data(really - 1)
        securealgorithm = pow(algorithmdata, securereally, really)
        if securealgorithm == 1 or securealgorithm == really - 1:
            continue
        for dataalgorithm in xrange(reallysecure - 1):
            securealgorithm = pow(securealgorithm, 2, really)
            if securealgorithm == really - 1:
                break
        else:
            return False
    return True

def reallysecurealgorithm(really, secure):
    reallydata = storage(secure)
    algorithmdata = False
    securedata = 0
    while not algorithmdata:
        securedata = data(2**(really-1))
        securedata = securedata + 2**(really-1)
        securedata = securedata - ((securedata % (2 * reallydata))-1)
        algorithmdata = (securedata > 2**(really-1)) and algorithm(securedata)
    algorithmdata = False
    datadata = 1
    while not algorithmdata:
        datadata +=1
        algorithmdata = pow(datadata, (securedata-1)/reallydata, securedata) > 1
    datadata = pow(datadata, (securedata-1)/reallydata, securedata)
    algorithmdata = 0
    while not algorithmdata:
        algorithmdata = data(2**secure) % reallydata
    return reallydata, securedata, datadata, algorithmdata

def reallysecuredata():
    print """
Welcome to the Really Secure Data Algorithm
Please choose from the following options:
1. Store main secret
2. Store custom secret
3. Exit
"""

def reallysecuredataalgorithm(algorithmsecuredata):
    print "Securing data storage algorithm, please wait..."
    reallydata, securedata, datadata, algorithmdata = reallysecurealgorithm(512,256)
    datareally = data(reallydata)
    datasecure = storage(256)
    datasecure = secure(reallydata, securedata, datadata, datasecure, algorithmdata, datareally)
    if not really(datasecure[0], datasecure[1], datadata, securedata, reallydata, pow(datadata, algorithmdata, securedata), datareally):
        print "Parameters not really secure. Try again later."
        return
    reallydata = reallydata * storage(1024 - math.log(reallydata,2))
    securedata = reallydata
    while True:
        reallydatadata = None
        reallysecuredata()
        algorithm = raw_input("Choose (1, 2, 3):\n")
        try:
            algorithm = int(algorithm)
        except:
            print "Invalid input"
            continue
        if algorithm == 1:
            reallydatadata = algorithmsecuredata
            reallydatadata = int(reallydatadata.encode('hex'),16)
        elif algorithm == 2:
            reallydatadata = raw_input("Custom secret:\n").decode('base64')
            reallydatadata = int(reallydatadata.encode('hex'),16)
        elif algorithm == 3:
            break
        else:
            print "Invalid input"
        if reallydatadata > reallydata:
            print "Invalid secret"
            continue
        datareallyreally = storage(math.log(securedata,2))
        datareallydata = (datareallyreally * reallydata) % securedata
        reallyreallysecure = secure(reallydata, securedata, reallydatadata, datareallyreally, algorithmdata, datareallydata)
        print "Secure Data", '.'.join(map(str, [reallydata, reallyreallysecure[0], reallyreallysecure[1], datareallyreally]))

flag = open('/home/ctf/flag.txt').read()
reallysecuredataalgorithm(flag)
