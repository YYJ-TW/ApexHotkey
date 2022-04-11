@echo off
chcp 65001
title Setup Apex Hot Key
echo 正在安裝程式所需的模組 Installing modules
pip install -r requirements.txt
echo 程式運作中 Program is running
py Main.py