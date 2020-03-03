from set import HashSet
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        elements = ['A', 'B', 'C']
        set = HashSet(elements)
        assert set.size is 3

    def test_size(self):
        elements = ['A', 'B', 'C', 'D', 'E']
        set = HashSet(elements)
        assert set.size is 5

    def test_contains(self):
        elements = ['P', 'C', 'X', 'U']
        set = HashSet(elements)
        assert set.contains('P') is True
        assert set.contains('C') is True
        assert set.contains('U') is True
        assert set.contains('D') is False
        assert set.contains('J') is False

    def test_add(self):
        elements = ['J', 'K']
        set = HashSet(elements)
        set.add('P')
        set.add('E')
        with self.assertRaises(KeyError):
            set.add('K')  # Element already exists
        with self.assertRaises(KeyError):
            set.add('E')  # Element already exists
        assert set.size is 4
        assert set.contains('P') is True
        assert set.contains('E') is True

    def test_remove(self):
        elements = ['U', '8', 'Q', 'D']
        set = HashSet(elements)
        with self.assertRaises(KeyError):
            set.remove('K')  # Element doesn't exist
        with self.assertRaises(KeyError):
            set.remove('0')  # Element doesn't exist
        set.remove('U')
        set.remove('Q')
        assert set.contains('U') is False
        assert set.contains('Q') is False
        with self.assertRaises(KeyError):
            set.remove('Q')  # Element doesn't exist anymore

    def test_union(self):
        elements = ['A', 'C', 'D', 'F']
        elements2 = ['A', 'B', 'D', 'F', 'G', 'H']
        elements3 = ['C', 'Y', 'T', 'A']
        set = HashSet(elements)
        set2 = HashSet(elements2)
        set3 = HashSet(elements3)
        self.assertCountEqual(set.union(set2).hash.values(), ['A', 'B', 'C', 'D', 'F', 'G', 'H'])  # Ignore item order
        self.assertCountEqual(set.union(set3).hash.values(), ['A', 'C', 'D', 'F', 'T', 'Y'])  # Ignore item order

    def test_intersection(self):
        elements = ['0', 'B', 'C', 'K']
        elements2 = ['0', 'D', 'E', 'C', 'Y', 'K']
        elements3 = ['B', 'D', 'P', 'K', 'G', '9']
        set = HashSet(elements)
        set2 = HashSet(elements2)
        set3 = HashSet(elements3)
        self.assertCountEqual(set.intersection(set2).hash.values(), ['0', 'C', 'K'])  # Ignore item order
        self.assertCountEqual(set.intersection(set3).hash.values(), ['B', 'K']) # Ignore item order

    def test_difference(self):
        elements = ['4', '7', '8', '9', '0']
        elements2 = ['4', '5', '6', '10', '8', '9']
        elements3 = ['1', '3', '5', '7', '0']
        set = HashSet(elements)
        set2 = HashSet(elements2)
        set3 = HashSet(elements3)
        self.assertCountEqual(set.difference(set2).hash.values(), ['7', '0'])  # Ignore item order
        self.assertCountEqual(set.difference(set3).hash.values(), ['4', '8', '9'])  # Ignore item order

    def test_is_subset(self):
        elements = ['Y', 'C', 'D']
        elements2 = ['C', 'G', 'U', 'D', 'T', 'Y']
        elements3 = ['P', 'H', 'Y', 'D', 'E', 'F']
        set = HashSet(elements)
        set2 = HashSet(elements2)
        set3 = HashSet(elements3)
        assert set.subset(set2) is True
        assert set.subset(set3) is False
        assert set2.subset(set3) is False

if __name__ == '__main__':
    unittest.main()