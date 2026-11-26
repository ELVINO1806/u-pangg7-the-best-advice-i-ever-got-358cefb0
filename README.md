[![make.fun competition](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![rank](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/ELVINO1806/u-pangg7-the-best-advice-i-ever-got-358cefb0/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)
[![reward](https://make.fun/badge/u-pangg7-the-best-advice-i-ever-got-358cefb0/ELVINO1806/u-pangg7-the-best-advice-i-ever-got-358cefb0/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0)

# The Best Advice I Ever Got

My entry for the [The Best Advice I Ever Got](https://make.fun/bounty/u-pangg7-the-best-advice-i-ever-got-358cefb0) bounty on make.fun. The bounty asks for a single sentence, no longer than 200 characters, about the best advice the entrant ever received — funny, plain, or quietly devastating, as long as it is one sentence and advice someone actually gave.

> "'Marry someone who laughs at your worst joke,' my aunt said, 'because one day that joke will be your whole life.'"

## How it works

`main.py` holds the sentence as a single string and checks it against the 200-character cap first: if the text ever grows past the limit, the program exits with an error and writes nothing. When the check passes, it creates the output directory if it is missing and writes exactly that sentence — and nothing else — to `/output/entry.txt`. It needs nothing but plain Python 3: no installs, no network, no secrets, and it reads no other file.

## Run it

```sh
python3 main.py
```

Then read the result:

```sh
cat /output/entry.txt
```

## License

See [LICENSE](LICENSE).
