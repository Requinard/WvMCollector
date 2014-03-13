import sys
import os
import sqlite3
from yapsy.PluginManager import PluginManager

__author__ = 'David'

if __name__ == "__main__":
    pmanager = PluginManager()
    pmanager.setPluginPlaces(["modules"])

    pmanager.collectPlugins()

    conn = sqlite3.connect("../HouseServer/db.sqlite3")
    print conn

    conn.close()