from datetime import datetime, timedelta, timezone


def get_expiration_time(minutes: int):
    return datetime.now(timezone.utc) + timedelta(minutes=minutes)