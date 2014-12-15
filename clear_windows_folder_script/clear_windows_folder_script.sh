#!/bin/bash
for username in /media/* ; do
    for partition in $username/* ; do
        if [ -d "$partition" ]; then
            if [ -d "$partition/\$RECYCLE.BIN" ]; then
                rm -rf "$partition/\$RECYCLE.BIN"
            fi
            if [ -d "$partition/System Volume Information" ]; then
                rm -rf "$partition/System Volume Information"
            fi
            if [ -d "$partition/.Trash-1000" ]; then
                rm -rf "$partition/.Trash-1000"
            fi
        fi
    done
done
