## Mojanpy [In Developing]

A simple in use Mojang API wrapper, include full implementation of Mojang API and Mojang Authentication.

## Installing
```
$ pip install mojanpy
```

## Usage examples
```py
import mojanpy

uuid = mojanpy.get_uuid("Notch")
print(uuid)
# 069a79f444e94726a5befca90e38aaf5
```
```py
import mojanpy

profile = mojanpy.get_uuid_profile("069a79f444e94726a5befca90e38aaf5")
print(profile.skin)
# http://textures.minecraft.net/texture/292009a4925b58f02c77dadc3ecef07ea4c7472f64e0fdc32ce5522489362680
```

## Progress
- [x] Base Mojang API support (not including authenticated routes)
- [x] Add error checks for input and output data
- [x] Full Mojang Authentication support
- [ ] Full Mojang API support
- [ ] Add documentation
- [ ] Add tests

## Future

- [ ] Add Microsoft Authentication Sheme
- [ ] Add Server Info support (Info about server, like playerlist, server icon and etc.)
- [ ] Add Query support (as Server Info, but return more data, like server plugins)
- [ ] Add RCON support
- [ ] Add some useful utils (skin saver, parsing players from server (if server return playerlist :( ), and etc.)

## Contact
DM me in Discord (FallenBoy#9813), if you're have some questions or suggestions about this
