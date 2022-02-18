# Anatomy of a Loglang Script
All LogLang scripts are a series of instructions executed one at a time. Each instruction has one or more components, each seperated by a `->` or 'into' symbol. Some instructions begin with special symbols such as `$`, and do not follow this structure.

This line has two components, `0` and `value`.
```
0 -> value
```

This line has three components, `0, 1`, `XOR`, and `result`.
```
0, 1 -> XOR -> result
```

# Storing Data
LogLang has only one data-type: *Booleans*. In LogLang, data is stored inside of mutable variables called `flags`. These `flags` can be set to either `0` or `1`, which could also be refered to as True or False, but digits are used as they more closely resemble digital signals. Flags can have any name, as long as it is lowercase and contains no special characters.

To store data in a `flag`, we `put` data `into` it. These words will come up a lot later on. Say we want to `put` a `0` into `value`; in LogLang, that instruction looks like this:
```
0 -> value
```
