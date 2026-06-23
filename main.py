import minecraft_launcher_lib
import subprocess

def launch():
    mc_dir = "/home/xteam23/.minecraft"
    mc_version = "1.8.9"

    minecraft_launcher_lib.install.install_minecraft_version(mc_version, mc_dir)
    
    forge = minecraft_launcher_lib.mod_loader.get_mod_loader("forge")
    mod_loader_id = forge.install(mc_version, mc_dir)

    options = {
            "username": "xteam23_",
            "uuid": "0000-0000000-0000",
            "token": "0",
            }

    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(mod_loader_id, mc_dir, options)

    subprocess.run(minecraft_command)

launch()

