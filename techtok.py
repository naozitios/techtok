import csv
def read_csv(filename):  
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)

# where they want to work
def parse(fn):
    data = read_csv(fn)[1:]
    length = len(data) #number of users
    '\\"text\\":\\"Jakarta\\"'
    passed = 0
    indo = 0
    india = 0
    remote = 0 ##
    sg = 0 ##
    HK = 0 ##
    bang = 0 ##
    NCR = 0 ##
    jak = 0 ## 
    bkk = 0 ##
    hanoi = 0 ##
    hcm = 0
    for i in data:
        if i[7] == 'true':
            passed += 1
        if i[23] == "Indonesia":
            indo += 1
        if i[23] == "India":
            india += 1
        for j in i:
            if '\\"text\\":\\"Jakarta\\"' in j:
                jak += 1
            if '\\"text\\":\\"Hong Kong\\"' in j:
                HK += 1
            if '\\"text\\":\\"Remote\\"' in j:
                remote += 1
            if '\\"text\\":\\"Singapore\\"' in j:
                sg += 1
            if '\\"text\\":\\"Bangalore\\"' in j:
                bang += 1
            if '\\"text\\":\\"National Capital Region\\"' in j:
                NCR += 1
            if '\\"text\\":\\"Bangkok\\"' in j:
                bkk += 1
            if '\\"text\\":\\"Hanoi\\"' in j:
                hanoi += 1
            if '\\"text\\":\\"Ho Chi Minh City\\"' in j:
                hcm += 1


    indoperc = round((float(indo)/float(length)) * 100,2)
    passperc = round((float(passed)/float(length)) * 100,2)
    indiaperc = round((float(india)/float(length)) * 100,2)
    print("Number of users:", length)
    print("Percentage of those from Indo:", indoperc , "%")
    print("Percentage of those from India:", indiaperc , "%")
    print("Percentage of those who passed:", passperc , "%")
    print("Number of those who want to work remotely:", remote)
    print("Number of those who want to work in Jakarta:", jak)
    print("Number of those who want to work in Hong Kong:", HK)
    print("Number of those who want to work in Singapore:", sg)
    print("Number of those who want to work in Bangalore:", bang)
    print("Number of those who want to work in National Capital Region:", NCR)
    print("Number of those who want to work in Bangkok:", bkk)
    print("Number of those who want to work in Hanoi:", hanoi)
    print("Number of those who want to work in Ho Chi Minh City:", hcm)
    return 
    
parse("data.csv")
