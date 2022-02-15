## Mojanpy [In Developing]

A simple in use Mojang API wrapper, include full implementation of Mojang API and Mojang Authentication, also support RCON/Query/Server Ping.

## Usage examples
```py
import mojanpy

uuid = mojanpy.get_uuid("Notch")
print(uuid)
```
```py
import mojanpy

uuid = mojanpy.get_uuid("Notch")
profile = mojanpy.get_uuid_profile(uuid)

print(profile.skin)
```
## Progress
- [x] Base Mojang API support (not including authenticated routes and etc.)
- [ ] Add in all methods error checks for input and output data
- [ ] Full Mojang Authentication support
- [ ] Full Mojang API support
- [ ] Add Server Pinger support
- [ ] Add Query support
- [ ] Add RCON support
- [ ] And more...

## Contact
DM me in Discord (FallenBoy#9813), if you're have some questions or suggestions about this
