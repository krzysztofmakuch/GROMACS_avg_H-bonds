from statistics import mean as mean
def read_file(file):
    '''
    '''
    f = open(file, 'r')

    hbonds = []
    maxwaters = []
    for line in f:
        splitline = line.split()
        #print(line)
        if splitline[0].isnumeric():
            #print(line)
            hbonds.append(int(splitline[1]))
            maxwaters.append(int(splitline[2]))

    f.close()

    print(mean(hbonds))
    print(mean(maxwaters))
