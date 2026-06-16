LAB 2: To implement Graph-Based Knowledge Representation – (Nodes, Edges, dictionary) and Rule-Based Knowledge Representation.

# Graph-Based and Rule-Based Knowledge Representation in Python

# -----------------------------
# Graph-Based Knowledge Representation
# -----------------------------

class KnowledgeGraph:
    def __init__(self):
        # Dictionary to store graph
        self.graph = {}

    # Add node to graph
    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    # Add edge between nodes
    def add_edge(self, node1, node2, relation):
        self.add_node(node1)
        self.add_node(node2)

        # Store relation as tuple
        self.graph[node1].append((node2, relation))

    # Display graph
    def display_graph(self):
        print("\nKnowledge Graph:")
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")


# Create graph object
kg = KnowledgeGraph()

# Add nodes and edges
kg.add_edge("Cat", "Animal", "is_a")
kg.add_edge("Dog", "Animal", "is_a")
kg.add_edge("Animal", "Living Thing", "belongs_to")
kg.add_edge("Bird", "Can Fly", "has_ability")

# Display graph
kg.display_graph()


# -----------------------------
# Rule-Based Knowledge Representation
# -----------------------------

class RuleBasedSystem:
    def __init__(self):
        self.facts = set()
        self.rules = []

    # Add fact
    def add_fact(self, fact):
        self.facts.add(fact)

    # Add rule
    def add_rule(self, condition, conclusion):
        self.rules.append((condition, conclusion))

    # Inference engine
    def infer(self):
        new_fact_added = True

        while new_fact_added:
            new_fact_added = False

            for condition, conclusion in self.rules:
                if condition in self.facts and conclusion not in self.facts:
                    print(f"Rule Applied: IF {condition} THEN {conclusion}")
                    self.facts.add(conclusion)
                    new_fact_added = True

    # Display facts
    def display_facts(self):
        print("\nKnown Facts:")
        for fact in self.facts:
            print("-", fact)


# Create rule-based system object
rbs = RuleBasedSystem()

# Add initial facts
rbs.add_fact("It is raining")

# Add rules
rbs.add_rule("It is raining", "Road is wet")
rbs.add_rule("Road is wet", "Drive carefully")

# Run inference
rbs.infer()

# Display all facts
rbs.display_facts()

Output: 
Knowledge Graph:
Cat -> [('Animal', 'is_a')]
Animal -> [('Living Thing', 'belongs_to')]
Dog -> [('Animal', 'is_a')]
Living Thing -> []
Bird -> [('Can Fly', 'has_ability')]
Can Fly -> []
Rule Applied: IF It is raining THEN Road is wet
Rule Applied: IF Road is wet THEN Drive carefully

Known Facts:
- Drive carefully
- Road is wet
- It is raining