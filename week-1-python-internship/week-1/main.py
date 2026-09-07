# Source - https://stackoverflow.com/q/60442518
# Posted by clarkus978, modified by community. See post 'Timeline' for change history
# Retrieved 2026-09-07, License - CC BY-SA 4.0

import dateutil.parser

time = "2020-02-25T00:02:43.000Z"
parsed_time = dateutil.parser.parse(time)
t_in_millisec = parsed_time.strftime('%s%f')
t_in_millisec[:-3]
