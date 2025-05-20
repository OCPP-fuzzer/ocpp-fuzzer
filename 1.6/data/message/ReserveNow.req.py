connectorId integer connectorId >= 0 1..1 Required. This contains the id of the connector to be reserved. A value of 0 means that the reservation is not for a specific connector.
expiryDate dateTime 1..1 Required. This contains the date and time when the reservation ends.
idTag IdToken 1..1 Required. The identifier for which the Charge Point has to reserve a connector.
parentIdTag IdToken 0..1 Optional. The parent idTag.
reservationId integer 1..1 Required. Unique id for this reservation.