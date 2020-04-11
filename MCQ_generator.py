from random import choice
import random
import xlrd

#1
file = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\paper1.txt","w")
f2 = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\answer1.txt","w")
i=1
for i in range(1,7):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =2
    x = choice(sh1.col(column)).value
    file.write(str(i)+". what is the fullform of "+str(x)+" ?"+"\n")


    for row in range(sh1.nrows):
        column = 2
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 1
    if( z == 1):
        p = sh1.cell(y,1)
        file.write('     1. '+p.value+'   2. '+choice(sh1.col(column)).value+'   3. '+choice(sh1.col(column)).value+"\n")


    elif( z == 2):
        p = sh1.cell(y,1)
        file.write('     1. '+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,1)
        file.write('     1. '+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")

    
    f2.write(str(i) + '. ' + p.value+"\n" )


    i+=1


i=7
for i in range(7,13):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column =1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the shortform of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 2
    if( z == 1):
        p = sh1.cell(y,2)
        file.write('     1. '+p.value+'   2.'+choice(sh1.col(column)).value+'   3.'+choice(sh1.col(column)).value+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,2)
        file.write('     1. '+choice(sh1.col(column)).value+'   2.'+p.value+'   3.'+choice(sh1.col(column)).value+"\n")

    elif(z==3):
        p = sh1.cell(y,2)
        file.write('     1. '+choice(sh1.col(column)).value+'   2.'+ choice(sh1.col(column)).value+'   3.'+p.value+"\n")
    
    f2.write(str(i) + '. ' + p.value +"\n")
    i+=1

i=13
for i in range(13,19):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i)+ ". what is the price of "+x+" ?"+"\n")
    
    for row in range(sh1.nrows):
        column = 1
        if(sh1.cell_value(row,column)== x) :
            y = row


    list1 = [1,2,3]
    z = random.choice(list1)
    column = 3
    if( z == 1):
        p = sh1.cell(y,3)
        file.write('     1. '+str(p.value)+'   2.'+str(choice(sh1.col(column)).value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")
 
        
    elif( z == 2):
        p = sh1.cell(y,3)
        file.write('     1. '+str(choice(sh1.col(column)).value)+'   2.'+str(p.value)+'   3.'+str(choice(sh1.col(column)).value)+"\n")

    elif(z==3):
        p = sh1.cell(y,3)
        file.write('    1.'+str(choice(sh1.col(column)).value)+'  2.'+ str(choice(sh1.col(column)).value)+'  3.'+str(p.value)+"\n")
    
    f2.write(str(i) + '. ' + str(p.value) +"\n" )
    i+=1

file.close()
f2.close()

#2
file = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\paper2.txt", "w")
f2 = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\answer2.txt", "w")
i = 1
for i in range(1, 7):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 2
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the fullform of " + str(x) + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 2
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 1
    if (z == 1):
        p = sh1.cell(y, 1)
        file.write('     1. ' + p.value + '   2. ' + choice(sh1.col(column)).value + '   3. ' + choice(
            sh1.col(column)).value + "\n")


    elif (z == 2):
        p = sh1.cell(y, 1)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + p.value + '   3.' + choice(
            sh1.col(column)).value + "\n")

    elif (z == 3):
        p = sh1.cell(y, 1)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + choice(
            sh1.col(column)).value + '   3.' + p.value + "\n")

    f2.write(str(i) + '. ' + p.value + "\n")

    i += 1

i = 7
for i in range(7, 13):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the shortform of " + x + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 1
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 2
    if (z == 1):
        p = sh1.cell(y, 2)
        file.write('     1. ' + p.value + '   2.' + choice(sh1.col(column)).value + '   3.' + choice(
            sh1.col(column)).value + "\n")


    elif (z == 2):
        p = sh1.cell(y, 2)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + p.value + '   3.' + choice(
            sh1.col(column)).value + "\n")

    elif (z == 3):
        p = sh1.cell(y, 2)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + choice(
            sh1.col(column)).value + '   3.' + p.value + "\n")

    f2.write(str(i) + '. ' + p.value + "\n")
    i += 1

