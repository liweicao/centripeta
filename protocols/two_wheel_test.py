"""
Testing for the control of pH_probe sequential movement

"""
from centripeta import Analyzer, Dispenser
from centripeta.utils import Logger
from pycont.controller import MultiPumpController
from commanduino import CommandManager
import pandas as pd
import logging

# Set up logger
logging.basicConfig(filename='log.txt', level=logging.INFO)
logger = logging.getLogger(__name__)

#Instantiate the command manager
mgr = CommandManager.from_configfile('platform_config_ports.json')
pumps = MultiPumpController.from_configfile('pycont_config.json')
a = Analyzer(mgr)
d = Dispenser(manager=mgr, pump_controller=pumps)

a.turn_wheel(n_turns=3)
a.horz_cond.move(10000)
a.horz_cond.home()
a.vert_cond.move(10000)
a.vert_cond.home()


# Instantiate the robotic controls 


#Read in conditions and run the robot
conditions = pd.read_csv('conditions/acetone_water_1.csv')
for i, condition in conditions.iterrows():
    logging.info("{Dipsensing condition %s"%i)
    d.dispense(pump_name="sample", volume =condition['sample']) 
    d.dispense(pump_name="acetone", volume=condition['acetone'])
    d.dispense(pump_name="water", volume=condition['water'])
    d.turn_wheel(n_turns=1)