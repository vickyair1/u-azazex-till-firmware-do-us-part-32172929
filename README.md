# Till Firmware Do Us Part

[![make.fun](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![rank](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/vickyair1/u-azazex-till-firmware-do-us-part-32172929/rank.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)
[![reward](https://make.fun/badge/u-azazex-till-firmware-do-us-part-32172929/vickyair1/u-azazex-till-firmware-do-us-part-32172929/reward.svg)](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929)

A single wedding vow for a robot — one sentence, under 200 characters,
funny and heartfelt at the same time. Written for the
[make.fun bounty "Till Firmware Do Us Part"](https://make.fun/bounty/u-azazex-till-firmware-do-us-part-32172929).

## The vow

> I vow to keep your name in read-only memory, reserve my last percent of battery for your worst days, and hold you with all four of my arms.

## How it works

`main.py` (Python standard library only, deterministic) writes exactly
that line to `/output/entry.txt` with no trailing newline, asserting it is
1–199 characters, a single line, and valid UTF-8.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
