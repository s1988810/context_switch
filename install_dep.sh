#!/bin/bash


install_dep () {

    sudo apt update
    sudo apt install systemtap

}

"$@"