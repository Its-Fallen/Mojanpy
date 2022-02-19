## Mojanpy [In Developing]

A simple in use Mojang API wrapper, include full implementation of Mojang API and Mojang Authentication.

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
- [x] Base Mojang API support (not including authenticated routes)
- [x] Add error checks for input and output data
- [ ] Full Mojang Authentication support
- [ ] Full Mojang API support

## Contact
DM me in Discord (FallenBoy#9813), if you're have some questions or suggestions about this
