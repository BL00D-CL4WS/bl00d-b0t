settings >> all off

# Usage

-- install
    - java
    - 
-- game opened in a browser, tab active

-----------------------------------

# single action and max 1 (sec)
#Settings.ClickDelay
#Settings.TypeDelay

# Note: Additionally you might use selectRegion() to interactively create a new region at runtime.

# To avoid the second search with the click() you can use:
#wait(someVisual)
#click(getLastMatch())
## or
#if exists(someOtherVisual):
#        click(getLastMatch())
#There are convenience shortcuts for this:
#wait(someVisual)
#click()
## or
#if exists(someOtherVisual):
#        click()