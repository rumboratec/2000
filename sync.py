import BlynkLib

BLYNK_AUTH = 'aef1a8506a9a44708fa7dedd78d13e3c'

# initialize Blynk with security enabled
blynk = BlynkLib.Blynk(BLYNK_AUTH)

def blynk_connected():
    # You can also use blynk.sync_virtual(pin)
    # to sync a specific virtual pin
    print("Updating all values from the server...")
    blynk.sync_all()

blynk.on_connect(blynk_connected)

# start Blynk (this call should never return)
blynk.run()
