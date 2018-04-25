#!/bin/bash
for((i=0;i<=1000;i++))
    do
        pack=$(sed -i '1s/^7Z/7z/g' CTFMisc/7z/*)
        echo $pack
        ps=$(cat CTFMisc/ps/*.txt)
        echo $ps
        unpackit=$(7za x CTFMisc/7z/* -oCTFMisc/temp -p)
        echo $unpackit
        rm CTFMisc/ps/*
        mv CTFMisc/temp/*.txt CTFMisc/ps/
        rm CTFMisc/7z/*
        mv CTFMisc/temp/* CTFMisc/7z/
    done