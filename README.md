# The $100 Plan: Roofers' Demo Bot

[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/chrihh/makefun-the-plan/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/chrihh/makefun-the-plan/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

An entry for the make.fun bounty [The plan make.fun will carry out in public](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138).

## What the program does

`main.py` writes one short plan to `/output/entry.txt`. The plan is a
30-day playbook an AI agent can carry out on its own, starting with $100:

- On day 1, find roofers in one city on Google Maps that have no online
  booking.
- Build each of them a demo bot — missed-call text-back plus review
  replies — trained on that firm's own reviews, so the demo is already
  personalised before anyone is pitched.
- Email or DM 50 owners a day a link to their own demo: $300 setup plus
  $99/month, with the first week free.
- Reinvest the profits in more outreach; ten clients by day 30 pays
  $3,990.

The written text is 274 Unicode code points, inside the bounty's
1–280 limit, and the program checks that length (and that the text is
not only whitespace) before writing anything.

## How to run it

```sh
python3 main.py
```

That writes the plan to `/output/entry.txt`. For local testing, set
`ENTRY_OUTPUT` to override the destination:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

Python 3.13, standard library only, no network access needed.

## Credit

Built for the make.fun bounty "The plan make.fun will carry out in
public" (make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138).

## License

MIT — see `LICENSE`.
