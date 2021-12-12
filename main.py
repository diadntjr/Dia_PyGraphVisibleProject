import csv
import matplotlib.pyplot as plt

def printcheckcsvfile():
    print(data)

def printlocation():
    inputData = str(input("원하시는 지역을 입력해주세요! "))
    for row in data:
        if inputData in row[2]:
            print(row)
    return inputData

def printSearchData(inputData):
    for row in data:
        if '경상남도' in row[2]:
            for i in row[6:7]:
                name.append(i)
            for j in row[5:6]:
                result.append(j)
    print(name)
    print(result)
    return result, name

def printGraph(inputData, name, result):
    plt.figure(dpi=150)
    plt.figure(figsize=(20, 8))
    plt.rc('font', family='NanumGothic')
    plt.title(inputData + '의 전통시장 점포수 현황')
    plt.xlabel('점포수')
    plt.ylabel('지역')
    plt.barh(name, result, color='tomato')
    plt.show()

if __name__ == '__main__' :
    result = []
    name = []
    f = open('./csv_file/소상공인시장진흥공단_전통시장현황_02_19_2021-2.csv', 'r')
    data = csv.reader(f)
    printcheckcsvfile()
    inputData = printlocation()
    printSearchData(inputData)
   # printGraph(inputData, name, result)