from azure.servicebus import ServiceBusService

from azure.servicebus import Message



def createSBS():

	service_namespace = 'RaspberryPiNSTest'

	key_name = 'RootManageSharedAccessKey' # SharedAccessKeyName

	key_value = 'yEcs0927kFYs1U8J7x4VCwZAaf3ck38hqSGY9YjiMAo=' # SharedAccessKey



	sbs = ServiceBusService(service_namespace,

		shared_access_key_name=key_name,

		shared_access_key_value=key_value)

	return sbs



def getId():

	iD = "0000000000000000"

	try:

		f = open('/proc/cpuinfo','r')

		for line in f:

			if line[0:6]=='Serial':

				iD = line[10:26]

		f.close()

	except:

		iD = "ERROR00000000000"

		f.close()

	return iD