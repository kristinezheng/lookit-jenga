## from https://github.com/kristinezheng/jenga-performance-art/tree/891ce2ee460f9815f56051e48f3788b27fd721b8

import sys
import time
import pybullet as p
import pybullet_data
import numpy as np
import os
import argparse
import json
from scipy.spatial.transform import Rotation

print("done importing")
INITIATE = 4
PERTURB = 6
CHECK = 5
INIT_CHECK = 7

class Sim:
    def __init__(self,
                 num_trials=5,
                 N=5,
                 save_dir=None,
                 seed=0,
                 display=False,
                 mh_iters=16):
        # tower params
        self.N = N
        self.y_len = 0.5
        self.x_len = 3 * self.y_len
        self.z_len = self.y_len * 3. / 5
        self.x_start, self.x_end = -0.5, 0.5
        self.y_start, self.y_end = -0.5, 0.5
        self.density = 1.
        self.mass = self.x_len * self.y_len * self.z_len * self.density
        self.friction = 0.5

        # FSM params
        self.is_init_tower = True
        self.start_time = time.time()
        self.perturb_time = time.time()
        self.epsilon = self.z_len / 50
        self.vel_epsilon = 0.01

        # trials params
        self.num_trials = num_trials
        self.num_falls = 0
        self.num_blocks_fallen = 0
        self.trials_sofar = 0
        self.prop_fallen_sofar = 0.
        self.save_dir = os.path.abspath(save_dir)
        if not os.path.exists(self.save_dir):
            os.makedirs(self.save_dir)
        self.seed = seed
        self.mh_iters = mh_iters

        # store positions
        self.initial_positions = dict()

        # pybullet
        if display:
            self.physicsClient = p.connect(p.GUI)
        else:
            print("no display")
            self.physicsClient = p.connect(p.DIRECT)
        print("done creating physics client")
        p.setAdditionalSearchPath(pybullet_data.getDataPath())  # optionally
        p.setGravity(0, 0, -10)

        self.visualShapeId = p.createVisualShape(shapeType=p.GEOM_BOX,
                                                 rgbaColor=[0.75, 0.6, 0.4, 1],
                                                 halfExtents=[self.x_len / 2, self.y_len / 2, self.z_len / 2])
        self.collisionShapeId = p.createCollisionShape(shapeType=p.GEOM_BOX,
                                                       halfExtents=[self.x_len / 2, self.y_len / 2, self.z_len / 2])
        # create ground
        planeId = p.loadURDF("plane.urdf")

        # self.bodies is a dictionary with (key, value) = (bodyID, 7-D initial_pose)
        self.bodies = {}

        # create initial structure (REMOVE ONCE DEBUGGED)
        # self.create_vertical_stack()
        self.mode = INITIATE

    def create_vertical_stack(self):
        z = self.z_len / 2
        for i in range(self.N):
            id = p.createMultiBody(baseMass=self.mass,
                                   baseInertialFramePosition=[0, 0, 0],
                                   baseCollisionShapeIndex=self.collisionShapeId,
                                   baseVisualShapeIndex=self.visualShapeId,
                                   basePosition=[0, 0, z],
                                   useMaximalCoordinates=True)
            self.bodies[id] = p.getBasePositionAndOrientation(id)
            z += self.z_len
        time.sleep(2)
        self.reset_bodies()
        time.sleep(2)

    def create_t_tower(self):
        """
        Towers that look like this:
        _____
          |
          |
          |
        The above is a height 3 t-tower.
        :return:
        """
        z = self.x_len / 2
        for i in range(self.N - 1):
            id = p.createMultiBody(baseMass=self.mass,
                                   baseInertialFramePosition=[0, 0, 0],
                                   baseCollisionShapeIndex=self.collisionShapeId,
                                   baseVisualShapeIndex=self.visualShapeId,
                                   basePosition=[0, 0, z],
                                   baseOrientation=Rotation.from_euler('xyz', [0, 90, 90], degrees=True).as_quat(),
                                   useMaximalCoordinates=True)
            self.bodies[id] = p.getBasePositionAndOrientation(id)
            z += self.x_len
        # put the last block horizontally on top.
        z = self.x_len * (self.N - 1) + self.z_len / 2
        id = p.createMultiBody(baseMass=self.mass,
                               baseInertialFramePosition=[0, 0, 0],
                               baseCollisionShapeIndex=self.collisionShapeId,
                               baseVisualShapeIndex=self.visualShapeId,
                               basePosition=[0, 0, z],
                               useMaximalCoordinates=True)
        self.bodies[id] = p.getBasePositionAndOrientation(id)
        time.sleep(2)
        self.reset_bodies()
        time.sleep(2)

    def create_structure(self, blocks):
        """
        Creates a structure given an array of block positions
        blocks is a length self.N array that stores (x_coord, y_coord, orientation).
        """
        z = self.z_len / 2
        for i in range(len(blocks)):
            x, y, theta = blocks[i]
            if len(self.bodies) == 0:
                z = self.z_len / 2
            else:
                # raycast to find the block directly beneath the one we want to place
                # max_z = the maximum height where we can spawn blocks.
                # We cast rays from this height in the area of an imaginary block.
                max_z = max(self.bodies.values(), key=lambda pos: pos[0][2])[0][2] + self.z_len
                ray_froms = []
                ray_tos = []

                # define the x-y area of the imaginary block we'll cast rays from
                x_extent = self.x_len / 2
                y_extent = self.y_len / 2
                if theta == np.pi / 2:
                    x_extent = self.y_len / 2
                    y_extent = self.x_len / 2
                x_range = np.linspace(x - x_extent, x + x_extent, num=20, endpoint=True)
                y_range = np.linspace(y - y_extent, y + y_extent, num=20, endpoint=True)

                # get rays from the maximum heights to beneath the floor
                for i in x_range:
                    for j in y_range:
                        ray_froms.append([i, j, max_z])
                        ray_tos.append([i, j, -.5])
                queries = p.rayTestBatch(ray_froms, ray_tos)
                max_z_obj = max(queries, key=lambda pos: pos[3][2])
                max_z_hit = max(0, max_z_obj[3][2])
                z = max_z_hit + self.z_len / 2
            id = p.createMultiBody(baseMass=self.mass,
                                   baseInertialFramePosition=[0, 0, 0],
                                   baseCollisionShapeIndex=self.collisionShapeId,
                                   baseVisualShapeIndex=self.visualShapeId,
                                   basePosition=[x, y, z],
                                   baseOrientation=p.getQuaternionFromEuler([0, 0, theta]),
                                   useMaximalCoordinates=True)
            p.changeDynamics(id, -1, lateralFriction=self.friction)
            self.bodies[id] = p.getBasePositionAndOrientation(id)
            z += self.z_len
        print("done creating")

    def create_structure_rigid(self, blocks):
        """
        Creates a structure given an array of block positions
        blocks is a length self.N dict in the form defined by save_data().
        """
        p.setGravity(0, 0, 0)
        for i in blocks.keys():
            obj = blocks[i]
            id = p.createMultiBody(baseMass=obj["mass"],
                                   baseInertialFramePosition=[0, 0, 0],
                                   baseCollisionShapeIndex=self.collisionShapeId,
                                   baseVisualShapeIndex=self.visualShapeId,
                                   basePosition=obj["pos"],
                                   baseOrientation=obj["ori"],
                                   useMaximalCoordinates=True)
            p.changeDynamics(id, -1, lateralFriction=self.friction)
            self.bodies[id] = p.getBasePositionAndOrientation(id)
        p.setGravity(0, 0, -10)

    def monte_carlo_shift(self, scale_pos=(0.1, 0.1), scale_ori=np.pi / 8):
        """
        Perturb the position and yaw of each block in the structure by a Gaussian.
        """
        for id in self.bodies:
            # Perturb the position in the x and y axes
            perturbation_pos = np.pad(np.random.normal(0., scale=scale_pos, size=(2,)), (0, 1))
            # Perturb the orientation in the z axis
            perturbation_ori = np.pad(np.random.normal(0., scale=scale_ori, size=(1,)), (2, 0))
            current_pos, current_ori = p.getBasePositionAndOrientation(id)
            current_ori = p.getEulerFromQuaternion(current_ori)
            new_pos = current_pos + perturbation_pos
            new_ori = p.getQuaternionFromEuler(current_ori + perturbation_ori)
            p.resetBasePositionAndOrientation(id, posObj=new_pos, ornObj=new_ori)

    def reset_bodies(self):
        """
        Reset bodies to initial positions and orientations.
        """
        for id in self.bodies:
            p.resetBasePositionAndOrientation(id, posObj=self.bodies[id][0], ornObj=self.bodies[id][1])

    def del_bodies(self):
        """
        Clear all blocks. Don't delete the plane which has id = 0.
        """
        num_bodies = p.getNumBodies()
        for id in range(1, num_bodies):
            p.removeBody(id)
        self.bodies = {}

    def check_fall(self):
        """
        Check if the bodies are falling
        """
        num_fallen = 0
        for id in range(1, p.getNumBodies()):
            current_z = p.getBasePositionAndOrientation(id)[0][2]
            if abs(current_z - self.bodies[id][0][2]) >= self.epsilon:
                num_fallen += 1
        return num_fallen

    def set_start_pos(self):
        for id in self.bodies:
            p.resetBasePositionAndOrientation(id, posObj=self.bodies[id][0], ornObj=self.bodies[id][1])
            self.bodies[id] = p.getBasePositionAndOrientation(id)

    def run(self):
        for i in range(10000):
            p.stepSimulation()
            time.sleep(1. / 240.)
        self.check_fall()
        p.disconnect()

    def store_data(self):
        data = {}
        for id in self.bodies:
            pos, orn = self.bodies[id]
            linVel, angVel = p.getBaseVelocity(id)
            data[id] = {
                "pos": pos,
                "ori": orn,
                "linVel": linVel,
                "angVel": angVel,
                "x_size": self.x_len,
                "y_size": self.y_len,
                "z_size": self.z_len,
                "mass": self.mass,
                "friction": self.friction
            }
        return data

    def reset_vars(self):
        self.trials_sofar = 0
        self.num_blocks_fallen = 0
        self.num_falls = 0
        self.prop_fallen_sofar = 0.
        self.mode = INITIATE
        self.del_bodies()

    def fsm(self, dt, blocks=None, is_final_config=False, is_initial=False):
        while True:
            if self.mode == INITIATE:
                print("initiate")
                self.del_bodies()
                if type(blocks) != str:
                    if not is_final_config:
                        self.create_structure(blocks)
                    else:
                        self.create_structure_rigid(blocks)
                else:
                    if blocks == "t_tower":
                        self.create_t_tower()
                    elif blocks == "vertical_stack":
                        self.create_vertical_stack()
                    else:
                        print("invalid structure type")
                        return
                self.start_time = time.time()
                self.mode = INIT_CHECK

            if self.mode == INIT_CHECK:
                if time.time() - self.start_time > 2:
                    print("checking")
                    if self.check_fall():
                        print("falling, going back to initiate")
                        self.reset_vars()
                        self.mode = INITIATE
                        return -1., {}
                    else:
                        print("no initial fall")
                        if is_initial:
                            data = self.store_data()
                            self.reset_vars()
                            return 1., data
                        else:
                            self.mode = PERTURB

            if self.mode == PERTURB:
                if all([np.linalg.norm(np.array(p.getBaseVelocity(id)[0]) - np.zeros((3,))) <= self.vel_epsilon for id in self.bodies]):
                    self.perturb_time = time.time()
                    self.set_start_pos()
                    #self.monte_carlo_shift(scale_pos=(0.125 * self.x_len, 0.125 * self.y_len))
                    self.monte_carlo_shift(scale_pos=(0.05 * self.x_len, 0.05 * self.y_len))
                    self.mode = CHECK
            elif self.mode == CHECK:
                if time.time() - self.perturb_time > 3.:
                    self.num_blocks_fallen = self.check_fall()
                    self.trials_sofar += 1
                    self.prop_fallen_sofar += min(1.0, float(self.num_blocks_fallen) / (self.N - 1))
                    print("trial", self.trials_sofar)
                    print("DEBUG prop fallen", self.num_blocks_fallen, float(self.num_blocks_fallen) / (self.N - 1), self.prop_fallen_sofar)
                    self.reset_bodies()

                    if self.trials_sofar == self.num_trials:
                        # score = average proportion of blocks fallen
                        fall_rate = self.prop_fallen_sofar / self.trials_sofar
                        print("fall rate:", fall_rate)
                        tower_config = self.store_data()
                        self.reset_vars()
                        return fall_rate, tower_config
                    else:
                        self.mode = PERTURB
            p.stepSimulation()
            time.sleep(dt)

    def metropolis_hastings(self, dt=1. / 240):
        """
        See the Wikipedia article for the pseudocode
        """
        stable = -1
        x = None
        init_data = None
        iters = 100
        while stable < 0:
            print("not yet stable")
            # initialize a bunch of random x positions normally distributed about the origin
            rand_scale = np.random.uniform(2, 4)
            # HACK: since we have a hard time finding a good initial tower large N,
            # we can start from a vertical stack if we don't get a good initialization after 100 iters
            if iters < 0:
                x = np.array([[0., 0., np.random.choice([0., np.pi / 2])] for _ in range(self.N)])
            else:
                x = []
                for _ in range(self.N):
                    rand_orn = np.random.choice([0., np.pi / 2])
                    if rand_orn == 0.:
                        x_scale = self.x_len / rand_scale
                        y_scale = self.y_len / rand_scale
                    else:
                        x_scale = self.y_len / rand_scale
                        y_scale = self.x_len / rand_scale
                    x.append(np.array([np.random.normal(scale=x_scale),
                                       np.random.normal(scale=y_scale),
                                       rand_orn]))
            stable, init_data = self.fsm(dt, blocks=x, is_initial=True)
            iters -= 1
        print("stable!")
        x_history = [init_data]
        prob_history = [stable]
        for i in range(self.mh_iters):
            print("iter:", i)
            perturbations = []
            for _ in range(self.N):
                # rand_angle = np.random.choice([0, np.pi / 2])
                perturbation = np.random.normal(loc=0,
                                                scale=[self.x_len / 4, self.y_len / 4, np.pi / 6],
                                                size=(3,))
                perturbation[2] = 0 if abs(abs(perturbation[2]) - np.pi / 2) > np.pi / 4 else np.pi / 2
                perturbations.append(perturbation)
            x_prime = x + perturbations
            P_x = -1
            data = None
            while P_x < 0.:
                # get the fall rate of x (higher -> more falls)
                P_x, data = self.fsm(dt, blocks=x)
            P_x_prime, data_prime = self.fsm(dt, blocks=x_prime)

            if P_x > 0.:
                acceptance_prob = min(1., P_x_prime / P_x)
            else:
                acceptance_prob = 1.
            rand_num = np.random.uniform()
            if acceptance_prob >= rand_num:
                # accept the candidate
                print("accepted")
                x = x_prime[:]
                prob = P_x_prime
                data_final = data_prime
            else:
                print("rejected")
                prob = P_x
                data_final = data
            x_history.append(data_final)
            prob_history.append(prob)
            identifier = time.time()
            filename = f"{prob}_{self.seed}_{identifier}.json"
            path = os.path.join(os.path.abspath(self.save_dir), filename)
            print("saving to disk:", path)
            with open(path, "w") as f:
                json.dump(data_final, f)
        '''
        highest_prob_ix = np.argmax(prob_history)
        highest_prob = prob_history[highest_prob_ix]
        highest_prob_data = x_history[highest_prob_ix]
        identifier = time.time()
        filename = f"{highest_prob}_{self.seed}_{identifier}.json"
        path = os.path.join(os.path.abspath(self.save_dir), filename)
        print("saving to disk:", path)
        with open(path, "w") as f:
            json.dump(highest_prob_data, f)
        '''
        return x_history, prob_history

