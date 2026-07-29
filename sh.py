import subprocess
import time
import webbrowser
import os
import playsound3
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

#This function will handle the execution of commands and handle piping
def execute_command(command):
    try:
        if "|" in command:
            #save it for restoration later
            s_in, s_out = (0, 0)
            s_in = os.dup(0)
            s_out = os.dup(1)

            #take commandut from stdin (first command)
            fdin = os.dup(s_in)

            #iterate over all piped commands
            for cmd in command.split("|"):
                #fdin will be stdin if it's the first iteration, and the readable at end of pipe if not
                os.dup2(fdin, 0)
                os.close(fdin)

                #restore stdout if its last cmd
                if cmd == command.split("|")[-1]:
                    fdout = os.dup(s_out)
                else:
                    fdin, fdout = os.pipe()

                #redirect stdout to pipe
                os.dup2(fdout, 1)
                os.close(fdout)

                try:
                    subprocess.run(cmd.strip().split())
                except Exception:
                    print("jshell: command not found: {}".format(cmd.strip()))

            #restore stdout and stdin
            os.dup2(s_in, 0)
            os.dup2(s_out, 1)
            os.close(s_in)
            os.close(s_out)
        else:
            subprocess.run(command.split(" "))

    except Exception:
        print("jshell: command not found: {}".format(command))


#function to convert absolute path and change directories
def jshell_cd(path):
    try:
        os.chdir(os.path.abspath(path)) #changing the directory and converting the path to absolute path, then putting it through os chdir.
    except Exception:
        pass

def jshell_clear():
    playsound3.playsound(os.path.join(SCRIPT_DIR, "timeout.mp3"), block=False)
    print("IM TIMING YOUR ASS OUT")
    time.sleep(3.2)
    print("FOR A FUCKING MONTH")
    time.sleep(0.8)
    command = 'cls' if os.name == 'nt' else 'clear'
    subprocess.run(command, shell=True)


def jshell_help():
    print("""
            A simple shell written in python 3.14
                Commands:
                help - Opens the help menu
                joebart - opens joe bart's socials in your system's default browser. useless feature, but cool none the less.
                clear - clears the current screen
                exit - exits the shell
            """)


def main():
    print("Type 'exit' to exit, or 'help' for a list of commands.")

    while True:
        command = input("$ ").strip().lower()
        if command == "exit":
            break
        elif command[:3] == "cd ":
            jshell_cd(command[3:])
        elif command in ["clear", "cls"]:
            jshell_clear()
        elif command == "help" or command == "?":
            jshell_help()
        elif command == "joebart":
            socialinks = [
                "https://www.twitch.tv/joe_bartolozzi",
                "https://www.youtube.com/@JoeBartolozzi",
                "https://www.instagram.com/joe.bartolozzi/?hl=en"
            ]
            for link in socialinks:
                webbrowser.open_new_tab(link)
                time.sleep(.2)
        else:
            execute_command(command)


#Run the shell
if __name__ == "__main__":
    main()