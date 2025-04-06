from datetime import datetime
from pydantic import BaseModel, field_validator


class Activity(BaseModel):
    date: datetime
    steps: int
    distance: int
    runDistance: int
    calories: int


    @field_validator('date', mode='before')
    @classmethod
    def parse_date(cls, value):
        if isinstance(value, datetime):
            return value
        try:
            return datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise ValueError(f"Неверный формат даты. Ожидался формат YYYY-MM-DD, получено: {value}")


    def to_list(self):
        return [self.date, self.steps, self.distance, self.runDistance, self.calories]
