# config.py

class Config:
    # Appium Server 
    APPIUM_SERVER_URL = "http://127.0.0.1:4723"

    # Android-specific configuration
    ANDROID = {
        "platformName": "Android",
        "platformVersion": "10.0",  # Android version on your device/emulator
        "deviceName": "5744a363",  # Name of the device or emulator --> adb devices 
        "appPackage": "com.uxbert.sfa",  
        "appActivity": "com.uxbert.sfa.MainActivity",  
        "automationName": "UiAutomator2",  
        #"noReset": F,  
        "fullReset": False,  
        "fastReset": True,
        "waitForIdleTimeout": 500,
        "waitForQuiescence": False
    }

    # iOS-specific configuration
    IOS = {
        "platformName": "",
        "platformVersion": "",  # iOS version on your device/simulator
        "deviceName": "",  # Name of the device or simulator
        "bundleId": "",  # app's bundle ID
        "automationName": "XCUITest",  
        "noReset": True,  
        "fullReset": False,  
    }

    # Common configuration
    TIMEOUT = 10  # Default timeout for waits, in seconds
    LOCALE = "EN"  # Default language 
    PLATFORM = "Android"
    
    pass
