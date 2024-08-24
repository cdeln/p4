# p4

p4 -> pppp -> Poor Persons Probabilistic Profiler.

Based on https://poormansprofiler.org, refactored to work for women too, and with several other improvements, including
- Split up code into several scripts
- Converted the AWK script to work with C++ identifiers
- Increase sample rate by attaching GDB to the process once and control it using Expect instead of re-attaching in a loop.
- Documented usage with manpages

Tech stack: AWK, Bash, Expect, GDB

## Installation
Use the `src`, or `./install` you must

## Documentation
`man p4`
