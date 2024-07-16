#!/bin/bash
chip=$1
channel=$2
freq=$3
duty=$4
echo chip $1 channel $2 set freq $3 duty $4%

period=$((1000000000/freq))
period_duty=$((period*duty/100))

if [ -d "/sys/class/pwm/pwmchip$chip/pwm$channel" ]; then
        echo skip export channel $channel
else
        echo $channel > /sys/class/pwm/pwmchip$chip/export
fi
echo 0 > /sys/class/pwm/pwmchip$chip/pwm$channel/duty_cycle
echo $period > /sys/class/pwm/pwmchip$chip/pwm$channel/period
echo $period_duty > /sys/class/pwm/pwmchip$chip/pwm$channel/duty_cycle
echo 1 > /sys/class/pwm/pwmchip$chip/pwm$channel/enable

echo set ok
