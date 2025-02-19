import torch
from legged_gym.envs.base.legged_robot_config import LeggedRobotCfg,LeggedRobotCfgPPO

class YunaCfg(LeggedRobotCfg):
    class env(LeggedRobotCfg.env):
        num_envs = 8
        num_observations = 66
        num_actions = 18
    
    class terrain(LeggedRobotCfg.terrain):
        curriculum = False
        mesh_type = 'plane'
        measure_heights = False
    
    class init_state(LeggedRobotCfg.init_state):
        pos = [0.0,0.0,0.3]

        default_joint_angles = {
            'base1': 0.,
            'base2': 0.,
            'base3': 0.,
            'base4': 0.,
            'base5': 0.,
            'base6': 0.,

            'shoulder1': 0.,
            'shoulder2': 0.,
            'shoulder3': 0.,
            'shoulder4': 0.,
            'shoulder5': 0.,
            'shoulder6': 0.,

            'elbow1': -1.5708,
            'elbow2': 1.5708,
            'elbow3': -1.5708,
            'elbow4': 1.5708,
            'elbow5': -1.5708,
            'elbow6': 1.5708,
        }

    class control(LeggedRobotCfg.control):
        stiffness = {'base1': 100.,'base2': 100.,'base3': 100.,'base4': 100.,'base5': 100.,'base6': 100.,
                     'shoulder1': 100.,'shoulder2': 100.,'shoulder3': 100.,'shoulder4': 100.,'shoulder5': 100.,'shoulder6': 100.,
                     'elbow1': 100.,'elbow2': 100.,'elbow3': 100.,'elbow4': 100.,'elbow5': 100.,'elbow6': 100.}
        
        damping = {'base1': 0.05,'base2': 0.05,'base3': 0.05,'base4': 0.05,'base5': 0.05,'base6': 0.05,
                     'shoulder1': 0.05,'shoulder2': 0.05,'shoulder3': 0.05,'shoulder4': 0.05,'shoulder5': 0.05,'shoulder6': 0.05,
                     'elbow1': 0.05,'elbow2': 0.05,'elbow3': 0.05,'elbow4': 0.05,'elbow5': 0.05,'elbow6': 0.05}
        
        action_scale = 0.25
        decimation = 4

    class asset(LeggedRobotCfg.asset):
        file = '{LEGGED_GYM_ROOT_DIR}/resources/robots/yuna/urdf/yuna.urdf'
        foot_name = 'FOOT'
        penalize_contacts_on = {'LINK'}
        terminate_after_contacts_on = {'base_link'}
        flip_visual_attachments = False
        self_collisions = 1
    
    class rewards(LeggedRobotCfg.rewards):
        soft_dof_pos_limit = 0.95
        soft_dof_vel_limit = 0.9
        soft_torque_limit = 0.9
        max_contact_force = 300.
        only_positive_rewards = False
        class scales( LeggedRobotCfg.rewards.scales ):
            termination = -200.
            tracking_ang_vel = 0.5
            torques = -5.e-4
            dof_acc = -2.e-7
            lin_vel_z = -0.5
            feet_air_time = 5.
            dof_pos_limits = -1.
            no_fly = 0.25
            dof_vel = -0.0
            ang_vel_xy = -0.0
            feet_contact_forces = -0.

class YunaCfgPPO(LeggedRobotCfgPPO):
    class runner(LeggedRobotCfgPPO.runner):
        run_name = 'yuna_test'
        experiment_name = 'flat'