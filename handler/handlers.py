def handleWhoIs(officers_in_lab):
    if len(officers_in_lab) == 0:
        message = "There doesn't seem to be any officers in the lab right now."
    else:
        message = "Here is the list of officers in the lab:\n" + "\n".join(officers_in_lab)

    return message

def handleUnknownInput(knownCommands):
    message = "Here are the commands that I support:\n"
    for key in knownCommands:
        message += key + '\n'

    return message
