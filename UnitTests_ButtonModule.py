from button import Button
from DownButton import DownButton
from UpButton import UpButton
from WateringButton import WateringButton
from ModeButton import ModeButton
from button_event_manager import ButtonEventManager
from buttonType import ButtonType
from io_manager import IOManager

def runButtonTest(testButton):
    print(testButton.getButtonType())
    testButton.setupButton()
    print(str(testButton.getButtonState()))
    return True

if __name__ == '__main__':   # Program entrance
    
    print(ButtonType().getButtonTypes())
    ioManager = IOManager()
    bev = ButtonEventManager(ioManager.getConfigObject())
    bev.setupButtons()
    for button in bev.buttonList:
        runButtonTest (button)

    
    while (True):
        pass