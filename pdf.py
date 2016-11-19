import os
import re
import time


def read_liver_pdf(path, filename):
    dirs = "gs -sDEVICE=txtwrite -o "+"output.txt "+os.getcwd()+"/"+filename
    p = os.popen(dirs)
    time.sleep(2)
    txt=""
    with open ('output.txt','r') as handle:
        txt+= handle.read()
    newtxt = repr(txt)
    lis = txt.split('\n')
    calc = lis[17:31]
    age = lis[6]
    l = ' '.join(calc)
    calcs = re.findall(r'([\d.]+) (?:\*H|\*L)? ', l, re.M)
    ages = re.findall(r'([\d.]+) Year.+\/(\w+)', age, re.M)
    data = {
        'age': ages[0][0],
        'gender': 1 if ages[0][1] == "Male" else 0,
        'tb': calcs[0],
        'db': calcs[1],
        'alkphos': calcs[5],
        'sgpt': calcs[4],
        'sgot': calcs[3],
        'tp': calcs[7],
        'albumin': calcs[3],
        'a/g': calcs[10]
    }
    ldata = [data['age'],data['gender'],data['tb'],data['db'],data['alkphos'],data['sgpt'],data['sgot'], data['tp'],data['albumin'],data['a/g']]
    os.remove('output.txt')
    data = {k: float(v) for k, v in data.items()}
    return ldata

def read_kidney_pdf(path, filename):
    dirs = "gs -sDEVICE=txtwrite -o "+"output.txt "+os.getcwd()+"/"+filename
    p = os.popen(dirs)
    time.sleep(2)
    txt=""
    with open ('output.txt','r') as handle:
        txt+= handle.read()
    newtxt = repr(txt)
    lis = txt.split('\n')
    calc = lis[17:24]
    age = lis[6]
    l = ' '.join(calc)
    calcs = re.findall(r'([\d.]+) (?:\*H|\*L)? ', l, re.M)
    ages = re.findall(r'([\d.]+) Year.+\/(\w+)', age, re.M)
    data = {
        'age': ages[0][0],
        'gender': 1 if ages[0][1] == "Male" else 0,
        'urea': calcs[0],
        'sc': calcs[1],
        'uric_acid': calcs[2],
        'sodium': calcs[3],
        'potassium': calcs[4],
        'chloride': calcs[5],
        'bicarbonate': calcs[6]
    }
    os.remove('output.txt')
    data = {k: float(v) for k, v in data.items()}
    return data

def read_blood_pdf(path, filename):
    dirs = "gs -sDEVICE=txtwrite -o "+"output.txt "+os.getcwd()+"/"+filename
    p = os.popen(dirs)
    time.sleep(2)
    txt=""
    with open ('output.txt','r') as handle:
        txt+= handle.read()
    newtxt = repr(txt)
    lis = txt.split('\n')
    for i,n in enumerate(lis):
        print i,n
    calc = lis[17:26]
    print calc
    age = lis[6]
    l = ' '.join(calc)
    calcs = re.findall(r'([\d.]+) (?:\*H|\*L)? ', l, re.M)
    print calcs
    ages = re.findall(r'([\d.]+) Year.+\/(\w+)', age, re.M)
    data = {
        'age': ages[0][0],
        'gender': 1 if ages[0][1] == "Male" else 0,
        'haemoglobin': calcs[0],
        'pcv': calcs[1],
        'tlc': calcs[2],
        'plates': calcs[3],
        'neutrop': calcs[4],
        'lymph': calcs[5],
        'mono':calcs[6],
        'eosion':calcs[7]
    }
    os.remove('output.txt')
    data = {k: float(v) for k, v in data.items()}
    return data
