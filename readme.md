# Three word sequences - New Relic Coding challenge
## Prequisites to run the program
- You **must** have Python >= 3.6 installed on your machine. This program uses features only found in newer versions of python.
- Preferred version of Python is >= 3.10.
- [Install python](https://www.python.org/downloads/)

## How to run the program
Run as command line tool.

```python app.py <path/to/file_one.txt> <path/to/file_two.txt> <path/to/file_n.txt>```

Pipe output from file with standard in.

```cat my_file.txt | python app.py```

## Example output
```
$ python app.py moby_dick.txt 
============================ Top 100: most frequent words found =======================
               the sperm whale          ------->                86
                  of the whale          ------->                78
               the white whale          ------->                71
                    one of the          ------->                64
                    of the sea          ------->                57
                    out of the          ------->                57
                   part of the          ------->                53
                     a sort of          ------->                51
                  of the sperm          ------->                43
                    in the sea          ------->                33
                      it was a          ------->                33
              the sperm whales          ------->                30
                       it is a          ------->                29
                   of the boat          ------->                29
                  for a moment          ------->                29
                   of the ship          ------->                28
                 of the whales          ------->                27
                   to the deck          ------->                27
                   the sea and          ------->                26
                   in order to          ------->                25
                   at the same          ------->                25
                  for the time          ------->                25
                   by no means          ------->                25
               the right whale          ------->                25
                    in the air          ------->                24
                     to be the          ------->                24
                 the same time          ------->                24
                      so as to          ------->                24
                 the bottom of          ------->                24
                   that in the          ------->                23
                must have been          ------->                23
                  out of sight          ------->                22
                   there is no          ------->                22
                   it was that          ------->                22
                   at the time          ------->                22
                  into the sea          ------->                22
                 of the pequod          ------->                22
                   there was a          ------->                21
                  now and then          ------->                21
                in the fishery          ------->                21
                 the whale and          ------->                20
                    it was not          ------->                20
                    it was the          ------->                20
                    ......              ......                  ....
=================================== End ============================================
```

```
$ cat moby_dick.txt | python app.py 
============================ Top 100: most frequent words found =======================
               the sperm whale          ------->                86
                  of the whale          ------->                78
               the white whale          ------->                71
                    one of the          ------->                64
                    of the sea          ------->                57
                    out of the          ------->                57
                   part of the          ------->                53
                     a sort of          ------->                51
                  of the sperm          ------->                43
                    in the sea          ------->                33
                      it was a          ------->                33
              the sperm whales          ------->                30
                       it is a          ------->                29
                   of the boat          ------->                29
                  for a moment          ------->                29
                   of the ship          ------->                28
                 of the whales          ------->                27
                   to the deck          ------->                27
                   the sea and          ------->                26
                   in order to          ------->                25
                   at the same          ------->                25
                  for the time          ------->                25
                   by no means          ------->                25
               the right whale          ------->                25
                    in the air          ------->                24
                     to be the          ------->                24
                    .....                   ...                 ...
=================================== End ============================================
```


## Known errors or bugs
- There could exist some issues with hyphenated words. The current regex might still concatenate them. I am unsure if this is expected or not.
    since running the program in the current state gets to the amount of three word characters provided in the sample output.

## Potential for improvement
- Build better regex to handle hypenated words or just remove them prior to executed the regex.
- Containerize the program with docker.
- Room for more robust QA. Better use of Mock (use some @patch decorators).
- Use a min-heap/max-heap to print out the most frequent words. Might get better optimization.
- Use a Git repository for version control and tracking of issues.