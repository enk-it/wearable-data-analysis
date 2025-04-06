CREATE TABLE sleep (
    date DateTime,
    deep_sleep_time UInt32,
    shallow_sleep_time UInt32,
    wake_time UInt32,
    start DateTime,
    stop DateTime,
    rem_time UInt32,
    naps String
)
ENGINE = MergeTree()
ORDER BY (date);

CREATE TABLE activity_stage (
    date DateTime,
    start_time DateTime,
    stop_time DateTime,
    distance UInt32,
    calories UInt32,
    steps UInt32
)
ENGINE = MergeTree()
ORDER BY (date, start_time);

CREATE TABLE activity_minute (
    datetime DateTime,
    steps UInt32
)
ENGINE = MergeTree()
ORDER BY (datetime);

CREATE TABLE activity (
    date DateTime,
    steps UInt32,
    distance UInt32,
    run_distance UInt32,
    calories UInt32
)
ENGINE = MergeTree()
ORDER BY (date);