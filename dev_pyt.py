import system_classes
import os
import rw_data as data

os.remove(python_data/command_scheduler)

prc_file = "python_data/procedures.py"
com_file = "python_data/commands.py"

scheduler = system_classes.command_scheduler(prc_file, com_file)

executables_list = scheduler.update_and_execute()

file = open("bash_commands.sh", "w")
for (i, executables) in enumerate(executables_list):
    comment = "#i3 command nr: " + (i+1).__str__()
    file.write(comment + "\n")
    for executable in executables:
        file.write(executable + "\n")

    file.write("sleep 0.9 \n \n")

file.close()
#a = 'i3-msg \'exec "google-chrome-stable --new-window https://wikipedia.com"\''
#file.write(a + "\n")






























