##############################################################################
# Halo rebaseline active servers
# Author: Sean Nicholson
# Version 1.0.0
# Date 10.26.2017
# v 1.0.0 - initial release
##############################################################################


import cloudpassage, yaml

def create_api_session(session):
    config_file_loc = "cloudpassage.yml"
    config_info = cloudpassage.ApiKeyManager(config_file=config_file_loc)
    session = cloudpassage.HaloSession(config_info.key_id, config_info.secret_key)
    return session

def get_config():
    with open('cloudpassage.yml') as config_settings:
        api_info = yaml.load(config_settings)
        fim_policy_id = ""
        fim_policy_id = api_info['defaults']['fim_policy_id']
    return fim_policy_id


def rebaseline_servers(session,fim_policy_id):
    rebaseline = cloudpassage.FimBaseline(session)
    fim_policy_baselines = rebaseline.list_all(fim_policy_id)
    halo_servers_list = []
    for baseline in fim_policy_baselines:
        rebaseline.update(fim_policy_id,baseline['id'],baseline['server_id'])


if __name__ == "__main__":
    api_session = None
    api_session = create_api_session(api_session)
    rebaseline_servers(api_session,get_config())
