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
import shutil
import argparse

def parseArgs():
    parser = argparse.ArgumentParser(description='Analysis the consistency of the apps.')
    parser.add_argument("-A", action="store", dest="apk_location", required=True, help="the path of the apk file")
    parser.add_argument("-O", action="store", dest="output_icon", required=True, help="the output directory of icons")
    parser.add_argument("-T", action="store", dest="apktool", help="the path of apktool.tar")
    #parser.add_argument("-h", action="store", dest="output", help="the output directory")
    args = parser.parse_args()
    return args


def decompile():
    args = parseArgs()

    if not args.apktool:
        logging.info("apktool is not sepecified, use /home/hjm/work/android/apktool/apktool.jar")
        args.apktool = "/home/hjm/work/android/apktool/apktool.jar"
        #print args.apktool
    #if not args.output:
    #    logging.info("the output is directed to ./out")
    args.output = "."

    if not os.path.exists(args.apktool):
        logging.error("cannot find the apktool.jar")
        return
    if not os.path.exists(args.apk_location):
        logging.error("cannot find the target direction")
        return

    #Decompile the apk file.
    os.system("java -jar " + args.apktool + " d " + args.apk_location + " -o " + os.path.join(args.output, "out"))
    #Dynamicly test the apk and get all the screenshoots of the activities in the app.
    #for each activity find the locatioin where it is an icon in the assets. trigger the location and get runtime logs.
    ##dytest(args.apk_loction)
    count=1
    for root, dirs, files in os.walk(args.apk_location):
        for name in files:
            if os.path.exists(os.path.join(args.output, "out")):
                shutil.rmtree(os.path.join(args.output, "out"))
            print "Extracting　"  + os.path.join(root, name)
            print count
            count=count+1
            # status = os.system(
            #     "java -jar " + args.apktool + " d " + os.path.join(args.apk_location, name) + " -o " + os.path.join(args.output, "out"))
            # print status
            os.system("unzip " + os.path.join(args.apk_location, name) + " -d out")
            os.system("./cppng.sh " + args.output_icon)

    return

def collectIcons():

    return


if __name__ == "__main__":
    decompile()
    collectIcons()
