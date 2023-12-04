from datetime import datetime

now = datetime.utcnow()			# Get the current date and time
timestamp = int(now.timestamp())# Calculate the seconds since January 1, 1970 (Unix timestamp)

print(f"Seconds since January 1, 1970: {timestamp:,.4f} or {timestamp:.2e} in scientific notation\n\
{now.strftime('%b %d %Y')}")
