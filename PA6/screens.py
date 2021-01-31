COMMANDS = {
    1: ("B", "Back"),
    2: ("A", "Add"),
    3: ("S", "Search"),
    4: ("P", "Prev"),
    5: ("N", "Next"),
    6: ("E", "Edit"),
    7: ("R", "Remove")
}

SCREENS = {
    0: {
        "type": 2
    },
    1: {
        "type": 0,
        "name": "Main menu",
        "message": "Guesses: ",
        "menu": [
            [0, "Play game"],
            [2, "Settings"]
            ],
        "commands": [
        ]
        },
    2: {
        "type": 0,
        "name": "Settings",
        "message": "",
        "menu": [
            [3, "Word list"],
            [6, "User list"],
            [7, "High-score list"],
            [4, "Change number of guesses"]
        ],
        "commands": [
            COMMANDS[1]
        ]
    },
    3: {
        "type": 1,
        "name": "word",
        "list": "self.words",
        "target": 5,
        "commands": [
            COMMANDS[2],
            COMMANDS[3],
            COMMANDS[4],
            COMMANDS[5],
            COMMANDS[1]
        ],
        "file_name": "words.txt"
    },
    4: {
        "type": 0,
        "name": "Input total guesses",
        "message": "",
        "menu": [
        ],
        "commands": [
            COMMANDS[1]
        ],
        "update_int": "self.total_guesses"
    },
    5: {
        "type": 0,
        "name": "select",
        "message": "",
        "menu": [
        ],
        "commands": [
            COMMANDS[6],
            COMMANDS[7],
            COMMANDS[1]
        ]
    },
    6: {
        "type": 1,
        "name": "user",
        "list": "self.users",
        "target": 5,
        "commands": [
            COMMANDS[2],
            COMMANDS[3],
            COMMANDS[4],
            COMMANDS[5],
            COMMANDS[1]
        ],
        "file_name": "users.txt"
    },
    7: {
        "type": 1,
        "name": "high-score",
        "list": "self.high_scores",
        "target": 8,
        "commands": [
            COMMANDS[1]
        ],
        "file_name": None
    },
    8: {
        "type": 0,
        "name": "select",
        "message": "",
        "menu": [
        ],
        "commands": [
            COMMANDS[1]
        ]
    }
}

