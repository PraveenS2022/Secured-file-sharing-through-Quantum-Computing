import qiskit
#pip install qiskit-ibm-runtime
from qiskit import generate_preset_pass_manager
from qiskit_ibm_runtime import QiskitRuntimeService

service = QiskitRuntimeService(token="2847b9aba1704d78391fdff3261cc4f79eca8f18ed83fbd327bdd2733dc9ac3cc5c9c1c32245d64048b5690008eee16410741db65e8e85928325093958760348",
                               channel="ibm_cloud")
#QiskitRuntimeService.save_account(channel="ibm_cloud", token="2847b9aba1704d78391fdff3261cc4f79eca8f18ed83fbd327bdd2733dc9ac3cc5c9c1c32245d64048b5690008eee16410741db65e8e85928325093958760348")

