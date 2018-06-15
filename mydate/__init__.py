from datetime import datetime
import argparse
import pytz


def now(timezone):
    if timezone is None:
        tz = pytz.utc
    else:
        tz = pytz.timezone(timezone)
    return datetime.now(tz=tz)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--timezone")
    args = parser.parse_args()
    print(now(args.timezone))