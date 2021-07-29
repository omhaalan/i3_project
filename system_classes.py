import pickle
import datetime as dt
import numpy as np

class command_scheduler:
    def __init__(self, procedures_file, commands_file):
        #Attempt to load existing commands
        self.cds_memory_file = "python_data/command_scheduler"
        try:
            self.commands = self.load_commands()
            print("hello")
        except:
            #Run scripts to intialize the standard commands 
            exec(open(procedures_file).read())
            exec(open(commands_file).read())
            self.commands = commands

        pause = 1

    def update_and_execute(self):
        executables = []
        command_mask = np.zeros(len(self.commands))
        #Loop through commands and determine if they should be executed
        for (i, command) in enumerate(self.commands):
            if command.decision():
                command_mask[i] = 1
                executables.append(command.strings)
        #Save the updated classes to memory
        self.save_classes()

        workspace_string = self.workspace_string(command_mask)
        #Put the new string in a list and append
        executables.append([workspace_string])
        return executables


    ## Functions for loading and storing
    def load_commands(self):
        # Load commands from prior update
        with open(self.cds_memory_file, 'rb') as file:
            commands = commands_dict = pickle.load(file)
        return commands

    def save_classes(self):
    # Save commands after update
        with open(self.cds_memory_file, 'wb') as file:
            pickle.dump(self.commands, file)

    ## Functions for debugging
    def debug_function(self):
        #Usefull studying values during the execution
        self.names = [com.workspace_name for com in self.commands]
        self.timings = [com.timing_manager for com in self.commands]
        self.periods = [ti.period_length for ti in self.timings]
        self.boots = [ti.last_boot for ti in self.timings]
        self.num_boots = [ti.num_boots_today for ti in self.timings]
        print(self.names)
        print(self.num_boots)

    ## Create workspace string
    def workspace_string(self, mask):
        #Find workspace to focus on
        ws_focus = self.choose_workspace_focus(mask)
        #assmbeling i3-msg
        i3_string = "i3-msg '\workspace " + ws_focus.__str__() + "'"
        return i3_string

    ## Function for handeling workspaces
    def choose_workspace_focus(self, mask):
        #Determine witch workspace to focus on (in case of conflict)
        #TODO: The algorithm assumes that no workspaces have number conflicts

        #Load workspace data into lists
        workspaces_numbers = [com.ws_num for com in self.commands]
        workspaces_focus = [com.ws_focus for com in self.commands]
        #Make numpy arrays
        wss_num = np.array(workspaces_numbers, dtype=int)
        wss_focus = np.array(workspaces_focus, dtype=int)
        #Mask out values 
        masked =  wss_num*wss_focus*mask
        #Find focus cadidate with the highest score
        if np.any(masked):
            ws_focus = masked.argmax()
        else:
            ws_focus = wss_num.argmax()

        return ws_focus

class command_class:
    # This is a skeleton class for different command_class
    def __init__(self, command_procedures, workspace_name, workspace_number, period_length, timing_string, start=dt.date.today(), ws_focus=False):

        self.command_procedures = command_procedures
        self.workspace_name = workspace_name

        self.ws_num = workspace_number
        #Set workspaec focus: Default is False
        self.ws_focus = ws_focus

        #Store timing decisions in timing class
        self.timing_manager = timing_manager(period_length, timing_string, start)

        self.strings = self.i3_string_assembly()

    def decision(self):
        #Decide if the command execute
        #This will be more complex if todoist is integrated properly
        return self.timing_manager.should_execute()

    def i3_string_assembly(self):
        #Assemble i3 executable strings
        i3 = "i3-msg 1324 '"
        ws = "worskspace " + self.ws_num.__str__() + ":" + self.workspace_name
        return [i3 + ws + procedure + "'" for procedure in self.command_procedures]

class timing_manager:
    #Not neccesary now but will be nice in the future
    #TODO This only works if the system just booted
    def __init__(self, period_length, timing_string, start): #, num_executions):
        self.time_dict = {
            "first": 1,
            "every": 2
        }

        #num_executions = is_string or datetime...    int or 'always' string 
        self.period_length = period_length
        self.timing = self.time_dict[timing_string]

        #Store timing data: A bit hacky -> last boot will be set to the past 
        self.last_boot = dt.date(start.year, start.month, start.day - period_length);
        self.num_boots_today = 0;

    def should_execute(self):

        #Set default value
        execute = False

        #Execute that should launch at every boot
        if self.timing == self.time_dict["every"]:
            execute = True

        #Evaluate apps that should only launch at the first boot of the day
        #Determine if if the command should launch of this day
        current_day = dt.date.today()
        boot_delta = current_day - self.last_boot
        if boot_delta.days >= self.period_length:
            #Evalute if the command has already been launched
            if (self.timing == self.time_dict["first"]) & self.num_boots_today == 0:
                execute = True

        #Save execution values 
        if execute:
            self.last_boot = current_day
            self.num_boots_today = self.num_boots_today + 1

        return execute


#TODO: Adding new commands
def new_command():
    print("Choose between the following procedures:")
    #Require input
    print("Choose between the following procedures:")
    #Require input
    #ETC


#Fix
#commands_file = 'python_data/commands'





