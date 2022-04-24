#!/usr/bin/bash

APP=$1
CURRENT_WINDOW=$(xdotool getactivewindow)
WINDOW_TO_TOGGLE=$(xdotool search --onlyvisible --class $APP)

# If the current window is our window to toggle - minimize it
if [[ "$CURRENT_WINDOW" == "$WINDOW_TO_TOGGLE" ]];then
  xdotool windowminimize $CURRENT_WINDOW
  exit 0
fi

# If window to toggle is active - activate it
SEARCH_TERM="[${APP:0:1}]${APP:1:${#APP}}"
if ps aux | grep "$SEARCH_TERM" | grep -v toggle
  then xdotool windowactivate $WINDOW_TO_TOGGLE
  else $APP&
fi   