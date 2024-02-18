from pyquil.quil import Program
from pyquil.api import QVMConnection
from pyquil.gates import H
from functools import reduce


qvm = QVMConnection()

dice = Program(H(0), H(1), H(2))

rolle_dice = dice.measure_all()