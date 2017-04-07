from math import sqrt, acos, pi

class Vector:
    def __init__(self, *coordinates):
        if not coordinates:
            raise ValueError('The Coordinates must be non empty')
        if isinstance(coordinates[0], list):
            self.coordinates = coordinates[0]
        else:
            self.coordinates = list(coordinates)
    def __iter__(self,index):
        return self.coordinates[index]
    def __getitem__(self,index):
        return self.coordinates[index]
    def __setitem__(self,index,value):
        self.coordinates[index] = value
    def __delitem__(self,index):
        del self.coordinates[index]
    def __contains__(self,item):
        return item in self.coordinates
    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)
    def __main__(self):
        print(self.__str__())
        return self
    def __len__(self):
        return len(self.coordinates)
    def __pos__(self):
        return self
    def __neg__(self):
        return Vector([-c for c in self.coordinates])
    def __abs__(self):
        return Vector([abs(c) for c in self.coordinates])
    def __eq__(self, v):
        return self.coordinates == v.coordinates
    def magnitude(self):
        return sqrt(sum([i**2 for i in self.coordinates]))
    def __lt__(self, v):
        return self.magnitude() < v.magnitude()
    def __gt__(self, v):
        return self.magnitude() > v.magnitude()
    def __add__(self, v):
        try:
            if type(v) is int:
                return Vector([c1+v for c1 in self.coordinates])
            elif type(v) is Vector:
                if len(self) == len(v):
                    return Vector([c1+c2 for c1, c2 in zip(self.coordinates, v.coordinates)])
                elif len(self) == 1:
                    return Vector([c1+v[0] for c1 in self.coordinates])
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            raise TypeError('Unsupported operand type(s) for +: ' + type(self) + ' and ' + type(v))
        except ValueError:
            raise ValueError('Vector.__add__: operand self(' + str(self) + ') has different dimension that operand v(' + str(v) + ')')
    def __radd__(self, v):
        return self + v
    def __sub__(self, v):
        return self + -v
    def __rsub__(self, v):
        return v + -self
    def __mul__(self, v):
        try:
            if isinstance(v, (int, float)):
                return Vector([c1*v for c1 in self.coordinates])
            elif type(v) is Vector:
                if len(self) == len(v):
                    return sum([c1*c2 for c1, c2 in zip(self.coordinates, v.coordinates)])
                elif len(self) == 1:
                    return Vector([c1*v[0] for c1 in self.coordinates])
                else:
                    raise ValueError
            else:
                raise TypeError
        except TypeError:
            raise TypeError('Unsupported operand type(s) for *: ' + type(self) + ' and ' + type(v))
        except ValueError:
            raise ValueError('Vector.__mul__: operand self(' + str(self) + ') has different dimension that operand v(' + str(v) + ')')
    def __rmul__(self, v):
        return self * v
    def __truediv__(self, s):
        return Vector([i/s for i in self.coordinates])
    def __floordiv__(self, s):
        return Vector([i//s for i in self.coordinates])
    def __mod__(self, s):
        return Vector([i%s for i in self.coordinates])
    def normalize(self):
        if self.is_zero():
            raise Exception('Cannot Normalize a Zero Vector')
        else:
            return self/self.magnitude()
    def is_zero(self, tolerance = 1e-10):
        return self.magnitude() < tolerance
    def angle_with(self, v):
        return acos(self.normalize() * v.normalize())
    def is_parallel_with(self, v):
        if self.is_zero() or v.is_zero():
            return True
        else:
            return self.angle_with(v) == 0 or self.angle_with(v) == pi
    def is_orthogonal_to(self, v):
        if self.is_zero() or v.is_zero():
            return True
        else:
            return abs(self.angle_with(v)) - pi/2 < 1e-10
    def projection(self, v):
        u = v.normalize()
        weight = self * u
        return weight * u
    def orthogonal(self, v):
        return self - self.projection(v)
    def cross_product(self, v):
        if len(self) != 3 or len(v) !=3:
            raise ValueError('Cross Products can only be computed on three-dimensional vectors!')
        else:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = v.coordinates
            return Vector(y1*z2-y2*z1, x2*z1-x1*z2, x1*y2-x2*y1)
    def quadrangular_area_with(self, v):
        return self.cross_product(v).magnitude()
    def triangular_area_with(self, v):
        return self.quadrangular_area_with(v) / 2
