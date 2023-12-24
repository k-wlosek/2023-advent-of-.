from pydantic import BaseModel

class Location(BaseModel):
    x: int
    y: int
    z: int

class Velocity(BaseModel):
    x: int
    y: int
    z: int

class Hailstone(BaseModel):
    loc: Location
    vel: Velocity


def parse_input(lines: list[str]) -> list[Hailstone]:
    hailstones = []
    for line in lines:
        split = line.split("@")
        locs = [x.strip() for x in split[0].split(",")]
        vels = [x.strip() for x in split[1].split(",")]
        loc = Location(x=int(locs[0]), y=int(locs[1]), z=int(locs[2]))
        vel = Velocity(x=int(vels[0]), y=int(vels[1]), z=int(vels[2]))
        hailstones.append(Hailstone(loc=loc, vel=vel))
    return hailstones

def pair_up(hailstones: list[Hailstone]) -> list[tuple[Hailstone]]:
    pairs = []
    for i in range(len(hailstones)):
        for j in range(i+1, len(hailstones)):
            if (hailstones[i], hailstones[j]) in pairs or (hailstones[j], hailstones[i]) in pairs:
                continue
            else:
                pairs.append((hailstones[i], hailstones[j]))
    return pairs

def cross(hailstoneA: Hailstone, hailstoneB: Hailstone):
    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det((hailstoneA.vel.y, hailstoneB.vel.y), (hailstoneA.vel.x, hailstoneB.vel.x))
    if div == 0:
        return None  # Lines don't intersect

    d1 = det((hailstoneA.loc.x, hailstoneA.loc.y), (hailstoneA.loc.x + hailstoneA.vel.x, hailstoneA.loc.y + hailstoneA.vel.y))
    d2 = det((hailstoneB.loc.x, hailstoneB.loc.y), (hailstoneB.loc.x + hailstoneB.vel.x, hailstoneB.loc.y + hailstoneB.vel.y))
    x = det((d1, d2), (hailstoneA.vel.x, hailstoneB.vel.x)) / div
    y = det((d1, d2), (hailstoneA.vel.y, hailstoneB.vel.y)) / div
    t1 = (x - hailstoneA.loc.x) / hailstoneA.vel.x
    t2 = (x - hailstoneB.loc.x) / hailstoneB.vel.x

    if t1 >= 0 and t2 >= 0:
        return (x, y)
    else:
        return None

def crossed_in_bounds(hailstoneA: Hailstone, hailstoneB: Hailstone, bound: tuple[int]) -> bool:
    crossed = cross(hailstoneA, hailstoneB)
    if crossed is None:
        return False
    else:
        return bound[0] <= crossed[0] <= bound[1] and bound[0] <= crossed[1] <= bound[1]
