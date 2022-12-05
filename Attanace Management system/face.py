from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.lang import Builder
import multiprocessing
import tkinter as tk
#import sys
#import os
#import sri

import subprocess

Window.size = (300,600)
#Builder String
helper_string = '''
ScreenManager:
    Main:
    Hello:
    

<Main>:
    name:'login'
    MDTextField:
        id:username
        hint_text:"Enter Username"
        line_color_focus:0,0,0.5,1
        helper_text:"Required"
        helper_text_mode:"on_error"
        pos_hint:{'center_x':0.5,'center_y':0.7}
        requires:True
        size_hint:(0.4,0.1)
    MDTextField:
        id:password
        hint_text:"Enter Password"
        line_color_focus:0,0,0.5,1
        helper_text:"Required"
        helper_text_mode:"on_error"
        pos_hint:{'center_x':0.5,'center_y':0.6}
        requires:True
        size_hint:(0.4,0.1)
        password:True
    MDRectangleFlatButton:
        text:'Submit'
        pos_hint:{'center_x':0.5,'center_y':0.5}
        on_release:root.manager.current='hello'
    
            
    
<Hello>:
    name: 'hello'
    BoxLayout:
        orientation:'vertical'
        MDToolbar:
            title: 'Attendance'
            md_bg_color: .1, .5, .5, 1
            specific_text_color: 1, 1, 1, 1
        MDBottomNavigation:
            panel_color: .1,.5,.5,1
            MDBottomNavigationItem:
                name: 'screen 1'
                text: 'Students'
                icon: 'account-group'
                ScrollView:
                    MDList:
                        TwoLineAvatarListItem:
                            text: "VENKATA SESHA SAI"
                            secondary_text: "IT"
                            on_release: print("venkat")
                        

                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/venkat.jpeg"
                        TwoLineAvatarListItem:
                            text: "KALAM"
                            secondary_text: "ECE"
                            on_release: print("kalam")

                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/kalam.jpeg"
                        TwoLineAvatarListItem:
                            text: "SRIKANTH"
                            secondary_text: "IT"
                            on_release: print("srikanth")

                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/srikanth.jpeg"
                                
                        TwoLineAvatarListItem:
                            text: "GOKUL"
                            secondary_text: "CHEM"
                            on_release: print("gokul")

                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/gokul.jpeg"
                        
                        TwoLineAvatarListItem:
                            text: "SARAN"
                            secondary_text: "IT"
                            on_release: print("saranee")
                            
                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/saran.jpeg"

                        TwoLineAvatarListItem:
                            text: "NITHIS KUMAR"
                            secondary_text: "IT"
                            on_release: print("chuthiya")
                            
                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/nithis.jpeg"

                        TwoLineAvatarListItem:
                            text: "Gautham"
                            secondary_text: "IT"
                            on_release: print("chuthiya")
                            
                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/gauthampunda.jpeg"

                        
                        
                        
                        
                                
                MDFloatingActionButton:
                    icon: "camera"
                    md_bg_color: app.theme_cls.primary_color
                    on_release:app.launchChild()
            
                
                
                
                
            MDBottomNavigationItem:
                name: 'screen 3'
                text: 'Students Absent'
                icon: 'account-multiple-remove'
                ScrollView:
                    MDList:
                        TwoLineAvatarListItem:
                            text: "NITHIS KUMAR"
                            secondary_text: "IT"
                            on_release: print("chuthiya")
                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/nithis.jpeg"

                        TwoLineAvatarListItem:
                            text: "Gautham Gandhi"
                            secondary_text: "IT"
                            on_release: print("gautham gandhi")
                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/gautham.jpeg"
                        TwoLineAvatarListItem:
                            text: "SARAN"
                            secondary_text: "IT"
                            on_release: print("saranee")
                            
                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/saran.jpeg"
                        TwoLineAvatarListItem:
                            text: "GOKUL"
                            secondary_text: "CHEM"
                            on_release: print("gokul")

                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/gokul.jpeg"
                        TwoLineAvatarListItem:
                            text: "SRIKANTH"
                            secondary_text: "IT"
                            on_release: print("srikanth")

                            ImageLeftWidget:
                                source:"C:/Users/SRIKANTH/Desktop/face/image/srikanth.jpeg"
                    

'''
class Main(Screen):
    pass

class Hello(Screen):
    pass
class Profile(Screen):
    pass



sm = ScreenManager()

sm.add_widget(Main(name='login'))
sm.add_widget(Hello(name = 'hello'))
sm.add_widget(Profile(name='profile'))





class DemoApp(MDApp):
    def build(self):
        screen = Screen()

        self.help_str = Builder.load_string(helper_string)

        screen.add_widget(self.help_str)

        return screen
    def launchChild(self):
        subprocess.call(['ipython', 'sri.py'], stdout=True)
        #subprocess.call(['ipython', 'exel.py'], stdout=True)
        print("fuck off")
    def logincheck(self):
        user=self.help_str.get_screen('login').ids.username.text
        password=self.help_str.get_screen('login').ids.password.text
        if(user==password):
            pass

if __name__=='__main__':
     DemoApp().run()