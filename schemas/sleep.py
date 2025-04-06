from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel


class Sleep(BaseModel):
    date: datetime
    deepSleepTime: int
    shallowSleepTime: int
    wakeTime: int
    start: datetime
    stop: datetime
    REMTime: int
    naps: str

    def to_list(self):
        return [self.date, self.deepSleepTime, self.shallowSleepTime, self.wakeTime, self.start, self.stop, self.REMTime, self.naps]
