import subprocess
import time
import webbrowser

def main():
    print("Type 'exit' to exit, or 'help' for a list of commands.")

    while True:
        command = input("$ ").strip().lower()
        if command == "exit":
            break
        elif command == "help" or command == "?":
            print("""
            A simple shell written in python 3.14
                Commands:
                help - Opens the help menu
                joebart - opens joe bart's socials in your system's default browser. useless feature, but cool none the less.
                exit - exits the shell
            """)
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
            execute_commands(command)

#function to execute commands
def execute_commands(command):
    try:
        subprocess.run(command.split())
    except Exception:
        print("jshell: command not found: {}".format(command))












#Run the shell

if __name__ == "__main__":
    main()
