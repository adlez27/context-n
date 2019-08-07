import sys
import os.path
import shutil
import configparser

ust = configparser.RawConfigParser(allow_no_value=True)
ust.optionxform = lambda option: option
ust.read(sys.argv[1])

config = configparser.RawConfigParser(allow_no_value=True)
config.optionxform = lambda option: option
if (os.path.exists(ust['#SETTING']['VoiceDir'] + "\\context-n.ini")):
    config.read(ust['#SETTING']['VoiceDir'] + "\\context-n.ini")
else:
    shutil.copyfile('default.ini', ust['#SETTING']['VoiceDir'] + "\\context-n.ini")
    config.read(ust['#SETTING']['VoiceDir'] + "\\context-n.ini")
    # TODO: GUI opens to create new per-vb settings

if ('#NEXT' in ust):
    first_note_dex = int(ust.sections()[3][-4:])
    last_note_count = len(ust.sections())-5
    partial = True
else:
    first_note_dex = int(ust.sections()[2][-4:])
    last_note_count = len(ust.sections())-4
    partial = False

def edit(current,next):
    if(config['settings'].getboolean('romaji')):
        if('n' in ust['#'+current]['Lyric']):
            valid = True
            for ex in config['exceptions']:
                if (ex in ust['#'+current]['Lyric']):
                    valid = False
                    break
            if(valid):
                for next_lyric in config['mapping']:
                    if(next_lyric in ust['#'+next]['Lyric']):
                        ust['#'+current]['Lyric'] = ust['#'+current]['Lyric'].replace('n',config['mapping'].get(next_lyric))
                        break
    else:
        if('ん' in ust['#'+current]['Lyric']):
            for next_lyric in config['mapping']:
                if(next_lyric in ust['#'+next]['Lyric']):
                    ust['#'+current]['Lyric'] = ust['#'+current]['Lyric'].replace('ん',config['mapping'].get(next_lyric))
                    break

note_count = 0
for note in ust.sections():
    if ((note != '#VERSION') and (note != '#SETTING') and (note != '#PREV') and (note != '#NEXT') and (note !='#TRACKEND')):
        current_note_dex = str(first_note_dex + note_count).zfill(4)
        next_note_dex = str(first_note_dex + note_count + 1).zfill(4)

        if(note_count == last_note_count):
            if(partial):
                next_note_dex = 'NEXT'
            edit(current_note_dex, next_note_dex)
            break
        else:
            edit(current_note_dex, next_note_dex)
            note_count += 1

with open(sys.argv[1], 'w') as output:
    ust.write(output, space_around_delimiters=False)
