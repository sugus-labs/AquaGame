# import time
# import json

# from weblabdeusto.weblabdeusto_client import WebLabDeustoClient
# from weblabdeusto.weblabdeusto_data import ExperimentId, Reservation, Command

# client = WebLabDeustoClient("http://www.weblab.deusto.es/weblab/")

# session_id = client.login("gustavo.martin", "221186")
# print client.list_experiments(session_id)

# exp_id = ExperimentId("aquarium", "Aquatic experiments")

# reservation = client.reserve_experiment(session_id, exp_id, "{}", "{}")
# print reservation.reservation_id
# print reservation.status

# reservation_id = reservation.reservation_id

# while reservation.status != Reservation.CONFIRMED:
#     print "Retrieving status"
#     reservation = client.get_reservation_status(reservation_id)
#     print reservation.status
#     time.sleep(3)

# print 
# print reservation
# print reservation.initial_configuration
# print reservation.time
# end_time = time.time() + reservation.time
# print 

# while end_time > time.time():
#     response = client.send_command(reservation_id, Command("get-status"))
#     commandstring = response.commandstring

#     print commandstring

#     blue_ball = json.loads(commandstring)['blue']

#     print "Blue ball: ", blue_ball
#     print client.get_reservation_status(reservation_id).time
#     print "But I thought that it was", end_time - time.time()

#     # client.send_command(reservation_id, Command("ball:blue:%s" % str(not blue_ball).lower()))

#     time.sleep(6)

# print "Finished"
# time.sleep(2)


# print client.get_reservation_status(reservation_id)
