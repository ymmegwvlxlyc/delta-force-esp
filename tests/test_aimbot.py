from delta_force_esp.aim.aimbot import Aimbot, AimConfig
from delta_force_esp.core.math3d import Vec3


class _FakeEnt:
    def __init__(self, handle, pos, visible=True):
        self.handle = handle
        self.visible = visible
        self._pos = pos

    def bone(self, _name):
        return self._pos


def test_pick_nearest_in_fov():
    bot = Aimbot(AimConfig(fov=15.0, visible_only=True))
    origin = Vec3(0, 0, 0)
    view = Vec3(0, 0, 0)
    ents = [_FakeEnt(1, Vec3(100, 100, 0)), _FakeEnt(2, Vec3(100, 1, 0))]
    assert bot.pick_target(origin, view, ents) == 2


def test_skip_invisible():
    bot = Aimbot(AimConfig(fov=30.0, visible_only=True))
    ents = [_FakeEnt(1, Vec3(100, 0, 0), visible=False)]
    assert bot.pick_target(Vec3(0, 0, 0), Vec3(0, 0, 0), ents) is None