import pyperclip
import mido

mid = mido.MidiFile("/Users/disphing/Desktop/web stuf/chronically online karaoke/songs/i/notes.mid")

# ♪
lyrics = [
    "Don't be sur>prised",
    "By my he>si>ta>tion",
    "If you bo>ther ask>ing",
    "For my pre>fer>ence",
    "",
    "I'm right be>tween",
    "The nor>mal dis>tri>bu>tion",
    "Cus the ma>jo>ri>ty's",
    "My on>ly re>ference",
    "",
    "The que>stion's asked",
    "You got me stu>tter>ing",
    "It tri>ckles down",
    "Through my men>ta>li>ty",
    "",
    "Some day soon",
    "You'll be the death of me",
    "I wish that we",
    "Could find an in->be>tween",
    "",
    "But in->be>tweens are",
    "All that you are",
    "Should we fi>nish",
    "Or go back to the start?",
    "",
    "All those things I could>n't",
    "Base on in>tu>i>tion",
    "I just need>ed some",
    "Ex>ter>nal in>flu>ence",
    "",
    "I guess I ne>ver real>ised",
    "I did>n't need help",
    "Oh what I'd give to stop",
    "Re>ly>ing on some>bo>dy else",
    "",
    "Yeah all those things I should>n't",
    "Base on in>tu>i>tion",
    "Let 'em shove me a>round",
    "Un>til I make a de>cision",
    "",
    "I guess I ne>ver real>ly",
    "Came clean with my>self",
    "Oh what I'd give to think",
    "Like some>bo>dy else",
    "",
    "♪>♪>♪>♪",
    "",
    "I al>ways tell my>self",
    "I should be more in>de>pen>dent",
    "Like I'm putt>ing my foot down",
    "",
    "Well, sup>pose that's more on me",
    "Than it is on them",
    "Could we just change the sub>ject now?",
    "",
    "Is this what I am?",
    "Should I just give up these plans?",
    "I would get it right this time",
    "If I could just make up my mind!",
    "",
    "♪>♪>♪>♪>♪>♪>♪>♪",
    "",
    "The que>stion's asked",
    "You got me stu>tter>ing",
    "It tri>ckles down",
    "Through my men>ta>li>ty",
    "",
    "A>ny day now",
    "You'll be the death of me",
    "But how am I meant to",
    "Find an in->be>tween?",
    "",
    "When all those things I could>n't",
    "Base on in>tu>i>tion",
    "I just need>ed some",
    "Ex>ter>nal in>flu>ence",
    "",
    "I guess I ne>ver real>ised",
    "I did>n't need help",
    "Oh what I'd give to stop",
    "Re>ly>ing on some>bo>dy else",
    "",
    "Yeah all those things I should>n't",
    "Base on in>tu>i>tion",
    "Let 'em shove me a>round",
    "Un>til I make a de>cision",
    "",
    "I guess I ne>ver real>ly",
    "Came clean with my>self",
    "Oh what I'd give to think",
    "Like some>bo>dy else",
    "",
    "♪>♪>♪>♪",
]

midList = []
for row in mid:
    midList.append(row)

noteEvents = []
for msgNo in range(len(midList)):
    msg = midList[msgNo]
    if msg.type == "note_on" or msg.type == "note_off":
        noteEvents.append(msg)

timetable = []
for msgNo in range(len(noteEvents)):
    msg = noteEvents[msgNo]
    if msg.type == "note_on":
        delayTime = msg.time
        for x in range(msgNo):
            delayTime += noteEvents[msgNo-(x+1)].time
        timetable.append(delayTime)

lyricsSeparated = []
lineNo = []
slideNo = []
currentLine = 0
currentSlide = 0
for line in lyrics:
    if line == "":
        currentLine = 0
        currentSlide += 1
    else:
        currentLine += 1
        current = line.split(" ")
        for word in current:
            if ">" in word:
                syllables = word.split(">")
                for y in range(len(syllables)):
                    if y+1 == len(syllables):
                        lyricsSeparated.append(syllables[y] + " ")
                        lineNo.append(currentLine)
                        slideNo.append(currentSlide)
                    else:
                        lyricsSeparated.append(syllables[y])
                        lineNo.append(currentLine)
                        slideNo.append(currentSlide)
            else:
                lyricsSeparated.append(word+ " ")
                lineNo.append(currentLine)
                slideNo.append(currentSlide)

lyricsClipboard = ""

lyricsClipboard += "[\n"
print("[")
lyricsClipboard += "    [\n"
print("    [")
lyricsClipboard += "        [\n"
print("        [")
for x in range(len(lyricsSeparated)):
    try:
        if lineNo[x+1] != lineNo[x] or slideNo[x+1] != slideNo[x]:
            lyricsClipboard += f'            ["{lyricsSeparated[x]}", {round(timetable[x],4)}]\n'
            print(f'            ["{lyricsSeparated[x]}", {round(timetable[x],4)}]')
        else:
            lyricsClipboard += f'            ["{lyricsSeparated[x]}", {round(timetable[x],4)}],\n'
            print(f'            ["{lyricsSeparated[x]}", {round(timetable[x],4)}],')
    except IndexError:
        lyricsClipboard += f'            ["{lyricsSeparated[x]}", {round(timetable[x],4)}]\n'
        print(f'            ["{lyricsSeparated[x]}", {round(timetable[x],4)}]')
    try:
        if lineNo[x+1] != lineNo[x]:
            lyricsClipboard += "        ],\n"
            print("        ],")
            lyricsClipboard += "        [\n"
            print("        [")
    except IndexError:
        pass
    try:
        if slideNo[x+1] != slideNo[x]:
            lyricsClipboard += "        ],\n"
            print("        ],")
            lyricsClipboard += "    ],\n"
            print("    ],")
            lyricsClipboard += "    [\n"
            print("    [")
            lyricsClipboard += "        [\n"
            print("        [")
    except IndexError:
        pass
lyricsClipboard += "        ]\n"
print("        ]")
lyricsClipboard += "    ]\n"
print("    ]")
lyricsClipboard += "]"
print("]")

pyperclip.copy(lyricsClipboard.replace("],\n        [\n        ],\n    ],","]\n    ],"))