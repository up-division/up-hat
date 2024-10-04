#!/bin/sh

# storage devicce $1 

if [ -d config ]; then
    umount config
    rm -r config/
fi

S_DISC_BLOCK=$1 
# Setup the device (configfs)
modprobe libcomposite
mkdir config
mount none config -t configfs
cd config/usb_gadget

# Add USB3 storage gadget
mkdir usb3_gadget
cd usb3_gadget
echo 0x1a0a > idVendor
echo 0xbadd > idProduct
echo "super-speed-plus" > max_speed
mkdir strings/0x409
echo 12345 > strings/0x409/serialnumber
echo "Intel" > strings/0x409/manufacturer
echo "Mass Storage Gadget" > strings/0x409/product
mkdir configs/c.1
mkdir configs/c.1/strings/0x409
echo "Config1" > configs/c.1/strings/0x409/configuration

# Setup functions
mkdir functions/mass_storage.usb0
echo "$S_DISC_BLOCK" > functions/mass_storage.usb0/lun.0/file
ln -s functions/mass_storage.usb0 configs/c.1
cd ..
# Enable the USB devices
ls /sys/devices/pci0000\:00/0000\:00\:0d.1/ | grep dwc > usb3_gadget/UDC

# Add USB2 storage gadget
mkdir -p usb2_gadget
cd usb2_gadget
echo 0x1a0a > idVendor
echo 0xbadd > idProduct
echo "high-speed" > max_speed
mkdir strings/0x409
echo 12345 > strings/0x409/serialnumber
echo "Intel" > strings/0x409/manufacturer
echo "Mass Storage Gadget" > strings/0x409/product
mkdir configs/c.1
mkdir configs/c.1/strings/0x409
echo "Config1" > configs/c.1/strings/0x409/configuration

# Setup functions
mkdir functions/mass_storage.usb1
echo "$S_DISC_BLOCK" > functions/mass_storage.usb1/lun.0/file
ln -s functions/mass_storage.usb1 configs/c.1
cd ..
# Enable the USB devices
ls /sys/devices/pci0000\:00/0000\:00\:14.1/ | grep dwc > usb2_gadget/UDC

