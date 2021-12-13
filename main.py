import csv
import matplotlib.pyplot as plt

def printlocation():
    inputData = str(input("원하시는 지역을 입력해주세요! "))
    for row in data:
        if inputData in row[2]:
            print(row)
    return inputData

def printSearchData(InputData):
    result = []
    name = []
    for row in data:
        if '부산광역시' in row[2]:
            for j in row[5::6]:
                result.append(int(j))
            for i in row[0:1]:
                name.append(i)
    print(name)
    print(result)
    return result, name

def printGraph(InputData, name, result):
    plt.figure(dpi=1200)
    plt.figure(figsize=(40, 30))
    plt.rc('font', family='NanumGothic')
    plt.title('부산광역시의 전통시장 점포수 현황')
    plt.xlabel('점포수')
    plt.ylabel('시장이름')
    plt.barh(name, result, color='tomato')
    plt.show()
    plt.savefig("test.jpg", format='jpg', dpi=1200)


if __name__ == '__main__' :
    f = open('./csv_file/소상공인시장진흥공단_전통시장현황_02_19_2021-2.csv', 'r')
    data = csv.reader(f)
    result, name = printSearchData()
    printGraph(name, result)