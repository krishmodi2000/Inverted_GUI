line = "#NMC,1,2,3,4,5"

if line[0] == '#':
    line = line.lstrip('#')
    line = line.rstrip()
    line = line.split(',')
    line = [int(l) if l.isnumeric() == True else l for l in line]
    print(line)
    [print(type(l)) for l in line]