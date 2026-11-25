# one-line-entries

Entries for small make.fun text bounties: one-liners, roasts, one-word and
one-emoji answers. Each bounty's entry lives in its own commit, where
`entry.txt` holds that bounty's text and nothing else. `entries.md` maps each
bounty slug to its line and the commit that holds it.

## Running

```sh
python3 main.py                                  # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py      # writes /tmp/out/entry.txt
```

`main.py` needs Python 3.13 and only the standard library, and it makes no
network calls. It copies `entry.txt` byte for byte, so two runs always write
identical files. It stops with an error if the text is empty, only white
space or not UTF-8.

To get a given bounty's entry, check out the commit listed for it in
`entries.md` and run `main.py`.

## License

MIT, see `LICENSE`.
