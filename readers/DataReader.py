from schemas.activity import Activity
from schemas.activity_minute import ActivityMinute
from schemas.activity_stage import ActivityStage
from schemas.heartrate_auto import HeartRate
from schemas.sleep import Sleep
from utils import get_csv_file_path
from abc import ABC

class DataReader(ABC):
    def __init__(
            self,
            base_path
    ):
        self.base_path = base_path

    fields = []
    file_name = ""
    model = None

    def read(self) -> list[type(model)]:
        path = f"{self.base_path}/{self.file_name}"
        filepath = get_csv_file_path(path)

        result = []

        with open(filepath, mode='r', encoding='utf-8-sig') as activity_file:
            self.fields = activity_file.readline().strip().split(',')

            for line in activity_file:
                line = line.strip()

                data_tuple = line.split(',')

                data = self.model(
                    **self.dictify(data_tuple)
                )

                result.append(
                    data
                )

        return result

    def dictify(self, list_data: list) -> dict:
        result = {}
        for k, v in zip(self.fields, list_data):
            result[k] = v
        return result



class ActivityReader(DataReader):
    file_name = "ACTIVITY"
    model = Activity

class ActivityMinuteReader(DataReader):
    file_name = "ACTIVITY_MINUTE"
    model = ActivityMinute

class ActivityStageReader(DataReader):
    file_name = "ACTIVITY_STAGE"
    model = ActivityStage

class SleepReader(DataReader):
    file_name = "SLEEP"
    model = Sleep

class HeartRateAutoReader(DataReader):
    file_name = "HEARTRATE_AUTO"
    model = HeartRate