from clickhouse import client
from readers.DataReader import ActivityReader, \
    ActivityMinuteReader, ActivityStageReader, SleepReader

MIFIT_DATA_PATH = "/home/silencer/PycharmProjects/PythonProject/zeppdata/mifit/7003661208_1743922138594"
AMAZFIT_DATA_PATH = "/home/silencer/PycharmProjects/PythonProject/zeppdata/amazfit/8728727394_1743921195619"

readers = [SleepReader, ActivityStageReader, ActivityMinuteReader, ActivityReader]

sleep = []
activity = []
activity_minute = []
activity_stage = []



for path in [AMAZFIT_DATA_PATH]:
    for reader in readers:
        reader_concrete = reader(path)

        match reader_concrete:
            case SleepReader():
                sleep.extend(reader_concrete.read())
            case ActivityStageReader():
                activity_stage.extend(reader_concrete.read())
            case ActivityMinuteReader():
                activity_minute.extend(reader_concrete.read())
            case ActivityReader():
                activity.extend(reader_concrete.read())


sleep_lists = [i.to_list() for i in sleep]
activity_lists = [i.to_list() for i in activity]
activity_minute_lists = [i.to_list() for i in activity_minute]
activity_stage_lists = [i.to_list() for i in activity_stage]

client.insert('sleep', sleep_lists)
client.insert('activity', activity_lists)
client.insert('activity_minute', activity_minute_lists)
client.insert('activity_stage', activity_stage_lists)
