#!/bin/bash

 #
 # Author: Jianmeng Huang 
 # <jianmenghuang<AT>gmail.com>
 #
 # File: cppng.sh
 # Create Date: 2017-05-18 22:25:16
 #

#set -x
#set -e


#rm the redundant icons
cd ../$1
rm -f =abc_ic_ab_back_mtrl_am_alpha.png* \
abc_ic_ab_back_mtrl_am_alpha.png* \
abc_ic_menu_copy_mtrl_am_alpha.png* \
abc_ic_menu_cut_mtrl_alpha.png* \
abc_spinner_mtrl_am_alpha.9.png* 

rm -f common_signin_btn_icon_disabled_dark.9.png* \
common_signin_btn_icon_disabled_focus_dark.9.png* \
common_signin_btn_icon_disabled_focus_light.9.png* \
common_signin_btn_icon_disabled_light.9.png* \
common_signin_btn_icon_focus_dark.9.png*

rm -f common_signin_btn_icon_focus_light.9.png* \
common_signin_btn_icon_normal_dark.9.png* \
common_signin_btn_icon_normal_light.9.png* \
common_signin_btn_icon_pressed_dark.9.png* \
common_signin_btn_icon_pressed_light.9.png* 

rm -f common_signin_btn_text_disabled_dark.9.png* \
common_signin_btn_text_disabled_focus_dark.9.png* \
common_signin_btn_text_disabled_focus_light.9.png* \
common_signin_btn_text_disabled_light.9.png* 

rm -f common_signin_btn_text_focus_dark.9.png* \
common_signin_btn_text_focus_light.9.png* \
common_signin_btn_text_normal_dark.9.png* \
common_signin_btn_text_normal_light.9.png* \
common_signin_btn_text_pressed_dark.9.png* \
common_signin_btn_text_pressed_light.9.png* 

rm -f ic_launcher.png* \
icon.png* \
ic_plusone_medium_off_client.png* \
ic_plusone_small_off_client.png* \
ic_plusone_standard_off_client.png* 

rm -f ic_plusone_tall_off_client.png* \
powered_by_google_dark.png* \
powered_by_google_light.png* 





cd ../appconsistency/out
#cp `find . -name *.png` ../../$1
images=`find . -name *.png`
if [ -n "$images" ]; then 
    cp --backup=numbered $images  ../../$1
else
    echo "apktool fails"
fi


