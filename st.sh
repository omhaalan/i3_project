#!/bin/bash

# setting up new mode for my DP23
xrandr --newmode "3440x1440" 148.5 1920 2008 2052 2200 1080 1089 1095 1125 +hsync +vsync
xrandr --addmode DP-2-3 3440x1440

# default monitor is eDP-1
MONITOR=eDP-1

# functions to switch from eDP-1 to DP23 and vice versa
function ActivateDP23 {
    echo "Switching to DP-2-3"
    xrandr --output DP-2-3 --mode 3440x1440 --output eDP-1 --off
    MONITOR=DP-2
}
function DeactivateDP23 {
    echo "Switching to eDP-1"
    xrandr --output DP-2-3 --off --output eDP-1 --auto
    MONITOR=eDP-1
}

# functions to check if DP23 is connected and in use
function DP23Active {
    [ $MONITOR = "DP-2" ]
}
function DP23Connected {
    ! xrandr | grep "^DP-2" | grep disconnected
}

# actual script
#while true
#do
#    if ! DP23Active && DP23Connected
#    then
#        ActivateDP23
#    fi
#
#    if DP23Active && ! DP23Connected
#    then
#        DeactivateDP23
#    fi
#
#    sleep 1s
#done


if ! DP23Active && DP23Connected
then
    ActivateDP23
fi
                                 
if DP23Active && ! DP23Connected
then
    DeactivateDP23
fi


#I3 start up dashboards



#Start freedom session
i3-msg 'workspace 9: Freedom of the day; exec "google-chrome-stable --args --new-window https://freedom.to/dashboard"'
i3-msg 'exec "google-chrome-stable --args --new-window gmail.com messenger.com hotmail.com"' 

sleep .8

#Work dashboard
i3-msg 'workspace 1:Work; exec "flatpak run com.toggl.TogglDesktop"'
i3-msg 'exec "google-chrome-stable --args --new-window https://todoist.com/app/filter/2318053198"'
i3-msg 'exec "google-chrome-stable --args --new-window https://freedom.to/dashboard"'

sleep 1 

#End the day; clean up todos
i3-msg 'workspace 0:End the day; exec "google-chrome-stable --args --new-window https://todoist.com/app/filter/_1627049328485'

sleep .8


#Planning the day
i3-msg 'workspace 10:Start the day; exec "google-chrome-stable --args --new-window  https://todoist.com/app/filter/2318047362"'
i3-msg 'exec "google-chrome-stable --args --new-window https://calendar.google.com/calendar/u/0/r"' 
sleep .3


setxkbmap -layout us_personal -variant colemak


