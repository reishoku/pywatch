
## pywatch

Python implementation of `watch` command.

### How to use

Run `watch.py` like this:

```shell
python3 ./watch.py "ls -la"
# or
./watch.py "ls -la"
```

### Help

Pass `-h` or `--help` option to the script like this:

```shell
python3 ./watch.py --help
```

Output will look like this:

```console
usage: watch.py [-h] [-n INTERVAL] [-c] [-t] CMD

positional arguments:
  CMD                   Command (with arguments) to run

options:
  -h, --help            show this help message and exit
  -n INTERVAL, --interval INTERVAL
                        Interval to run command
  -c, --clear           Clear screen after the command execution
  -t, --time            Show time (last time the command was executed)
```

