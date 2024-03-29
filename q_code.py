from pyquil import Program
from pyquil.gates import *
from pyquil import get_qc

p = Program()
ro = p.declare("ro-memory", "BIT", 1)
p += X(0)
p += MEASURE(0, ro[0])

print(p)

qc = get_qc('1q-qvm')
executable = qc.compile(p)
result = qc.run(executable)
bit_strings = result.get_register_map().get("ro-memory")

print(bit_strings)