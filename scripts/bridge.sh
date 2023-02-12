#!/bin/bash

ip link add $1 type bridge
ip link set $1 up
ip link set enp5s0 master $1
ip address add dev $1 $2
