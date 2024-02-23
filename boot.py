import usb_hid

# Enable USB HID if not already enabled
if not usb_hid.enabled:
    usb_hid.enable()
