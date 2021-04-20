# theMostAnoyingPopup
Disclaimer:
  This may not work for you, or even be that annoying, but I have found that (partially because of its simplicity) it has been extremely effective for me).


Description:
  I recently decided to code an annoying notification, to remind me of some tasks I have to complete about once a week. The more annoying the notification, the more likely a person is to get the task it's reminding you of done so you can dismiss it. While there are probably plenty of ways to make an annoying popup (alarms, flashing lights, popups that stick permanently on the screen), I wanted to ensure that it was not annoying in a way that slows down the completion of the task of which it is reminding you. After several days spent working with the built in Windows notifications, I learned that there were specific limitations of the implementation that disallow this use case. So, I decided to think more creatively. The thing that has always annoyed me the most on Windows are app windows that are open unnecessarily. For this reason, I realized a simple implementation was going to be the best. Using what I learned working with Windows notifications, I leveraged the inbuilt Windows Task Scheduler to save on system resources when the program is not running, and then spent a few minutes in python creating a window for the popup with Tkinter.
  When run at a scheduled time, the program pops up telling you what to do. If you don't, it just sits there, wasting space on your hot bar, mocking you. Once you complete the task, you can press the button in the window, and it will close automatically. As I said, simple. But for me personally, it has been incredibly effective. This has been especially true for small tasks that can be done in a minute or two. These are small enough to be tempting to just do later (especially if you two minutes away from the end of a tutorial for example) but I find it always works out better if you just take care of said task when you remember it.


Usage:
  For testing:
    python popupwindow.py "The text you want to be on the popup"
  
  On system:
    Open Window's Task Scheduler and add a new task. Set when you want the popup to appear under the "Triggers" tab and then add a new "Action" under the "Actions" tab.
    In that "action", place the path to your Python installation under "Program/script". Then under "Add arguments (optional)", place the path to popupwindow.py and then the text you want to appear on the popup in quotation marks (ex: popupwindow.py "Check weekly event in game.")
    At the time you specified or when the event you set occurs, the popup will trigger automatically.
    Once you have completed the task, press the button in the center of the window.
