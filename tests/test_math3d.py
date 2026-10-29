from delta_force_esp.core.math3d import Vec3, world_to_screen, angle_delta


def test_look_at_basic():
    a = Vec3(0, 0, 0)
    b = Vec3(100, 0, 0)
    ang = a.look_at(b)
    assert abs(ang.y) < 1e-6 and abs(ang.x) < 1e-6


def test_angle_delta_wrap():
    d = angle_delta(Vec3(0, 179, 0), Vec3(0, -179, 0))
    assert d <= 2.001


def test_world_to_screen_behind():
    m = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, -1, 0, 0, 0, 1]
    assert world_to_screen(Vec3(0, 0, 0), m, (1920, 1080)) is None