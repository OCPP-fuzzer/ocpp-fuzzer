ocppVersion
OCPPVersionEnumType
1..1
Required. Defines the OCPP version used for thiscommunication function.his field is ignored, since the OCPP version to use is determined during the websocket handshake.
ocppTransport
OCPPTransportEnumType
1..1
Required. Defines the transport protocol (e.g. SOAP or JSON). Note: SOAP is not supported in OCPP 2.0, but is supported by other versions of OCPP.
ocppCsmsUrl
string[0..512]
1..1
Required. URL of the CSMS(s) that this Charging Station communicates with, without the Charging Station identitypart.The SecurityCtrlr.Identity field is appended to ocppCsmsUrl to provide the full websocket URL
messageTimeout
integer
1..1
Required. Duration in seconds before a message send by the Charging Station via this network connection times- out. The best setting depends on the underlying network and response times of the CSMS. If you are looking for a some guideline: use 30 seconds as a starting point.
securityProfile
integer
1..1
Required. This field specifies the security profile used when connecting to the CSMS with this NetworkConnectionProfile.
ocppInterface
OCPPInterfaceEnumType
1..1
Required. Applicable Network Interface.Charging Station is allowed to use a different network interface to connect if the given one does not work
vpn
VPNType
0..1
Optional. Settings to be used to set up the VPN connection
apn
APNType
0..1
Optional. Collection of configuration data needed to make a data-connection over a cellular network.