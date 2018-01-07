
# ToDo!: restart daily -- bonus

# ToDo!: all task types or one at a time
def do_tasks(task_type):
    click("tasks-button.png")
    # ToDo!: use switch-like instead of if?
    if task_type == "personal":
        print "personal"
    elif task_type == "clan":
        click("tasks-clan-tab-inactive.png")
        # it often takes significant amount of time to repopulate the list
        wait(3)
        r = find("tasks-tab-header.png").below(100).find("tasks-bullet.png").right(525)
        r.find("tasks-window.start-button.png").click()
        wait(1)
        # move the mouse away(the button changes) and wait to check if the task  is auto
        mouseMove(100,100)
        wait(1)
        r.find("tasks-window.claim-button.png").click()
        wait(1)
        mouseMove(100,100)
        wait(1)
        exit(0)
    elif task_type == "premium":
        print "premium"
    else:
        raise Exception('Bad Task Type')

def open_loki_chest():
    click("loki-chest-button.png")
    wait("loki-chest-window.png", 5)
    try:
        click("loki-chest-window.claim-button.png")
    except:
        if exists("loki-chest-window.close-button.png"):
            click("loki-chest-window.close-button.png")
        else:
            raise Exception("Something went wrong...")


def help_clanmates():
    # ToDo!: is the "if" need? better trow?
    if exists("help-clanmates-button.png"):
        click("help-clanmates-button.png")
        #wait("help-clanmates-window-help-all-button.png", 5)
        click("help-clanmates-window-help-all-button.png")
        click("x-button.png")


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

def read_news():
    if exists("news-button.png"):
        click(getLastMatch())
        wait("news-window-header.png", 5)
        click("news-window.read-all-button")
        # ToDo!: use observe() or whatever they call it?
        # ToDo!: move all trailing waits after the caller?
        wait(2)

def get_daily_bonus():
    if exists("daily-bonus-button.png"):
        click(getLastMatch())
    # FIX ME. or not?
    #click("daily-bonus-window.claim-button.png")
    

def main():
    #setShowActions(True)
    #Settings.MinSimilarity = 0.9 
    # ToDo!: enumeration for task_type? supported in Python 3
    #TASKS = ["personal", "clan", "premium"]
    TASKS = ["clan"]

    # ToDo!: if not running
    switchApp("Vikings: War of Clans")

    # ToDo!: check if the browser has the focus? sometimes fails when on a diff desktop
    wait(2)

    #show_mode_selection()
    # ToDo!: once daily?
    read_news()
    get_daily_bonus()
    open_loki_chest()
    help_clanmates()

    # ToDo!: temporary
    #for index in range(len(TASKS)):
    #    do_tasks(TASKS[index])

    sleep(2)

if __name__ == "__main__":
    main()