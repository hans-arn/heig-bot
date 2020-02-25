#!/usr/bin/python3
"""
    Copyright 2019 Gabriel Roch

    This file is part of heig-bot.

    heig-bot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    heig-bot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with heig-bot. If not, see <https://www.gnu.org/licenses/>.
"""
import telegram.ext
import sys
import subprocess
import json
import os
from heig.init import config
from heig.user import User


for i in os.scandir(config["database_directory"]):
    id = i.name[:-7]
    user = User(id)
    user.gaps().check_gaps_notes(id, auto=True)

#for id in config["logs_userid"]:
    #updater.bot.send_message(chat_id=id, text="Bonjour")

