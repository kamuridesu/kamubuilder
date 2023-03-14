import subprocess as sp


def checkDistro(distro_manager):
    p = sp.Popen(
        ["which", distro_manager], stdout=sp.PIPE, stdin=sp.PIPE, stderr=sp.PIPE
    )
    p.communicate()
    return p.returncode == 0


def getPackageManager():
    if checkDistro("apt-get"):
        return "apt-get"
    if checkDistro("apt"):
        return "apt"
    if checkDistro("pacman"):
        return "pacman"
    if checkDistro("xbps"):
        return "xbps"


if __name__ == "__main__":
    print(getPackageManager())
