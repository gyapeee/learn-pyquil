from pyquil import Program, get_qc
from pyquil.gates import *
from pyquil.quilbase import Declare

program = Program(
    Declare("ro", "BIT" ,2),
    H(0), # Hadamart gate, put the qbit into superposition 
    CNOT(0,1), # Controlled-NOT entangle qbits
    MEASURE(0, ("ro", 0)),
    MEASURE(1, ("ro", 1)),
).wrap_in_numshots_loop(10)

qc = get_qc("9q-square-qvm")
result = qc.run(qc.compile(program)).get_register_map().get("ro")
print(result)