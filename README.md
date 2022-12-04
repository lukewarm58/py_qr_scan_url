## Barcode Scanner + Python Script = Open URLs contained in QR Codes

### System Basics

- Barcode Scanner = Tera D5100 (USB device configured for a "Virtual COM connection")
- Tera D5100 uses generic Windows drivers
- On my machine, the D5100 appears in Device Manager under `Ports (COM & LPT)` as `USB-SERIAL CH340 (COM3)`
- Tested on a Windows 10 machine
- Tested using Python 3.9.12

### Operational Basics

- upon program launch, you will be shown a list of available COM ports and prompted to make a selection
  - program assumes a baud rate of 9600
- once connected, the program should sit quietly in the background until a QR Code is scanned
- once a QR code is scanned a new broswer tab will open and will be directed to the URL baked into the QR Code
  - New tabs should open in your default browser
  - As written, the program is 'stupid' in the sense that it does not check to confirm that the scanned code is a legitimate URL 
  - If you scan the UPC on a box of cereal it will try to navigate to http://cheerios_upc/
  - If the scanned code does not begin with `http://` or `www.` or a typical url scheme, `webbrowser` assumes you are trying to open a file
  - On my Windows machine, `webbrowser` tries to open files using... gasp!... Internet Explorer (not my default browser!)
  - **IMPORTANT DETAIL**: the program assumes that the scanned QR Code terminates with a carriage return (`\r` aka `0x0D` in hex)
  
### Quick Install Guide (Windows 10)
  
- Make sure python is installed
  - open a command prompt and type `python --version`
  - if you don't have python go to [python.org](https://www.python.org/downloads/) and install version 3.9 (any version 3.x will likely work)
- Create a folder to store the `.py` script (e.g. `C:\Documents\Code\qr_scan_url\`)
- Copy the `.py` script from this repo into your newly created folder
- Fire up VScode
  - go to File &rarr; Open Folder
  - select the folder you just created
  - go into the terminal (to open a terminal go to View &rarr; Terminal)
  - you should be positioned inside your newly created directory (e.g. `C:\Documents\Code\qr_scan_url\`)
  - type `python -m venv venv` .... this creates a virtual environment
  - type `.\venv\Scripts\activate` .... this activates the virtual environment
  - type `pip install pyserial` .... this installs the pySerial package inside the virtual environment
  - to confirm that pyserial has installed correctly type `pip list`
  - open the `.py` script (should be visible in the left side Explorer window)
  - you should be able to run the program by clicking on the `Run Python File` icon in the upper right corner (looks like a Play button)
  