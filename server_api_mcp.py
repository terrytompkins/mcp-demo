from mcp.server.fastmcp import FastMCP
import random

# Create an MCP server
mcp = FastMCP("API Server")

@mcp.tool()
def get_random_fact() -> str:
    """Return a random fun fact."""
    facts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
        "A day on Venus is longer than its year. Venus takes 243 Earth days to rotate on its axis but only 225 Earth days to orbit the Sun.",
        "Bananas are berries, but strawberries aren't. In botanical terms, a berry is a fleshy fruit produced from a single ovary.",
        "The shortest war in history lasted only 38-45 minutes. The Anglo-Zanzibar War of 1896 ended when the British bombarded the Sultan's palace.",
        "Octopuses have three hearts. Two pump blood to the gills, while the third pumps it to the rest of the body.",
        "The Great Wall of China is not visible from space with the naked eye, despite the popular myth.",
        "A group of flamingos is called a 'flamboyance'.",
        "The average person spends 6 months of their lifetime waiting for red lights to turn green.",
        "Polar bears are left-handed. Well, left-pawed to be more accurate.",
        "The first oranges weren't orange. The original oranges from Southeast Asia were actually green."
    ]
    return random.choice(facts)

# Run the server
if __name__ == "__main__":
    mcp.run() 