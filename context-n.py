import sys
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

ust = configparser.RawConfigParser(allow_no_value=True)
ust.optionxform = lambda option: option
ust.read(sys.argv[1])

if ('#NEXT' in ust):
    first_note_dex = int(ust.sections()[3][-4:])
    last_note_count = len(ust.sections())-5
    partial = True
else:
    first_note_dex = int(ust.sections()[2][-4:])
    last_note_count = len(ust.sections())-4
    partial = False

note_count = 0

for note in ust.sections():
    if ((note != '#VERSION') and (note != '#SETTING') and (note != '#PREV') and (note != '#NEXT') and (note !='#TRACKEND')):
        current_note_dex = str(first_note_dex + note_count).zfill(4)
        next_note_dex = str(first_note_dex + note_count + 1).zfill(4)

        if(note_count == last_note_count):
            if(partial):
                next_note_dex = 'NEXT'
            if('ん' in ust['#'+current_note_dex]['Lyric']):
                for next_kana in config['mapping']:
                    if(next_kana in ust['#'+next_note_dex]['Lyric']):
                        ust['#'+current_note_dex]['Lyric'] = ust['#'+current_note_dex]['Lyric'].replace('ん',config['mapping'].get(next_kana))
            break
        else:
            if('ん' in ust['#'+current_note_dex]['Lyric']):
                for next_kana in config['mapping']:
                    if(next_kana in ust['#'+next_note_dex]['Lyric']):
                        ust['#'+current_note_dex]['Lyric'] = ust['#'+current_note_dex]['Lyric'].replace('ん',config['mapping'].get(next_kana))
            note_count += 1

with open(sys.argv[1], 'w') as output:
    ust.write(output, space_around_delimiters=False)
