
def converttime(seconds):
    minutes, seconds = divmod(seconds, 60)
    if minutes <= 10:
        return str("%02d"%minutes) + ":" + str("%02d"%seconds)
    else:
        return str(minutes) + ":" + str("%02d"%seconds)
