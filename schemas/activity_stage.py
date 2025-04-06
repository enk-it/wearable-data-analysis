from datetime import datetime, time
from pydantic import BaseModel, field_validator


class ActivityStage(BaseModel):
    date: datetime
    start: time # %H:%M
    stop: time # %H:%M
    distance: int
    calories: int
    steps: int

    @field_validator('start', 'stop', mode='before')
    @classmethod
    def parse_time(cls, value):
        if isinstance(value, time):
            return value  # Если значение уже time, возвращаем его как есть
        try:
            parsed_time = datetime.strptime(value, '%H:%M').time()
            return parsed_time
        except ValueError:
            raise ValueError(
                f"Неверный формат времени. Ожидался формат HH:MM, получено: {value}")


    def to_list(self):
        # Объединяем date и start в start_datetime
        start_datetime = datetime(
            self.date.year,
            self.date.month,
            self.date.day,
            self.start.hour,
            self.start.minute,
            self.start.second
        )
        # Объединяем date и stop в stop_datetime
        stop_datetime = datetime(
            self.date.year,
            self.date.month,
            self.date.day,
            self.stop.hour,
            self.stop.minute,
            self.stop.second
        )
        # Возвращаем список с объединёнными start_datetime и stop_datetime
        return [self.date, start_datetime, stop_datetime, self.distance, self.calories, self.steps]