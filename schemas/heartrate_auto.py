from datetime import datetime, time

from pydantic import BaseModel, field_validator


class HeartRate(BaseModel):
    date: datetime
    time: time
    heartRate: int

    @field_validator('time', mode='before')
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
        combined_datetime = datetime(
            self.date.year,
            self.date.month,
            self.date.day,
            self.time.hour,
            self.time.minute
        )
        return [combined_datetime, self.heartRate]
