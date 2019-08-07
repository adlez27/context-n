# context-n
The pronunciation of the syllabic nasal in Japanese depends strongly on the context of the following consonant. This plugin automates the process of selecting the appropriate variation of the nasal in UTAU. It is compatible with both hiragana `ん` and romaji `n`. Lyrics in the UST may be in CV or VCV, and have any number of prefixes and suffixes.

When using the plugin with a voicebank for the first time, it creates a `context-n.ini` file in the voicebank folder. Settings are copied from `default.ini`, which uses hiragana and matches the encoding of KYE's voicebank. To enable romaji compatibility, users can manually copy settings from `default-romaji.ini` instead.

You are free to distribute your voicebank including the context-n.ini file, and free to redistribute the entire plugin in accordance with the license.

Please submit all bug reports, feature requests, etc. via Github Issues.

Format of `context-n.ini`
```
[settings]
romaji=true/false
[exceptions]
na
ni
nu
ne
no
[mapping]
lyric=nasal
k=ng
t=n
p=m
か=んng
た=んn
ぱ=んm
```
Settings has the romaji flag.

Exceptions has lyrics which contain `n` but do not correspond to `ん`. These are only used when romaji is set to `true`.

Mapping has the correspondence between lyrics and the nasal consonant that should precede it. The plugin checks whether the following note contains the lyric rather than whether the following note exactly matches the lyric, meaning that `k` will match with `ka`, `ki`, etc. Mappings earlier in the list take precedence over ones later in the list, so if `ch` is placed before `h`, the plugin will use the `ch` mapping for the lyric `cha` instead of the `h` mapping.
