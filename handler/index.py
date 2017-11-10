import handlers

def handle_input(user_input, officers_in_lab):
    handler_map = {
        "whois": handlers.handleWhoIs(officers_in_lab)
    }

    if user_input not in handler_map:
        return handlers.handleUnknownInput(handler_map)
    else:
        return handler_map[user_input]
