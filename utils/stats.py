"""Module for tracking stats in historical analysis."""

# Track overall stats.
#   How many notifications followed by slides?
#   How many notifications not followed by slides?
#   How many slides were not missed?
stats = {
    "notifications_issued": 0,
    "associated_notifications": 0,
    "unassociated_notifications": 0,
    "unassociated_notification_points": [],
    "relevant_slides": [],
    "unassociated_slides": [],
    "notification_times": {},
    "earliest_reading": None,
    "latest_reading": None,
}