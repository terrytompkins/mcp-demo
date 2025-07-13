import random
from typing import List

class RandomFacts:
    """A simple class to manage and retrieve random facts."""
    
    def __init__(self, facts: List[str] = None):
        """Initialize with a list of facts.
        
        Args:
            facts: List of facts to use. If None, uses default facts.
        """
        if facts is None:
            self.facts = [
                "Cats have five toes on their front paws, but only four on their back paws.",
                "Bananas are berries, but strawberries are not.",
                "The unicorn is the national animal of Scotland.",
                "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
                "A group of flamingos is called a 'flamboyance'.",
                "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after just 38 minutes.",
                "Octopuses have three hearts.",
                "The Great Wall of China is not visible from space with the naked eye, despite the popular myth.",
                "A day on Venus is longer than its year.",
                "The average person spends 6 months of their lifetime waiting for red lights to turn green."
            ]
        else:
            self.facts = facts
    
    def get_random_fact(self) -> str:
        """Get a random fact from the collection.
        
        Returns:
            A randomly selected fact
        """
        if not self.facts:
            return "No facts available."
        return random.choice(self.facts)
    
    def add_fact(self, fact: str) -> None:
        """Add a new fact to the collection.
        
        Args:
            fact: The fact to add
        """
        if fact and fact not in self.facts:
            self.facts.append(fact)
    
    def get_all_facts(self) -> List[str]:
        """Get all facts in the collection.
        
        Returns:
            List of all facts
        """
        return self.facts.copy()
    
    def count_facts(self) -> int:
        """Get the number of facts in the collection.
        
        Returns:
            Number of facts
        """
        return len(self.facts) 