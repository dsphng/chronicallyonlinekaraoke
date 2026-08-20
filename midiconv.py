import pyperclip
import mido

# directory for ur midi file goes here
mid = mido.MidiFile("")

# ♪
lyrics = [
    "Ly>rics go here"
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