def run_sim(args):
    sim = Sim(**args)
    print("performing metropolis hastings")
    history, probs = sim.metropolis_hastings()


def test_stability(args, sculpture_type="sculpture", sculpture_name = None):
    sim = Sim(**args)
    N = args["N"]
    print(f"Testing stability of height {N} stack")
    stable, init_data = sim.fsm(1./240, blocks=sculpture_type, is_final_config=True, is_initial=False)

    identifier = time.time()
    if not sculpture_name:
        sculpture_name = "unknown"
    filename = f"{sculpture_name}_{sim.N}_{sim.num_trials}_{identifier}.json"
    path = os.path.join(os.path.abspath(sim.save_dir), filename)
    print("saving to disk:", path)
    with open(path, "w") as f:
        json.dump(stable, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--display", action='store_true', help="True to show pyglet display, false otherwise")
    parser.add_argument("--save_dir", default="../json", type=str, help="where to save the pymunk envs")
    parser.add_argument("--num_trials", default=20, type=int, help="how many times we perturb each structure")
    parser.add_argument("--mh_iters", default=16, type=int, help="how many Metropolis-Hastings samples")
    parser.add_argument("--seed", default=0, type=int, help="seed for multithreading")
    parser.add_argument("--N", default=10, type=int, help="how many blocks to generate")

    parser.add_argument("--blocks", default="../2_20_towers/7979.json", type=str, help="position/orientation of block tower to generate")

    args = parser.parse_args()

    init_args = {"display": args.display,
                 "save_dir": args.save_dir,
                 "num_trials": args.num_trials,
                 "N": args.N,
                 "seed": args.seed,
                 "mh_iters": args.mh_iters}
    # run_sim(init_args)
    # print('args blocks:', args.blocks)

    with open(args.blocks) as file:
        structure = json.load(file)

    dict_filt = lambda x, y: dict([ (i,x[i]) for i in x if i in y ])
    #use less blocks
    filtered_structure = dict_filt(structure.copy(), set(str(a) for a in range(1,args.N+1)))
    # print('(str(a) for a in range(1,args.N)', set(str(a) for a in range(1,args.N)))
    # print('filtered_structure', filtered_structure.keys())
    name = args.blocks.split('/')[-1][:-5]
    test_stability(init_args, sculpture_type=filtered_structure, sculpture_name=name)#"t_tower")


#### python ipe.py --save_dir /Users/kristinezheng/lookit-jenga/analysis_src/saved_results --num_trials 50 --N 10 --blocks /Users/kristinezheng/lookit-jenga/2_20_towers/7979.json###
#### python ipe.py --display --save_dir /Users/kristinezheng/lookit-jenga/analysis_src/saved_results --num_trials 50 --N 10 --blocks /Users/kristinezheng/lookit-jenga/2_20_towers/7979.json###
### python ipe.py --display --save_dir /Users/kristinezheng/lookit-jenga/analysis_src/saved_results --num_trials 5 --N 5 --blocks /Users/kristinezheng/lookit-jenga/2_20_towers/7979.json###