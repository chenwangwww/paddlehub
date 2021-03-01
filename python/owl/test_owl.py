from owlready2 import *

onto = get_ontology("./pizza_onto.owl")
onto.load()

class NonVegetarianPizza(onto.Pizza):
    equivalent_to = [
        onto.Pizza
        & (onto.has_topping.some(onto.MeatTopping)
        | onto.has_topping.some(onto.FishTopping))
    ]
    def eat(self):
        print("Beurk! I'm vegetarian!")

test_pizza = onto.Pizza("test_pizza_owl_identifier")
test_pizza.has_topping = [
    onto.CheeseTopping(),
    onto.TomatoTopping()
]

print(test_pizza.__class__)

# sync_reasoner()

print(test_pizza.__class__)
# test_pizza.eat()