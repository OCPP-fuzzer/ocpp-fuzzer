name
identifierString[0..50]
1..1
Required. Name of the component. Name should be taken from the list of standardized component names whenever possible. Case Insensitive. strongly advised to use Camel Case.
instance
identifierString[0..50]
0..1
Optional. Name of instance in case the component exists as multiple instances. Case Insensitive. strongly advised to use Camel Case.
evse
EVSEType
0..1
Optional. Specifies the EVSE when component is located at EVSE level, also specifies the connector when component is located at Connector level.