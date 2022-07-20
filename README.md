## [DEPRECATED] Mojanpy [DEPRECATED]

A simple in use Mojang API wrapper, include full implementation of [Mojang API](https://wiki.vg/Mojang_API) and [Mojang Authentication](https://wiki.vg/Authentication).

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
