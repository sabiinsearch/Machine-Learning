from gym.envs.registration import register

register(
    id='bussinessCtlr-v0',
    entry_point='envs.envs_bussiness:BussinessEnv',
)

register(
    id='bussinessCtlr-v1',
    entry_point='envs.envs_bussiness:BussinessEnv',
)
