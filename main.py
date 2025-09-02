from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.toast.kivytoast.kivytoast import toast
import requests
import webbrowser
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivy.core.audio import SoundLoader
from kivy.uix.image import Image,AsyncImage,CoreImage
from kivymd.uix.textfield import MDTextField
from kivy.uix.videoplayer import VideoPlayer
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.button import MDRectangleFlatButton, MDFlatButton, MDRaisedButton, MDFillRoundFlatButton, MDFillRoundFlatIconButton, MDRoundFlatIconButton, MDRoundFlatButton, MDFloatingActionButton, MDIconButton
from kivy.properties import ObjectProperty
from kivy.metrics import dp
import requests
import time
import mimetypes
import random
from android.permissions import request_permissions, Permission
from kivy.animation import Animation
from kivy.utils import platform
from android.storage import primary_external_storage_path
from kivy.properties import StringProperty
from kivy.core.clipboard import Clipboard
from kivy.storage.jsonstore import JsonStore
import os
import re
import datetime
import time
import sqlite3
from kivy.clock import Clock
import io
import base64
import webbrowser
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.dialog import MDDialog
from jnius import JavaException
import threading

kv='''
Manager:
    Fir:
    Sec:
<Fir>:
    name:'login'
    MDTextField:
        id: lf1
        mode: 'round'
        helper_text: 'Required'
        required: True
        hint_text: 'Enter Username' 
        pos_hint:{'center_y':0.8}             
        
    MDFloatingActionButton:
        icon:'login'
        pos_hint:{'center_x':0.5,'center_y':0.7}    
        size_hint_x:0.5 
        on_press:app.login() 
        
        
<Sec>:
    name:'home'

        
    MDTextFieldRect:
        id:tf1
        helper_text: 'Required'
        required: True
        hint_text: 'ENTER MSG'  
        size_hint_y:0.05 
        size_hint_x:0.6          
        pos_hint:{'center_y':0.05,'center_x':0.35}       
                 

    MDFloatingActionButton:
        id:tb1
        icon:'send'
        pos_hint:{'center_x':0.8,'center_y':0.05}
        size_hint_x:0.2
        on_press:app.send()

	ScrollView:
	    id:s1
		size_hint_y:0.8	   
	    pos_hint:{'center_y':0.5}
	      	    
	    MDBoxLayout:
	        id:b1
	        orientation:'vertical'
	        adaptive_height:True
	        spacing:10
	        padding:30

    MDTopAppBar:
        id:ta1
        title:'MESSAGE'
        pos_hint:{'top':1}
        md_bg_color:1,0,0,1
        left_action_items:[['menu',lambda x:nd1.set_state('open')]]

    MDNavigationDrawer:
        id:nd1
	    MDBoxLayout:
	        spacing:dp(30)
	        orientation: 'vertical'
	        adaptive_height: True
	        pos_hint:{'center_y':0.8}
	        MDLabel:
	            id:ndl1
	            text: ''	            
	            pos_hint:{'left':1}
	            theme_text_color: 'Primary'
	            font_style: 'H6'	
		
		    MDRaisedButton:
				id:ndb1
				text:'logout'
				size_hint_x:0.5
				on_release:app.logout()      
        


'''








class Manager(ScreenManager):
	pass




class Fir(Screen):
	pass		

class Sec(Screen):
	pass

	
