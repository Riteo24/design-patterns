"""Легковаговик: дерева спільно використовують незмінні дані свого типу."""
from dataclasses import dataclass


@dataclass(frozen=True)
class TreeType:
    # Внутрішній стан спільний для всіх дерев цього типу.
    name: str
    color: str
    texture: str

    def draw(self, x, y):
        # Координати — зовнішній стан, вони не зберігаються в TreeType.
        return f"{self.name} ({self.color}, {self.texture}) у точці ({x}, {y})"


class TreeFactory:
    def __init__(self):
        self._types = {}

    def get_tree_type(self, name, color, texture):
        key = (name, color, texture)
        if key not in self._types:
            self._types[key] = TreeType(*key)
        return self._types[key]

    def count_types(self):
        return len(self._types)


@dataclass
class Tree:
    x: int
    y: int
    tree_type: TreeType

    def draw(self):
        return self.tree_type.draw(self.x, self.y)


class Forest:
    def __init__(self, factory):
        self._factory = factory
        self.trees = []

    def plant(self, x, y, name, color, texture):
        tree_type = self._factory.get_tree_type(name, color, texture)
        self.trees.append(Tree(x, y, tree_type))

    def draw(self):
        return [tree.draw() for tree in self.trees]


def main():
    factory = TreeFactory()
    forest = Forest(factory)
    forest.plant(1, 2, "Дуб", "зелений", "oak.png")
    forest.plant(4, 5, "Дуб", "зелений", "oak.png")
    forest.plant(7, 8, "Сосна", "темно-зелений", "pine.png")
    for line in forest.draw():
        print(line)
    print(f"Дерев: {len(forest.trees)}, спільних типів: {factory.count_types()}")
    print(f"Дуби мають один TreeType: {forest.trees[0].tree_type is forest.trees[1].tree_type}")


if __name__ == "__main__":
    main()
