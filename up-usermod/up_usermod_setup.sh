#!/bin/bash -x

input=$1
if [ "$input" = "" ]
then
	input="$USER"
fi
echo "set user name $input" 

sudo cp -r lib /
sudo cp -r etc /

for group in gpio leds spi i2c pwm; do
	if ! getent group $group >/dev/null; then
		addgroup --system $group
	fi
done

# gpio functionality
sudo usermod -a -G gpio ${input}

# leds
sudo usermod -a -G leds ${input}

# spi
sudo usermod -a -G spi ${input}

# i2c
sudo usermod -a -G i2c ${input}

# uart
sudo usermod -a -G dialout ${input}

# pwm
sudo usermod -a -G pwm ${input}

echo "Install Completed/n"
echo "Now reboot the system in 10 seconds"
sleep 10
sudo reboot
