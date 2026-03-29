# chronically online karaoke !!
it is exactly what it sounds like

---

basically i dont know what im doing and i have very limited experience with github and software development in general so im just gonna dump everything ive got for this so far into this repository and pray that someone who knows what theyre doing can turn it into something worthwhile yknow :3 anyway

## how does it work ??

i mean if youve ever done karaoke or seen those karaoke instrumental videos on youtube its basically just that and not much more; theres a list of songs you can choose from and then whichever one you pick it plays the instrumental to that song and the lyrics show up on screen and you can sing along to it and its super cool and stuff

i will now go through what each file in this repository does

## index.html

this is essentially the entire front end; the javascript at the bottom processes everything in each song folder

## tracks.json

this contains all the info / metadata about each song in the songs folder, basically the stuff that shows up in the search window + before each song actually plays.

its also where you match up each song to its directory within the songs folder. also each song has a "color" attribute that ive yet to do anything with; my idea was to change the yellow highlighted text when the song starts playing to whatever color it says in there but i havent implemented it yet

## songs folder

once each song has its metadata listed in tracks.json, it naturally needs its own folder. each folder for each song requires the following inside:
- "track.mp3": the backing track; most of these ive recreated from scratch bc i like it better as a music production exercise than just using some ai acapella remover, plus even if it isnt perfect its a lot more charming and reminiscent of those other older janky karaoke instrumentals. to anyone making their own karaoke versions of songs, i highly encourage you to do the same[^1]
- "notes.json": very simple timetable of every syllable that shows up in the lyrics. it works as a series of nested lists, strictly adhering the following structure:
  - each syllable is notated as a two-item list; the syllable itself as a string, followed by its exact timestamp in seconds, typically rounded to 4 decimals
  - the last syllable of every word is followed by a space within the string
  - each syllable tuple is contained within a larger list for each line
  - each line list is contained within a larger list for each "slide". when in play, the front end will clear all lyrics from one slide before moving on to the next. DO NOT have more than 4 lines per slide

example:
```
[
    [
        [
            ["This ", 1.1111],
            ["is ", 1.2222],
            ["a ", 1.3333],
            ["ly", 1.4444],
            ["ric ", 1.5555]
        ],
        [
            ["This ", 2.1111],
            ["is ", 2.2222],
            ["a", 2.3333],
            ["no", 2.4444],
            ["ther ", 2.5555],
            ["ly", 2.6666],
            ["ric ", 2.7777]
        ]
    ],
    [
        [
            ["♪", 4],
            ["♪", 5],
            ["♪", 6],
            ["♪ ", 7]
        ],
        [
            ["That ", 8.1111],
            ["was ", 8.2222],
            ["a ", 8.3333],
            ["four ", 8.4444],
            ["beat ", 8.5555],
            ["in", 8.6666],
            ["stru", 8.7777],
            ["men", 8.8888],
            ["tal ", 9],
            ["break ", 9.1111],
        ]
    ]
]
```
- "cover.png": these can be any size but ive been doing mine at 128x128 bc they render at 64x64 and im on a retina display
- some folders in this repository might have a "notes.mid" file; this isnt necessary, those are just what i use to create the syllable timetables (see midiconv.py)

## midiconv.py

this is a rly scuffed tool i was using to generate syllable timetables for each song; it takes a midi file as input and requires the `mido` and `pyperclip` libraries
lyrics are inputted line by line, with spaces separating words and greater-than signs separating syllables. the following is the input notation for the example under "notes.json"
```
[
    "This is a ly>ric",
    "This is a>no>ther lyric",
    "",
    "♪>♪>♪>♪",
    "That was a four beat in>stru>men>tal break"
]
```
ensure that the midi file you're using as input only has one instrument and that the BPM is set to 60 (VERY IMPORTANT). also make sure that the number of notes in the midi file exactly matches the number of syllables in the lyric input

this script will take the start times of each note as input and map them to each syllable in sequential order. upon running it, it will output a faux json file to the console line by line and then copy it in full to your clipboard. you can then paste that into a new json file. i wasnt lying when i said it was scuffed

i will say also the output has a tendency to have a few extra commas here and there so you may have to delete them manually. your code editor should flag them down for you hopefully

---

if you're unsure of anything you can go through the example songs ive included and dissect them a little OR feel free to message me on discord (@disphing) or twitter (@dsphng)

have fun !! :3

[^1]: the only exception to this is laced up by tsubi club which uses the original stems, laced up is licensed under creative commons so i figured it was ok hehe; also on the subject of instrumentals fuckboy by brakence is incomplete
