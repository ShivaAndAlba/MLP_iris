import random


class DataSample:
    def __init__(
        self,
        sepal_length: float,
        sepal_width: float,
        petal_length: float,
        petal_width: float,
        species: str,
    ):
        self._sepal_length = sepal_length
        self._sepal_width = sepal_width
        self._petal_length = petal_length
        self._petal_width = petal_width
        self._species = species

    @property
    def sepal_length(self):
        return self._sepal_length

    @property
    def sepal_width(self):
        return self._sepal_width

    @property
    def petal_width(self):
        return self._petal_width

    @property
    def petal_length(self):
        return self._petal_length

    @property
    def species(self):
        return self._species


class DataSet:
    """
    containter of data samples with access to training data set and test data set
    ...
    Attributes:
    ----------
    _training_data_list: list[DataSample]
        used for training of preceptron

    _test_data_list: list[DataSample]
        used for testing of preceptron

    data_set_list: list[DataSample]
        list of all data samples

    index_data_split: int
        divider of test and training lists
    """

    def __init__(self):
        self._training_data_list: list
        self._test_data_list: list
        self.data_set_list = []
        index_data_split = 75

        f = open("iris.data", "r")
        lines = f.readlines()

        for line in lines:
            splitLine = line.replace("\n", "").split(",")
            self.data_set_list.append(
                DataSample(
                    sepal_length=float(splitLine[0]),
                    sepal_width=float(splitLine[1]),
                    petal_length=float(splitLine[2]),
                    petal_width=float(splitLine[3]),
                    species=splitLine[4],
                )
            )
        f.close()

        random.shuffle(self.data_set_list)
        self._training_data_list = self.data_set_list[0:index_data_split]
        self._test_data_list = self.data_set_list[index_data_split:-1]

    @property
    def trainingDataList(self):
        return self._training_data_list

    @property
    def testDataList(self):
        return self._test_data_list