class Demo(MDApp):
    def build(self):
        self.b=Builder.load_string(kv)	
        self.number1=''
        self.url='https://chatapp-26e4a-default-rtdb.firebaseio.com/msg.json'
        self.api='x3eMg4dzBwIc0olCOwPvU3ogJoM7QKorJRVDwMEQ'
        self.tu=f'{self.url}?auth={self.api}'
        self.dict={}
        self.store=JsonStore('user.json')
        if self.store.exists('user'):
            Clock.schedule_once(lambda x: threading.Thread(target=self.on,daemon=True).start(),2)
            u1=self.store.get('user')['username']
            self.number1=u1
            self.b.get_screen('home').ids.ndl1.text=f'YOUR USERNAME:- {self.number1}'
            self.b.current='home'
            
        else:
            self.b.current='login'        
            
        return self.b				
			
    def login(self):
    	try:
    	    number=self.b.get_screen('login').ids.lf1.text
    	    self.b.get_screen('login').ids.lf1.text=''
    	    if number.strip()=='':
                toast('PLEASE ENTER NUMBER')
          
    	    else:
    	        self.dict={}
    	        Clock.schedule_once(lambda x: threading.Thread(target=self.on,daemon=True).start(),2)
    	        self.b.get_screen('home').ids.b1.clear_widgets()
    	        self.b.current='home'        
    	        self.b.transition.direction='left'   
    	        self.number1=number
    	        self.b.get_screen('home').ids.ndl1.text=f'YOUR USERNAME:- {number}'
    	        self.store.put('user',username=number)
    	        
    	        
                
                
    	except Exception as e:
            toast(str(e))    	           	                    
  
    def send(self):
        try:
            msg=self.b.get_screen('home').ids.tf1.text.strip()
            if msg.strip()=='':
                toast('PLEASE ENTER MSG FIRST')
            else:
                tim=str(f'{time.strftime("%d-%m-%Y")}\n{time.strftime("%H:%M:%S")}')
                num=self.number1
                jso={'msg':msg,'time':tim,'number':num}
                requests.post(self.tu,json=jso)
                self.b.get_screen('home').ids.tf1.text=''
            
        except Exception as e:
            toast(str(e))		
            
    def on(self):
        while True:
            try:
                data=requests.get(self.tu).json()
                if data is None:
                    Clock.schedule_once(lambda x: toast(str('NO MESSAGE FOUND')))
                    Clock.schedule_once(lambda x:self.b.get_screen('home').ids.b1.clear_widgets())
                    
                    continue
                    
                if self.dict != data:
                    d={}
                    for k in data:
                        if self.dict.get(k) != data[k]:
                            d[k]=data.get(k)
                            
                            
                    self.dict=data
                    Clock.schedule_once(lambda x,da=d:self.add(da))
                  
                                           
                
            except Exception as e:
                toast(str(e))

    def add(self,data):
        try:
            s1=self.b.get_screen('home').ids.b1         
            for k,v in data.items():                         
	            c1=MDCard(adaptive_height=True,md_bg_color= (0.80, 0.96, 0.76, 1) if v.get('number')==self.number1 else (0.95, 0.95, 0.95, 1),radius=[0,0,0,0],size_hint_x=0.95,pos_hint={'right':1} if v.get('number') == self.number1 else {'x':0})
	            l1=MDLabel(text=str(v.get('msg')),adaptive_height=True)
	            l2=MDLabel(text=str(v.get('time')),adaptive_height=True,halign='right')
	            l3=MDLabel(text=f"send_by:-{v.get('number')}" if v.get('number') != self.number1 else f"send_by:- YOU",adaptive_height=True,halign='left')
	            b1 = MDRaisedButton(
    text='copy',
    on_release=lambda btn, text=v.get('msg'): self.copy(text)
)
	           	            
	            bo1=MDBoxLayout(orientation='vertical',adaptive_height=True,spacing=1,padding=1)
	            bo1.add_widget(l3)
	            bo1.add_widget(l1)
	            bo1.add_widget(l2)
	            bo1.add_widget(b1)
	            c1.add_widget(bo1)
	            s1.add_widget(c1)
	            Clock.schedule_once(lambda dt: self.b.get_screen('home').ids.s1.scroll_to(s1.children[0]))
          
        except Exception as e:
            toast(str(e))     
                
    def logout(self):
        try:
            self.b.get_screen('home').ids.b1.clear_widgets()
            self.dict={}
            self.b.current='login' 
            self.b.transition.direction='right'
            self.b.get_screen('home').ids.nd1.set_state('close')
            self.b.get_screen('home').ids.b1.clear_widgets()
            if self.store.exists('user'):
                self.store.delete('user')
            
            
        except:
            pass            
        
    def copy(self,e):
        Clipboard.copy(e)        
        
        
Demo().run()						
								
