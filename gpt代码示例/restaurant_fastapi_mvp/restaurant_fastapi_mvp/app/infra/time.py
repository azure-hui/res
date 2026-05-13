from datetime import datetime, timezone


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def isoformat_utc(dt: datetime | None = None) -> str:
    dt = dt or now_utc()
    return dt.isoformat()
