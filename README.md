# context-n
The pronunciation of the syllabic nasal in Japanese depends strongly on the context of the following consonant. This plugin automates the process of selecting the appropriate variation of the nasal in UTAU.

Default config matches KYE's voicebank. and is confirmed to work with hiragana CV and VCV. Users may edit global settings in config.ini in the plugin folder, or set individual voicebank settings by creating context-n.ini in their voicebank folder. You are free to distribute your voicebank including the context-n.ini file, and free to redistribute the entire plugin in accordance with the license.

Users may be able to use the plugin with romaji Japanese voicebanks or with standard CVVC voicebanks via custom config. Please submit an issue if there are any problems with doing so.

Format of config.ini/context-n.ini
```
[mapping]
lyric=nasal
ka=ng
ta=n
pa=m
か=んng
た=んn
ぱ=んm
```