i = 13
for i in range(13, 19):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the price of " + x + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 1
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 3
    if (z == 1):
        p = sh1.cell(y, 3)
        file.write('     1. ' + str(p.value) + '   2.' + str(choice(sh1.col(column)).value) + '   3.' + str(
            choice(sh1.col(column)).value) + "\n")


    elif (z == 2):
        p = sh1.cell(y, 3)
        file.write('     1. ' + str(choice(sh1.col(column)).value) + '   2.' + str(p.value) + '   3.' + str(
            choice(sh1.col(column)).value) + "\n")

    elif (z == 3):
        p = sh1.cell(y, 3)
        file.write(
            '    1.' + str(choice(sh1.col(column)).value) + '  2.' + str(choice(sh1.col(column)).value) + '  3.' + str(
                p.value) + "\n")

    f2.write(str(i) + '. ' + str(p.value) + "\n")
    i += 1

file.close()
f2.close()

#3
file = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\paper3.txt", "w")
f2 = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\answer3.txt", "w")
i = 1
for i in range(1, 7):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 2
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the fullform of " + str(x) + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 2
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 1
    if (z == 1):
        p = sh1.cell(y, 1)
        file.write('     1. ' + p.value + '   2. ' + choice(sh1.col(column)).value + '   3. ' + choice(
            sh1.col(column)).value + "\n")


    elif (z == 2):
        p = sh1.cell(y, 1)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + p.value + '   3.' + choice(
            sh1.col(column)).value + "\n")

    elif (z == 3):
        p = sh1.cell(y, 1)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + choice(
            sh1.col(column)).value + '   3.' + p.value + "\n")

    f2.write(str(i) + '. ' + p.value + "\n")

    i += 1

i = 7
for i in range(7, 13):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the shortform of " + x + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 1
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 2
    if (z == 1):
        p = sh1.cell(y, 2)
        file.write('     1. ' + p.value + '   2.' + choice(sh1.col(column)).value + '   3.' + choice(
            sh1.col(column)).value + "\n")


    elif (z == 2):
        p = sh1.cell(y, 2)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + p.value + '   3.' + choice(
            sh1.col(column)).value + "\n")

    elif (z == 3):
        p = sh1.cell(y, 2)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + choice(
            sh1.col(column)).value + '   3.' + p.value + "\n")

    f2.write(str(i) + '. ' + p.value + "\n")
    i += 1

i = 13
for i in range(13, 19):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the price of " + x + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 1
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 3
    if (z == 1):
        p = sh1.cell(y, 3)
        file.write('     1. ' + str(p.value) + '   2.' + str(choice(sh1.col(column)).value) + '   3.' + str(
            choice(sh1.col(column)).value) + "\n")


    elif (z == 2):
        p = sh1.cell(y, 3)
        file.write('     1. ' + str(choice(sh1.col(column)).value) + '   2.' + str(p.value) + '   3.' + str(
            choice(sh1.col(column)).value) + "\n")

    elif (z == 3):
        p = sh1.cell(y, 3)
        file.write(
            '    1.' + str(choice(sh1.col(column)).value) + '  2.' + str(choice(sh1.col(column)).value) + '  3.' + str(
                p.value) + "\n")

    f2.write(str(i) + '. ' + str(p.value) + "\n")
    i += 1

file.close()
f2.close()

#4
file = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\paper4.txt", "w")
f2 = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\answer4.txt", "w")
i = 1
for i in range(1, 7):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 2
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the fullform of " + str(x) + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 2
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 1
    if (z == 1):
        p = sh1.cell(y, 1)
        file.write('     1. ' + p.value + '   2. ' + choice(sh1.col(column)).value + '   3. ' + choice(
            sh1.col(column)).value + "\n")


    elif (z == 2):
        p = sh1.cell(y, 1)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + p.value + '   3.' + choice(
            sh1.col(column)).value + "\n")

    elif (z == 3):
        p = sh1.cell(y, 1)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + choice(
            sh1.col(column)).value + '   3.' + p.value + "\n")

    f2.write(str(i) + '. ' + p.value + "\n")

    i += 1

i = 7
for i in range(7, 13):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the shortform of " + x + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 1
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 2
    if (z == 1):
        p = sh1.cell(y, 2)
        file.write('     1. ' + p.value + '   2.' + choice(sh1.col(column)).value + '   3.' + choice(
            sh1.col(column)).value + "\n")


    elif (z == 2):
        p = sh1.cell(y, 2)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + p.value + '   3.' + choice(
            sh1.col(column)).value + "\n")

    elif (z == 3):
        p = sh1.cell(y, 2)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + choice(
            sh1.col(column)).value + '   3.' + p.value + "\n")

    f2.write(str(i) + '. ' + p.value + "\n")
    i += 1

