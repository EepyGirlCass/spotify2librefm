# spotify2librefm



python script to convert spotify history jsons to the format lastfm2librefm's import.py uses

also improves import.py:

* scrobbles 50 songs at once
* retries if there's an error
* waits at least SLEEP\_BETWEEN\_SCROBBLES *total* time between scrobbles rather than always sleeping
* displays completion percentage, tracks scrobbled, estimated completion time, ignored scrobbles



spotify listen history can be downloaded here: <https://www.spotify.com/us/account/privacy/>



I'm leaving the original export.py cause it should still work with import.py, its untested though

I get about 10 scrobbles / second on my system, in theory you could get up to 50/s before being rate limited

