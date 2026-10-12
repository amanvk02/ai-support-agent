# Notification troubleshooting

## Notifications disabled
Source ID: docs_notifications

Order notifications are sent only when notifications_enabled is true.
If disabled, enable notifications in account settings.

## Authentication rejected
Source ID: docs_authentication

HTTP 401 means the receiving endpoint rejected authentication.
Check whether the configured credential matches the receiver's requirements.
A 401 alone does not establish whether a credential expired.

## Delivery timeout
Source ID: docs_timeout

The delivery service waits up to 5000 milliseconds for a response.
If no response arrives, the attempt is recorded as a timeout.
Check receiver availability and response time.