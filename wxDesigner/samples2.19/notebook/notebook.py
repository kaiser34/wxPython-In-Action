#!/bin/env python
#----------------------------------------------------------------------------
# Name:         notebook.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
from notebook_wdr import *

# constants

ID_TEST = 100

# WDR: classes

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome to Notebook!")
        
        # insert main window here
        
        # WDR: handler declarations for MyFrame
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, ID_TEST, self.OnTest)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_ABOUT, "About...", "Program info")
        file_menu.Append(ID_TEST, "Test dialog...", "Test dialog")
        file_menu.Append(wx.ID_EXIT, "Quit...", "Quit program")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "File")
        
        self.SetMenuBar(menu_bar)
    
    # WDR: handler implementations for MyFrame
    
    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "Welcome to Notebook\n(C)opyright 2000 Robert Roebling",
            "About Notebook", wx.OK|wx.ICON_INFORMATION)
        dialog.CentreOnParent()
        dialog.ShowModal()
    
    def OnTest(self, event):
        dialog = wx.Dialog(self, -1, "Notebook pages")
        NotebookFunc(dialog, True)
        dialog.CentreOnParent()
        dialog.ShowModal()
    
    def OnQuit(self, event):
        self.Close(True)
    
    def OnCloseWindow(self, event):
        self.Destroy()

#----------------------------------------------------------------------------

class MyApp(wx.App):
    
    def OnInit(self):
        frame = MyFrame(None, -1, "Notebook", [20,20], [500,340])
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

