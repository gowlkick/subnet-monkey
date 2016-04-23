# Subsection of subnet calculator to work out derivation
# of newtwork and broadcast addresses from CIDR input.

def network_range(first_octet, second_octet, third_octet, fourth_octet, interesting_octet, CIDR):
	# Source list containing list elements of IP range
	# that will be used to generate network and broadcast
	# addresses.
	octet_list = [first_octet, second_octet, third_octet, fourth_octet]

	# Base of the IP range list that will serve as the template
	# for the common portions of the beginnings (prefix portion)
	# of the network and broadcast addresses.
	base_list = []

	# Generate the common octets of each address.
	while CIDR > 8:
		CIDR -= 8
		base_list.append(octet_list[0])
		octet_list.remove(octet_list[0])

	# Generate the prefix for the network range.
	beginning_range = octet_list[0]
	network_address_list = base_list[:]
	network_address_list.append(beginning_range)

	# Run the network_address list through fill_0 to make it 4 elements
	# long. 
	network_address_list = fill_0(network_address_list)

	# Convert to a dotted quad string.
	network_address = list_to_string(network_address_list)

	# Generate the host range for the interesting octet	
	interesting_range = 255 - interesting_octet	

	# Generate the broadcast address from the host range.
	ending_range = str(int(octet_list[0]) + interesting_range)
	broadcast_address_list = base_list[:]
	broadcast_address_list.append(ending_range)
	broadcast_address_list = fill_255(broadcast_address_list)

	# Convert to a dotted quad string.
	broadcast_address = list_to_string(broadcast_address_list)

	return network_address, broadcast_address




# Function to fill out a 4-element list with 0's.
def fill_0(address):
	while len(address) < 4:
		address.append('0')
	return address

# Function to fill out a 4-element list with 255's.
def fill_255(address):
	while len(address) < 4:
		address.append('255')
	return address

# Function to convert a 4-element list to a dotted quad string.
def list_to_string(address_list):
	address_output = str()
	for i in range(len(address_list)):
	    if i < 3:
           address_output = address_output + address_list[i] + '.'
        else:
           address_output = address_output + address_list[i]
	return address_output

