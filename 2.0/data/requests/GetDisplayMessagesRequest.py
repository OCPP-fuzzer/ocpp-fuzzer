id
integer
0..*
Optional. If provided the Charging Station shall return Display Messages of the given ids. This field SHALL NOT contain more ids than set in NumberOfDisplayMessages.maxLimit.
requestId
integer
1..1
Required. The Id of this request.
priority
MessagePriorityEnumType
0..1
Optional. If provided the Charging Station shall return Display Messages with the given priority only.
state
MessageStateEnumType
0..1
Optional. If provided the Charging Station shall return Display Messages with the given state only.