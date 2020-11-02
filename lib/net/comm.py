import sys
import os
import uuid
from . import fire
from ..data_v.table import User, Game

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

def G_SetID():
    id = uuid.uuid1()
    User["id"] = id

def gui_SetPseudo(pseudo):
    fire.inject_pseudo(Game["cube"], Game["ply"], pseudo)
