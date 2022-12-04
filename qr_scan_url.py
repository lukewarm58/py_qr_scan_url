## Barcode Scanner in Virtual COM Port Mode
## Program Purpose = scan a QR code with a url and then open said url in a new browser tab
## L. Robertson, December 2022
##
## REQUIRED PACKAGES:
##      pyserial (DANGER: Do not install serial separately from pyserial, conflicts will arise... ask me how I know)
## HELPFUL LINKS:
##      I couldn't get this to work but I still found it useful: https://gist.github.com/maxwiese/db51e4a60d0c09727413e7f5f45af03f
## GOTCHAS:
##      QR Code must terminate with a carriage return (aka: \r   aka: 0x0D)
#------------------------------------------------------------------------------
from time import sleep
import serial
import serial.tools.list_ports
import webbrowser
#------------------------------------------------------------------------------
def search_for_ports():
    list_of_ports = list(serial.tools.list_ports.comports())
    return list_of_ports
#------------------------------------------------------------------------------
def reconnect_loop(com_port):
    while True:     #infinite loop until the connection is re-established
        try:
            serial_conn = serial.Serial(com_port)   #returns an error if a connection is not made
            break   #once a connection is reestablished we can break the loop
        except:
            sleep(3)    #delay before we try again
    
    print("connection has been re-established")
    return serial_conn
#------------------------------------------------------------------------------
if __name__ == "__main__":
    
    print('\nAvailable ports:')
    list_of_ports = search_for_ports()
    index_count = 0   #a dumb counter to keep track of the number of available ports
    for index, port in enumerate(list_of_ports):
        print('[index: {}] {}'.format(index, port.description))
        index_count = index
    
    while True:
        com_port_index = input("\nSelect the port you wish to use (use index number) > ")        #caution, ser_device will be a string.
        if com_port_index.isnumeric():
            if int(com_port_index) <= index_count:
                com_port = list_of_ports[int(com_port_index)].device
                break
            else:
                print("Invalid selection. Please try again.")
        else:
            if com_port_index == 'q':
                print("Exiting program...goodbye")
                exit(0)
            else:
                print("Invalid selection. Please try again.")

    # while True:
    #     try:
    #         baudrate = input("\nEnter baudrate [9600 is typical] > ")
    #         break
    #     except:
    #         print('\ninvalid baudrate...try again')
    
    try:
        serial_conn = serial.Serial(com_port)
        #serial_conn = serial.Serial(com_port, baudrate)
        print("port details: {}" .format(serial_conn))
    except:
        print("error thrown trying to connect to the serial port... program will now exit")
        exit(0)

    print('\nconnection established... let\'s get scanning') 
    

    while serial_conn.is_open:
        try:
            qr_url = serial_conn.read_until(b'\r')  #note: qr_url type will be <class 'bytes'>...assumes qr code ends is 0x0D (carriage return aka \r)
            qr_url_string = qr_url.decode("utf-8")
            print(qr_url_string)
            b = webbrowser.open_new_tab(qr_url_string)
        except:
            print("connection lost... let's try to get it back.")
            serial_conn = reconnect_loop(com_port)

    
    exit(0) 
#------------------------------------------------------------------------------