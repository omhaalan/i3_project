#i3 1234 command nr: 1
i3-msg 'exec worskspace 11:Workflatpak run com.toggl.TogglDesktop'
i3-msg 'exec worskspace 11:Workgoogle-chrome-stable --args --new-window https://todoist.com/app/filter/2318047973'
i3-msg 'exec worskspace 11:Workgoogle-chrome-stable --args --new-window https://freedom.to/dashboard'
sleep 0.9 
 
#i3 1234 command nr: 2
i3-msg 'exec worskspace 10:End_of_daygoogle-chrome-stable --args --new-window https://track.toggl.com/reports/summary/4998663'
i3-msg 'exec worskspace 10:End_of_daygoogle-chrome-stable --args --new-window https://todoist.com/app/filter/23182994947'
sleep 0.9 
 
#i3 1234 command nr: 3
i3-msg '\workspace 4'
sleep 0.9 
 
