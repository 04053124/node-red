[
    {
        "id": "1e75856a.53026b",
        "type": "tab",
        "label": "Flow 1"
    },
    {
        "id": "bf829850.1ba998",
        "type": "rpi-gpio in",
        "z": "1e75856a.53026b",
        "name": "Button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 108,
        "y": 74,
        "wires": [
            [
                "413d2021.4be46",
                "9aa53b8c.7a4d18"
            ]
        ]
    },
    {
        "id": "413d2021.4be46",
        "type": "debug",
        "z": "1e75856a.53026b",
        "name": "",
        "active": true,
        "console": "false",
        "complete": "false",
        "x": 442,
        "y": 74,
        "wires": []
    },
    {
        "id": "e65a70a1.69a72",
        "type": "rpi-gpio out",
        "z": "1e75856a.53026b",
        "name": "LED",
        "pin": "11",
        "set": true,
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 770,
        "y": 200,
        "wires": []
    },
    {
        "id": "9aa53b8c.7a4d18",
        "type": "switch",
        "z": "1e75856a.53026b",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "outputs": 2,
        "x": 350,
        "y": 180,
        "wires": [
            [
                "19924a50.e32466"
            ],
            [
                "d59ff27.50a161"
            ]
        ]
    },
    {
        "id": "19924a50.e32466",
        "type": "change",
        "z": "1e75856a.53026b",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 550,
        "y": 180,
        "wires": [
            [
                "e65a70a1.69a72"
            ]
        ]
    },
    {
        "id": "d59ff27.50a161",
        "type": "change",
        "z": "1e75856a.53026b",
        "name": "change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 550,
        "y": 240,
        "wires": [
            [
                "e65a70a1.69a72"
            ]
        ]
    }
]
