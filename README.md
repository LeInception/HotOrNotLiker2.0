# HotOrNotLiker2.0
HotOrNot auto-liker 2021

After hotornot updated their API my old auto-liker script does not work.

They may have updated it after seeing my simple source code, so I sat down and re-wrote it again in 38 lines!

This project requires selenium and only currently runs on windows.

I will update it to MacOS and Linux if there's enough intererst.

# Usage

1. Type `python3 hotornot.py`
2. Log into hotornot/badoo
3. Profit!


# Why does the old script not work

Hotornot now uses the 'isTrusted' flag when detecting clicks, these can not be easily simulated using javascript.

Hence we have to use Selenium for Python, a controllable browser!
