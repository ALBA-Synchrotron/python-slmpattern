from microscope.clients import Client

slm_url = "PYRO:HDMIslm@127.0.0.1:8001"

slm = Client(slm_url)

seq = [(0, 0, 450), (60, 0, 450)]

slm.set_sim_sequence(seq)
pos = slm.getCurrentPosition()
print("Position {}".format(pos))
slm.cycleToPosition(1)
pos = slm.getCurrentPosition()
print("Position {}".format(pos))
angle = slm.get_sim_diffraction_angle
print("Angle {}".format(pos))
slm.set_sim_diffraction_angle(60)
angle = slm.get_sim_diffraction_angle
print("Angle {}".format(pos))
