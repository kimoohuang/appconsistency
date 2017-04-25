#!/usr/bin/python
# -*- coding: UTF-8 -*-

 #
 # Author: Jianmeng Huang 
 # <jianmenghuang<AT>gmail.com>
 #
 # File: appconsistency.py
 # Create Date: 2017-04-24 16:48:18
 #

import sys,os, logging
import argparse

def startAnalysis():
    parser = argparse.ArgumentParser(description='Analysis the consistency of the apps.')
    parser.add_argument("-A", action="store", dest="apk_loction", required=True, help="the path of the apk file")
    parser.add_argument("-T", action="store", dest="apktool", help="the path of apktool.tar")
    parser.add_argument("-O", action="store", dest="output", help="the output directory")
    args = parser.parse_args()

    if not args.apktool:
        logging.info("apktool is not sepecified, use /home/hjm/work/android/apktool/apktool.jar")
        args.apktool = "/home/hjm/work/android/apktool/apktool.jar"
        #print args.apktool
    if not args.output:
        logging.info("the output is directed to ./out")
        args.output = "."

    if not os.path.exists(args.apktool):
        logging.error("cannot find the apktool.jar")
        return
    if not os.path.exists(args.apk_loction):
        logging.error("cannot find the target apk")
        return

    #Decompile the apk file.
    os.system("java -jar " + args.apktool + " d " + args.apk_loction + " -o " + os.path.join(args.output, "out"))
    #Dynamicly test the apk and get all the screenshoots of the activities in the app.
    #for each activity find the locatioin where it is an icon in the assets. trigger the location and get runtime logs.
    ##dytest(args.apk_loction)


    return

if __name__ == "__main__":
    startAnalysis()