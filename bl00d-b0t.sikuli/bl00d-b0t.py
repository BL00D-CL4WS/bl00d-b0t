
# ToDo!: restart daily -- bonus

def do_task():
    r = find("tasks-tab-header.png").below(100).find("tasks-bullet.png").right(525)
    while True:
        if r.exists("tasks-window.claim-button.png"):
            click("tasks-window.claim-button.png")
        r.find("tasks-window.start-button.png").click()
        wait(1)
        # move the mouse away(the button changes) and wait to check if the task  is auto
        mouseMove(100,100)
        wait(1)
        try:
            r.find("tasks-window.claim-button.png").click()
        except:
            if r.exists("boost.png"):
                while True:
                    if r.exists("tasks-window.claim-button.png"):
                        r.click("tasks-window.claim-button.png")
                    wait(5)
                raise Exception("Something went wrong...")
        mouseMove(100,100)
        wait(1)
        if exists("tasks-tab-done.png"):
            break

# ToDo!: all task types or one at a time
def do_tasks():
    #TASKS = ["personal", "clan", "premium"]
    #for index in range(len(TASKS)):
        # ToDo!: use switch-like instead of if?
        #if TASKS[index] == "personal":
            click("tasks-button.png")
            wait(1)
            if not exists("tasks-tab-done.png"):
                do_task()
            else:
                click("tasks-clan-tab-inactive.png")
                wait(2)
        #elif TASKS[index] == "clan":
            if not exists("tasks-tab-done.png"):
                do_task()
            else:
                click("tasks-premium-tab-inactive.png")
                wait(2)
        #elif task_type == "premium":
            if not exists("tasks-tab-done.png"):
                do_task()

def open_loki_chest():
    click("loki-chest-button.png")
    wait("loki-chest-window.png", 3)
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
        wait(1)
        wait("help-clanmates-window-help-all-button.png", 2)
        click("help-clanmates-window-help-all-button.png")
        click("x-button.png")

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
        wait("news-window-header.png", 2)
        click("news-window.read-all-button")
        # ToDo!: use observe() or whatever they call it?
        # ToDo!: move all trailing waits after the caller?
        # wait(2)

def get_daily_bonus():
    if exists("daily-bonus-button.png"):
        click(getLastMatch())
        # FIX ME. or not?
        wait("daily-bonus-window.claim-button.png", 2).click()

def main():
    #setShowActions(True)
    #Settings.MinSimilarity = 0.9 
    # ToDo!: if not running
    switchApp("Vikings: War of Clans")
    # ToDo!: check if the browser has the focus? sometimes fails when on a diff desktop
    wait(1)
    #show_mode_selection()
    while True:
        #read_news()
        #get_daily_bonus()
        open_loki_chest()
        help_clanmates()
        do_tasks()
        sleep(2)

if __name__ == "__main__":
    main()