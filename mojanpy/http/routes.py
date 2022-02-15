# base Mojang API routes without authentication
class BaseRoutes:
    username_to_uuid = (
        lambda username: "https://api.mojang.com/users/profiles/minecraft/{0}".format(
            username
        )
    )
    usernames_to_uuids = "https://api.mojang.com/profiles/minecraft"
    name_history = lambda uuid: "https://api.mojang.com/user/profiles/{0}/names".format(
        uuid
    )
    user_profile = lambda uuid: "https://sessionserver.mojang.com/session/minecraft/profile/{0}".format(
        uuid
    )
    blocked_servers = "https://sessionserver.mojang.com/blockedservers"
    sale_statistic = "https://api.mojang.com/orders/statistics"


# Profile Mojang API routes for authenticated users
class AuthenticatedRoutes:
    profile_information = "https://api.minecraftservices.com/minecraft/profile"
    player_attributes = "https://api.minecraftservices.com/player/attributes"
    profile_name_change_info = (
        "https://api.minecraftservices.com/minecraft/profile/namechange"
    )
    check_product_voucher = "https://api.minecraftservices.com/productvoucher/giftcode"
    name_availability = lambda name: "https://api.minecraftservices.com/minecraft/profile/name/{0}/available".format(
        name
    )
    change_name = lambda name: "https://api.minecraftservices.com/minecraft/profile/name/{0}".format(
        name
    )
    change_skin = "https://api.minecraftservices.com/minecraft/profile/skins"
    upload_skin = "https://api.minecraftservices.com/minecraft/profile/skins"
    reset_skin = lambda uuid: "https://api.mojang.com/user/profile/{0}/skin".format(
        uuid
    )
    cape_visibility = "https://api.minecraftservices.com/minecraft/profile/capes/active"  # DELETE or PUT
    verify_security_location = "https://api.mojang.com/user/security/location"
    get_security_questions = "https://api.mojang.com/user/security/challenges"
    send_security_answers = "https://api.mojang.com/user/security/location"
    get_migration_info = "https://api.minecraftservices.com/rollout/v1/msamigration"
    account_migration_otp = (
        "https://api.minecraftservices.com/twofactorauth/migration/otp"
    )
    verify_migration_otp = lambda uuid: "https://api.minecraftservices.com/twofactorauth/migration/otp/{0}/verify".format(
        uuid
    )
    submit_migration_token = "https://api.minecraftservices.com/migration/token"
    connect_xbox_live = "https://sisu.xboxlive.com/connect/XboxLive"
