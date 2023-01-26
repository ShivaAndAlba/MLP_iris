
# ------- Data managment - start --------
class DataSmaple:
    sepal_length: int
    sepal_width: int
    petal_length: int
    petal_width: int
    species: str

    def __init__(self, sepal_length, sepal_width, petal_length, petal_width, species):
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species

class DataSet:
    trainingDataLlist: list
    testDataList: list

    def __init__(self):
        dataSetList = []
        indexDataSplit = 75

        f = open("iris.data", "r")
        lines = f.readlines()

        for line in lines:
            splitLine = line.replace('\n', '').split(',')
            dataSetList.append(
                DataSmaple(
                    sepal_length = splitLine[0],
                    sepal_width =  splitLine[1],
                    petal_length = splitLine[2],
                    petal_width = splitLine[3],
                    species = splitLine[4])
            )
        
        random.shuffle(dataSetList)
        self.trainingDataList = dataSetList[0:indexDataSplit]
        self.testDataList = dataSetList[indexDataSplit:-1]
        
# ------- Data managment - end --------