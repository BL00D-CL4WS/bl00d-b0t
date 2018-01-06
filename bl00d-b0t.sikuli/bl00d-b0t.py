
# ToDo!: all task types or one at a time
def do_tasks(task_type):
    find("tasks-button.png").click()
    # ToDo!: use switch-like instead of if?
    if task_type == "personal":
        print "personal"
    elif task_type == "clan":
        "tasks-clan-tab-inactive.png"
        find("tasks-clan-tab-inactive.png").click()
    elif task_type == "premium":
        print "premium"
    else:
        raise Exception('Bad Task Type')

def open_loki_chest():
    find("loki-chest-button.png").click()
    wait("loki-chest-window.png", 5)
    try:
        find("loki-chest-window.claim-button.png").click()
    except:


def help_clanmates():
    if exists("help-clanmates-button.png"):
        click("help-clanmates-button.png")
        wait("help-clanmates-window-help-all-button.png", 5)
        find("help-clanmates-window-help-all-button.png").click()

def loop_all():
    while True:
        #open_loki_chest()
        # ToDo!: all task types or one at a time
        for index in range(len(TASKS)):
            do_tasks(TASKS[index])
    
        sleep(10)
        break

def show_mode_selection():
    items = ("loop all", "farm")
    selected = select("Please select mode", "put some title here", options = items)
    if selected == None:
        exit(0)
    elif selected == items[0]:
        loop_all()
    elif selected == items[1]:
        show_farming_options()

def show_farming_options():
    popup("Not Implemented!", "put some title here")


Settings.MinSimilarity = 0.95
# ToDo!: enumeration for task_type? supported in Python 3
#TASKS = ["personal", "clan", "premium"]
TASKS = ["clan"]

switchApp("Mozilla Firefox")

#show_mode_selection()
open_loki_chest()
help_clanmates()
sleep(2)
