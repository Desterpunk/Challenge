def saveData(c,str):
    file = open(str,"a")
    file.write(c.name + "\n")
    file.close()
    frecuencia = {}
    file = open(str, 'r')
    lines = file.readlines()
    for line in lines:
        if line in frecuencia:
            frecuencia[line] += 1
        else:
            frecuencia[line] = 1
    file.close()
    
    return frecuencia

                   
def clearData():
    file = open("cache\\firstPlace.txt","w")
    file.write("SCORE: ")
    file.close()
    file = open("cache\\secondPlace.txt","w")
    file.write("SCORE: ")
    file.close()
    file = open("cache\\thirdPlace.txt","w")
    file.write("SCORE: ")
    file.close()