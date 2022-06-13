#!/bin/bash


install_dep () {

    sudo apt update
    sudo apt install systemtap
    #debug info install of the current kernel
    sudo apt install "linux-image-"$(uname -r)"-dbgsym"

}

"$@"