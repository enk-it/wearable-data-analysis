from readers.DataReader import ActivityReader, \
    ActivityMinuteReader, ActivityStageReader, SleepReader

MIFIT_DATA_PATH = "/home/silencer/PycharmProjects/PythonProject/zeppdata/mifit/7003661208_1743922138594"


readers = [SleepReader, ActivityStageReader, ActivityMinuteReader, ActivityReader]


for reader in readers:
    reader_concrete = reader(MIFIT_DATA_PATH)

    print(reader_concrete.read())

