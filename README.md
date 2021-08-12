# waveshare-rest-api

This is a simple python app that can be run on Raspberry Pi (tested with Pi zero with Three-colour 2.13"). Bear in mind that I am not a python developer.

I run app with 
sudo nohup flask run --host=0.0.0.0 > log.txt 2>&1 &

app.py mentions amiga4ever font that can be downloaded from here: https://www.dafont.com/amiga-forever.font and needs to be placed in pic directory.

Please note that the drawing is executed in order for each color and red/yellow is painted over the black in the end.  

Currently there are two endpoints 
- one for drawing at POST /json 
- one for clearing the e-paper at GET /clear

## POST /json
```json
{
    "flip":true,
    "operations":[
{
    "type": "IMG",
    "color": "BLACK",
    "x": 104,
    "y": 104,
    "posx":54,
    "posy":0,
    "img":"Qk2+BgAAAAAAAD4AAAAoAAAAZAAAAGgAAAABAAEAAAAAAIAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD////////////////wAAAA////////////////8AAAAIAAAAAAf/////////AAAACAAAAAAH/////////wAAAAn///P/x/////////8AAAAJ///z/8f/////////AAAACf//8//H/////////wAAAAn///P/x/////////8AAAAJ///z/8f/////////AAAACf//8//H/////////wAAAAn///P/x/////////8AAAAJ///z/8H/////////AAAACf//8//w/////////wAAAAn///P//B////////8AAAAJ///z//8P////////AAAACf//8///z////////wAAAAn///P//8////////8AAAAJ///z///n////////AAAACf//8B//4////////wAAAAn///AH//H///////8AAAAJ////w//5////////AAAACf////P/+H///////wAAAAn////5/8E///////8AAAAJ////+f/An///////AAAACf////n/AA///////wAAAAH////5/gwH/h/wBwcAAAAB////+f4fB/4f8AcHAAAAA/////kAHiP+D/AAAwAAAAP////4AABj/gf4+AMAAAAD////+AgB8/4H+P+HAAAAA/////p4D/n+A/j/hwAAAAP////6+Af4/hDw+AMAAAAD////+vgD+P4QcPgDAAAAA/////hzwfz+EDj/BwAAAAP////4B+D8//////8AAAAD////+QfgfP//////AAAAA/////gAAAAAAAAAAAAAAAP////wAAAAAAAAAAAAAAAD////8AAAAAAAAAAAAAAAA/////P5+DBDD7/4+AAAAAP////z+PgQQQ+f+PgAAAAD////8/j5iOAPj/j4AAAAA/////P4MIBgB4f4+AAAAAP////z+BDEMAOD+PgAAAAD5///8/gIhjERgfj4AAAAA+P///PwxAgAAAh4+AAAAAPg///z8MQYAIAIePgAAAAD8H//8/////////j4AAAAAfw///H//8f/5z/4+AAAAAj+D//4f/zMiCc/+PgAAAAIf4f//j/8SAAEP/j4AAAADH/B//8f/AkTAD/4+AAAAA4/gD//x/xHAAI/+PgAAAAPHwAf/8f8xwgnP/j4AAAADwYIB//h///////4+AAAAA/GPAP/8P//////+PgAAAAP4PwA//h8P///4/j4AAAAD/H8IH/+YGDAhwf4+AAAAA/5/Dg//mREiBJH+PgAAAAP+Pw4BAJkRIgCR/j4AAAAD/j8PwACZACIggf4+AAAAA/8/D8B8mQgiIcP+PgAAAAP/nw/A/J///////j4AAAAD/48Pwfyf//////4+AAAAA/+PD8D8n//////+PgAAAAP/gw/E/J///////j4AAAAD/+APwPgAAAAAAAAeAAAAA//4D4DAAAAAAAAAPgAAAAP//A/+AH////////4AAAAD//8P/gD////////+AAAAA///D////////////gAAAAP//w////////////4AAAAD//8P///////////+AAAAA///D////////////gAAAAP//w////////////4AAAAD//8P///////////+AAAAA///D////////////gAAAAP//w////////////4AAAAD//8P///////////+AAAAA///D////////////gAAAAP//w////////////4AAAAD//8P///////////+AAAAA///D////////////gAAAAP//w////////////4AAAAD//8P/+AAAAAAAf/+AAAAA///D//wAAAAAAH//gAAAAP//w//8f/////x//4AAAAD//8P//H/////8f/+AAAAA///D//h////gBH//gAAAAP//w//4f///4AR//4AAAAD//8P/+H///+PEf/+AAAAA///D//h////jxH//gAAAAP//w//4f///48R//4AAAAD//8P/+H///+PEf/8AAAAA///D//x////jxH//EAAAAP//w//8f///48R//BAAAAD//8P//H///+PEf/hwAAAA///D//x////jxH/48AAAAP//w//8f///4AR/4PAAAAD//8P//H///+AEf8PwAAAA///D//h//////D/D8AAAAP//wAAAAAAAAAAAB/AAAAD//8AAAAAAAAAAAA/wAAAA////////////////8AAAAA=="
},
{
    "type": "IMG",
    "color": "RED",
    "x": 104,
    "y": 104,
    "posx":54,
    "posy":0,
    "img":"Qk2+BgAAAAAAAD4AAAAoAAAAZAAAAGgAAAABAAEAAAAAAIAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP///wD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD//////5+DBDD7///wAAAA//////+PgQQQ+f//8AAAAP//////j5iOAPj///AAAAD//////4MIBgB4f//wAAAA//////+BDEMAOD//8AAAAP//////gIhjERgf//AAAAD//////wxAgAAAh//wAAAA//////8MQYAIAIf/8AAAAP////////////////AAAAD////////8f/5z///wAAAA////////zMiCc///8AAAAP///////8SAAEP///AAAAD////////AkTAD///wAAAA////////xHAAI///8AAAAP///////8xwgnP///AAAAD////////////////wAAAA////////////////8AAAAP///////8P///4///AAAAD///////4GDAhwf//wAAAA///////+REiBJH//8AAAAP///////kRIgCR///AAAAD///////5ACIggf//wAAAA///////+QgiIcP//8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAP////////////////AAAAD////////////////wAAAA////////////////8AAAAA=="
},
{
    "type": "TEXT",
    "color": "BLACK",
    "x": 0,
    "y": 0,
    "size": 8,
    "text": "Hello"

},
{
    "type":"LINE",
    "color":"RED",
    "x1":0,
    "y1":10,
    "x2":20,
    "y2":20,
    "fill":0
},
{
    "type":"RECTANGLE",
    "color":"BLACK",
    "x1":10,
    "y1":30,
    "x2":50,
    "y2":40,
    "outline":0
},
{
    "type":"ARC",
    "color":"RED",
    "x1":10,
    "y1":50,
    "x2":50,
    "y2":90,
    "start":0,
    "end":360,
    "fill":0
},
{
    "type":"CHORD",
    "color":"BLACK",
    "x1":160,
    "y1":10,
    "x2":180,
    "y2":30,
    "start":0,
    "end":180,
    "fill":0
},
{
    "type":"POLYGON",
    "color":"RED",
    "points":[160,30,190,40,165,45],
    "fill":0
}
]}
```

