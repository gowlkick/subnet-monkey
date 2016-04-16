""" 
    SUBNET CALCULATOR WRITTEN IN PYTHON TO
    WORK WITHIN THE FOLLOWING CONSTRAINTS:

 * Work with IPv4 only (for now)
 * Identify if input is a valid IP address
   in CIDR format
 * Output breakdown of information about 
   subnet:
     * Network address
     * Broadcast address
     * Subnet mask (in dotted quad)
     * Usable IP/host range
     * Total IPs and Usable IPs
"""

# Function to prompt for IP address
def get_address():
    address = raw_input('Enter an IPv4 address in CIDR format that'
	      'you would like subnetted (e.g., 192.168.0.1/24): ')
    ip_elements = address.split('.')
    first_octet = ip_elements[0]
    second_octet = ip_elements[1]
    third_octet = ip_elements[2]
    last_bit = ip_elements[3].split('/')
    fourth_octet = last_bit[0]
    CIDR = last_bit[1]


# Still trying to get the error checking to work on this:

    # Checking to make sure the length of the input is not outside
    # the possible range of valid IPv4 addresses.
    #while (len(address) > 18 or len(address) < 9 or 
    #	  len(address.split('.')) != 4):
#    while len(address.split('.')) != 4 or first_octet <= 0 or
#		 first_octet >= 224 or 
#		all(i < 0 for i in (second_octet, third_octet, fourth_octet)) or
#		all(i > 255 for i in (second_octet, third_octet,fourth_octet)) 
#		or CIDR < 1 or CIDR > 32):
#	print "That doesn't look quite right. Care to try again? "
#       address = raw_input('Enter an IPv4 address in CIDR format that'
#		  'you would like subnetted (e.g., 192.168.0.1/24): ')
        
    # Checking that each of the elements are numbers
    #while 

    # Checking that each element is in the correct range


    return (address, first_octet, second_octet, third_octet, 
	   fourth_octet, CIDR)

"""
Function to call after error has been identified to prompt
for corrected input
(This currently doesn't work to get a new address into the
'address' variable. Working on it.)
"""
#def try_again(address):
#    print "%s doesn't look like a valid IPv4 address in CIDR notation."
#    address = get_address()
#    return address

"""
Function to convert CIDR slash notation to dotted quad
This function isn't so brute force as a dictionary lookup,
but it does toss values into lists to be converted to 
integers and strings toward the end. It could likely be 
made less clunky.
"""
def subnet_convert(CIDR):
    mask_elements = [] #This list is a placeholder for the elements of the subnet octets
    binary = [] #This list is a placeholder for the binary bits to convert to an integer for placement later
    interesting = str() #string value of the interesting octet of the subnet mask
    subnet_mask = str() #final string value of the subnet mask

    # Convert the CIDR slash value to a value 1 - 8 (and add 255's to the mask_elements list)
    while CIDR > 8:
        CIDR -= 8
        mask_elements.append('255')

    # Turn the CIDR slash value into a binary equivalent in list form
    while len(binary) < 8 and CIDR > 0:
        binary.append('1')
	CIDR -= 1
 
    while len(binary) < 8:
        binary.append('0')

    # Convert the binary list to a string value, then convert that string to the integer value of the binary result
    for i in range(len(binary)):
	interesting  = interesting + binary[i]
	i += 1
    interesting = int(interesting, 2)

    # Append the converted integer to the mask_elements (as a string). Finish it off with 0's to make four octets.
    mask_elements.append(str(interesting))
    while len(mask_elements) < 4:
	mask_elements.append('0')

    # Convert the mask_elements list to string form and assign to subnet_mask.
    for i in range(len(mask_elements)):
	if i < 4:
	    subnet_mask = subnet_mask + mask_elements[i] + '.'
	else:
	    subnet_mask = subnet_mask + mask_elements[i]
    return subnet_mask


# Function to calculate usable IPs (including host IPs)
def calc_usable_IPs(CIDR):
    usable_IPs = str()
    if CIDR == 32:
        usable_IPs = "single host address"
    else:
	usable_IPs = str((2 ** (32-CIDR)) - 2)
    return usable_IPs


"""
Get the address to subnet
"""
address = get_address()

"""
 Break the address into octects and subnet mask
"""
#ip_elements = address.split('.')

"""
Assign the elements of this list to individual variables for checking
"""
first_octet = address[1]
second_octet = address[2]
third_octet = address[3]
#last_bit = ip_elements[3].split('/')
fourth_octet = address[4]
CIDR = address[5]

"""
Checking the octet values to ensure they are in range
"""


# Call function to convert CIDR slash notation to dotted quad subnet mask
subnet_mask = subnet_convert(CIDR)



network_address = 
broadcast_address = 
usable_IPs = calc_usable_IPs(CIDR)
usable_host_address_range = 

