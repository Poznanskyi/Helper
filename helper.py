import bot
import sort
import notes
from pathlib import Path

if __name__ == "__main__":
    while True:
        work_with = input(
            "With what part of helper you want to work? (contacts / notes / files) ")
        if work_with.lower() == "contacts":
            if bot.CONTACT_SERIALIZATION_PATH.exists():
                bot.ADDRESS_BOOK.deserialize(bot.CONTACT_FILE_NAME)
            bot.main()
            bot.ADDRESS_BOOK.serialize()
        elif work_with.lower() == "notes":
            if notes.NOTEBOOK_SERIALIZATION_PATH.exists():
                notes.NOTES_BOOK.deserialize(notes.NOTEBOOK_FILE_NAME)
            notes.main()
            notes.NOTES_BOOK.serialize()
        elif work_with.lower() == "files":
            sort.clean()
            sort.DIR_PATH = ""
        elif work_with.lower() in ["cancel", "close", "exit", "good bye"]:
            print("Bye")
            break
        else:
            print("Wrong command")

