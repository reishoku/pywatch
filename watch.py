#!/usr/bin/python3

import sys
import time
import argparse
import datetime
import subprocess


def clear() -> None:
    return print('\033[H\033[J')


def interval(n) -> int:

    if not isinstance(n, int):
        raise ValueError

    try:
        _n: int = int(n)
    except ValueError:
        return False
    except Exception:
        return False

    return _n if _n > 0 else 1  # 1: default interval


def main(cmd: list, interval: int, clearscreen: bool, showtime: bool) -> None:
    if not isinstance(cmd, list):
        raise TypeError

    if not isinstance(interval, int):
        raise TypeError

    if not isinstance(clearscreen, bool) or not isinstance(showtime, bool):
        raise TypeError

    if not len(cmd) > 0:
        raise ValueError

    try:
        _cmdres: list = []
        while True:
            if clearscreen:
                clear()

            if showtime:
                timeformat: str = "%Y/%m/%d %H:%M:%S"
                print(
                    "Current time: {}\n".format(datetime.datetime.now().strftime(timeformat)),
                    file=sys.stderr
                )

            _cmdres = \
                subprocess.run(
                    cmd, capture_output=True, text=True
                ).stdout.splitlines().copy() \
                + [""]
            if _cmdres != []:
                for line in _cmdres:
                    print(line)
            time.sleep(interval)
    except Exception as e:
        raise e


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n", "--interval",
        type=int,
        required=False,
        default=1,
        help="Interval to run command"
    )
    parser.add_argument(
        "-c", "--clear",
        action="store_true",
        default=False,
        help="Clear screen after the command execution"
    )
    parser.add_argument(
        "-t", "--time",
        action="store_true",
        default=False,
        help="Show time (last time the command was executed)"
    )
    parser.add_argument(
        "cmd",
        metavar="CMD",
        type=str,
        help="Command (with arguments) to run"
    )

    args = parser.parse_args()

    if not isinstance(args.cmd, str):
        raise argparse.ArgumentTypeError
    if not len(args.cmd) > 0:
        raise ValueError

    # main routine
    try:
        main(
            cmd=(args.cmd).split(),
            interval=args.interval,
            clearscreen=args.clear,
            showtime=args.time,
        )
    except KeyboardInterrupt:
        pass
    except Exception as e:
        SystemExit(e)  # implement later (maybe never)

    exit(0)
