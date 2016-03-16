## TODO a model for a request for pickup and delivery of a person or
## package

import routes
import sim_util

class Pickup:
	def __init__(self, uid, time, start, dest, is_human):
		self.uid = uid

		## convert to seconds after midnight
		self.time_ordered = sim_util.seconds_since_midnight(time)

		self.start_loc = start
		self.dest_loc = dest
		self.is_human = is_human
		self.routefind()
		## TODO: differing fare priority
		## TODO: arrival time for packages

	def approx_dur(self):
		## based on 10 mph, gives as-bird-flies in seconds
		return sim_util.ll_dist_m(self.start_loc, self.dest_loc) / 4.47 
		
	def routefind(self):
		route = routes.finder.get_dirs(self.start_loc, self.dest_loc)[0]
		dur = 0
		for l in route["legs"]:
			dur += l["duration"]["value"]
		self.duration = dur
		self.route = route

	def getTimeOrdered(self):
		return self.time_ordered

	def getPickupLoc(self):
		return self.start_loc

	def getDuration(self):
		return self.duration

	def getType(self):
		if self.is_human:
			return "PASSENGER"
		else:
			return "PARCEL"

	def getRoute(self):
		return self.route

	def getDest(self):
		return self.dest_loc

	def getID(self):
		return self.uid
