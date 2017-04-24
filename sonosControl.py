import requests
import os

IP = '192.168.0.5'

def setIp(ip):
	IP = ip


def play():
#Sends a Play command to the Sonos
	ACTION = '"urn:schemas-upnp-org:service:AVTransport:1#Play"'
	ENDPOINT = '/MediaRenderer/AVTransport/Control'
	BODY = '''
	<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
	 s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
	  <s:Body>
		<u:Play xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
		  <InstanceID>0</InstanceID>
		  <Speed>1</Speed>
		</u:Play>
	  </s:Body>
	</s:Envelope>
	'''

	HEADERS = {
		'Content-Type': 'text/xml',
		'SOAPACTION': ACTION
	}

	URL = 'http://{ip}:1400{endpoint}'.format(ip=IP, endpoint=ENDPOINT)

	REQ = requests.post(URL, data=BODY, headers=HEADERS)

	print("Response:")
	print(REQ.content)
	
	
def setOE3():
#sends a command to set OE3 as Radio sender
	ACTION = '"urn:schemas-upnp-org:service:AVTransport:1#SetAVTransportURI"'
	ENDPOINT = '/MediaRenderer/AVTransport/Control'
	BODY = '''
	<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
	 s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
	  <s:Body>
		<u:SetAVTransportURI xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
			<InstanceID>0</InstanceID>
			<CurrentURI>x-sonosapi-stream:s8007?sid=254&amp;flags=32</CurrentURI>
		<CurrentURIMetaData>&lt;DIDL-Lite xmlns:dc=&quot;http://purl.org/dc/elements/1.1/&quot; xmlns:upnp=&quot;urn:schemas-upnp-org:metadata-1-0/upnp/&quot; xmlns:r=&quot;urn:schemas-rinconnetworks-com:metadata-1-0/&quot; xmlns=&quot;urn:schemas-upnp-org:metadata-1-0/DIDL-Lite/&quot;&gt;&lt;item id=&quot;R:0/0/1&quot; parentID=&quot;R:0/0&quot; restricted=&quot;true&quot;&gt;&lt;dc:title&gt;OE3 Hitradio&lt;/dc:title&gt;&lt;upnp:class&gt;object.item.audioItem.audioBroadcast&lt;/upnp:class&gt;&lt;desc id=&quot;cdudn&quot; nameSpace=&quot;urn:schemas-rinconnetworks-com:metadata-1-0/&quot;&gt;SA_RINCON65031_&lt;/desc&gt;&lt;/item&gt;&lt;/DIDL-Lite&gt;</CurrentURIMetaData>
		</u:SetAVTransportURI>
	  </s:Body>
	</s:Envelope>
	'''

	HEADERS = {
		'Content-Type': 'text/xml',
		'SOAPACTION': ACTION
	}

	URL = 'http://{ip}:1400{endpoint}'.format(ip=IP, endpoint=ENDPOINT)

	REQ = requests.post(URL, data=BODY, headers=HEADERS)

	print("Response:")
	print(REQ.content)
	
def setInput():
#sends a command to use the chinch input as input
	ACTION = '"urn:schemas-upnp-org:service:AVTransport:1#SetAVTransportURI"'
	ENDPOINT = '/MediaRenderer/AVTransport/Control'
	BODY = '''
	<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
	 s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
	  <s:Body>
		<u:SetAVTransportURI xmlns:u="urn:schemas-upnp-org:service:AVTransport:1">
			<InstanceID>0</InstanceID>
			<CurrentURI>x-rincon-stream:RINCON_000E5821BF5601400</CurrentURI>
		<CurrentURIMetaData></CurrentURIMetaData>
		</u:SetAVTransportURI>
	  </s:Body>
	</s:Envelope>
	'''

	HEADERS = {
		'Content-Type': 'text/xml',
		'SOAPACTION': ACTION
	}

	URL = 'http://{ip}:1400{endpoint}'.format(ip=IP, endpoint=ENDPOINT)

	REQ = requests.post(URL, data=BODY, headers=HEADERS)

	print('Response:')
	print(REQ.content)
	
def setVolume(volume):
	if(int(volume)>100):
		volume = 100
	if(int(volume)<0):
		volume = 0
		
	ACTION = '"urn:schemas-upnp-org:service:RenderingControl:1#SetVolume"'
	ENDPOINT = '/MediaRenderer/RenderingControl/Control'
	BODY = '''
	<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
	 s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
	  <s:Body>
		<u:SetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1">
		  <InstanceID>0</InstanceID>
		  <Channel>Master</Channel>
		  <DesiredVolume>''' + str(volume) + '''</DesiredVolume>
		</u:SetVolume>
	  </s:Body>
	</s:Envelope>
	'''

	HEADERS = {
		'Content-Type': 'text/xml',
		'SOAPACTION': ACTION
	}

	URL = 'http://{ip}:1400{endpoint}'.format(ip=IP, endpoint=ENDPOINT)

	REQ = requests.post(URL, data=BODY, headers=HEADERS)

	print("Response:")
	print(REQ.content)

def getVolume():
	ACTION = '"urn:schemas-upnp-org:service:RenderingControl:1#GetVolume"'
	ENDPOINT = '/MediaRenderer/RenderingControl/Control'
	BODY = '''
	<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/"
	 s:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">
	  <s:Body>
		<u:GetVolume xmlns:u="urn:schemas-upnp-org:service:RenderingControl:1">
		  <InstanceID>0</InstanceID>
		  <Channel>Master</Channel>
		</u:GetVolume>
	  </s:Body>
	</s:Envelope>
	'''

	HEADERS = {
		'Content-Type': 'text/xml',
		'SOAPACTION': ACTION
	}

	URL = 'http://{ip}:1400{endpoint}'.format(ip=IP, endpoint=ENDPOINT)

	REQ = requests.post(URL, data=BODY, headers=HEADERS)

	print("Response:")
	print(REQ.content)

	volStr = REQ.text
	beg = volStr.find("<CurrentVolume>")
	end = volStr.find("</CurrentVolume>")
	volStr = volStr[beg+15:end]

	return int(volStr)