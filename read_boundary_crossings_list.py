import numpy
import csv
import datetime
from astropy import units as u

@numpy.vectorize
def ymdhm_to_datetime(ymd,hours_minutes):
    ### Function to change a (doy (in yyyyddd format), hours, minutes, second) to a datetime object datetime.datetime(YYYY, mm, dd, HH, MM, SS)
    return datetime.datetime.strptime(ymd+'T'+hours_minutes,'%Y/%m/%dT%H:%M')


def read_boundary_crossings_list(file):

	with open(file,'r') as f:
		reader=csv.reader(f,delimiter=";")
		header=next(reader)
		data=numpy.array(list(reader))

	indice = numpy.array(data[:,0],dtype="str")
	doy = numpy.array(data[:,1],dtype="str")
	ymd= data[:,2]
	hours_minutes = data[:,3]
	date = ymdhm_to_datetime(ymd,hours_minutes)
	boundary = data[:,4]
	direction_crossing = data[:,5]
	notes = data[:,6]
	xyz_jss = numpy.array((data[:,7], data[:,8], data[:,9]), dtype="float")
	xyz_iau = numpy.array((data[:,10], data[:,11], data[:,12]), dtype="float")
	rtp_iau = numpy.array((data[:,13], data[:,14], data[:,15]), dtype="float")
	pdyn = numpy.array(data[:,16],dtype="float")
	standoff_dist_mp = numpy.array(data[:,17],dtype="float")
	standoff_dist_bs = numpy.array(data[:,18],dtype="float")


	return(header, indice, date, boundary, direction_crossing, notes, xyz_jss, xyz_iau, rtp_iau, pdyn, standoff_dist_mp, standoff_dist_bs)