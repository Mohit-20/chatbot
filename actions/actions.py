from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import webbrowser
import os
import subprocess


class ActionStudyMaterial(Action):

    def name(self) -> Text:
        return "action_study_material"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        entities = tracker.latest_message['entities']
        print(entities)
        try:
            for i in entities:
                if i['entity'] == 'subject':
                    subject = i['value']
                elif i['entity'] == 'material_type':
                    material_type = i['value']
                else:
                    material_type = i['value']
                    
            if subject == 'python':
                if material_type == 'interview':
                    url = 'https://www.interviewbit.com/python-interview-questions/'
                    webbrowser.register('chrome',
                    	None,
                    	webbrowser.BackgroundBrowser("C://Users//gangs//AppData//Local//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)
                    dispatcher.utter_message(text="open chrome...")
                    
                elif material_type == 'tutorial':
                    url = 'https://www.youtube.com/results?search_query=python+interview+tutorial'
                    webbrowser.register('chrome',
                    	None,
                    	webbrowser.BackgroundBrowser("C://Users//gangs//AppData//Local//Google//Chrome//Application//chrome.exe"))
                    webbrowser.get('chrome').open(url)
                    dispatcher.utter_message(text="open chrome..")
                else:
                    dispatcher.utter_message(text="No Match Found Try again...")
        except Exception as e:
            dispatcher.utter_message(text="".format(e))
                
        return []

class ActionNotepad(Action):

    def name(self) -> Text:
        return "action_open_notepad"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            os.system("Notepad")
            dispatcher.utter_message(text="Opening Notepad....")
            return []
        
class ActionStudentPortal(Action):

    def name(self) -> Text:
        return "action_open_portal"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            url = 'https://student.itvedant.com/index.php/site/index'
            webbrowser.register('chrome',
                None,
                webbrowser.BackgroundBrowser("C://Users//gangs//AppData//Local//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open(url)
            dispatcher.utter_message(text="Opening Student Portal..")
            return []

class ActionStudentPortal(Action):

    def name(self) -> Text:
        return "action_open_camera"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            subprocess.run('start microsoft.windows.camera:', shell=True)
            dispatcher.utter_message(text="Opening Camera")
            return []

class ActionOpenApp(Action):

    def name(self) -> Text:
        return "action_vlc_app"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            subprocess.call('C://Program Files//VideoLAN//VLC//vlc.exe')
            dispatcher.utter_message(text="Opening Application...")
            return []