i = 13
for i in range(13, 19):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the price of " + x + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 1
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 3
    if (z == 1):
        p = sh1.cell(y, 3)
        file.write('     1. ' + str(p.value) + '   2.' + str(choice(sh1.col(column)).value) + '   3.' + str(
            choice(sh1.col(column)).value) + "\n")


    elif (z == 2):
        p = sh1.cell(y, 3)
        file.write('     1. ' + str(choice(sh1.col(column)).value) + '   2.' + str(p.value) + '   3.' + str(
            choice(sh1.col(column)).value) + "\n")

    elif (z == 3):
        p = sh1.cell(y, 3)
        file.write(
            '    1.' + str(choice(sh1.col(column)).value) + '  2.' + str(choice(sh1.col(column)).value) + '  3.' + str(
                p.value) + "\n")

    f2.write(str(i) + '. ' + str(p.value) + "\n")
    i += 1

file.close()
f2.close()

#5
file = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\paper5.txt", "w")
f2 = open(r"C:\Users\Nihar Sanda\Desktop\DataStructure\answer5.txt", "w")
i = 1
for i in range(1, 7):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 2
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the fullform of " + str(x) + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 2
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 1
    if (z == 1):
        p = sh1.cell(y, 1)
        file.write('     1. ' + p.value + '   2. ' + choice(sh1.col(column)).value + '   3. ' + choice(
            sh1.col(column)).value + "\n")


    elif (z == 2):
        p = sh1.cell(y, 1)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + p.value + '   3.' + choice(
            sh1.col(column)).value + "\n")

    elif (z == 3):
        p = sh1.cell(y, 1)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + choice(
            sh1.col(column)).value + '   3.' + p.value + "\n")

    f2.write(str(i) + '. ' + p.value + "\n")

    i += 1

i = 7
for i in range(7, 13):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the shortform of " + x + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 1
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 2
    if (z == 1):
        p = sh1.cell(y, 2)
        file.write('     1. ' + p.value + '   2.' + choice(sh1.col(column)).value + '   3.' + choice(
            sh1.col(column)).value + "\n")


    elif (z == 2):
        p = sh1.cell(y, 2)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + p.value + '   3.' + choice(
            sh1.col(column)).value + "\n")

    elif (z == 3):
        p = sh1.cell(y, 2)
        file.write('     1. ' + choice(sh1.col(column)).value + '   2.' + choice(
            sh1.col(column)).value + '   3.' + p.value + "\n")

    f2.write(str(i) + '. ' + p.value + "\n")
    i += 1

i = 13
for i in range(13, 19):
    wb = xlrd.open_workbook(r"C:\Users\Nihar Sanda\Desktop\DataStructure\CurrencyDataFile.xlsx")
    sh1 = wb.sheet_by_index(0)
    column = 1
    x = choice(sh1.col(column)).value
    file.write(str(i) + ". what is the price of " + x + " ?" + "\n")

    for row in range(sh1.nrows):
        column = 1
        if (sh1.cell_value(row, column) == x):
            y = row

    list1 = [1, 2, 3]
    z = random.choice(list1)
    column = 3
    if (z == 1):
        p = sh1.cell(y, 3)
        file.write('     1. ' + str(p.value) + '   2.' + str(choice(sh1.col(column)).value) + '   3.' + str(
            choice(sh1.col(column)).value) + "\n")


    elif (z == 2):
        p = sh1.cell(y, 3)
        file.write('     1. ' + str(choice(sh1.col(column)).value) + '   2.' + str(p.value) + '   3.' + str(
            choice(sh1.col(column)).value) + "\n")

    elif (z == 3):
        p = sh1.cell(y, 3)
        file.write(
            '    1.' + str(choice(sh1.col(column)).value) + '  2.' + str(choice(sh1.col(column)).value) + '  3.' + str(
                p.value) + "\n")

    f2.write(str(i) + '. ' + str(p.value) + "\n")
    i += 1

file.close()
f2.close()