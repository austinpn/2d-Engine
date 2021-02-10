
from numbers import Number
from collections.abc import Sequence
class Vector(Sequence):
    """Defines vector object.
    """
    def __init__(self, *vals:Number):
        """Create Vector object
        Args:
            *vals (Number): ordered numbers to generate vector with
        Raises:
            ValueError: If non-number passed in *vals
        """
        self.__numZeros = 0
        self._vector = [0]*len(vals)
        i = 0
        for val in vals:
            if(not isinstance(val, Number)):
                raise ValueError()
            if(val==0): self.__numZeros+=1
            
            self._vector[i] = float(val)
            i+=1
    
    def __setitem__(self, i, val: Number):
        """Sets value at given index

        Args:
            i (int): index to update
            val (float): New value to be assigned at the given index
        """
        wasZero = self._vector[i]==0
        self._vector[i] = float(val)
        isZero = self._vector[i] == 0
        if(wasZero and not isZero): self.__numZeros-=1
        if((not wasZero) and isZero): self.__numZeros+=1

    def __getitem__(self, i):
        """Getter for item from given location

        Args:
            i (int): index to retrieve value from

        Returns:
            float: value retrieved from given index
        """
        return self._vector[i]
    
    def __len__(self):
        return self.dimension

    def __iter__(self):
        """Returns iterator of vector

        Returns:
            Iterator: iterator representation of object
        """
        return iter(self._vector)    
    
    def __eq__(self, value):
        """Vectors are equal if stored values are equal. They do not have to be the same instance to be equal

        Args:
            value (var): Value to test equality against

        Returns:
            bool: True is both are vectors and same values stored in same sequence
        """
        return isinstance(value, type(self)) and (self._vector == value._vector)

    @staticmethod
    def sum(*vectors: Sequence) -> 'Vector':
        """Sums Sequences and returns a new vector
        Args:
            *vectors (Sequence): The Sequences to be summed.

        Returns:
            Vector: Sum of components of passed vectors.
        """
        if(len(vectors)==0):
            return Vector()
        if(len(vectors)==1):
            return get_inert_vector(len(vectors[0]))
            return None


        targ = get_inert_vector(
            len (max(vectors, key = lambda k: len(k)))
        )
        
        for i in range(len(targ)):
            for vector in vectors:
                if(len(vector) <= i):
                    continue
                targ[i]+=vector[i]
        return targ
    def __add__(self, term):
        """Sum a vector and an Sequence, returning a Vector

        Args:
            term (Sequence): Sequence term

        Returns:
            Vector: sum of given vector and Sequence
        """
        if(not isinstance(term, Sequence)):
            raise ValueError(Sequence)
        return Vector.sum(self,term)
    def __radd__(self, term):
        """Sum an Sequence and vector

        Args:
            term (Sequence): Sequence term

        Returns:
            Vector: some of vector and Sequence
        """
        return self+term
    
    def __mul__(self, factor):
        """Multiply vector by given factor

        Args:
            factor (Number): Number to multiply vector components by

        Raises:
            ValueError: Raised if non-number factor given
        """
        if(not isinstance(factor, Number)):
            raise ValueError(Number)
        newVectArr = [x*factor for x in self._vector]
        return(Vector(*newVectArr))      
    def __rmul__(self, factor):
        """Multiply vector by given factor

        Args:
            factor (Number): Number to multiply vector components by

        Raises:
            ValueError: Raised if non-number factor given
        """
        return self*factor
    

    def copy(self):
        """Makes copy of Vector object

        Returns:
            Vector: copy of Vector object
        """
        return Vector(*self._vector.copy())

    @property
    def dimension(self):
        """Getter for dimension of Vector

        Returns:
            int: Dimension of vector
        """
        return len(self._vector)

    @property
    def inert(self):
        return self.__numZeros==self.dimension

    def update(self, sequence):
        self._vector = list(sequence)


def get_inert_vector(dimension: int)-> Vector:
    """Getter for zeroed vector of given dimension

    Args:
        dimension (int): Dimension for the returned vector

    Returns:
        Vector: Zeroed vector of given dimension
    """
    return Vector( *([0]*dimension) )
