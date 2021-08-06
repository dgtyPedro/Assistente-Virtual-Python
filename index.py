# query : query string that we want to search for.
# tld : tld stands for top level domain which means we want to search our result on google.com or google.in or some other domain.
# lang : lang stands for language.
# num : Number of results we want.
# start : First result to retrieve.
# stop : Last result to retrieve. Use None to keep searching forever.
# pause : Lapse to wait between HTTP requests. Lapse too short may cause Google to block your IP. Keeping significant lapse will make your program slow but its safe and better option.
# Return : Generator (iterator) that yields found URLs. If the stop parameter is None the iterator will loop forever.

import speech_recognition as sr
import os
from gtts import gTTS
from googlesearch import search
import webbrowser


r=sr.Recognizer()
with sr.Microphone() as source:                
    audio = r.listen(source)   

    
phrase=r.recognize_google(audio, language = "en-us", show_all=False)
print(phrase)
phrase_list=phrase.split()
phrase_option=phrase_list[0]
actionlist = ('search', 'play', 'buy', 'find', 'open')


if any(x in phrase_option for x in actionlist):
    print('Running')
    
    class IaSearch:
        def __init__(self):
            actiongo = phrase_option
            textgo = phrase_list
            phrase_list.pop(0)  

        def GoSearch(self):
                       
            what_search=''.join([str(item) for item in phrase_list])
            url = "https://www.google.com.tr/search?q={}".format(what_search)
            webbrowser.open_new_tab(url)

        def GoPlay(self):
            pass

        def GoBuy(self):
            pass

        def GoFind(self):
            pass

        def GoOpen(self):
            pass
    
        
    
    


    
    run=IaSearch()
    if phrase_option=='search':  
        run.GoSearch()
    elif phrase_option=='play':
        run.GoPlay()
    elif phrase_option=='buy':
        run.GoBuy()
    elif phrase_option=='find':
        run.GoFind()
    elif phrase_option=='open':
        run.GoOpen()
    
    

